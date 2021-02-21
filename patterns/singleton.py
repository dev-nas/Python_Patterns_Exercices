class Single:
    __instance = None
    
    # def __init__(self):
    #     if Single.__instance == None:
    #        Single.__instance = self
    #     else:
    #         raise Exception("Please use Single.get_instance !")
    
    def __new__(cls)
    
    @classmethod
    def get_instance(cls):
        """ méthode de classe
        qui va vérifier la disponibilité d'une instance 
        ou demander sa création au constructeur"""
        if cls.__instance == None:
            # Single()
            cls()
        return cls.__instance

if __name__ == "__main__":
    # contrôle de l'instanciation par la méthode de classe : OK
    # s1 = Single.get_instance()
    # s2 = Single.get_instance()
    # print(f"Unique instance ? {s1 is s2}")
    # print(f"proof: s1 in {id(s1)}, s2 in {id(s2)}")
    
    # par l'instanciation directe: problème
    try:
        s1 = Single()
        s2 = Single()
        print(f"Unique instance ? {s1 is s2}")
    except Exception as e:
        print(e)