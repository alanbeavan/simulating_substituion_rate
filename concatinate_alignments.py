#!/usr/bin/env python3.6
"""Concatinate phylip files from directory into 1 phylip."""

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
              "sequence_directory output_file")

def main():
    """Load the sequences and write them as a phylip."""
    directory, output = read_args(sys.argv[1:])
    files = glob.glob(directory + "/*phy")
    seqs = {}
    for file in files:
        lines = mod.get_file_data(file)[1:]
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
        out.write(key + "\t" + value + "\n")
    out.close()


if __name__ == "__main__":
    main()
