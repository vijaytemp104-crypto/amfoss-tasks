import sqlite3


def make_tables():
    db = sqlite3.connect("berry_broker.db")
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                wallet INTEGER DEFAULT 1000,
                bank INTEGER DEFAULT 0,
                last_sail INTEGER DEFAULT 0)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS inventory (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            item_name TEXT,
            status TEXT DEFAULT 'active')""")
    
    db.commit()
    db.close()


def add_new_user(user_id):
    db = sqlite3.connect("berry_broker.db")
    cur = db.cursor()

    cur.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)",(user_id,))

    db.commit()
    db.close()


def check_balance(user_id):
    add_new_user(user_id)

    db = sqlite3.connect("berry_broker.db")
    cur = db.cursor()

    cur.execute("SELECT wallet, bank FROM users WHERE user_id = ?",(user_id,))

    balance = cur.fetchone()

    db.close()

    return balance

def get_last_sail(user_id):
    add_new_user(user_id)

    db = sqlite3.connect("berry_broker.db")
    cur = db.cursor()

    cur.execute("SELECT last_sail FROM users WHERE user_id = ?",(user_id,))

    last_sail = cur.fetchone()[0]

    db.close()

    return last_sail


def give_sail_reward(user_id, reward, current_time):
    db = sqlite3.connect("berry_broker.db")
    cur = db.cursor()

    cur.execute("""UPDATE users
        SET wallet = wallet + ?, last_sail = ?
        WHERE user_id = ?""",(reward, current_time, user_id))

    db.commit()
    db.close()

def trade_berries(sender_id, receiver_id, amount):
    add_new_user(sender_id)
    add_new_user(receiver_id)

    db = sqlite3.connect("berry_broker.db")
    cur = db.cursor()

    cur.execute("SELECT wallet FROM users WHERE user_id = ?",(sender_id,))

    sender_wallet = cur.fetchone()[0]

    if sender_wallet < amount:
        db.close()
        return False

    cur.execute("UPDATE users SET wallet = wallet - ? WHERE user_id = ?",(amount, sender_id))

    cur.execute("UPDATE users SET wallet = wallet + ? WHERE user_id = ?",(amount, receiver_id))

    db.commit()
    db.close()

    return True
def buy_item(user_id,item_name,price):
    add_new_user(user_id)
    db = sqlite3.connect("berry_broker.db")
    cur = db.cursor()

    cur.execute("SELECT wallet FROM users WHERE user_id = ?",(user_id,))

    wallet = cur.fetchone()[0]
    if wallet < price:
        db.close()
        return False

    cur.execute("UPDATE users SET wallet = wallet - ? WHERE user_id = ?",(price, user_id))
    cur.execute("INSERT INTO inventory (user_id, item_name) VALUES (?, ?)",(user_id, item_name))

    db.commit()
    db.close()

    return True

def get_inventory(user_id):
    db = sqlite3.connect("berry_broker.db")
    cur = db.cursor()
    cur.execute(
         """SELECT item_name, status, COUNT(*)
        FROM inventory
        WHERE user_id = ?
        GROUP BY item_name, status""",
        (user_id,))

    items = cur.fetchall()

    db.close()

    return items

def get_richest_users():
    db = sqlite3.connect("berry_broker.db")
    cur = db.cursor()

    cur.execute("""
        SELECT user_id, wallet + bank
        FROM users
        ORDER BY wallet + bank DESC
        LIMIT 5
    """)

    richest_users = cur.fetchall()

    db.close()

    return richest_users
