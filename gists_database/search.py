from .models import Gist
import sqlite3
from datetime import datetime

def search_gists(db_connection, **kwargs):
    query = '''
        SELECT * FROM gists '''
    
    for kwarg, value in kwargs.items():
        if isinstance(value, datetime):
            query = query + 'WHERE datetime({}) == datetime(:{})'.format(kwarg, kwarg)
        else:
            query = query + 'WHERE {} = :{}'.format(kwarg, kwarg)
    cursor = db_connection.execute(query, kwargs)
    results = [Gist(gist) for gist in cursor]
    return results

