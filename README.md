# Desafio Workshop Fábrica 2023_2 COM SQLITE (Tem a Versão em Postgres)

O projeto é uma API que utiliza os metodos GET, PUT, POST, DELETE e utilizando o SQLITE3(o basico) como banco de dados para o projeto. 

O tema do desafio é inspirado no IMDB, aonde se cria uma interação de classes entre Pessoas e Filmes, aonde se cadastra Filmes que podem ser usados por Pessoas que dão notas para os filmes e Pessoas diferentes podendo dar diferente notas a algum Filme anteriormente cadastrado (inclusive diferentes pessoas podem dar notas a um mesmo Filme).

# Vamos iniciar o projeto, Primeiro tem que criar o Ambiente Virtual no terminal da pasta.

python -m venv venv

# Após isso ativa-se o Ambiente Virtual.

.\venv\Scripts\activate.ps1

# Após o Ambiente ter sido ativado (cheque se aparece um "(venv)" no inicio do terminal) e então vamos baixar tudo que precisa para o crud, puxando do arquivo requirements.txt 

pip install -r requirements.txt

# Apos baixar tudo, Vamos fazer as migrações.

python manage.py makemigrations

python manage.py migrate

# Após isso, cheque se está tudo funcionando.

python manage.py runserver

# E para checar a API, recomendo o Postman.
