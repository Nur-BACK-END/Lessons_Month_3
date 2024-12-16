import sqlite3
from db import queries


store_db = sqlite3.connect('db/store.sqlite3')
products_db = sqlite3.connect('db/products_details.sqlite3')

store_cursor = store_db.cursor()
products_cursor = products_db.cursor()

async def database_create_store():
    if store_db:
        print('База данных магазина уже существует')
    store_cursor.execute(queries.CREATE_TABLE_shop)

async def database_create_products_details():
    if products_db:
        print('База данных с подробной информацией уже существует.')
    products_cursor.execute(queries.CREATE_TABLE_products_details)

async def sql_insert_store(modelname, size, price, productid, photo):
    store_cursor.execute(queries.INSERT_shop_QUERY, (
        modelname, size, price, productid, photo
    ))
    store_db.commit()

async def sql_insert_products_details(productid, category, infoproduct):
    products_cursor.execute(queries.INSERT_products_details_QUERY, (
        productid, category, infoproduct
    ))
    products_db.commit()