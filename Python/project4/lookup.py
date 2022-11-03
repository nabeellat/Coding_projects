#Nabeel Latifi


"""
Reads a list of chromaticities and names from the CSV file
(name given as first command line argument) and provides a
lookup service using keyboard input.  Each time the user
enters a chromaticity in the format
  r g b
the name will be found and printed, or a message will be
shown indicating the chromaticity was not in the CSV file.
Entering a blank line ends the program.
"""

import sys
import csv

if len(sys.argv)!=2:
    print("ERROR: Required command line argument missing.\n")
    print("Usage: {} FILENAME".format(sys.argv[0]))
    print("Reads chromaticity dictionary from FILENAME (CSV)")
    print("then performs interactive name lookup.")
    sys.exit(1)

# Pretend that for some reason we can't use Python's
# `dict` data type to store the chromaticity-name pairs.
# An easy to implement but ridiculously inefficient
# approach is to just store a list of chromaticities,
# and a list of names, in the same order.  
chromaticities = []
names = []
with open(sys.argv[1],"rt",newline="") as infile:
    rdr = csv.DictReader(infile)
    for row in rdr:
        c = [int(row["red"]),int(row["green"]),int(row["blue"])]
        chromaticities.append(c)
        names.append(row["name"])

# Main command loop: Read a line, parse it, look it up
for line in sys.stdin:
    line = line.strip() # ignore leading and trailing whitespace
    # blank line?  If so, exit the loop (ending the program)
    if not line:
        break
    # Attempt to parse the line as three integers
    # and check they form a chromaticity, c
    try:
        c = [int(x) for x in line.split()]
        if len(c) != 3 or sum(c) != 255:
            print("<invalid>")
            continue
    except ValueError:
        # the input line couldn't be parsed as integers
        print("<invalid>")
        continue
    # Find the chromaticity's name
    try:
        i = chromaticities.index(c)
        # If the previous line succeeds, then c was in the
        # list of chromaticities and i is its position.
        # So the name of c is in position i in `names`.
        print(names[i])
    except ValueError:
        # c was not found in list chromaticities
        print("<not found>")
