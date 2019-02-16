import csv
import sqlite3

def create_table():
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE scouting (team_number int , matchNumber int ,  starting_level int , cargoHigh int, cargoMid int, cargoLow int, hatchHigh int, hatchMid int, hatchLow int, climb int, other text)''')
    except Exception as e: print(e)

def submit(team_number, matchNumber, starting_level, cargoHigh, cargoMid, cargoLow, hatchHigh, hatchMid, hatchLow, otherSide, climb, other):
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    scouting_info = (int(team_number), int(matchNumber), int(starting_level), int(cargoHigh), int(cargoMid), int(cargoLow), int(hatchHigh), int(hatchMid), int(hatchLow), int(climb), other)
    cursor.execute("INSERT INTO scouting VALUES (?,?,?,?,?,?,?,?,?,?,?)", scouting_info)
    conn.commit()

def create_mechanical_table():
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE mechanical (teamNumber int, notes text) ''')
    except Exception as e: print(e)

def submit_mechanical(teamNumber, notes):
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    mechanical_info = (teamNumber, notes);
    cursor.execute("INSERT INTO mechanical VALUES (?, ?)", (mechanical_info))
    conn.commit()


def create_electrical_table():
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE electrical (teamNumber int, teamStructure text, numberOfMembers int, timeManagement text, waitsOnMechanical int, dictatedSizePosition text, timeToFinalize text, anythingDifferent text, anythingSpecial text, brownoutPrevention text, preseasonContent text, helpsWithStrategy int, pneumatics text, anyEncoders int, encodersUse text, canOrPwm text, wiredLEDs text, other text) ''')
    except Exception as e: print(e)

def submit_electrical(teamNumber, teamStructure, numberOfMembers, timeManagement, waitsOnMechanical, dictatedSizePosition, timeToFinalize, anythingDifferent, anythingSpecial, brownoutPrevention, preseasonContent, helpsWithStrategy, pneumatics, anyEncoders, encodersUse, canOrPwm, wiredLEDs, other):
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    electrical_info = (int(teamNumber), teamStructure, int(numberOfMembers), timeManagement, int(waitsOnMechanical), dictatedSizePosition, timeToFinalize, anythingDifferent, anythingSpecial, brownoutPrevention, preseasonContent, int(helpsWithStrategy), pneumatics, int(anyEncoders), encodersUse, canOrPwm, wiredLEDs, other);
    cursor.execute("INSERT INTO electrical VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (electrical_info))
    conn.commit()


def create_programming_table():
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE programming (teamNumber int, usesGithub int, progSize int, programLang text, other text) ''')
    except Exception as e: print(e)

def submit_programming(teamNumber, usesGithub, progSize, programLang, other):
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    programming_info = (int(teamNumber), int(usesGithub), int(progSize), programLang, other)
    cursor.execute("INSERT INTO programming VALUES (?,?,?,?,?)", (programming_info))
    conn.commit()

#BAM Stuff

def create_media_table():
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE media (teamNumber int, notes text) ''')
    except Exception as e: print(e)

def submit_media(teamNumber, notes):
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    media_info = (teamNumber, notes);
    cursor.execute("INSERT INTO media VALUES (?, ?)", (media_info))
    conn.commit()

def create_fundraising_table():
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE fundraising (teamNumber int, notes text) ''')
    except Exception as e: print(e)

def submit_fundraising(teamNumber, notes):
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    fundraising_info = (teamNumber, notes);
    cursor.execute("INSERT INTO fundraising VALUES (?, ?)", (fundraising_info))
    conn.commit()

#CSV Exports

def create_programming_csv():
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    data = cursor.execute("SELECT * FROM programming")
    with open('programming.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(('Github?'))
        writer.writerows(data)


def create_electrical_csv():
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    data = cursor.execute("SELECT * FROM electrical")
    with open('electrical.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(('Good Wires?'))
        writer.writerows(data)

def create_mechanical_csv():
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    data = cursor.execute("SELECT * FROM mechanical")
    with open('mechanical.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(('Notes'))
        writer.writerows(data)


def create_csv():
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    data = cursor.execute("SELECT * FROM scouting")
    with open('output.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(('Team Number', 'Starting Point', 'Cargo High', 'Cargo Mid', 'Cargo Low', 'Hatch High', 'Hatch Mid', 'Hatch Low', 'Climb', 'Other'))
        writer.writerows(data)
