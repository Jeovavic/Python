#Chegar a vinais diferentes na historia, de acordo com as respostas que eu passe para o programa

#Qual é o cenário: Eu estou numa guerra entre duas nações, e nós temos 2 lados: ladoA e ladoB. Somenete o ladoA irá vencer, e o ladoB irá perder!
#tomar as decisõess corretar para chegar até a virótia, que somento o lado A irá conseguir!

import PySimpleGUI as sg

class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no note ou no sul? (n/s)'
        self.pergunta2 = 'Você prefere a espada ou escudo? (espada/escudo)'
        self.pergunta3 = 'Qual é a sua especialidade? (linha de ferente/tatico)'
        self.finalHistoria1 = 'Você será um heroi na linha de frente!'
        self.finalHistoria2 = 'Você será um heroi protegendo todas as nossas tropas!'
        self.finalHistoria3 = 'Você irá se sacrificar na batalha!'
        self.finalHistoria4 = 'Você não é capaz de lutar nessa batalha!'

    def Iniciar(self):
        #layout 
        layout = [
            [sg.Output(size=(50,10))],
            [sg.Input(size=(25,0), key='escolha')],
            [sg.Button('Iniciar'),sg.Button('Responder')]
        ]
        #criar a janela
        self.janela = sg.Window('Jogo de Aventura', layout=layout)
        while True:
            #Ler os dados
            self.LerValores()
            #fazer algo com os dados
            if self.evento == 'Iniciar':
                print(self.pergunta1)
                self.LerValores()
                if self.valores['escolha'] == 'n':
                    print(self.pergunta2)
                    self.LerValores()
                    if self.valores['escolha'] == 'espada':
                        print(self.finalHistoria1)
                    if self.valores['escolha'] == 'escudo':
                        print(self.finalHistoria2)
                if self.valores['escolha'] == 's':
                    print(self.pergunta3)
                    self.LerValores()
                    if self.valores['escolha'] == 'linha de frente':
                        print(self.finalHistoria3)
                    if self.valores['escolha'] == 'tatico':
                        print(self.finalHistoria4)

    def LerValores(self):
        self.evento, self.valores = self.janela.Read()

jogo = JogoDeAventura()
jogo.Iniciar()