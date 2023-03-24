import platform

class Database:
    def __init__(self) -> None:
        self.url = '.\\data\\db.txt' if platform.system() == "Windows" else "./data/db.txt"
        self.usuarios = self.loadUsers()

    def loadUsers(self):
        with open(self.url, 'r') as file:
            usuarios = file.read()
            return [int(x) for x in usuarios.split('\n') if x]
        
    def getUsers(self):
        return self.usuarios
    
    def createUser(self, id):

        if type(id) is not int:
            raise TypeError

        if self.isRegistered(id):
            return 'Ya estas registrado.'
        
        self.writeId(id)

        return 'Registrado exitosamente'
    
    
    def writeId(self, id):
        with open(self.url, 'a') as file:
            file.write(str(id))
            file.write('\n')
        
        self.usuarios.append(id)

    def isRegistered(self, id):
        return id in self.usuarios

    def cantidadUsuarios(self):
        return len(self.usuarios)