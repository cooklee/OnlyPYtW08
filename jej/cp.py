import datetime


def get_date(request):
    return {'jajeczko': datetime.datetime.now().date()}
