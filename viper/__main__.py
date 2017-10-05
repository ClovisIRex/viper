import argparse


def main(args=None):
    """
    Main Routine and Entry Point.

    :param args: flags passed manually to viper
    """
    parser = argparse.ArgumentParser(
        description="Packaging made easier than it needs to be."
    )
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")

    if type(args) == list:
        args = parser.parse_args(args)
    else:
        args = parser.parse_args()

    if args.verbose:
        print("verbosity enabled")

if __name__ == "__main__":
    main()
