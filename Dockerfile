# Usando imagem base do Python 3.13
FROM python:3.13

# Definir diretório de trabalho dentro do container
WORKDIR /app

# Copiar arquivos do repositório local para dentro do container
COPY . /app

# Definir comando padrão (aqui vamos rodar a versão final)
CMD ["python", "main.py"]
