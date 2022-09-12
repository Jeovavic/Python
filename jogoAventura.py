#Chegar a vinais diferentes na historia, de acordo com as respostas que eu passe para o programa

#Qual é o cenário: Eu estou numa guerra entre duas nações, e nós temos 2 lados: ladoA e ladoB. Somenete o ladoA irá vencer, e o ladoB irá perder!
#tomar as decisõess corretar para chegar até a virótia, que somento o lado A irá conseguir!

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
        resposta1 = input(self.pergunta1)
        if resposta1 == 'n':
            resposta1B = input(self.pergunta2)
            if resposta1B == 'espada':
                print(self.finalHistoria1)
            if resposta1B == 'escudo':
                print(self.finalHistoria2)
        if resposta1 == 's':
            resposta1B = input(self.pergunta3)
            if resposta1B == 'linha de frente':
                print(self.finalHistoria3)
            if resposta1B == 'tatico':
                print(self.finalHistoria4)

jogo = JogoDeAventura()
jogo.Iniciar()