import logging
import os.path
from modules.config_reader import read_config
from modules.date_util import get_date_string
from modules.file_util import make_dir_if_not_exist, add_content_to_file

config = read_config()


def transfer_file_logs(log_type=None, input_json=[]):
    match log_type:
        case 'app_logs':
            dest_config = config['app_logs']['dest']
        case 'mail_logs':
            dest_config = config['mail_logs']['dest']
        case 'unknown_logs':
            dest_config = config['unknown_logs']['dest']
    parent_path = dest_config['parent_dir_path']
    filename = dest_config['filename']
    for json_instance in input_json:
        date_instance = get_date_string(json_instance.get('timestamp'))
        sub_folder = str(date_instance)
        full_path = os.path.join(parent_path, sub_folder, filename)
        make_dir_if_not_exist(full_path)
        add_content_to_file(full_path, json_instance)
        logging.info(f'inserted json {json_instance}')
