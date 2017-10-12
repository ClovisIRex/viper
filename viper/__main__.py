import argparse
import sys

import viper
from viper.commands.bite import BiteCommand
from viper.commands.freeze import FreezeCommand


def _optional_commands(parser):
    parser.add_argument(
            "-V", "--version",
            version="%(prog)s {}".format(viper.__version__),
            action="version"
        )
    parser.add_argument(
        "-v", "--verbose",
        help="increase output verbosity",
        action="store_true"
    )
    return parser


def _main_commands(parser):
    FreezeCommand(parser)
    BiteCommand(parser)
    return parser


def main(args=None):
    """
    Main Routine and Entry Point.

    :param args: flags passed manually to viper
    """
    parser = argparse.ArgumentParser(
        description="Packaging made easier than it needs to be."
    )
    parser = _optional_commands(parser)

    parser_commands = parser.add_subparsers(
        title="Commands",
        dest="commands"
    )
    parser_commands = _main_commands(parser_commands)

    if type(args) == list:
        args = parser.parse_args(args)
    else:
        args = parser.parse_args()

    try:
        args.action(args)  # Investigate why this fails
    except AttributeError:
        pass

    # Display help and exit if no arguments passed
    if len(sys.argv[1:]) == 0:
        parser.print_help()
        parser.exit(0)

    if args.verbose:
        print("verbosity enabled")


if __name__ == "__main__":
    main()
