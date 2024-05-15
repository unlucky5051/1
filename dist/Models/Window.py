from dist.Models.Base import *
from dist.Models.Condition import *
from dist.Models.Cabinet import Cabinet

class Window(Base):
    id = PrimaryKeyField(unique=True)
    open_close = BooleanField(null = False,default = 0)
    condition_id = ForeignKeyField(Condition)
    cabinet_id = ForeignKeyField(Cabinet)

    class Meta:
        db_table = 'Windows'