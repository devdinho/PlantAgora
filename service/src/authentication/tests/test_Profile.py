from unittest import skip

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from authentication.models import Profile
from plantagora.models import BaseAddress, Grower
from utils.models import City, State


@pytest.mark.django_db
def test_register_user_success():
    client = APIClient()

    state = State.objects.create(name="São Paulo", abbreviation="SP")
    city = City.objects.create(name="Campinas", state=state)

    payload = {
        "fullname": "João Silva",
        "username": "01001001011",
        "password": "senhaSegura123",
        "document": "01001001011",
        "birthdate": "01/01/2000",
        "cell": "11999999999",
        "zipcode": "13000000",
        "gender": 1,
        "scholarity": 3,
        "fulladdress": "Rua das Flores, 123, Apto 5",
        "city": "Campinas / SP",
    }

    url = reverse("CreateProfileRestView-list")
    response = client.post(url, data=payload, format="json")

    assert response.status_code == 201 or response.status_code == 200

    assert Profile.objects.filter(username="01001001011").exists()

    profile = Profile.objects.get(username="01001001011")
    assert profile.first_name == "João"
    assert profile.last_name == "Silva"

    grower = Grower.objects.get(profile=profile)
    assert grower.address.city == city
    assert grower.cell == "11999999999"

    address = BaseAddress.objects.get(id=grower.address.id)
    assert address.street == "Rua das Flores"
    assert address.number == "123"


@pytest.mark.django_db
def test_login_user_success():
    client = APIClient()

    user = Profile.objects.create_user(
        username="01001001011",
        password="senhaSegura123",
        email="joao@email.com",
        first_name="João",
        last_name="Silva",
    )

    login_url = reverse("token_obtain_pair")

    payload = {"username": "01001001011", "password": "senhaSegura123"}

    response = client.post(login_url, data=payload, format="json")

    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data


@pytest.mark.django_db
def test_profile_view_list_and_update():
    client = APIClient()

    user = Profile.objects.create_user(
        username="01001001011",
        password="senha123",
        email="joao@email.com",
        first_name="João",
        last_name="Teste",
    )

    login_url = reverse("token_obtain_pair")

    payload = {"username": "01001001011", "password": "senha123"}

    response = client.post(login_url, data=payload, format="json")

    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data

    # === 1. Testa o GET /api/profile/ ===
    list_url = reverse("ProfileRestView-list")
    access_token = response.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    response = client.get(list_url)

    assert response.status_code == 200
    assert response.data["username"] == "01001001011"
    assert response.data["email"] == "joao@email.com"

    # === 2. Testa o PUT /api/profile/{id}/ (update) ===
    detail_url = reverse("ProfileRestView-detail", args=[user.id])
    payload = {
        "first_name": "Joãozinho",
        "last_name": "Atualizado",
        "username": "01001001011",
        "email": "joao@email.com",
        "password": "senha123",  # write_only, mas necessário para validação se for obrigatória
    }

    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    response = client.put(detail_url, data=payload, format="json")
    assert response.status_code == 200
    assert response.data["first_name"] == "Joãozinho"
    assert response.data["last_name"] == "Atualizado"

    user.refresh_from_db()
    assert user.first_name == "Joãozinho"

    # === 3. Testa que POST não é permitido ===
    response = client.post(list_url, data=payload, format="json")
    assert response.status_code == 405

    # === 4. Testa que DELETE não é permitido ===
    response = client.delete(detail_url)
    assert response.status_code == 405
