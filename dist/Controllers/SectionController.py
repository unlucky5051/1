from dist.Models.Section import *

class SectionController():

    def add(self,name):
        validator = ModelValidator(Section(name = name))
        if validator.validate():
            Section.create(name = name)
            print('Секция ламп добавлена')
        else:
            print('Ошибка -', validator.errors['name'])

    def print_get(self):
        for row in Section.select():
            print(row.id, row.name)

