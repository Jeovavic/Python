import string
import secrets

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(caracteres) for i in range(comprimento))
    return senha

quantidade = int(input("Quantas senhas você deseja gerar? "))
comprimento = int(input("Qual o comprimento de cada senha? "))

print("Aqui estão suas senhas:")
for i in range(quantidade):
    senha = gerar_senha(comprimento)
    print("Senha {}: {}".format(i+1, senha))