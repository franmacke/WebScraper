import requests
import json
from .Database import Database

class TelegramBot:
    def __init__(self, token):
        self.token = token
        self.offset = 0
        self.usuarios = Database()

    def estaLaCamiseta(self):
        for usuario in self.usuarios:
            self.sendMessage('Hay camisetas de algun talle.', usuario)

    def sendMessage(self, text, chat_id):
        try:
            requests.get(f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={chat_id}&text={text}')
            print('Mensaje ok')
        except:
            print('Hubo un error al mandar el mensaje')

    def getMessages(self):
        response = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates?offset={self.offset}').text
        response_body = json.loads(response)

        return response_body['result']

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
                self.sendMessage('Ya estabas registrado', id)

            self.offset = update_id + 1

    def update(self, estado):
        self.getUsers()

        if estado:
            self.estaLaCamiseta()

        print("Usuarios registrados:", self.usuarios.cantidadUsuarios())
