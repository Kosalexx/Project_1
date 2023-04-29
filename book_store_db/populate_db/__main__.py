import sys
import os
from main import populate_db


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
AVAILABLE_FLAGS = ('-d', '-n')

if __name__ == '__main__':
    config_list = sys.argv
    for ind in range(1, len(config_list), 2):
        flag = config_list[ind]
        if flag not in AVAILABLE_FLAGS:
            raise ValueError('Invalid flag. Available flags: "-n", "-d".')
        elif flag == '-d':
            db_name = config_list[ind + 1]
        elif flag == '-n':
            num_data = config_list[ind + 1]
    if not db_name.endswith(".db"):
        raise ValueError('Unsupported DB file.')
    if not num_data.isalnum():
        raise ValueError('Number of generated data after flag "-n" must be '
                         'integer.')
    generate_number = int(num_data)
    populate_db(db_name=db_name, num=generate_number)
