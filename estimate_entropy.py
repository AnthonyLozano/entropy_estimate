#!/usr/bin/python
# -*- encoding: UTF-8 -*-
"""
Simple Entropy Estimator.

Usage:
    estimate_entropy.py INPUT
    estimate_entropy.py -h | --help | --version

Arguments:
    INPUT path to file containing random data to read.
Options:
    -h --help     Show this screen.
    --version     Show version.
"""
from docopt import docopt
from collections import Counter
from functools import partial
from math import log2

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Simple Entropy Estimator 1.0')
    filename = arguments['INPUT']

    byte_counts = Counter()
    total_bytes = 0
    with open(filename, 'rb') as infile:
        for chunk in iter(partial(infile.read, 1024), b''):  # read in chunks until we read an empty string.
            for byte in chunk:
                byte_counts[byte] += 1
                total_bytes += 1
    #pprint(byte_counts)
    entropy = 0
    for byte, count in byte_counts.items():
        prob = count / total_bytes
        entropy += prob * log2(1 / prob)
    print("{} bits per byte".format(entropy))

