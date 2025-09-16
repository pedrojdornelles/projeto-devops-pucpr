import datetime
import platform

def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo ao mundo DevOps"

def main():
    print("Hello, DevOps! 🚀")
    print("Testando versionamento com GitHub Desktop.")

    # Nova funcionalidade: saudação personalizada
    print("\n=== Saudação personalizada ===")
    print(saudacao("Pedro"))  # aqui você pode trocar pelo seu nome

    # Informações do ambiente
    print("\n=== Informações do sistema ===")
    print(f"Sistema operacional: {platform.system()} {platform.release()}")
    print(f"Versão do Python: {platform.python_version()}")
    print(f"Data/Hora atual: {datetime.datetime.now()}")

    # Pequeno loop de teste
    print("\n=== Contagem rápida ===")
    for i in range(1, 6):
        print(f"Número {i}")

if __name__ == "__main__":
    main()
