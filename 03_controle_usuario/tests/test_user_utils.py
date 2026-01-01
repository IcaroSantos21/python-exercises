import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from user_utils import search_user, user_create, user_update

def test_search_user_found():
    users = [
        {'id': 1, 'name': 'nicolas', 'email': 'nicolas@gmail.com', 'activate': True},
        {'id': 2, 'name': 'patricia', 'email': 'patricia@gmail.com', 'activate': True}
    ]

    user = search_user(users, 2)

    assert user['name'] == 'patricia'

def test_search_user_not_found():
    users = [
        {'id': 1, 'name': 'osvaldo', 'email': 'patricia', 'activate': True}
    ]

    with pytest.raises(ValueError):
        search_user(users, 99)

def test_user_create_success():
    users = []
    user_create(users, 'isabela', 'isabela@gmail.com',)

    assert len(users) == 1
    assert users[0]['name'] == 'isabela'
    assert users[0]['email'] == 'isabela@gmail.com'
    assert users[0]['activate'] is True

def test_user_create_first_id_is_1():
    users = []
    user_create(users, 'nicolas', 'nicolas@gmail.com')

    assert users[0]['id'] == 1

def test_user_create_id_increment():
    users = []
    user_create(users, 'maria', 'maria@gmail.com')
    user_create(users, 'yasmin', 'yasmin@gmail.com')

    assert users[0]['id'] == 1
    assert users[1]['id'] == 2

def test_user_create_duplicate_email():
    users = []
    user_create(users, 'camilly', 'camilly@gmail.com')
    with pytest.raises(ValueError):
        user_create(users, 'outra', 'camilly@gmail.com')

def test_user_create_does_not_modify_list_on_error():
    users = []
    user_create(users, 'camilly', 'camilly@gmail.com')
    with pytest.raises(ValueError):
        user_create(users, 'outra', 'camilly@gmail.com')

    assert len(users) == 1

def test_user_update_success():
    users = [
        {'id': 1, 'name': 'nicolas', 'email': 'nicolas@gmail.com', 'activate': True},
        {'id': 2, 'name': 'isabela', 'email': 'isabela@gmail.com', 'activate': True}
        ]
    
    update_user = user_update(
        users,
        2,
        {'name': 'isabella'}
    )

    assert users[1]['id'] ==  2
    assert users[1]['name'] == 'isabella'
    assert users[1]['email'] == 'isabela@gmail.com'

def test_user_update_not_found():
    users = [
        {"id": 1, "name": "Ana", "email": "ana@email.com"},
    ]

    with pytest.raises(ValueError):
        user_update(
            users,
            99,
            {'name': 'teste'}
        )

def test_user_update_cannot_change_id():
    users = [
        {'id': 1, 'name': 'Ana', 'email': 'ana@email.com'},
    ]
    with pytest.raises(ValueError):
        user_update(
            users,
            1,
            {'id': 11, 'name': 'teste'}
        )
        