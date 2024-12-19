import sqlite3
from db import queries

store_db = sqlite3.connect('db/store.sqlite3')
products_db = sqlite3.connect('db/products_details.sqlite3')
collections_db = sqlite3.connect('db/collections.sqlite3')

store_cursor = store_db.cursor()
products_cursor = products_db.cursor()
collections_cursor = collections_db.cursor()

async def database_create_store():
    if store_db:
        print('База данных магазина уже существует')
    store_cursor.execute(queries.CREATE_TABLE_store)

async def database_create_products_details():
    if products_db:
        print('База данных с подробной информацией о продуктах уже существует.')
    products_cursor.execute(queries.CREATE_TABLE_products_details)

async def database_create_collections():
    if collections_db:
        print('База данных коллекций уже существует')
    products_cursor.execute(queries.CREATE_TABLE_products_details)

async def sql_insert_store(modelname, size, price, productid, photo):
    store_cursor.execute(queries.INSERT_store_QUERY, (
        modelname, size, price, productid, photo
    ))
    store_db.commit()

async def sql_insert_products_details(productid, category, infoproduct):
    products_cursor.execute(queries.INSERT_products_details_QUERY, (
        productid, category, infoproduct
    ))
    products_db.commit()

async def sql_insert_collections(productid, category):
    collections_cursor.execute(queries.INSERT_collection_QUERY, (
        productid, category
    ))


# CRUD - Read
# =====================================================

# Основное подключение к базе (Для CRUD)
def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    SELECT * from store s
    INNER JOIN store_details  sd 
    ON s.product_id = sd.product_id
    """).fetchall()
    conn.close()
    return products


# CRUD - Delete
# =====================================================

def delete_product(product_id):
    conn = get_db_connection()

    conn.execute('DELETE FROM store WHERE product_id = ?', (product_id,))

    conn.commit()
    conn.close()