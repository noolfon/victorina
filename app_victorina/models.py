import time
import csv
from peewee import (SqliteDatabase, Model, TextField, AutoField)

db = SqliteDatabase('data_riddles.db')


class _Model(Model):
    class Meta:
        database = db


class Riddles(_Model):
    class Meta:
        db_table = "table_riddles"

    id = AutoField(primary_key=True)
    riddles = TextField(null=True)
    response = TextField(null=True)

    def __str__(self):
        return f'{self.riddles},{self.response}'


# def init_db():
#     Riddles.drop_table("table_riddles")
#     Riddles.create_table()
#     count = 0
#     with open('list_riddles.csv', 'r', encoding="utf-8") as file:
#         reader = csv.reader(file, delimiter=',')
#         for s in reader:
#             try:
#                 count += 1
#                 Riddles.create(riddles=s[0], response=s[1])
#                 print(count)
#             except Exception as ex:
#                 print(ex)
#                 time.sleep(2)
#                 continue
#     print("db created!")
