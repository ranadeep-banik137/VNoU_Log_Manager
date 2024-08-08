import json
import os.path
import logging

from modules.config_reader import read_config

config = read_config()


def fetch_file(file_type):
    file = None
    try:
        match file_type:
            case 'app_logs':
                src_config = config['app_logs']['src']
            case 'mail_logs':
                src_config = config['mail_logs']['src']
            case 'unknown_logs':
                src_config = config['unknown_logs']['src']

        src = src_config['path']
        path = src_config['filename']
        file = os.path.join(src, path)
    except Exception as err:
        logging.error(f'No log file found {err}')
    return file


def make_dir_if_not_exist(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory) and directory != '':
        os.makedirs(directory)
    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='') as file:
            logging.debug(f'File at {file_path} created')


def add_content_to_file(filepath, content):
    with open(filepath, 'a') as file:
        json_content = json.dumps(content)
        file.write(json_content + '\n')


def clear_file_contents(filepath):
    pass

