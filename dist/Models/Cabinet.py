from dist.Models.Base import *

# Модель описывает сущность(таблицу) БД Cabinets

class Cabinet(Base):
    window_name = 'Кабинеты'
    # название и тип полей (столбцов)
    id = PrimaryKeyField(unique=True)
    name = CharField(max_length=15,null=False,unique=True)
    department = CharField(max_length=150,null=False)

    # название таблицы
    class Meta:
        table_name = 'Cabinets'
        messages = {
            'name.required': 'Введите имя',
            'required': 'Введите значение',
            'unique': 'Значение должно быть уникальным',

        }

