import pytest

class TestYougileProjects:

    # ПОЗИТИВНЫЕ ТЕСТЫ
    def test_create_project_success(self, api_client, project_data):
        """Создание проекта с валидными данными"""
        response = api_client.create_project(project_data)
        assert response.status_code == 201
        assert "id" in response.json()

    def test_get_project_success(self, api_client, created_project):
        """Получение существующего проекта"""
        response = api_client.get_project(created_project)
        data = response.json()
        assert response.status_code == 200
        assert data["id"] == created_project
        assert "title" in data

    def test_update_project_success(self, api_client, created_project):
        """Обновление проекта с валидными данными"""
        update_data = {"title": "Updated Project Title"}
        response = api_client.update_project(created_project, update_data)
        assert response.status_code == 200
        assert "id" in response.json()

    # НЕГАТИВНЫЕ ТЕСТЫ
    def test_create_project_without_title(self, api_client):
        """Создание проекта без title"""
        response = api_client.create_project({})
        assert response.status_code == 400

    def test_get_project_not_found(self, api_client):
        """Получение несуществующего проекта"""
        response = api_client.get_project("non_existent_id_123")
        assert response.status_code == 404

    def test_update_project_empty_title(self, api_client, created_project):
        """Обновление с пустым title"""
        response = api_client.update_project(created_project, {"title": ""})
        assert response.status_code in [400, 422]