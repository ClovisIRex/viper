import subprocess


def test_viper_command():
    """
    Ensure viper command exists.
    """
    subprocess.run("viper", check=True)
