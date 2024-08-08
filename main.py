from modules.transfer_util import transfer_file_logs
from modules.file_util import fetch_file
from modules.file_reader import get_json_objects_from_file


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logs = ['app_logs', 'mail_logs', 'unknown_logs']
    for log in logs:
        json_objs = get_json_objects_from_file(fetch_file(log))
        transfer_file_logs(log, json_objs)
