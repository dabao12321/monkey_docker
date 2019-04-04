import argparse

def _list():
    # TODO implement
    print("Listing...")

def main(argv):
    parser = argparse.ArgumentParser(
        prog='list', description='List your jobs')
    args = parser.parse_args(argv)
    _list()

if __name__ == '__main__':
    main(sys.argv[1:])
