class Observer():
    def update(self, subject):
        print("Observer: My sunject just updated and told me about it")
        print("Observer: It's state is now - "+ str(subject._state))
        
    
class Subject():
    _state = 0
    _observerlist=[]
    
    def attach(self, observer):
        self._observerlist.append(observer)
        
    def remove(self, observer):
        self._observerlist.remove(observer)
        
    def notify(self):
        print("Subject: I'm notifying my observers ...")
        for i in self._observerlist:
            i.update(self)
    
    def updateState (self, n):
        print("Subject: I've received a state update!")
        self._state=n
        self.notify()