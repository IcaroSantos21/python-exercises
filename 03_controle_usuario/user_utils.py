def user_create(users, id, name, email, active=True):
    for user in users:
        if id == user['id']:
            raise ValueError('ID já existe')
        if email == user['email']:
            raise ValueError('Email já existe')
    users_add = {"id": id, "name": name,"email": email, "activate": active}
    users.append(users_add)

def deactivate_user(users, id):
    user_found = False
    for user in users:
        if id == user['id']:
            user_found = True
            if user['activate'] is False:
                raise ValueError('Usuário já está desativado')
            user['activate'] = False
            break
        if not user_found:
            raise('Usuário não encontrado')
        
def activate_user(users, id):
    user_found = False
    for user in users:
        if id == user['id']:
            user_found = True
            if user['activate'] is True:
                raise ValueError('Usuário já está ativo')
            user['activate'] = True
            break
        if not user_found:
            raise('Usuário não encontrado')
        
def list_users(users):
    for user in users:
        for key, item in user.items():
            print(f"{key} ------ {item}")

def show_user(users, id):
    user_found = False
    for user in users:
        if id == user['id']:
            user_found = True
            for key, item in user.items():
                print(f"{key} ------ {item}")
            break
        if not user_found:
            raise ValueError('Usuário não encontrado')