from dist.Connection.connection_peewee import *

class Controller():
    if __name__ == '__main__':
        try:
            connect_peewee().connect()
            connect_peewee()

        except peewee.DatabaseError as px:
            print("Controller")
            print(str(px))






