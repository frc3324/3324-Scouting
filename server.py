from flask import Flask, render_template, request, send_file
import database

app = Flask(__name__)
database.create_table()
database.create_pit_table();

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/match_scouting', methods=['GET', 'POST'])
def match_scouting():
    return render_template('form.html')

@app.route('/pit_scouting', methods=['GET', 'POST'])
def pit_scouting():
	return render_template('pit_scouting.html')

@app.route('/submitted_pit', methods=['GET', 'POST'])
def submitted_pit():
	database.submit_pit_table(uses_Github=request.form['uses_Github'])
	return render_template('submitted.html')

@app.route('/submitted_match', methods=['GET', 'POST'])
def submitted_match():
    database.submit(team_number=request.form['team'], sandstorm_rocket_points=request.form['sandstorm_rocket_points'], sandstorm_cargoship_points=request.form['sandstorm_cargoship_points'], starting_level=request.form['starting_level'], teleop_rocket_points=request.form['teleop_rocket_points'], teleop_cargoship_points=request.form['teleop_cargoship_points'], climb=request.form['climb'], other=request.form['other'])
    return render_template('submitted.html')

@app.route('/download_data', methods=['GET', 'POST'])
def download_csv():
    database.create_csv()
    return send_file('output.csv')

@app.route('/graphic.png', methods=['GET', 'POST'])
def graphic():
    return send_file('graphic.png')


if __name__ == "__main__":
    app.run(host='0.0.0.0')