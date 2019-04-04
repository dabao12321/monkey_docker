import argparse

def _check(id):
    # TODO implement
    print("Checking {}".format(id))

def main(argv):
    parser = argparse.ArgumentParser(
        prog='check', description='Check status of a job')
    parser.add_argument("id",
                        help="monkey id of job")
    args = parser.parse_args(argv)
    _check(args.id)

if __name__ == '__main__':
    main(sys.argv[1:])
