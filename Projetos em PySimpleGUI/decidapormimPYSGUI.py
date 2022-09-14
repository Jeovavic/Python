#projeto 5
#faça uma pergunta para o programa  e ele dará uma resposta

import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza!!!!!',
            'Sem dúvidas alguma!!!',
            'Ela pode até dizer que não, mas não se deixe enganar, além de maconheira é mentirosa',
            'Sim!!!!!! Fumante!!!!!'
        ]
    
    def Iniciar(self):
        #Layout
        layout = [
            [sg.Text('Faça sua pergunta: ')],
            [sg.Input(size=(50,20))],
            [sg.Output(size=(50,10))],
            [sg.Button('Botão mágico da verdade')]
        ]
        #criar a janela
        self.janela = sg.Window('Truth Machine!', layout=layout)
        while True:
            #ler os valores
            self.eventos, self.valores = self.janela.Read()
            #fazer algo com os valores
            if self.eventos == 'Botão mágico da verdade':
                print(random.choice(self.respostas))
            

decida = DecidaPorMim()
decida.Iniciar()