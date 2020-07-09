#!/usr/bin/env python3
import pandas as cute
import argparse
def argparser():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('--InputFile','-f',type=str,help='enter your csv file: ')
    return parser.parse_args()
args = argparser()
f = args.InputFile
def file(f):
    x = cute.read_csv(f, sep = "\t", header = 0)
    y = cute.DataFrame(x)
    print(y)
file(f)
