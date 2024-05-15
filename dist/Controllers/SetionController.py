from dist.Models.Section import *

class SectionController():

    def get(self):
        return Section.select()

    def print_get(self):
        for el in self.get():
            print(el.name)
    def add(self,name):
        validator = ModelValidator(Section(name=name))
        if validator.validate():
            Section.create(name=name)
            print('Новая запись добавлена')
        else:
            print(validator.errors['name'])
    #  загрузить большое количество данных
    # №1 С помощью СПИСКА СЛОВАРЕЙ и метода CREATE подход медленный по нескольким причинам: https://docs.peewee-orm.com/en/latest/peewee/querying.html
    def add_many_One(self,date):
        for field in date:
            validator = ModelValidator(Section(name=field['name']))
            if validator.validate():
                Section.create(**field)
                print('Новые записи добавлены')
            else:
                print(validator.errors['name'])
        # for field in date:
        #     Section.create(**field)
        print('-------------------------')

    # №2  С помощью СПИСКА КОРТЕЖЕЙ и метода  insert_many() не работает если добавлять одну запись
    def add_many_Two(self,date):
        for field in date:
            flag = False
            error = ''
            validator = ModelValidator(Section(name=field))
            print(field)
            if validator.validate():
                flag = True
            else:
                error = validator.errors['name']

            if flag:
                Section.insert_many(date,fields=[Section.name]).execute()
                print('Новые записи добавлены')
            else:
                print(error)




    def show(self,name):
        validator = ModelValidator(Section(name=name))

        if validator.validate() != True:
            query = Section.get(Section.name == name)
            print(query.id, query.name)
        else:
            print('Нет такой секции')
