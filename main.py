import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
db = create_engine("sqlite:///meubanco.db")

# Conexão com banco de dados.
Session = sessionmaker(bind=db)
session = Session()

# I/O
# I = input (Entrada)
# O = output (Saída)

# Criando tabela.
Base = declarative_base()


class Usuario(Base):
    # Definindo nome da tabela.
    __tablename__ = "usuarios"

    # Definindo atributos da tabela.
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # Definindo atributos da classe.
    def __init__(self, nome: str, email: str, senha: str) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)

os.system("cls || clear")

for i in range(2):
    senha = input("Digite seu senha: ")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")

    usuario = Usuario(senha=senha, nome=nome, email=email)
    session.add(usuario)
    session.commit()


    #Mostrando conteúdo do banco de dados.
    lista_usuarios = session.query(Usuario).all()

    for usuario in lista_usuarios:
        print(f"{usuario.id} - {usuario.nome} - {usuario.email}")

# Deletando um usuario
email_usuario = input("Informe o e-mail do usuario: ")
usuario = session.query(Usuario).filter_by(email="marta@gmail.com").first()
session.delete(usuario)
session.commit()
print("\nUsuario deletado com sucesso.")


lista_usuario = session.query(Usuario).all()

for usuario in lista_usuario:
    print(f"{usuario.senha} - {usuario.nome} - {usuario.email}")


# Atualizar um usuário
print("\nAtualizando os dados de um usuario")

email_usuario = input("Informe o e-mail do usuario")

usuario = session.query(Usuario).filter_by(email = email_usuario).first()

if usuario:
    usuario.nome = input("Digite seu nome: ")
    usuario.email = input("Digite seu e-mail: ")
    usuario.senha = input("Digite sua senha: ")
    session.commit()
else:
    print("Usuario não encontrado.")

#Pesquisando um usuario.
print("\nPesquisando um usuario pelo email.")

email_usuario = input("Informe o e-mail do usuario: ")

usuario = session.query(Usuario).filter_by(email = email_usuario).first()
if usuario:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email}")
else: 
    print("Usuario não encontrado.")

session.close()