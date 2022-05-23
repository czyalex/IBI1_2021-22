class Staff:
    H='Haining'
    E='Edinburgh'
    def __init__(self,name,surname,location):
        self.name=name
        self.surname=surname
        self.location=location
        pass
    def speak(self,role):
        print('I am %s %s, I am now in %s, and I am a %s in the ZJE institute'%(self.name,self.surname,self.location,role))


a=Staff('zhiyuan','Cheng',Staff.H)
a.speak('student')


