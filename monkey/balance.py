import argparse

def _balance():
    # TODO implement
    print("Checking your balance...")

def main(argv):
    parser = argparse.ArgumentParser(
        prog='balance', description='Check your balance')
    args = parser.parse_args(argv)
    _balance()

if __name__ == '__main__':
    main(sys.argv[1:])
