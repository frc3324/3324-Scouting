import csv
import sqlite3

def create_table():
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE scouting (team_number int , sandstorm_rocket_points int , sandstorm_cargoship_points int, starting_level int, teleop_rocket_points int, teleop_cargoship_points int, climb int, other text)''')
    except Exception as e: print(e)

def submit(team_number, sandstorm_rocket_points, sandstorm_cargoship_points, starting_level, teleop_rocket_points, teleop_cargoship_points, climb, other):
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    scouting_info = (int(team_number), int(sandstorm_rocket_points), int(sandstorm_cargoship_points), int(starting_level), int(teleop_rocket_points), int(teleop_cargoship_points), int(climb), other)
    cursor.execute("INSERT INTO scouting VALUES (?,?,?,?,?,?,?,?)", scouting_info)
    conn.commit()

def create_pit_table():
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    try: 
        cursor.execute('''CREATE TABLE pit_scouting (uses_Github int)''')
    except Exception as e: print(e)


def submit_pit_table(uses_Github):
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    scouting_info = (int(uses_Github))
    cursor.execute("INSERT INTO pit_scouting VALUES (?)", (scouting_info,))
    conn.commit()

def create_csv():
    conn = sqlite3.connect('scouting.db')
    cursor = conn.cursor()
    data = cursor.execute("SELECT * FROM scouting")
    with open('output.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(('Team Number', 'Sandstorm Rocket Points', 'Sandstorm Cargoship Points', 'Starting Level', 'Teleop Rocket Points', 'Teleop Cargoship Points', 'Climb', 'Other'))
        writer.writerows(data)

