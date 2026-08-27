import pytest
import requests

BASE_URL = "https://admin-api.macrozheng.com"
USERNAME = "admin"
PASSWORD = "macro123"


@pytest.fixture(scope="session")
def auth_token():
    """获取token"""
    url = f"{BASE_URL}/admin/login"
    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()

        assert data["code"] == 200, f"登录失败:{data.get('message')}"

        token_data = data["data"]
        # 组合token
        return token_data["tokenHead"] + token_data["token"]
    except Exception as e:
        pytest.fail(f"获取Token失败：{str(e)}")


@pytest.fixture
def api_client(auth_token):
    # 封装一个自动携带Header的请求客户端
    class Client:
        def __init__(self, token):
            self.headers = {"Authorization": token}
            self.base_url = BASE_URL

        def get(self, path, params=None):
            url = f"{self.base_url}{path}"
            resp = requests.get(url, headers=self.headers, params=params)
            return self._validate(resp)

        def post(self, path, json=None):
            url = f"{self.base_url}{path}"
            resp = requests.post(url, headers=self.headers, json=json)
            return self._validate(resp)

        def _validate(self, resp):
            assert resp.status_code == 200, f"HTTP Error:{resp.status_code}, Body:{resp.text}"
            return resp.json()

    return Client(auth_token)