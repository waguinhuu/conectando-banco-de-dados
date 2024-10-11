import os

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
db = create_engine("sqlite:///meubanco2.db")

# Conexão com banco de dados.
Session = sessionmaker(bind=db)
session = Session()


# Criando tabela.
Base = declarative_base()


class Aluno(Base):
    __tablename__ = "Alunos"

    r_a = Column("R.A", String, primary_key=True)
    nome = Column("nome", String)
    idade = Column("idade", Integer)
    email = Column("email", String)

    def __init__(self, r_a: str, nome: str, idade: int, email: str) -> None:
        self.r_a = r_a
        self.nome = nome
        self.idade = idade
        self.email = email
    

Base.metadata.create_all(bind=db)


for i in range(2):
    os.system("cls || clear")

    r_a = input("Digite seu R.A: ")
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    email = input("Digite seu email: ")

    aluno = Aluno(r_a=r_a, nome=nome, idade=idade, email=email)
    session.add(aluno)
    session.commit()
    print()


    #Mostrando conteúdo do banco de dados.
    lista_aluno = session.query(Aluno).all()

    for aluno in lista_aluno:
        print(f"{aluno.r_a} - {aluno.nome} - {aluno.email}")


# Deletando um aluno
aluno = session.query(Aluno).filter_by(email="marta@gmail.com").first()
session.delete(aluno)
session.commit()

lista_aluno = session.query(Aluno).all()

for aluno in lista_aluno:
    print(f"{aluno.r_a} - {aluno.nome} - {aluno.email}")
