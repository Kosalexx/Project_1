import sys
import os
from main_script import populate_db


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
AVAILABLE_FLAGS = ('-d', '-f')

if __name__ == '__main__':
    config_list = sys.argv
    for ind in range(1, len(config_list), 2):
        flag = config_list[ind]
        if flag not in AVAILABLE_FLAGS:
            raise ValueError('Invalid flag. Available flags: "-d", "-f".')
        elif flag == '-d':
            db_name = config_list[ind + 1]
        elif flag == '-f':
            data_file = config_list[ind + 1]
    if not db_name.endswith(".db"):
        raise ValueError('Unsupported DB file.')
    if data_file.split('.')[1] not in ('json', 'csv'):
        raise ValueError('Unsupported data file.')
    populate_db(db_name=db_name, file_name=data_file)
