import datetime
import platform

def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo ao mundo DevOps!"

def mostrar_info_sistema():
    print("\n=== Informações do sistema ===")
    print(f"Sistema operacional: {platform.system()} {platform.release()}")
    print(f"Versão do Python: {platform.python_version()}")
    print(f"Data/Hora atual: {datetime.datetime.now()}")

def contagem():
    print("\n=== Contagem rápida ===")
    for i in range(1, 10):
        print(f"Número {i}")

def somar(a, b):
    return a + b

def eh_par(numero):
    return numero % 2 == 0

def main():
    print("Hello, DevOps!")

    # Saudação personalizada
    print("\n=== Saudação personalizada ===")
    nome = input("Digite seu nome: ")
    print(saudacao(nome))

    # Outras funcionalidades
    mostrar_info_sistema()
    contagem()

if __name__ == "__main__":
    main()