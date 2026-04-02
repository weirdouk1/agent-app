from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///data.db")

with engine.connect() as conn:

  conn.execute(text("""
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
  )
  """))

  conn.execute(text("""
  CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER
  )
  """))

  conn.execute(text("""
  CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    product_id INTEGER,
    amount INTEGER
  )
  """))

  conn.execute(text("DELETE FROM users"))
  conn.execute(text("DELETE FROM products"))
  conn.execute(text("DELETE FROM orders"))

  conn.execute(text("""
  INSERT INTO users (name, city) VALUES
  ('Ravi', 'Hyderabad'),
  ('Anita', 'Mumbai'),
  ('Kiran', 'Bangalore')
  """))

  conn.execute(text("""
  INSERT INTO products (name, price) VALUES
  ('Laptop', 70000),
  ('Phone', 30000),
  ('Tablet', 20000)
  """))

  conn.execute(text("""
  INSERT INTO orders (user_id, product_id, amount) VALUES
  (1, 1, 70000),
  (2, 2, 30000),
  (3, 3, 20000),
  (1, 2, 30000)
  """))

  conn.commit()

print("✅ Multi-table DB ready")