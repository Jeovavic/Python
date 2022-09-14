#projeto 5
#faça uma pergunta para o programa  e ele dará uma resposta
import random
import PySimpleGUI

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você que sabe',
            'Não faz isso Não!',
            'Acho que tá na hora!'
        ]
    
    def Iniciar(self):
        input('Faça sua pergunta: ')
        print(random.choice(self.respostas))

decida = DecidaPorMim()
decida.Iniciar()