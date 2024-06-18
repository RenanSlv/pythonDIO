import socket # Faz relacionamento da placa de rede com o SO
import sys

def main():
    try:
        # af_intet = ip , socket_stream = tcp
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou!")
        print(f"Erro : {e}")
        sys.exit()

    print("Socket criado com sucesso.")

    host_alvo = input("Digite o host ou ip a ser conectado: ")
    porta_alvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((host_alvo, int(porta_alvo)))
        print(f"Cliente TCP conectado com sucesso. No host {host_alvo} e na porta {porta_alvo}")
        s.shutdown(2)
    except socket.error as e:
        print("A conexão falhou! (TCP)")
        print(f"Erro : {e}")
        sys.exit()

if __name__ == "__main__":
    main()
