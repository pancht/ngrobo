"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

Defines nRoBo command line switches.

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""
import argparse
import os

from cli.build import build
from cli.check import check
from cli.development import set_switch_environment
from cli.downloads import downloads
from cli.publish import publish
from nrobo.util.commands.ncommands import clear_screen
from nrobo.util.python import verify_set_python_install_pip_command
from nrobo.util.process import terminal
import subprocess
terminal(["pip", "install", "-r",  "requirements.txt"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


class BUILD_VERSION:
    """Build Version.

       Could be major | minor | patch"""
    MAJOR = "major"
    MINOR = "minor"
    PATCH = "patch"


def nrobo_cli() -> None:
    """Parses nrobo cli and executes the command."""

    clear_screen()
    verify_set_python_install_pip_command()

    parser = argparse.ArgumentParser(
        prog="nrobo",
        description='nRoBo package and upload utility')
    parser.add_argument("-b", "--build", help="Build package", action="store_true")
    parser.add_argument("-s", "--skip", help="Skip tests", action="store_true")
    parser.add_argument("-c", "--check", help="Check package bundle before upload", action="store_true")
    parser.add_argument("-p", "--publish", help="Publish package", action="store_true")
    parser.add_argument("-t", "--target", help="Target pypi repository. Options: test | prod")
    parser.add_argument("-e", "--env",
                        help="Set/switch environment between production_machine and development. Options: test | prod")
    parser.add_argument("-d", "--debug", help="Build package", action="store_true", default=False)
    parser.add_argument("-o", "--override", help="Build package", action="store_true", default=False)
    parser.add_argument("--major", help="Increment major version", action="store_true", default=False)
    parser.add_argument("--minor", help="Increment minor version", action="store_true", default=False)
    parser.add_argument("--downloads", help="Number of downloads", action="store_true", default=False)

    # parse cli args
    args = parser.parse_args()

    from nrobo import EnvKeys
    os.environ[EnvKeys.DEBUG] = str(args.debug)

    if args.build:
        if args.target:
            # Check what version to build. Major | Minor | Patch (Default)
            if args.major:
                build(args.target, override=args.override, build_version=BUILD_VERSION.MAJOR, skip_tests=args.skip)
            elif args.minor:
                build(args.target, override=args.override, build_version=BUILD_VERSION.MINOR, skip_tests=args.skip)
            else:
                build(args.target, override=args.override, build_version=BUILD_VERSION.PATCH, skip_tests=args.skip)
        else:
            print("Missing CLI arg -t | --target")
            exit(1)
    elif args.check:
        check()
    elif args.downloads:
        downloads()
        exit(0)
    elif args.publish:
        if args.target:
            publish(args.target, override=args.override)
        else:
            print("Missing CLI arg -t | --target")
            exit(1)
    elif args.env:

        set_switch_environment(args.env)

    else:
        print("Invalid argument or missing arguments!")
        exit(1)
