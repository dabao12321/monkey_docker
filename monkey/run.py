#!/usr/bin/env python3

import argparse

def _run(file):
    # TODO implement
    print("Running {}".format(file))

def main(argv):
    parser = argparse.ArgumentParser(prog='run', description='Start a job')
    parser.add_argument("file",
                        help="path to main python file")
    args = parser.parse_args(argv)
    _run(args.file)

if __name__ == '__main__':
    main(sys.argv[1:])
