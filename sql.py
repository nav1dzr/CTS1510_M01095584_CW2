
import sqlite3
conn = sqlite3.connect('DATA/telligence_platform.db')


def add_user(conn,name,hash):
    curr = conn.cursor()
    sql = ("""INSERT INTO users (username, password_hash) VALUES (?, ?) """)
    param = (name,hash) 
    curr.execute(sql,param)
    conn.commit()


def get_user():
    curr = conn.cursor()
    sql = ("""SELECT * FROM users""")
    curr.execute(sql)
    users = curr.fetchall()
    return users

def migrate_user_data():
    with open("DATA/users.txt", "r") as f:
        users = f.readlines()
    for user in users:
       name, hash = user.strip().split(",")
       add_user(conn,name,hash)
    conn.close()