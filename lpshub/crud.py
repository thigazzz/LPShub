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

class Script:
    def __init__(self, database: Database):
        self.database = database
    
    def add(self, path: str) -> None | Tuple[int, str]:
        """
        Adds a new script in to database to be executed.
        When the path of file or file not exists, an error
        is returned showing a message.

        Param:
            path: str 
                The path of Python script
        
        """
        if os.path.isfile(path) == False:
            return (1, "Broken")

        venv_dir = self.__get_venv_dir(path)
        id = 1

        new_script = (id, path, venv_dir)

        self.database.add(path)

    def __get_venv_dir(self, path: str) -> str | bool:
        """
        Get the Virual Environment path/dir (the full path to venv) 
        by a file path.
        When no have a venv directory, is returned FALSE.

        Param:
            path: str
                The path of a file to get the venv directory
            
        Returns:
            venv_dir: str
                Full path to Venv directory of a file
        """
        if self.__is_not_venv_in(path):
            return False

        return 'hard coded'

    def __is_not_venv_in(self, dir: str):
        return False
    