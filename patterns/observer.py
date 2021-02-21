#  = Subject = Observable
class Publisher:
    def __init__(self):
        # on va remplacer une liste par un set()
        # set: non indexable, les valeurs non modifiables
        # set: mais on peut ajouter, ou enlever des valeurs
        # set: itérable
        # set: unicité des valeurs gérée automatiquement
        # self._subscribers = []
        #self._subscribers = set()
        self._subscribers = {}
    
    def register(self, subscriber, update_func="update"):
        # self._subscribers.append(subscriber)
        # self._subscribers.add(subscriber)
        f = getattr(subscriber, update_func)
        self._subscribers[subscriber] = f
    
    def unregister(self, subscriber):
        # self._subscribers.remove(subscriber)
        # self._subscribers.discard(subscriber)
        del self._subscribers[subscriber]
        
    # envoi de messages aux subscribers
    def notify(self, msg):
        # for sub in self._subscribers:
        #     sub.update(msg)
        # "_" remplace toute varable non utilisée dans un bloc sous jacent
        for _, func in self._subscribers.items():
            func(msg)

# = Observer
class Subscriber:
    def __init__(self, name):
        self._name = name
    
    # mise à jour de l'état de l'objet 
    # d'après le message
    def update(self, msg):
        print(f"{self._name} got message {msg}!")

class AltSubscriber:
    def __init__(self, name):
        self._name = name
    
    # mise à jour de l'état de l'objet 
    # d'après le message
    def receive(self, msg):
        print(f"{self._name} received message {msg}!")

if __name__ == "__main__":
    pub = Publisher()
    subs = {}
    # for name in ("alice", "bob", "charlie"):
        # subs[name] = Subscriber(name)
        # pub.register(subs[name])
        # si on ajoute plusieurs fois le même objet, le set ignore
        # pub.register(subs[name])
    
    sub1 = Subscriber("joe")
    sub2 = AltSubscriber("jane")
    pub.register(sub1)
    pub.register(sub2, "receive")
    
    pub.notify("Hi Everybody")
    pub.unregister(sub2)
    pub.notify("Bye")