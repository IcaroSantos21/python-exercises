import user_utils 
import menu 
import json_utils 
users = json_utils.load_json('users.json')

while True:
    menu.display_menu()
    try:
        option = int(input('Digite aqui: '))
        if option == 1:
            name = input('Digite o nome do usuário: ')
            email = input('Digite o email do usuário: ')
            user_utils.user_create(users, name, email)
            print(f"O usuário {name} foi criado com sucesso")
            json_utils.save_json('users.json', users)
        elif option == 2:
            id = int(input('Digite o id do usuário que deseja ativar: '))
            user_utils.activate_user(users, id)
            print(f"Usuário ativado com sucesso")
            json_utils.save_json('users.json', users)
        elif option == 3:
            id = int(input('Digite o id do usuário que deseja desativar: '))
            user_utils.deactivate_user(users, id)
            print(f"Usuário desativado com sucesso")
            json_utils.save_json('users.json', users)
        elif option == 4:
            user_utils.list_users(users)
        elif option == 5:
            id = int(input('Digite o id do usuário que deseja ver: '))
            user_utils.show_user(users, id)
        elif option == 6:
            print("saindo...")
            break
        else:
            print("Opção inválida")
    except ValueError as e:
        print(f'Erro: {e}')