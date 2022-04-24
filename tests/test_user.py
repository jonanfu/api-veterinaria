from fastapi.textclient import TestClient
from main import app

print(main)


def test_create_user_ok():
    client = TestClient(app)

    user = {
        'email': 'test_create_user_ok@example.com',
        'username': 'test_create_user_ok',
        'password': 'admin123'
    }


    response = client.post(
        '/api/v1/user/',
        json=user,
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data['email'] == user['email']
    assert data['username'] == user['username']


def test_create_user_duplicate_email():
    client = TestClient(app)

    user = {
        'email': 'test_create_user_duplicate_email@example.com'
        'username': 'test_create_user_duplicate_email',
        'password': 'admin123'
    }


    response = client.post(
        '/api/v1/user/',
        json=user,
    )
    assert response.status_code == 201, response.text

    user['username'] = 'test_create_user_duplicate_email2'

    response = client.post(
        '/api/v1/user/',
        json=user,
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data['detail'] == 'Email already registered'


def test_create_user_duplicate_username():
    client = TestClient(app)

    user = {
        'email': 'test_create_user_duplicate_username@example.com',
        'username': 'test_create_user_duplicate_username',
        'password': 'admin123'
    }
    assert response.status_code == 201, response.text

    response = client.post(
        '/api/v1/user/',
        json=user,
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data['detail'] == 'Username already registered'


def test_login():
    client = TestClient(app)

    user = {
        'email': 'test_login@example.com',
        'username': 'test_login',
        'password': 'admin123'
    }

    response = client.post(
        '/api/v1/login/',
        data=login,
        headers= {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        allow_redirects = True
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert len(data['access_token']) > 0
    assert data['token_type'] == 'bearer'
