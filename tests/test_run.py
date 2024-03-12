"""
Test for running a script.
"""
import os
from lpshub.run_script import run_script

def test_show_error_when_file_not_have_success_running():
    """
    Test for when running a broken Python file or a file with errors.
    When the failure happens, the function must return an Error tuple.
    In this case, it must return an error describing which Python
    file has an error and which, because of this, the file did not run.

    An example of how the API of this behavior must be:
    >>> run_script(python_file_with_internal_errors)
    (1, 'Error') == (exit_code, error's message)

    >>> run_script(broken_file)
    (1, 'Error') == (exit_code, error's message)

    >>> run_script(nonexistent_file)
    (1, 'Error') == (exit_code, error's message)
    
    """
    # TODO: create a fake environment which mocks the venv behavior and files
    sut = run_script
    fake_path = './tests/fake/fake_broken_file.py'
    with open(fake_path, 'a') as f:
        f.write("raise Exception('Error')")
    

    error = sut(fake_path)

    assert error[0] > 0
    assert error[1] == "Error running this file"

    os.remove(fake_path)

def test_show_error_when_path_is_broken():
    """   
    Test for when running a wrong path or named Python file.

    An example of how the API of this behavior must be:
    >>> run_script(wrong_name)
    (1, 'Error') == (exit_code, error's message)

    >>> run_script(nonexistent_file)
    (1, 'Error') == (exit_code, error's message)

    >>> run_script(wrong_path_file)
    (1, 'Error') == (exit_code, error's message)
    """
    sut = run_script
    error = sut('broken_path/broken_file.any')
    assert error[0] > 0
    assert error[1] == "Broken"
