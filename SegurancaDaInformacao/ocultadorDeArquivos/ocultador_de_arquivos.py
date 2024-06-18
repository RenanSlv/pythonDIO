import ctypes

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('./ocultadorDeArquivos/arquivo.txt', atributo_ocultar)

if retorno:
    print('Arquivo foi ocultado.')
else:
    print('Arquivo não foi ocultado.')
