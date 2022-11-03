
"""Builds a chromaticity tree with certain operations"""
class Chroma:
    """Stores Chromaticity and makes comparisons"""
    def __init__(self,r,g,b):
        """initiailizes r,g,b attributes"""
        self.r = r
        self.g = g
        self.b = b
        if not (self.r + self.g + self.b == 255) or self.r < 0 or self.b < 0 or self.g < 0:
            raise ValueError("Invalid Input")
            
                
    def __eq__(self,other):
        """checks if two chromas are equal if red green and blue are equal"""
        if not isinstance(other,Chroma):
            return NotImplemented
        else:
            return self.r == other.r and self.g == other.g and self.b == other.b
    def more_red_than(self,other):
        """checks if one chroma is more red then"""
        if not self.r > other.r:
            return False
        else:
            return True
    def more_green_than(self,other):
        """checks if one chroma is more green than the other"""
        if not self.g > other.g:
            return False
        else:
            return True
    def more_blue_than(self,other):
        """return true if blue dir of chroma is more than the other"""
        if not self.b > other.b:
            return False
        else:
            return True
class ChromaNode:
    """A node in a tree that has up to three children, a key that is a Chroma, and a value name that is a string. 
    Such nodes will be used to build a tree that stores a mapping from chromaticities to names."""
    def __init__(self,key,name,red=None,green=None,blue=None,parent=None):
        """initializes attributes of chromanode"""
        self.key = key
        self.name = name
        self.red = red
        self.green = green
        self.blue = blue
        self.parent = parent
    def set_red(self,other):
        """set in red tree and set prev to parent"""
        self.red = other
        other.parent = self
    def set_green(self,other):
        """set in green tree"""
        self.green = other
        other.parent = self
    def set_blue(self,other):
        """set in blue tree"""
        self.blue = other
        other.parent = self
class ChromaTree:
    """Maintain a tree of ChromaNode objects that satisfies the Chromaticity Tree Condition."""
    def __init__(self):
        """initizlize root"""
        self.root = None
    def insert(self,node,dir = 0):
        """insert node"""
        cur = self.root
        prev = None
        branch = None
        while cur != None:
            prev = cur
            if dir == 0:
                if node.key.more_red_than(prev.key):
                    cur = prev.red
                    branch = 'red'
                elif node.key.more_green_than(prev.key):
                    cur = prev.green
                    branch = 'green'
                elif node.key.more_blue_than(prev.key):
                    cur = prev.blue
                    branch = 'blue'
            elif dir == 1:
                if node.key.more_blue_than(prev.key):
                    cur = prev.blue
                    branch = 'blue'
                elif node.key.more_green_than(prev.key):
                    cur = prev.green
                    branch = 'green'

                elif node.key.more_red_than(prev.key):
                    cur = prev.red
                    branch = 'red'
        if prev == None:
            # This is the first node to be inserted
            self.root = node
        else:
            # Make x a child of prev
            if branch == 'red':
                prev.set_red(node)
            elif branch == 'blue':
                prev.set_blue(node)
            elif branch == 'green':
                prev.set_green(node)
                
    def search(self,key):
        """returns searched node"""
        return self._search(key,self.root)
    
    def _search(self,key,base):
        if base == None:
            return

        if key == base.key:
            return base
        
        result = None

        if key.more_red_than(base.key):
            result = self._search(key, base.red)

        if result is None and key.more_blue_than(base.key):
            result = self._search(key,base.blue)

        if result is None and key.more_green_than(base.key):
            result = self._search(key,base.green)

        return result


    def __len__(self,node = None):
        """return total number of nodes in the tree"""
        blen = 0
        rlen = 0
        glen = 0
        if node is None:
            node = self.root
        if node == None:
            return 0
        if node.red == None and node.green == None and node.blue == None:
            return 1
        if node.blue:
            blen = self.__len__(node.blue)
        if node.red:
            rlen = self.__len__(node.red)
        if node.green:
            glen = self.__len__(node.green)
        return 1 + blen + rlen + glen
    def depth(self,node = None):
        """return longest depth of the tree"""
        reddepth = 0
        bluedepth = 0
        greendepth = 0

        if self.root is None:
            return 0

        if node == None:
            node = self.root
        
        if node.red == None and node.green == None and node.blue == None:
            return 0

        if node.red:
            reddepth =  self.depth(node.red)
        if node.blue:
            bluedepth =  self.depth(node.blue)
        if node.green:
            greendepth =  self.depth(node.green)
        
        return 1 + max(reddepth,bluedepth,greendepth)
    
class ChromaNameMapping():
    """Maintain a mutable collection of key-value pairs, 
    where keys are Chromau objects and values are strings (names of the chromaticities), 
    using a ChromaTree as the backing data structure."""
    def __init__(self):
        """init attributes"""
        self.T = ChromaTree()

    def __setitem__(self,key,name):
        """sets name to key"""
        self.T.insert(ChromaNode(key, name))
    
    def __getitem__(self,key):
        """get name of key"""
        node = self.T.search(key)
        if node:
            return node.name

        raise KeyError()    
        
    def __len__(self):
        """return len of T"""
        return len(self.T)



