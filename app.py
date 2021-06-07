from peewee import *
import os.path
from sys import argv
from datetime import datetime
from random import randint

name_db = 'DB.db'
db = SqliteDatabase(name_db)


class BaseModel(Model):
    class Meta:
        database = db


class clients(BaseModel):
    name = CharField()
    city = CharField()
    address = CharField()


class orders(BaseModel):
    client = ForeignKeyField(clients, backref='client')
    date = DateField()
    amount = IntegerField()
    description = CharField()


def create_tables():
    file_path = name_db
    if (os.path.exists(file_path) == True):
        os.remove(name_db)
        print('>> removed')
    db.create_tables([clients, orders])
    print('>> created')


def R(j):

    D = [
        ['Anna', 'Nikita', 'Ivan', 'Sofya', 'Danil', 'Arina', 'Petr', 'Igor'],
        ['Surgut', 'Kogalym', 'Nizhnevartovsk', 'Lynator',
            'Megion', 'Barsovo', 'Solnechniy', 'Nefteugansk'],
        ['Lenina', 'Mira', '30 let pobedy', 'Profsouzov',
            'Universitetskaya', 'Bakhilova'],
        ['2019-12-05', '2015-04-11', '2020-01-01', '2019-06-25',
            '2018-07-12' '2015-08-01', '2010-03-14'],
        ['Izosoft', 'Pux', 'Sintepon', 'Sintetika', 'Sherst', 'Shelter', 'Termofin']
    ]

    return (D[j][randint(0, len(D[j])-1)])


def filling_tables():
    N = 15
    for i in range(N):
        note = clients.create(name=R(0), city=R(1), address=R(2))
        note.save()
    for i in range(N):
        note = orders.create(client=randint(0, 15), date=R(
            3), amount=randint(100, 10000), description=R(4))
        note.save()
    print('>> filled')


def print_tables(tablename):
    if tablename == 'clients':
        print('\nИмя\tГород\tАдресс')
        query = clients.select().order_by(clients.id)
        for row in query:
            print(row.name, row.city, row.address, sep='\t', end='\n')
    elif tablename == 'orders':
        print('\nId Клиента\t\tДата\t\tСумма\t\tОписание')
        query = orders.select().order_by(orders.id)
        for row in query:
            print(row.client, row.date, row.amount,
                row.description, sep='\t\t', end='\n')
    else:
        print('Такой таблицы не существует')


if __name__ == "__main__":
    try:
        action = argv[1]
        if action == 'init':
            create_tables()
        if action == 'fill':
            filling_tables()
        if action == 'show':
            tablename = argv[2]
            print_tables(tablename)
        if action == 'all':
            create_tables()
            filling_tables()
            tablename = argv[2]
            print_tables(tablename)
    except:
        print("Справка:\nЗапуск программы >> python app.py параметр\nПараметры:\n\tinit - создание базы данных;\n\tfill - заполнение базы данными;\n\tshow [tablename] - показать содержимое таблицы;\n\tall [tablename] - создание, заполнение, вывод;\nСуществующие таблицы: clients, orders")
    v = len(clients.select())
    print(v)
