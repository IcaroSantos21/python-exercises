from user_utils import user_create, user_update, deactivate_user
from json_utils import save_json, load_json

def test_user_full_flow(tmp_path):
    users = []

    # 1 - Criar
    user_create(users, 'icaro', 'icaro@gmail.com')
    assert len(users) == 1

    # 2 - Atualizar
    user_update(users, 1, {'name': 'Icaro Rodrigues'})
    assert users[0]['name'] == 'Icaro Rodrigues'

    # 3 - Desativar
    deactivate_user(users, 1)
    assert users[0]['activate'] is False

    # 4 - Salvar
    file_path = tmp_path / 'users.json'
    save_json(file_path, users)

    # 5 - Carregar
    loaded_users = load_json(file_path)

    # 6 - Validar
    assert loaded_users[0]['name'] == 'Icaro Rodrigues'
    assert loaded_users[0]['email'] == 'icaro@gmail.com'
    assert loaded_users[0]['activate'] is False