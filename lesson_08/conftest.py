import pytest
import os
import random
from dotenv import load_dotenv
from yougile_client import YougileClient

load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    return "https://ru.yougile.com"


@pytest.fixture(scope="session")
def auth_token():
    token = os.getenv("YOUGILE_API_TOKEN")
    if not token:
        pytest.fail("YOUGILE_API_TOKEN not found. Create .env file with your token")
    return token


@pytest.fixture(scope="session")
def api_client(base_url, auth_token):
    return YougileClient(base_url, auth_token)


@pytest.fixture
def project_data():
    return {
        "title": f"Test Project {random.randint(1000, 9999)}"
        # Убрал description - он не нужен для создания
    }


@pytest.fixture
def created_project(api_client, project_data):
    response = api_client.create_project(project_data)
    assert response.status_code == 201
    project_id = response.json()["id"]

    yield project_id

    # Cleanup
    api_client.delete_project(project_id)