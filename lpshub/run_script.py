import os
import re
import subprocess
from typing import Tuple

def run_script(path_file: str) -> Tuple[int, str]:
    if os.path.isfile(path_file) == False:
        return (1, "Broken")

    pattern = re.compile(r"\w+\..+")
    match = pattern.search(path_file)
    path = path_file[:match.span()[0]]

    # TODO: option for any venv dir with any name
    venv = subprocess.run([f"{path}venv/bin/python", path_file], stdout=subprocess.PIPE)
    result = subprocess.run(['python3', path_file], stdout=subprocess.PIPE)

    if result.returncode > 0:
        return (1, "Error running this file")