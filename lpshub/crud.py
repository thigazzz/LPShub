"""
Module for CRUD interactions of script: Add, Delete and Update a script
in database
"""
from collections import namedtuple
from abc import ABC, abstractmethod
from typing import Tuple

class Database(ABC):
    @abstractmethod
    def create(self, item) -> None:
        ...
    @abstractmethod
    def read_one(self, id: int):
        ...
    @abstractmethod
    def read_all(self) -> list:
        ...
    @abstractmethod
    def update(self, id: int, item) -> None:
        ...
    @abstractmethod
    def delete(self, id: int) -> None:
        ...
import os
import json
class DatabaseWithJSON(Database):
    def __init__(self):
        self.database_path = './database/scripts.json'
        if os.path.exists('./database') == False:
            os.makedirs('./database')
        if os.path.exists(self.database_path) == False:
            with open(self.database_path, 'w') as f:
                j = json.dumps({'scripts': []})
                f.write(j)

    def create(self, item) -> None:
        scripts = self.read_all()
        scripts.append(item)

        with open(self.database_path, 'w') as f:
            j = json.dumps({'scripts': scripts})
            f.write(j)

    def read_one(self, id: int):
        ...
    def read_all(self) -> list:
        with open(self.database_path, 'r') as f:
            j = json.load(f)

        return j['scripts'] # scripts
    def update(self, id: int, item) -> None:
        ...
    def delete(self, id: int) -> None:
        ...

from itertools import count
class Script:
    c = count()
    def __init__(self, database: Database):
        self.database = database
    
    def add(self, file_path: str, venv_info: tuple) -> None | Tuple[int, str]:
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