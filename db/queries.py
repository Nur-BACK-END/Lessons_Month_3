CREATE_TABLE_registered = """
    CREATE TABLE IF NOT EXISTS registered(
    id TNTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT,
    age TEXT,
    gender  TEXT,
    email TEXT,
    photo TEXT
    
    )
"""


INSERT_registered_QUERY = """
    INSERT INTO O registered (fullname,age,gender,email,photo)
    VALUES (?,?,?,?,?)
"""




CREATE_TABLE_products_details  = """
    CREATE TABLE IF NOT EXISTS products_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    productid TEXT,
    category TEXT,
    infoproduct TEXT
    )
"""

INSERT_products_details_QUERY = """
    INSERT INTO products_details (productid, category, infoproduct)
    VALUES (?, ?, ?)
"""



CREATE_TABLE_store = """
CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product TEXT,
    size TEXT,
    price REAL,
    photo TEXT,
    productid INTEGER
)
"""

CREATE_TABLE_collection_products = """
    CREATE TABLE IF NOT EXISTS collection_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    productid TEXT,
    collection TEXT
    )
"""

INSERT_collection_QUERY = """
    INSERT INTO collection (id, productid, collcetion)
    VALUES (?, ?)
"""

INSERT_store_QUERY = """
INSERT INTO store (name_product, size, price, photo, productid)
VALUES (?, ?, ?, ?, ?)
"""