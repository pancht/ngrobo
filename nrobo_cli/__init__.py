from nrobo_cli.build import build
from nrobo_cli.check import check
from nrobo_cli.publish import publish
import argparse
from nrobo.util.commands.ncommands import clear_screen

def nrobo_cli():
    """
    Parses nrobo cli and executes the command.

    :return:
    """
    clear_screen()

    parser = argparse.ArgumentParser(
        prog="nrobo",
        description='norobo package and upload utility')
    parser.add_argument("-b", "--build", help="Build package", action="store_true")
    parser.add_argument("-c", "--check", help="Check package bundle before upload", action="store_true")
    parser.add_argument("-p", "--publish", help="Publish package", action="store_true")
    parser.add_argument("-t", "--target", help="Target pypi repository. Options: test | prod")

    args = parser.parse_args()

    if args.build:
        build(args.target)
    elif args.check:
        check()
    elif args.publish:
        publish(args.target)
    else:
        print("Invalid argument or missing arguments!")
        exit(1)
