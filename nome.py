while True:
    print("1-Cadastrar pessoa")
    print("2-Lista Cadastros")
    print("3-Procurar Pessoa Especifica")
    op = int(input())#Escolha da opcao
    if op == 1:
        nova = [] # cria uma lista para adicionar o id, nome e idade da pessoa
        id = input("Id da pessoa")
        nome = input("Digite o nome da pessoa")
        idade = input("Idade da pessoa")
        nova.append(id)
        nova.append(nome)
        nova.append(idade)
        listas.append(nova)#Adiciona a lista criada com o cadastro da pessoa dentro da lista

    elif op == 2:
        for mostrar in listas:
            for mostrar2 in mostrar:
                print(mostrar2)#mostra tudo dentro da

    elif op == 3:
        print("pensando")


        Cadastrando uma pessoa...

def cadastrar(pessoas):
    identificador = input('Id? ')
    nome = input('Nome? ')
    idade = int(input('Idade? '))
    pessoas.append((identificador, nome, idade))


    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sistema',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET default_storage_engine=InnoDB'
        }
    }
}
