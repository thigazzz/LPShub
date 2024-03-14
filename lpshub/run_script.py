import os
import re
import subprocess
from typing import Tuple
from lpshub.crud import Script

def run_script(script: Script) -> Tuple[int, str]:
    file = script.path
    venv = script.venv

    if venv:
        venv_cmd = subprocess.run([f"{venv}/bin/python", file], stdout=subprocess.PIPE)
    result = subprocess.run(['python3', file], stdout=subprocess.PIPE)

    if result.returncode > 0:
        return (1, "Error running this file")