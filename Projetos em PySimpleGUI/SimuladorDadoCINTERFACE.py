#Simulador de dado
#Simulador o uso de um dado, gerando um valor de 1 até 6

import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self) :
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'
        #layout simplegui
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'),sg.Button('não')]
        ]

    def Iniciar(self):
          #criar uma janela
        self.janela = sg.Window('Simulador de Dado',layout=self.layout)
          #ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'não' or self.eventos == 'n':
                print('Agradecemos a sua partificação!')
            else:
                print('Favor digitar sim ou não')
        except: 
            print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()