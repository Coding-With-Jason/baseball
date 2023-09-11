from baseball_app.config.mysqlconnection import connectToMySQL
from .player import Player

class Team:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.players = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM teams;"

        results = connectToMySQL('baseball').query_db(query)
        teams = []

        for d in results:
            teams.append( cls(d) )
        return teams

    @classmethod
    def save(cls, data):
        query= "INSERT INTO teams (name) VALUES (%(name)s);"
        result = connectToMySQL('baseball').query_db(query,data)
        return result

    @classmethod
    def get_one_with_players(cls, data ):
        query = "SELECT * FROM teams LEFT JOIN players on teams.id = players.team_id WHERE teams.id = %(id)s;"
        results = connectToMySQL('baseball').query_db(query,data)
        print(results)
        team = cls(results[0])
        for row in results:
            n = {
                'id': row['players.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'player_number': row['player_number'],
                'created_at': row['players.created_at'],
                'updated_at': row['players.updated_at']
            }
            team.players.append( Player(n) )
        return team
