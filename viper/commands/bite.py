import sys

import os

from viper.commands import CommandFactory
from viper.util import create_file


class BiteCommand(CommandFactory):
    def __init__(self, parser):
        parser_setup = parser.add_parser(
            "bite",
            aliases=[],
            help="inject viper into python",
        )
        parser_setup.set_defaults(action=self.run)

    @staticmethod
    def run(args=None):
        site_packages = next(p for p in sys.path if 'site-packages' in p)
        site_file = os.path.join(site_packages, 'sitecustomize.py')
        if create_file(site_file):
            print("Success: Viper Injected")


if __name__ == "__main__":
    BiteCommand.run()
