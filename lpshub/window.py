import PySimpleGUI as sg

layout = [
    [sg.Input(key='-PATH-'), sg.Input(key='-VENV-'), sg.Button('Adicionar Script', key='-ADD-')]
]
from crud import ScriptCRUD
from database.database import DatabaseWithJSON

c = ScriptCRUD(DatabaseWithJSON())

window = sg.Window(
    "LPShub",
    layout=layout
)
while True:
    event, values = window.read()

    match event:
        case '-ADD-':
            print(values['-PATH-'], values['-VENV-'])
            file_path = values['-PATH-']
            venv = (True, values['-VENV-']) if values['-VENV-'] else (False, '')
            c.add(file_path, venv)
        case None:
            break

window.close()