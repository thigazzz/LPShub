import os
import json
from typing import Tuple
from collections import namedtuple
from abc import ABC, abstractmethod

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
