from django.shortcuts import reverse


def test_index(client):
    url = reverse('core:test_index')
    response = client.get(url)
    assert response.status_code == 200
    assert 'core/index.html' in [
        template.name for template in response.templates
    ]
    assert 'Куда пойти — Москва глазами Артёма' in response.content.decode()
