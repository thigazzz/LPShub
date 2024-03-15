"""
Module for CRUD interactions of script: Add, Delete and Update a script
in database
"""
import os
from typing import Tuple, List
from itertools import count
from collections import namedtuple
from database.database import Database

Script = namedtuple('Script', 'id, path, venv')

class ScriptCRUD:
    c = count()
    def __init__(self, database: Database):
        self.database = database
    
    def add(self, file_path: str, venv_info: tuple) -> None | Tuple[int, str]:
        # TODO: Refactor documentation
        """
        Adds a new script in to database to be executed.
        When the path of file or file not exists, an error
        is returned showing a message.

        Param:
            path: str 
                The path of Python script
        
        """
        if os.path.isfile(file_path) == False:
            return (1, "Broken")
        
        _venv = False
        if venv_info[0] == True:
            if os.path.exists(venv_info[1]) == False:
                return (1, "Virtual Environment path is wrong")
            _venv = {'path': venv_info[1]}

        id = next(self.c) # TODO: change type of ID
        new_script = {'id': id, 'path': file_path, 'venv': _venv}
        self.database.create(new_script)

        return Script(id=id, path=file_path, venv=_venv['path'] if _venv else _venv)


    def list_all(self) -> List[Script]:
        # TODO: Refactor documentation
        """
        >>> list_all()
        [Script(), Script(), Script()]
        """
        json_list = self.database.read_all()
        scripts = []
        for json_item in json_list:
            scripts.append(
                Script(
                    id=json_item['id'], 
                    path=json_item['path'],
                    venv=json_item['venv']['path'] if json_item['venv'] else json_item['venv']
                )
            )

        return scripts