import PySimpleGUI as sg
from crud import ScriptCRUD
from database.database import DatabaseWithJSON

c = ScriptCRUD(DatabaseWithJSON())
scripts = c.list_all()

def create_item_element(scripts) -> list:
    elements = []
    for script in scripts:
        element = [sg.Text(script.id), sg.Text(script.path)]
        elements.append(element)

    return elements

script_line = create_item_element(scripts)

layout = [
    [sg.Input(key='-PATH-'), sg.Input(key='-VENV-'), sg.Button('Adicionar Script', key='-ADD-')],
    [sg.Frame('Scripts', layout=script_line,key='-CONTAINER-')]
]

window = sg.Window(
    "LPShub",
    layout=layout
)
while True:
    event, values = window.read()

    match event:
        case '-ADD-':
            file_path = values['-PATH-']
            venv = (True, values['-VENV-']) if values['-VENV-'] else (False, '')
            script = c.add(file_path, venv)
            window.extend_layout(window['-CONTAINER-'], [[sg.Text(script.id), sg.Text(script.path)]])
        case None:
            break

window.close()