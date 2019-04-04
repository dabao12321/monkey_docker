import argparse
import sys
from monkey import run, check, save, list, remote, balance

def main():
    parser = argparse.ArgumentParser(
        description='The Monkey CLI'
    )

    subparsers = parser.add_subparsers(help='Subcommand to run', dest='command')
    subparsers.required = True

    parser_run = subparsers.add_parser('run', help='Start a job')
    parser_run.set_defaults(func=run.main)

    parser_check = subparsers.add_parser('check', help='Check status of a job')
    parser_check.set_defaults(func=check.main)

    parser_save = subparsers.add_parser('save', help='Save job output to your local machine')
    parser_save.set_defaults(func=save.main)

    parser_list = subparsers.add_parser('list', help='List your jobs')
    parser_list.set_defaults(func=list.main)

    parser_remote = subparsers.add_parser('remote', help='Login to a remote')
    parser_remote.set_defaults(func=remote.main)

    parser_balance = subparsers.add_parser('balance', help='Check your balance')
    parser_balance.set_defaults(func=balance.main)

    args = parser.parse_args(sys.argv[1:2])
    args.func(sys.argv[2:])

if __name__ == '__main__':
    main()
