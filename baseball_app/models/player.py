from baseball_app.config.mysqlconnection import connectToMySQL

class Player:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.player_number = data['player_number']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO players (first_name, last_name,player_number,team_id) VALUES (%(first_name)s, %(last_name)s, %(player_number)s, %(team_id)s);"
        return connectToMySQL('baseball').query_db(query,data)