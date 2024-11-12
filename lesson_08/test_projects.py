import requests
import pytest


@pytest.fixture
def create_project(base_url, headers):
    """Создает проект перед выполнением тестов
      и удаляет его после выполнения."""
    project_data = {"title": "Test Project"}
    response = requests.post(
        f"{base_url}/api-v2/projects", headers=headers, json=project_data
    )
    assert response.status_code == 201, (
        f"Проект не был создан: {response.status_code} {response.text}"
    )
    project_id = response.json().get("id")
    yield project_id

    # Удаляем проект после выполнения тестов
    if project_id:
        requests.delete(
            f"{base_url}/api-v2/projects/{project_id}",
            headers=headers
        )


def test_create_project(base_url, headers):
    """Тест создания проекта."""
    project_data = {"title": "Test Project"}
    response = requests.post(
        f"{base_url}/api-v2/projects", headers=headers, json=project_data
    )
    assert response.status_code == 201, (
        f"Проект не был создан: {response.status_code} {response.text}"
    )
    assert "id" in response.json(), "Ответ не содержит ID проекта"


def test_get_all_projects(base_url, headers):
    """Тест получения всех проектов."""
    response = requests.get(f"{base_url}/api-v2/projects", headers=headers)
    assert response.status_code == 200, "Не удалось получить список проектов"
    response_data = response.json()
    assert "content" in response_data, "Ответ не содержит ключа 'content'"
    assert isinstance(
        response_data["content"], list
    ), "Ответ 'content' не является списком"


def test_update_project(base_url, headers, create_project):
    """Тест обновления проекта."""
    update_data = {"title": "Updated Project Title"}
    response = requests.put(
        f"{base_url}/api-v2/projects/{create_project}",
        headers=headers,
        json=update_data
    )
    assert response.status_code == 200, (
        f"Проект не был обновлен: {response.status_code} {response.text}"
    )

    # Проверка обновления через GET запрос
    get_response = requests.get(
        f"{base_url}/api-v2/projects/{create_project}", headers=headers
    )
    assert get_response.status_code == 200, (
        f"Не удалось получить проект по ID: {get_response.status_code} "
        f"{get_response.text}"
    )
    assert get_response.json().get("title") == "Updated Project Title", (
        "Название проекта не обновлено"
    )


def test_get_project_by_id(base_url, headers, create_project):
    """Тест получения проекта по ID."""
    response = requests.get(
        f"{base_url}/api-v2/projects/{create_project}", headers=headers
    )
    assert response.status_code == 200, (
        f"Не удалось получить проект по ID: {response.status_code} "
        f"{response.text}"
    )
    assert response.json().get("id") == create_project, \
        "ID полученного проекта не совпадает"


def test_create_project_missing_fields(base_url, headers):
    """Тест создания проекта с отсутствующими обязательными полями."""
    incomplete_data = {}
    response = requests.post(
        f"{base_url}/api-v2/projects", headers=headers, json=incomplete_data
    )
    assert response.status_code == 400, \
        "Ожидался статус 400 при отсутствии обязательных полей"
