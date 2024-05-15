from dist.Config.config_peewee import *


# Базовая модель

class Base(Model):
    window_name = 'Название окна'

    class Meta:
        # подключение к БД
        database = connect_peewee()
        messages = {
            'name.required': 'Введите имя',
            'required': 'Введите значение',
            'unique': 'Значение должно быть уникальным',

        }
