import json
import numpy as np
import scipy.optimize

class APSConfig(dict):
    """
    Class that loads the APS setup info from a JSON file
    and supports access to items using either attribute
    (e.g. obj.tsep) or key (e.g. obj["tsep"]) syntax.
    """
    added_fields = [ "filename", "dimension" ]

    def __init__(self,filename):
        self.filename = filename
        with open(filename,"r",newline="",encoding="UTF-8") as fp:
            d = json.load(fp)
        assert "base_stations" in d
        dim = None
        for b in d["base_stations"]:
            if dim is None:
                dim = len(b)
            else:
                assert len(b) == dim
        self.dimension = dim
        super().__init__(d)

    def __getattr__(self,a):
        return self[a]

    def __setattr__(self,a,v):
        self[a] = v

    def save(self,filename):
        with open(filename,"w",newline="",encoding="UTF-8") as fp:
            json.dump({k:v for k,v in self.items() if k not in self.added_fields},fp)


class TimeVector(list):
    """
    Class to store a tuple of measured times of chirp onsets
    with support for solving the pseudorange equations.
    """
        
    def __init__(self,config,*args):
        """
        Initialize with a given configuration object and chirp receive times
        passed as other arguments, e.g.
            TimeVector(conf, 1.1, 1.2, 1.3)
        means there are 3 base stations, and chirps were received at client
        times 1.1, 1.2, and 1.3.
        """
        if not isinstance(config,APSConfig):
            raise ValueError("First argument must be an APSConfig object")
        self.config = config # APSConfig instance
        # Can only work if we have as many timings as base stations
        assert len(args) == len(self.config.base_stations)
        super().__init__(args)
        # Vector of expected times from trigger pulse to chirp emissions (multiples of tsep)
        self.emit_delays = np.array([ i*self.config.tsep for i in range(len(self.config.base_stations)) ])
        # Differences of given times and expected emission times
        self.pre_rho = np.array(self) - self.emit_delays
        print("pre_rho=",self.pre_rho)
        # Numpy array of the base station positions (axis 1 = x,y,z)
        self.bs_pos = np.array(self.config.base_stations)
        # Centroid of the base stations
        self.bs_mid = np.mean(self.bs_pos,axis=0)
    
    def pseudorange_error(self,epos,pos):
        """
        Given an extended position vector epos (consisting of [x,y,...,delta])
        compute the error in the pseudorange equations for each of the base
        stations.  Returns a numpy vector of length equal to number of stations.
        """
        delta = epos[-1]
        # pos = epos[:-1] # (x,y) or (x,y,z)
        rho = self.config.speed * ( self.pre_rho - delta )

        # vectors pointing from this position to each base station
        # in a 2D array
        displacements = self.bs_pos - pos
        err = rho - np.linalg.norm(displacements,axis=1)
        #print("Psuedorange error for epos={} is {}".format(epos,err))
        return err

    def pseudorange_normsq(self,epos):
        v = self.pseudorange_error(epos)
        normv = np.dot(v,v)
        return normv

    def solve_eposition(self,max_allowed_error=1):
        delta_initial_guess = self[0]
        epos0 = np.append(self.bs_mid,delta_initial_guess)
        print("Solver using initial guess epos =",epos0)
        res = scipy.optimize.minimize(self.pseudorange_normsq, epos0, method="CG", jac=None, options={"disp":True, "gtol":1e-3,"eps":1e-9})
        if not res.success:
            raise Exception("Failed to find solution: {}".format(res.message))
        if abs(res.fun) > max_allowed_error:
            raise Exception("Failed to find solution: minimizer at {} has pseudorange error norm {}, max allowed is {}".format(res.x,res.fun,max_allowed_error))
        return res.x
