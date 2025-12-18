import mysql.connector
from rich import print as pr
from platform import system
import random
import os
import time


# ============> starting xampp <=============

system_name = system()
if system_name == 'Windows':
    pr('[blue] Starting xampp ...')
    os.system('cd/ && cd xampp && start xampp_start.exe')
    time.sleep(5)
    pr('[green]Xampp started.')

elif system_name == 'Linux':
    os.system('sudo /opt/lampp/xampp start')
    pr('[green]Xampp started\n')

# ============> do have a database or no <============

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database=f'')
cursor = cnx.cursor()
do_have_database = input('Do you have a database ? y/n =>')

if do_have_database == 'n':
    database_name = input('enter a name to create a data base =>')
    create_database = f'CREATE DATABASE {database_name}'
    cursor.execute(create_database)

database = input('ENTER YOUR DATABASE NAME =>>')

# ===========> connecting to database <============

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database=f'{database}')
pr("[green]connected to the database\n")

cursor = cnx.cursor()
do_have_table = input('Do you have a table ? y/n =>')

if do_have_table == 'n':
    table_name = input('enter a name to create a table =>')
    create_database = f'CREATE TABLE {table_name} (User varchar(20), password int(4), score_hads int(3))'
    cursor.execute(create_database)

table = input('ENTER YOUR TABLE OF USER AND PASSWORD NAME =>>')

# ===========> login or sing up<==========

dic = dict()

while True:
    ls = input("login? or sing up? (for login use l for sing up use s): ")

    if ls == 'l':
        read = f'SELECT `User`, `password` FROM `{table}`;'
        cursor.execute(read)
        for (User, password) in cursor:
            dic[User] = password
        name = input("Enter your user name:")

        if name in dic.keys():
            pas = input("Enter your password:")
            pas = int(pas)

            if pas == int(dic[name]):
                pr(f'[green]hi {name} wellcome to my project!')
                check = 'y'
                break
        else:
            print("sing up first!!\n")

    elif ls == 's':
        read = f'SELECT `User`, `password` FROM `{table}`;'
        cursor.execute(read)

        for (User, password) in cursor:
            dic[User] = password

        name = input("Enter your user name:")
        pas = input("Enter your password:")
        write = f'INSERT INTO {table} VALUES(\'{name}\', \'{pas}\', 0)'

        if name not in dic.keys():
            cursor.execute(write)
            cnx.commit()
            print("done!!now login again\n")
        else:
            print("this name is already taken\n")


# ===========> def`s <===========

def check_in():
    if check == 'y':
        pr("""
[blue]baraye bazi hadse adad benevis (game);
[deep_sky_blue1]baraye didan user haye table khod benevis (users);
[yellow]baraye sakht qrcode benevis (qrcode);
[purple4]baraye didan emtiaze benevis (score);

[red]baraye khoroj benevis (exit);


""")


def game():
    global read_score
    number = random.randint(1, 100)

    hads = input("hadse khod ra vared konid:")
    hads = int(hads)
    score = 0
    try_hads = 0

    while hads != number:
        try_hads += 1
        if number > hads:
            pr("[red]my number is bigger\n")
        elif number < hads:
            pr("[red]my number is smaller\n")

        hads = input("hadse khod ra vared konid:")

        hads = int(hads)

    if hads == number:
        pr('[green]yooo haa!!! you did it!!!!')

    if try_hads == 1:
        score = 10

    elif 5 >= try_hads > 1:
        score = 5
    elif 10 >= try_hads > 5:
        score = 2

    print(f'you got {score} score')

    read = f'SELECT `score_hads` FROM `{table}` WHERE User = \'{name}\''

    cursor.execute(read)

    for score_hads in cursor:
        read_score = score_hads

    read_score = read_score[0]

    read_score = int(read_score)

    game_score = score + read_score

    set_score = f'UPDATE `{table}` SET `score_hads`=\'{game_score}\' WHERE User = \'{name}\''

    cursor.execute(set_score)
    cnx.commit()

def total_score():
    global read_score
    read = f'SELECT `score_hads` FROM `{table}` WHERE User = \'{name}\''

    cursor.execute(read)

    for score_hads in cursor:
        read_score = score_hads

    print('your score =', read_score[0])



    # ============> what should do? <============


check_in()
kar = input(":")

while kar != 'exit':

    if kar == 'game':
        game()
        check_in()
    elif kar == 'score':
        total_score()
        check_in()

    kar = input(":")

# ============> stopping xampp <=============
if kar == 'exit':
    cursor.close()
    cnx.close()

    if system_name == 'Windows':
        pr('[blue] Stopping xampp ...')
        os.system('cd/ && cd xampp && start xampp_stop.exe')
        time.sleep(7)
        pr('[green]Xampp stopped.')

    elif system_name == 'Linux':
        pr('[blue] Stopping xampp ...')
        os.system('sudo /opt/lampp/xampp stop')
        pr('[green]Xampp stopped.\n')