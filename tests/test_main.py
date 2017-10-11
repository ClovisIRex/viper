import subprocess

import sys


def test_viper_command():
    """
    Ensure viper command exists.
    """
    if sys.version_info < (3, 5):
        subprocess.call('viper')
    else:
        subprocess.run("viper")
