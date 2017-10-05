import argparse

import sys

import viper


def main(args=None):
    """
    Main Routine and Entry Point.

    :param args: flags passed manually to viper
    """
    parser = argparse.ArgumentParser(
        description="Packaging made easier than it needs to be."
    )
    parser.add_argument(
        "-V", "--version", version="%(prog)s {}".format(viper.__version__),
        action="version")
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")

    if type(args) == list:
        args = parser.parse_args(args)
    else:
        args = parser.parse_args()

    # Display help and exit if no arguments passed
    if len(sys.argv[1:]) == 0:
        parser.print_help()
        parser.exit(0)

    if args.verbose:
        print("verbosity enabled")

if __name__ == "__main__":
    main()
