from flask import render_template, redirect, request
from baseball_app import app
from baseball_app.models.team import Team


@app.route('/')
def index():
    return redirect('/teams')

@app.route('/teams')
def teams():
    teams = Team.get_all()
    return render_template("index.html", all_teams = teams)


@app.route('/create/team',methods=['POST'])
def create_team():
    Team.save(request.form)
    return redirect('/teams')

@app.route('/team/<int:id>')
def show_team(id):
    data = {
        "id": id
    }
    return render_template('team.html', team=Team.get_one_with_players(data))