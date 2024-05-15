
from Dist.Model.Base import *
from Dist.Model.Cabinet import Cabinet


class Camera(Base):
    window_name = 'Видеонаблюдение'
    id = PrimaryKeyField(unique=True)
    name = CharField(max_length=15,null=False,unique=True)
    link = TextField(null=False)
    cabinet_id = ForeignKeyField(Cabinet.id)

    class Meta:
        table_name = 'Cameras'