#!/usr/bin/env python3.6
"""Concatinate phylip files from path into 1 phylip."""

import re
import glob
import sys
import my_module as mod

def read_args(args):
    """Extract the directory and output from the user."""
    try:
        return args[0], args[1]
    except:
        print("Usage: python3 concatinate_alignments.py " \
              "path output_file")

def main():
    """Load the sequences and write them as a phylip."""
    path, output = read_args(sys.argv[1:])
    prepath = path
    path += "_[0-9]*"
    files = glob.glob(path)
    seqs = {}
    for i in range(1, len(files)+1):
        lines = mod.get_file_data(prepath + "_" + str(i) + ".phy")[1:]
        for line in lines:
            fields = re.split(r'\s{2,}', line)
            seq = re.sub(" ", "", fields[1])
            if fields[0] in seqs:
                seqs[fields[0]] += seq
            else:
                seqs[fields[0]] = seq
    
    out = open(output, "w")
    flag = 1
    for key, value in seqs.items():
        if flag:
            out.write(str(len(seqs)) + "  " + str(len(value)) + "\n")
            flag = 0
        out.write(key + "  " + value + "\n")
    out.close()


if __name__ == "__main__":
    main()
