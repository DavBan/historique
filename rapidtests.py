class test():
    def __init__(self):
        self.toto = "salut"

    def printtoto(self):
        print(self.toto)

    def __call__(self, *args, **kwds):
        print(self.toto)
        return True
    
class test2(test):
    def __init__(self):
        super().__init__()
        self.toto="coucou"


toto = test()
toto2 = test2()
if(toto()):
    toto.printtoto()

if(toto2()):
    toto2.printtoto()

print(getattr(toto, 'printtoto').__name__)