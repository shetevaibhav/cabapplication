import sqlite3
conn=sqlite3.connect("cabsbooking.db")
conn.cursor()
try:
    conn.execute('''
        CREATE TABLE admin(
            admin_id INTEGER PRIMARY KEY,
            admin_username varchar(20) NOT NULL,
            admin_password varchar(20) NOT NULL)''')

    conn.execute('''
        CREATE TABLE car_dealar
        (
            car_dealarid INTEGER PRIMARY KEY,
            car_dealarname varchar(20) NOT NULL,
            car_dealarpassword varchar(20) NOT NULL,
            car_dealaremail varchar(20) NOT NULL,
            car_dealarphone varchar(20) NOT NULL) ''')

    conn.execute('''
        CREATE TABLE cabs
        (
            cab_id INTEGER PRIMARY KEY,
            cab_name varchar(20) NOT NULL,
            cab_number varchar(20) NOT NULL,
            cab_type varchar(20) NOT NULL,
            cab_model varchar(20) NOT NULL,
            cab_delarid INT(11) NOT NULL,
            cab_from varchar(20) NOT NULL,
            cab_to varchar(20) NOT NULL)''')

    conn.execute('''
        CREATE TABLE users
        (
            user_id INTEGER PRIMARY KEY,
            user_name varchar(20) NOT NULL,
            user_password varchar(20) NOT NULL,
            user_email varchar(20) NOT NULL,
            user_phone INT(20) NOT NULL)''')
    print("table created sucessfully")
except:
    print("tables are not created")