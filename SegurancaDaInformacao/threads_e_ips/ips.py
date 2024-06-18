import ipaddress

ip = '192.168.0.1'
ip2 = '192.168.0.0/24'

endereco = ipaddress.ip_address(ip)
rede = ipaddress.ip_network(ip2) # Para liberar qualquer ip colocar strict=False

print(endereco + 256)
print(endereco + 2000)

print(rede)
print('#' * 25)

for ip in rede:
    print(ip)