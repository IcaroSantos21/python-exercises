def user_create(users, name, email, active=True):
    if users:
        next_id = max(user['id'] for user in users) + 1
    else:
        next_id = 1
    for user in users:
        if id == user['id']:
            raise ValueError('ID já existe')
        if email == user['email']:
            raise ValueError('Email já existe')
    users_add = {"id": next_id, "name": name,"email": email, "activate": active}
    users.append(users_add)

def search_user(users, id):
    for user in users:
        if user['id'] == id:
            return user
    
    raise ValueError('Usuário não encontrado')

def user_update(users, id, new_data):
    user = search_user(users, id)
    if 'id' in new_data:
        raise ValueError('Não é permitido trocar o id')
    for key, value in new_data.items():
        if isinstance(value, str) and value.strip() == '':
            continue
        user[key] = value
    return user
    
def deactivate_user(users, id):
    user = search_user(users, id)
    if user['activate'] is False:
            raise ValueError('Usuário já está desativado')
    user['activate'] == True
        
def activate_user(users, id):
    user = search_user(users, id)
    if user['activate'] is True:
        raise ValueError('Usuário já está ativo')
    user['activate'] == True

def list_users(users):
    for user in users:
        for key, item in user.items():
            print(f"{key} ------ {item}")

def show_user(users, id):
    user = search_user(users, id)
    for key, item in user.items():
        print(f"{key} ------ {item}")