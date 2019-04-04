import argparse

def _save(id):
    # TODO implement
    print("Saving {}".format(id))

def main(argv):
    parser = argparse.ArgumentParser(
        prog='save', description='Save job output to your local machine')
    parser.add_argument("id",
                        help="monkey id of job")
    args = parser.parse_args(argv)
    _save(args.id)

if __name__ == '__main__':
    main(sys.argv[1:])
