import os
import time

caminho = f'C:\\Users\\Renan\\Desktop\\cursos\\DIO\\004_FormacaoPythonDeveloper\\seguranca\\pingmultiplo\\hosts.txt'
with open(caminho, 'r') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('-' * 60)
        os.system("ping " + ip)
        print('-' * 60)
        time.sleep(3)

