from dist.Models.Base import *
from dist.Models.Cabinet import Cabinet


class Electrical_line(Base):
    id = PrimaryKeyField(unique=True)
    state = BooleanField(null=False)
    cabinet_id = ForeignKeyField(Cabinet,unique=True)

    class Meta:
        table_name = 'Electrical_lines'