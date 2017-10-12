import sys

import os

from tests.common import run_command


def test_bite_command():
    run_command("viper", "bite")
    site_packages = next(p for p in sys.path if 'site-packages' in p)
    assert 'sitecustomize.py' in os.listdir(site_packages)
