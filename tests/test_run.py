"""
Test run script feature
"""
import os
import subprocess
from pytest import mark
from typing import Tuple

def is_not_path_correct(path: str) -> bool:
    if path == 'broken_path': #HARD CODE
        return True
    return False

def run_script(path_file: str) -> Tuple[int, str]:
    result = subprocess.run(['python3', path_file], stdout=subprocess.PIPE)
    if result.returncode > 0:
        return (1, "Broken")
    # os.system(f"source venv/bin/activate")
    # os.system(f"python3 {path_file}")
    # code = process.exitcode

def test_show_error_when_file_not_have_success_running():
    """
    Test the return of function when any failure occurs.
    When failure happens the function must return a Error tuple

    >>> run_script(broken_path)
    (1, 'Error') == (exit_code, error's message)

    >>> run_script(broken_file)
    (1, 'Error') == (exit_code, error's message)

    >>> run_script(nonexistent_file)
    (1, 'Error') == (exit_code, error's message)
    
    """
    sut = run_script
    error = sut('broken_path')
    assert error[0] > 0
    assert error[1] == "Broken"
