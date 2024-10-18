# Dockerfile-backend

# Imagem
FROM python:3.9

# Diretório de trabalho no cantainer
WORKDIR /app

# Copiar arquivos de dependencias e instalar
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copiar restante dos arquivos do projeto
COPY . /app

# Comando para executar aplicacao
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]