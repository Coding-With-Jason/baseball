from flask import render_template, redirect, request
from baseball_app import app
from baseball_app.models import team, player

@app.route('/players')
def players():
    
    return render_template('player.html', teams= team.Team.get_all())


@app.route('/create/player',methods=['POST'])
def create_player():
    player.Player.save(request.form)
    return redirect('/')