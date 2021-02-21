import pymysql
from api import GoRestApiClient
import json

# le Client du pattern Factory
class User:
    # def __init__(self, _id, factory):
    def __init__(self, _id, resource):
        self.__id = _id
        # self._factory = factory
        self._factory = store.get_factory(resource)
        # appel à la méthode get_user de la Factory, quelqu'elle soit
        try:
            data = self._factory.get_user(self.__id)
            # si on connaît les champs retournés
            #self.name = data["name"]
            # ...
            # de façon dynamique
            for key, value in data.items():
                setattr(self, key, value)
        except ValueError as ve:
            print(ve)
    def __str__(self):
        return f"name: {self.name}, email: {self.email}, gender: {self.gender}"

# la Factory pour retourner les données utilisateur depuis l'api
# ici le "produit" du pattern sera soit la GoRestApi, 
# soit l'implémentation de pymysql pour l'autre Factory
class UserApiFactory:
    def __init__(self):
        self._api = GoRestApiClient()
    
    def get_user(self, _id):
        return self._api.get_user(_id)

class UserDbFactory:
    def __init__(self):
        self._db = pymysql.connect(host="localhost", user="stagiaire", password="a123456!", database="api_users")
    
    def get_user(self, _id):
        # pymysql.cursors.DictCursor permet de "fetcher" des dictionnaires plutôt que des tuples
        with self._db.cursor(pymysql.cursors.DictCursor) as cur:
            cur.execute(f"SELECT * FROM users WHERE id = {_id}")
        return cur.fetchone()
    
    # fermeture la connection quand l'objet est détruit
    def __del__(self):
        self._db.close()

class UserJsonFactory:
    def __init__(self):
        self._json_file = "users.json"
    
    def get_user(self, _id):
        with open(self._json_file, "r") as json_f:
            return json.loads(json_f.read())[str(_id)]

# magasin de factories 
class UserFactoryStore:
    def __init__(self):
        self._factories = {}
    
    def register_resource(self, resource, factory_class):
        self._factories[resource] = factory_class
    
    def get_factory(self, resource):
        factory = self._factories.get(resource)
        if not factory:
            raise ValueError(f"{resource} not available!")
        # instanciation automatique de la factory
        return factory()

store = UserFactoryStore()
store.register_resource("api", UserApiFactory)
store.register_resource("db", UserDbFactory)
store.register_resource("json", UserJsonFactory)

if __name__ == "__main__":
    # test api
    # _api = GoRestApiClient()
    # print(_api.get_user(153))
    # test mysql
    # conn = pymysql.connect(host="localhost", user="stagiaire", password="a123456!", database="api_users", autocommit=True)
    # with conn:
    #     with conn.cursor() as cur:
    #         cur.execute("SELECT * FROM users WHERE id = 153")
    #         print(cur.fetchone())
    # api_factory = UserApiFactory()
    # db_factory = UserDbFactory()
    #user = User(1, "api")
    #print(user)
    # user2 = User(153, "db")
    # print(user2)
    user3 = User(153, "json")
    print(user3)
        