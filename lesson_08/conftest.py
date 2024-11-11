import pytest


@pytest.fixture
def base_url():
    return "https://ru.yougile.com"


@pytest.fixture
def headers():
    return {
        "Authorization": "Bearer your_token",  # Замените на ваш токен
        "Content-Type": "application/json"
    }
