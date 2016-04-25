# Simple Entropy Estimator

Scans a file of binary random data and estimates the bits per byte of entropy in that file.

## Installation

Install docopt

`pip install docopt`

Then just download the script and run it.
TODO Get this on pypi

## Usage


```
Simple Entropy Estimator.

Usage:
    estimate_entropy.py INPUT
    estimate_entropy.py -h | --help | --version

Arguments:
    INPUT path to file containing random data to read.
Options:
    -h --help     Show this screen.
    --version     Show version.
```
Make sure the input file contains a very large sample from your random data source.

## Motivation

The SAIFE endpoint library expects to know how many bits per byte of data is passed to it with the AddEntropy function.
This script provides a simplistic, easy way to *estimate* that number.