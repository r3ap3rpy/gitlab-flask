import demo_app

def test_hello():
    client = demo_app.app.test_client()

    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello World!'

def test_cicd():
    client = demo_app.app.test_client()

    response = client.get('/cicd')
    assert response.status_code == 200
    assert response.data == b'GitLab is awesome!'

def test_404():
    client = demo_app.app.test_client()

    response = client.get('/foobar')
    assert response.status_code == 403
