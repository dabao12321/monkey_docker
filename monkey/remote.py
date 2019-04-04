import argparse

def _remote(address):
    # TODO implement
    print("Logging into {}".format(address))

def main(argv):
    parser = argparse.ArgumentParser(
        prog='remote', description='Login to a remote')
    parser.add_argument("address",
                        help="address of monkey remote")
    args = parser.parse_args(argv)
    _remote(args.address)

if __name__ == '__main__':
    main(sys.argv[1:])
