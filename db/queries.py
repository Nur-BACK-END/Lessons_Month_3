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