import requests
import json
from .Database import Database

class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.offset = 0
        self.usuarios = Database()
        self.prevState = {
            'XS': False,
            'S': False,
            'M': False,
            'L': False,
            'XL': False,
            '2XL': False
        }

    def estaLaCamiseta(self, estado):
        tallesDisponibles = [key for key, value in estado.items() if value]
        talles = ''.join(tallesDisponibles)

        for usuario in self.usuarios.getUsers():
            self.sendMessage(f'Hay camisetas de talle: {talles}', usuario)
            self.sendMessage(f'https://www.adidas.com.ar/camiseta-titular-argentina-3-estrellas-2022/IB3593.html?cm_sp=SLOT-4.5-_-HOME_%3F_%3F_HOME_%3F-_-PRODUCTSELECTIONCAROUSEL-PRODUCT-CARD-_-1007018')

    def sendMessage(self, text, chat_id):
        try:
            requests.get(f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={chat_id}&text={text}')
            print('Mensaje ok')
        except:
            print('Hubo un error al mandar el mensaje')

    def getMessages(self):
        response = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates?offset={self.offset}').text
        response_body = json.loads(response)
        
        try:
            return response_body['result']
        except:
            print("Error en la respuesta")
            return []

    def getUsers(self):
        mensajes = self.getMessages()

        for mensaje in mensajes:
            comando = mensaje['message']['text']
            id = int(mensaje['message']['from']['id'])
            update_id = mensaje['update_id']

            if comando == '/registrar':
                self.sendMessage(self.usuarios.createUser(id), id)

            elif comando == '/start':
                self.sendMessage('Hola!', id)

            else:
                self.sendMessage('No rompas las bolas', id)

            self.offset = update_id + 1

    def update(self, estado: dict):
        self.getUsers()

        if estado != self.prevState and len(self.prevState.keys()) > 0:
            self.estaLaCamiseta(estado)

        self.prevState = estado

        print("Usuarios registrados:", self.usuarios.cantidadUsuarios())
