import random
from random import randint
from conf import MODEL
import os
import json
AUTHOR_FILE = ''

dict_book = {
    'model' : MODEL
}

authors = ['F.Dostaevskiy', 'A.Pushkin', 'L.Tolstoy']
with open('authors.txt', 'w') as file:
    for line in authors:
        file.write(line + '\n')


title = ['Apple', 'Orange', 'Lime']
with open('books.txt', 'w') as file:
    for line in title:
        file.write(line + '\n')

pk = dir(os)
count = 1
for i in pk:
    count += 1



discount = int(randint(0,100))


def func_gen(pk = 1):
    while True:
        yield {
            "pk": pk,
            "title": None,
            "year": func_gen_y(),
            "pages": func_gen_pag,
            "isbn13":None,
            "rating": func_gen_rat(),
            "price":func_gen_pri(),
            "discount" :func_gen_discount(),
            "author" : None

        }
        pk += 1


def func_gen_y():
    year = int(randint(1760, 1890))
    return year

def func_gen_pag():
    pages = int(randint(50, 1700))
    return pages

def func_gen_rat():
    rating = float(randint(1, 5))
    return rating

def func_gen_pri():
    price = float(randint(250, 1700))
    return price

def func_gen_discount():
    discount = int(randint(0, 100))
    return discount



# # ToDo через if main
# 1 инициализировать функцию генартор
# сгенерировать список из n книг (словарей)
# записать в файл в формате json

if __name__ == '__main__':
    def func_gen(pk=1)
        print(func_gen())

