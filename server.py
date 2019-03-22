from flask import Flask, render_template, request, send_file
import database
import getJson
import sys
from os import system
#try:
#    if sys.argv[1] != "":
#        event_key = sys.argv[1]
#except:
#event_key = "2019paca"
#system("python3 getJson.py " + event_key)
app = Flask(__name__)
database.create_table()
database.create_mechanical_table()
database.create_electrical_table()
database.create_programming_table()

database.create_media_table()
database.create_fundraising_table()

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/match_scouting', methods=['GET', 'POST'])
def match_scouting():
    return render_template('form.html')

@app.route('/submitted_match', methods=['GET', 'POST'])
def submitted_match():
    database.submit(team_number=request.form['team'], matchNumber=request.form['matchNumber'], starting_level=request.form['starting_level'], cargoHigh=request.form['cargoHigh'], cargoMid=request.form['cargoMid'], cargoLow=request.form['cargoLow'], hatchHigh=request.form['hatchHigh'], hatchMid=request.form['hatchMid'], hatchLow=request.form['hatchLow'], otherSide=request.form['otherSide'], climb=request.form['climb'], other=request.form['other'])
    return render_template('submitted.html')

#Engineering Scouting Forms

@app.route('/mechanical_scouting', methods=['GET', 'POST'])
def mechanical_scouting():
    return render_template('mechanical_scouting.html')

@app.route('/submitted_mechanical', methods=['GET', 'POST'])
def submitted_mechanical():
    database.submit_mechanical(teamNumber=request.form['teamNumber'], notes=request.form['notes'])
    return render_template('submitted.html')


@app.route('/electrical_scouting', methods=['GET', 'POST'])
def electrical_scouting():
    return render_template('electrical_scouting.html')

@app.route('/submitted_electrical', methods=['GET', 'POST'])
def submitted_electrical():
    database.submit_electrical(teamNumber=request.form['teamNumber'], teamStructure=request.form['teamStructure'], numberOfMembers=request.form['numberOfMembers'], timeManagement=request.form['timeManagement'], waitsOnMechanical=request.form['waitsOnMechanical'], dictatedSizePosition=request.form['dictatedSizePosition'], timeToFinalize=request.form['timeToFinalize'], anythingDifferent=request.form['anythingDifferent'], anythingSpecial=request.form['anythingSpecial'], brownoutPrevention=request.form['brownoutPrevention'], preseasonContent=request.form['preseasonContent'], helpsWithStrategy=request.form['helpsWithStrategy'], pneumatics=request.form['pneumatics'], anyEncoders=request.form['anyEncoders'], encodersUse=request.form['encodersUse'], canOrPwm=request.form['canOrPwm'], wiredLEDs=request.form['wiredLEDs'], other=request.form['other'])
    return render_template('submitted.html')

@app.route('/programming_scouting', methods=['GET', 'POST'])
def programming_scouting():
    return render_template('programming_scouting.html')

@app.route('/submitted_programming', methods=['GET', 'POST'])
def submitted_programming():
    database.submit_programming(teamNumber=request.form['teamNumber'], usesGithub=request.form['usesGithub'], progSize=request.form['progSize'], programLang=request.form['programLang'], other=request.form['other'])
    return render_template('submitted.html')


#BAM Scouting Forms Form

@app.route('/media_scouting', methods=['GET', 'POST'])
def media_scouting():
    return render_template('media_scouting.html')

@app.route('/submitted_media', methods=['GET', 'POST'])
def submitted_media():
    database.submit_media(teamNumber=request.form['teamNumber'], notes=request.form['notes'])
    return render_template('submitted.html')


@app.route('/fundraising_scouting', methods=['GET', 'POST'])
def fundraising_scouting():
    return render_template('fundraising_scouting.html')

@app.route('/submitted_fundraising', methods=['GET', 'POST'])
def submitted_fundraising():
    database.submit_fundraising(teamNumber=request.form['teamNumber'], notes=request.form['notes'])
    return render_template('submitted.html')



#CSV Exports

@app.route('/programming_data', methods=['GET', 'POST'])
def programming_csv():
    database.create_programming_csv()
    return send_file('programming.csv')

@app.route('/electrical_data', methods=['GET', 'POST'])
def electrical_csv():
    database.create_electrical_csv()
    return send_file('electrical.csv')

@app.route('/mechanical_data', methods=['GET', 'POST'])
def mechanical_csv():
    database.create_mechanical_csv()
    return send_file('mechanical.csv')

@app.route('/match_data', methods=['GET', 'POST'])
def download_csv():
    database.create_csv()
    return send_file('output.csv')

@app.route('/icon.png', methods=['GET', 'POST'])
def icon():
    return send_file('icon.png')

@app.route('/font.ttf', methods=['GET', 'POST'])
def font():
    return send_file('font.ttf')

@app.route('/teamInformation.json', methods=['GET', 'POST'])
def teamInformation():
    return send_file('teamInformation.json')

@app.route('/autofill.js', methods=['GET', 'POST'])
def autofill():
    return send_file('autofill.js')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
