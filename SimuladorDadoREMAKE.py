import random

class SimuladordeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 12
        self.mensagem = 'Você gostaria de gerar um valor para o dado?'

    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's':
                self.GerarValordoDado()
            elif resposta == 'não' or resposta == 'n':
                print('Agradecemos sua participação!')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def GerarValordoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladordeDado()
simulador.Iniciar()
