# Dockerfile frontend

FROM python:3.9

# Diretorio de trabalho do container
WORKDIR /app

# Copiar os arquivos de dependencias e instalar
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# copiar restante dos arquivos
COPY . /app

# Executar aplicacao
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]