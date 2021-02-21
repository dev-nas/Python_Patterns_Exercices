class SingleMeta(type):
    
    # on crée un catalogue d'instances singleton par classes utilisant la métaclasse
    # c'est le pattern "MultiSingleton"
    __instances = {}
    
    # on redéfinit la méthode __call__ qui est à l'origine de l'instanciation
    # on crée la méthode avec la signature la plus générique (*args, **kwargs)
    # on crée l'instance par type (super())
    # on fait le contôle d'instance pour la classe instanciée au niveau de la métaclasse
    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        cls_name = instance.__class__.__name__
        if cls_name not in cls.__instances:
            cls.__instances[cls_name] = instance
        return cls.__instances[cls_name]

class MysqlConnection(metaclass=SingleMeta):
    pass

class RedisConnection(metaclass=SingleMeta):
    pass

if __name__ == "__main__":
    m1, m2 = MysqlConnection(), MysqlConnection()
    r1, r2 = RedisConnection(), RedisConnection()
    print(f"Unique instance for mysql ? {m1 is m2}")
    print(f"proof: m1 in {id(m1)}, m2 in {id(m2)}")
    print(f"Unique instance for redis ? {m1 is m2}")
    print(f"proof: r1 in {id(r1)}, r2 in {id(r2)}")
    
        