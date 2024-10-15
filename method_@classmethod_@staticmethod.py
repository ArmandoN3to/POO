class Coneection:
    def __init__(self,host = 'localhost'):
        self.host=host
        self.user =None
        self.password =None
    
    def set_user(self,user): #setter
        self.user = user
    def set_password(self,password):#todo metodo que eu tiver que usar self
                                    #esse metodo é um metodo de instancia
        self.password = password

    @classmethod    #metodo de classe
    def create_with_auth(cls,user,password):
        connection=cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log (msg):
        print('LOG:',msg)

c1 =Coneection()
p2=Coneection.create_with_auth('Armando','455')
print(p2.user)
print(p2.password)
Coneection.log('essa é a mensagem log ')
