from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print(f"Piloto: {piloto} Km: {trajeto}\n")


t_carro1 = Thread(target=carro, args=[1, "João"])
t_carro2 = Thread(target=carro, args=[1.5, "Marcelo"])

t_carro1.start()
t_carro2.start()

