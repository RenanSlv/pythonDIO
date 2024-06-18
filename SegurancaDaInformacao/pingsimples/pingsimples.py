from os import system

print("#" * 60)
ip_ou_host = input("Digite o ip ou host a ser verificado: ")
print("-" * 60)

system(f"ping -n 6 {ip_ou_host}")
print("-" * 60)
