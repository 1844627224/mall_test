import requests


class TestOrder:


    def test_get_order_list(self, api_client):
        """正向用例：获取订单列表"""
        path = "/order/list"
        params = {"pageNum": 1, "pageSize": 5}

        result = api_client.get(path, params=params)

        assert result["code"] == 200

    def test_get_order_list_no_token(self):
        """反向用例：订单列表，无 token"""
        url = "https://admin-api.macrozheng.com/order/list"
        params = {"pageNum": 1, "pageSize": 5}

        resp = requests.get(url, params=params)
        result = resp.json()

        assert resp.status_code == 200
        assert result["code"] == 401, f"预期无权限，实际返回: {result}"

    def test_get_order_setting(self, api_client):
        """正向用例：获取订单设置"""
        path = "/orderSetting/1"

        result = api_client.get(path)

        assert result["code"] == 200

    def test_get_order_setting_no_token(self):
        """反向用例：获取订单设置，无 token"""
        url = "https://admin-api.macrozheng.com/orderSetting/1"

        resp = requests.get(url)
        result = resp.json()

        assert resp.status_code == 200
        assert result["code"] == 401, f"预期无权限，实际返回: {result}"

    def test_get_return_apply_list(self, api_client):
        """正向用例：获取退货申请列表"""
        path = "/returnApply/list"
        params = {"pageNum": 1, "pageSize": 5}

        result = api_client.get(path, params=params)

        assert result["code"] == 200

    def test_get_return_apply_list_no_token(self):
        """反向用例：获取退货申请列表，无 token"""
        url = "https://admin-api.macrozheng.com/returnApply/list"
        params = {"pageNum": 1, "pageSize": 5}

        resp = requests.get(url, params=params)
        result = resp.json()

        assert resp.status_code == 200
        assert result["code"] == 401, f"预期无权限，实际返回: {result}"
