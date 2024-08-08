import logging
import os
import json
from modules.config_reader import read_config

config = read_config()


def get_file_names_from_dir(folder_path=f'{os.getenv("PROJECT_PATH", "")}'):
    return [f"{folder_path}/{file_name}" for file_name in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file_name))]


def get_json_objects_from_file(json_file_path):
    json_objects = []
    clear_file_data = config['clear_file_after_transfer']
    try:
        with open(json_file_path, 'r+' if clear_file_data else 'r') as json_file:
            for line in json_file:
                try:
                    line = line.replace("'", '"')
                    json_obj = json.loads(line)
                    json_objects.append(json_obj)
                except json.JSONDecodeError as e:
                    logging.error(f'Error in parsing JSON {e}')
            if clear_file_data:
                json_file.seek(0)
                json_file.truncate()
    except FileNotFoundError as err:
        logging.error(f"File not found: {json_file_path} {err}")
    # Now `json_objects` contains all the JSON objects from the file
    return json_objects


def get_json_objects_from_directory(file_dir):
    json_objects = []
    file_list = get_file_names_from_dir(file_dir)
    for file in file_list:
        json_objects.extend(get_json_objects_from_file(file))
    return json_objects
