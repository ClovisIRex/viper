import subprocess

import sys


def run_command(*args):
    if sys.version_info < (3, 5):
        subprocess.call(args)
    else:
        subprocess.run(args)
