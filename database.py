import csv
import sqlite3
import re
import json

constants = json.load(open('./static/constants.json'))


def create_table(table):
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE ''' + str(table) + " " + str(tuple(constants["questionIndexes"][table])))
    except Exception as e: print(e)

def submit_form(data, table):
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    for m in data:
        dataString = ""
        sqlString = "INSERT INTO " + table + " VALUES "
        for x in range (len(json.loads(data[m]))):
            if (x == 0):
                sqlString += "(?"
            else:
                sqlString += ",?"
        sqlString += ")"
        cursor.execute(sqlString, tuple(json.loads(data[m])))
    conn.commit()

def get_data():
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    data = {}
    for item in constants["tables"]:
        cursor.execute("SELECT * FROM " + item)
        data[item] = json.dumps(cursor.fetchall())
    return data

def create_csv(table):
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    data = cursor.execute("SELECT * FROM " + table)
    with open(table + '.csv', 'w', encoding="UTF-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(constants["questions"][table])
        writer.writerows(data)
