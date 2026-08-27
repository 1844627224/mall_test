import requests

class TestLogin:
    """
    登录模块自动化测试
    """
    BASE_URL = "https://admin-api.macrozheng.com"
    USERNAME = "admin"
    PASSWORD = "macro123"

    def test_login_success(self):
        """正向用例：正确账号密码，应成功"""
        url = f"{self.BASE_URL}/admin/login"
        payload = {
            "username": self.USERNAME,
            "password": self.PASSWORD
        }

        response = requests.post(url, json=payload)
        result = response.json()

        assert response.status_code == 200
        assert result["code"] == 200, f"业务状态码异常：{result}"
        assert "token" in result.get("data", {}), "返回数据中缺少 token 字段"
        assert result["data"]["token"], "token 为空"

    def test_login_wrong_password(self):
        """反向用例：密码错误，应失败"""
        url = f"{self.BASE_URL}/admin/login"
        payload = {
            "username": self.USERNAME,
            "password": "123456"
        }

        response = requests.post(url, json=payload)
        result = response.json()

        assert response.status_code == 200

        assert result["code"] == 500, f"预期业务失败，实际返回: {result}"
        assert result["message"] == "密码不正确", f"预期错误信息'密码不正确'，实际: {result['message']}"
