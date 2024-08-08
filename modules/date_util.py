from datetime import datetime


def get_date_string(input_date):
    datetime_obj = datetime.fromisoformat(input_date)
    date_only = datetime_obj.date()
    return date_only
