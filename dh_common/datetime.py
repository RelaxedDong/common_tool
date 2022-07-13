import datetime

FORMAT_DATETIME = u'%Y-%m-%d %H:%M:%S'
FORMAT_DATE = u'%Y-%m-%d'


def datetime_to_str(date, date_format=FORMAT_DATETIME, process_none=False):
    """
    convert {@see datetime} into date string ('2011-01-12')
    """
    if process_none and date is None:
        return ''
    return date.strftime(date_format)


def str_to_datetime(date_str, date_format=FORMAT_DATETIME, process_none=False):
    """
    convert date string ('2011-01-12') into {@see datetime}
    """
    if process_none and not date_str:
        return None
    date = datetime.datetime.strptime(date_str, date_format)
    return date