import os

FILE_SEP = '_'
TXT_EXTENSION = '.txt'
INPUT_FOLDER = 'Inputs'

def getInputLines(year,day):
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    inputs_dir = os.path.join(root_dir, INPUT_FOLDER)

    file_name = str(year) + FILE_SEP +f'{day:02d}' + TXT_EXTENSION
    filepath = os.path.join(inputs_dir, file_name)

    with open(filepath, 'r') as file:
        return file.read().splitlines()
    
    return []