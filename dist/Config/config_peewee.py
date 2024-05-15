from peewee import *
def connect_peewee():
    return MySQLDatabase(
        'VikV1234_smartoffice',
        user = 'VikV1234_unlucky',
        password = '111111',
        host = '10.11.13.118'
    )