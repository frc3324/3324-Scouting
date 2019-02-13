from flask import Flask, render_template, request, send_file
import database
import getJson

app = Flask(__name__)
database.create_table()
database.create_mechanical_table()
database.create_electrical_table()
database.create_programming_table()

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/match_scouting', methods=['GET', 'POST'])
def match_scouting():
    return render_template('form.html')

@app.route('/submitted_match', methods=['GET', 'POST'])
def submitted_match():
    database.submit(team_number=request.form['team'], sandstorm_rocket_points=request.form['sandstorm_rocket_points'], sandstorm_cargoship_points=request.form['sandstorm_cargoship_points'], starting_level=request.form['starting_level'], teleop_rocket_points=request.form['teleop_rocket_points'], teleop_cargoship_points=request.form['teleop_cargoship_points'], climb=request.form['climb'], other=request.form['other'])
    return render_template('submitted.html')



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

@app.route('/font.ttf', methods=['GET', 'POST'])
def font():
    return send_file('font.ttf')

@app.route('/2018ohcl.json', methods=['GET', 'POST'])
def ohcl():
    return send_file('2018ohcl.json')

@app.route('/autofill.js', methods=['GET', 'POST'])
def autofill():
    return send_file('autofill.js')

if __name__ == "__main__":
    app.run(host='0.0.0.0')