# Desafio Workshop Fábrica 2023_2 (POSTGRESQL)

O projeto é uma API que utiliza os metodos GET, PUT, POST, DELETE e utilizando o PostgresSQL como banco de dados para o projeto. 
Obs: Precisa do PostgresSQL para rodar esta versão da API

O tema do desafio é inspirado no IMDB, aonde se cria uma interação de classes entre Pessoas e Filmes, aonde se cadastra Filmes que podem ser usados por Pessoas que dão notas para os filmes e Pessoas diferentes podendo dar diferente notas a algum Filme anteriormente cadastrado (inclusive diferentes pessoas podem dar notas a um mesmo Filme).

# Vamos iniciar o projeto, Primeiro tem que criar o Ambiente Virtual no terminal da pasta.

python -m venv venv

# Após isso ativa-se o Ambiente Virtual.

.\venv\Scripts\activate.ps1

# Após o Ambiente ter sido ativado (cheque se aparece um "(venv)" no inicio do terminal) e então vamos baixar tudo que precisa para o crud, puxando do arquivo requirements.txt 

pip install -r requirements.txt

# Caso queira mudar o banco de dados para um limpo, vá no Settings do Projeto e troque as informações no Data_Base para o servidor de sua preferencia

(Name é o Nome do Servidor, User é o nome do Usuario do Postgres e Password é a senha do postgres que você criou, Já o Host é o Host descrito na criação do Servidor)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'FilmesPostgresDB',
        'USER':'postgres',
        'PASSWORD':'django123',
        'HOST':'localhost',
    }
}

# Após isso, cheque se está tudo funcionando.

python manage.py runserver

# E para checar os metodos PUT e DELETE, recomendo o Postman.
