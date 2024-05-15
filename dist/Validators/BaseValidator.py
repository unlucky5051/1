import peewee
from peewee_validates import ModelValidator,DEFAULT_MESSAGES

class BaseValidator():

    class Meta:

        messages = {
            'name.required': 'Введите имя',
            'required': 'Введите значение',
            'unique': 'Значение должно быть уникальным',

        }
