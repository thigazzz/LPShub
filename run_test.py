import os
import subprocess
import re
from pytest import mark
from typing import Tuple

def run_script(path_file: str) -> Tuple[int, str]:
    if os.path.isfile(path_file) == False:
        return (1, "Broken")
    print("a")
    pattern = re.compile(r"\w+\..+")
    match = pattern.search(path_file)
    path = path_file[:match.span()[0]]


    print(f"{path}venv/bin/python", path_file)

    venv = subprocess.run([f"{path}venv/bin/python", path_file], stdout=subprocess.PIPE)
    result = subprocess.run(['python3', path_file], stdout=subprocess.PIPE)

    print("a")

    if result.returncode > 0:
        return (1, "Error running this file")


if __name__ == "__main__":
    run_script("./bla.py")