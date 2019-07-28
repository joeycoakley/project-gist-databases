import sqlite3
import gists_database.importer
from gists_database.models import Gist
from datetime import datetime
db = sqlite3.connect('tests/populated_gists_database.db')
db.row_factory = sqlite3.Row

# cursor = db.execute('SELECT * FROM gists')

# for gist in cursor:
#     print('Github Id: ', gist['github_id'])
#     print('Html Url: ', gist['html_url'])
#     print('Git Pull Url: ', gist['git_pull_url'])
#     print('Git Push Url: ', gist['git_push_url'])
#     print('Commits Url: ', gist['commits_url'])
#     print('Forks Url: ', gist['forks_url'])
#     print('Public: ', gist['public'])
#     print('Created At: ', gist['created_at'])
#     print('Updated At: ', gist['updated_at'])
#     print('Comments: ', gist['comments'])
#     print('Comments Url: ', gist['comments_url'])
#     print('=' * 60)


def search_gists(db_connection, **kwargs):
    query = '''
        SELECT * FROM gists '''
    
    for kwarg, value in kwargs.items():
        if isinstance(value, datetime):
            query = query + 'WHERE datetime({}) == datetime(:{})'.format(kwarg, kwarg)
        else:
            query = query + 'WHERE {} = :{}'.format(kwarg, value)
    cursor = db_connection.execute(query, kwargs)
    results = [Gist(gist) for gist in cursor]
    return results


    # 2014-05-03T20:26:08Z

d = datetime(2014, 5, 3, 20, 26, 8)

print(search_gists(db, html_url='https://gist.github.com/18bdf248a679155f1381'))



# gist = gists[0]
# gist.github_id == '18bdf248a679155f1381'