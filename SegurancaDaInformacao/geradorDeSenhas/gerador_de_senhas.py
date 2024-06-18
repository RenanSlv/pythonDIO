import random
import string

tamanho_da_senha = int(input("Digite o tamanho da senha: "))

chars = string.ascii_letters + string.digits + "ç!@#$%&*()-=+_?/"

rnd = random.SystemRandom() # os.urandom

print(''.join(rnd.choice(chars) for i in range(tamanho_da_senha)))