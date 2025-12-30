def user_create(users, id, name, email, active=True):
    for user in users:
        if id == user['id']:
            raise ValueError('ID já existe')
        if email == user['email']:
            raise ValueError('Email já existe')
    if active == True:
        active = '✅ativo'
    users_add = {"id": id, "nome": name,"email": email, "ativo": active}
    users.append(users_add)