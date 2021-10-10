def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert 'core/index.html' in [
        template.name for template in response.templates
    ]
    assert 'Куда пойти — Москва глазами Артёма' in response.content.decode()
