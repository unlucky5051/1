from dist.Models.Base import *
from dist.Models.Cabinet import *
# Модель описывает сущность(таблицу) БД Air_conditioners

class Air_conditioners(Base):
    window_name = 'Кондиционеры'
    # название и тип полей (столбцов)
    id = PrimaryKeyField(unique=True)
    name = CharField(max_length=15,null=False,unique=True)
    state = BooleanField()
    cabinet_id = ForeignKeyField(Cabinet)

    class Meta:
        table_name = 'Air_conditioners'