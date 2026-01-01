import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import user_utils

def test_search_user_found():
    users = [
        {'id': 1, 'name': 'nicolas', 'email': 'nicolas@gmail.com', 'activate': True},
        {'id': 2, 'name': 'patricia', 'email': 'patricia', 'activate': True}
    ]

    user = user_utils.search_user(users, 2)

    assert user['name'] == 'patricia'

def test_search_user_not_found():
    users = [
        {'id': 1, 'name': 'osvaldo', 'email': 'patricia', 'activate': True}
    ]

    with pytest.raises(ValueError):
        user_utils.search_user(users, 99)