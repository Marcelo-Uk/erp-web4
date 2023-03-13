FROM python:3.9-slim-buster

# Define o diretório de trabalho do contêiner
WORKDIR /app

# Copia os arquivos do projeto para o contêiner
COPY . /app

COPY venv /app/venv

# Cria um novo ambiente virtual Python
RUN python -m venv venv

# Ativa o ambiente virtual Python
RUN . venv/bin/activate.bat

# Atualiza o pip
RUN pip install --upgrade pip

# Instala as dependências do projeto
RUN pip install -r requirements.txt

# Define as variáveis de ambiente para o PostgreSQL
ENV POSTGRES_USER=postgres
ENV POSTGRES_DB=leinertex-alpha-4
ENV POSTGRES_HOST=localhost
ENV DATABASE_PASSWORD_FILE=/run/secrets/db_password

# Copia o arquivo de senha do banco de dados para o contêiner
COPY db_password.txt /run/secrets/db_password

# Define as permissões corretas para o arquivo de senha do banco de dados
RUN chmod 400 /run/secrets/db_password

# Define a porta que será exposta
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["/bin/bash", "-c", "source ./venv/scripts/activate && python manage.py runserver 0.0.0.0:8000"]


#Comando para criar a imagem
# docker build -t leinertex-web4 .

# docker run --name db --network casatechnetwork -e POSTGRES_PASSWORD=Nov@roch@135 -d postgres