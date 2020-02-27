from flask import Flask, render_template, request, send_file
import database
import getJson
import sys
from os import system

import json

#try:
#    if sys.argv[1] != "":
#        event_key = sys.argv[1]
#except:
#event_key = "2019paca"
# system("python3 getJson.py " + "2019tes")
app = Flask(__name__)

constants = json.load(open('./static/constants.json'))

for item in constants["tables"]:
    database.create_table(item)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/raw_data', methods=['GET', 'POST'])
def raw_data():
    data = database.get_data()
    return render_template('data_viewer/raw_data.html', allData=json.dumps(data), constants=json.dumps(constants))

@app.route('/exports', methods=['GET', 'POST'])
def exports():
    return render_template('data_viewer/exports.html')

@app.route('/calculated_team_averages', methods=['GET', 'POST'])
def calculated_team_averages():
    data = database.getData()
    return render_template('data_viewer/calculated_team_averages.html', allData=json.dumps(data), constants=json.dumps(constants))

@app.route('/form', methods=['GET', 'POST'])
def return_form():
    return render_template('forms/' + request.args.get('type') + '_scouting.html', constants=json.dumps(constants))

@app.route('/submit', methods=['GET', 'POST'])
def submit_form():
    database.submit_form(request.get_json(), request.args.get('form'))
    return render_template('submitted.html')

@app.route('/csv_export', methods=['GET', 'POST'])
def csv_export():
    database.create_csv(request.args.get('table'))
    return send_file(request.args.get('table') + '.csv', as_attachment=True)

@app.route('/icon.png', methods=['GET', 'POST'])
def icon():
    return send_file('icon.png')

@app.route('/teamInformation.json', methods=['GET', 'POST'])
def teamInformation():
    return send_file('teamInformation.json')

@app.route('/autofill.js', methods=['GET', 'POST'])
def autofill():
    return send_file('autofill.js')

if __name__ == '__main__': app.run(host='0.0.0.0',port='8080')
