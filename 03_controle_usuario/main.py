from user_utils import *
from menu import *
users = []

while True:
    display_menu()
    option = int(input('Digite aqui: '))
    if option == 1:
        name = input('Digite o nome do usuário: ')
        email = input('Digite o email do usuário: ')
        user_create(users, name, email)
        print(f"O usuário {name} foi criado com sucesso")
    elif option == 2:
        id = int(input('Digite o id do usuário que deseja ativar: '))
        activate_user(users, id)
    elif option == 3:
        id = int(input('Digite o id do usuário que deseja desativar: '))
        deactivate_user(users, id)
    elif option == 4:
        list_users(users)
    elif option == 5:
        id = int(input('Digite o id do usuário que deseja ver: '))
        show_user(users, id)
    elif option == 6:
        print("saindo...")
        break
    else:
        print("Opção inválida")