from cli.build import build
from cli.check import check
from cli.publish import publish
from cli.devlopment import set_switch_environment
import argparse
from nrobo.util.commands.ncommands import clear_screen
from nrobo.util.python import verify_set_python_install_pip_command


def nrobo_cli():
    """
    Parses nrobo cli and executes the command.

    :return:
    """
    clear_screen()
    verify_set_python_install_pip_command()

    parser = argparse.ArgumentParser(
        prog="nrobo",
        description='norobo package and upload utility')
    parser.add_argument("-b", "--build", help="Build package", action="store_true")
    parser.add_argument("-c", "--check", help="Check package bundle before upload", action="store_true")
    parser.add_argument("-p", "--publish", help="Publish package", action="store_true")
    parser.add_argument("-t", "--target", help="Target pypi repository. Options: test | prod")
    parser.add_argument("-e", "--env", help="Set/switch environment between production and development. Options: test | prod")
    parser.add_argument("-d", "--debug", help="Build package", action="store_true", default=False)

    args = parser.parse_args()

    if args.build:
        if args.target:
            build(args.target, args.debug)
        else:
            print("Missing CLI arg -t | --target")
            exit(1)
    elif args.check:
        check(args.debug)
    elif args.publish:
        if args.target:
            publish(args.target, args.debug)
        else:
            print("Missing CLI arg -t | --target")
            exit(1)
    elif args.env:

        set_switch_environment(args.env, args.debug)

    else:
        print("Invalid argument or missing arguments!")
        exit(1)
