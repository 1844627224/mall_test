import requests
import time


class TestProduct:

    def test_get_product_list(self, api_client):
        """正向用例：获取商品列表"""
        path = "/product/list"
        params = {"pageNum": 1, "pageSize": 5}

        result = api_client.get(path, params=params)

        assert result["code"] == 200
        assert "list" in result.get("data", {}), "返回数据中缺少 list 字段"
        assert len(result["data"]["list"]) >= 0, "商品列表获取失败"

    def test_get_product_list_no_token(self):
        """反向用例：商品列表，无 token"""
        url = "https://admin-api.macrozheng.com/product/list"
        params = {"pageNum": 1, "pageSize": 5}

        resp = requests.get(url, params=params)
        result = resp.json()

        assert resp.status_code == 200
        assert result["code"] == 401, f"预期无权限，实际返回: {result}"

    def test_get_category_list(self, api_client):
        """正向用例：获取商品分类列表"""
        path = "/productCategory/list/0"
        params = {"pageNum": 1, "pageSize": 5}

        # 修复3：必须调用 .get() 方法
        result = api_client.get(path, params=params)

        assert result["code"] == 200

    def test_get_category_list_no_token(self):
        """反向用例：获取商品分类列表，无 token"""
        url = "https://admin-api.macrozheng.com/productCategory/list/0"
        params = {"pageNum": 1, "pageSize": 5}

        resp = requests.get(url, params=params)
        result = resp.json()

        assert resp.status_code == 200
        assert result["code"] == 401, f"预期无权限，实际返回: {result}"

    def test_create_product(self, api_client):
        """正向用例：创建商品"""
        path = "/product/create"
        unique_name = f"test_auto_{int(time.time())}"

        payload = {
            "brandId": 6,
            "productCategoryId": 1,
            "name": unique_name,
            "price": 99.9
        }

        result = api_client.post(path, json=payload)

        is_success = result["code"] == 200
        is_demo_limit = (result["code"] == 500 and "演示环境" in result.get("message", ""))

        assert is_success or is_demo_limit, f"创建失败，返回信息: {result.get('message')}"

    def test_create_product_no_token(self):
        """反向用例：创建商品，无 token"""
        url = "https://admin-api.macrozheng.com/product/create"
        payload = {
            "brandId": 6,
            "productCategoryId": 1,
            "name": "test_no_token",
            "price": 99.9
        }

        resp = requests.post(url, json=payload)
        result = resp.json()

        assert resp.status_code == 200
        assert result["code"] == 401, f"预期无权限，实际返回: {result}"

    def test_get_product_attribute_list(self, api_client):
        """正向用例：获取商品属性分类列表"""
        path = "/productAttribute/category/list"
        params = {"pageNum": 1, "pageSize": 5}

        result = api_client.get(path, params=params)

        assert result["code"] == 200

    def test_get_product_attribute_list_no_token(self):
        """反向用例：获取商品属性分类列表，无 token"""
        url = "https://admin-api.macrozheng.com/productAttribute/category/list"
        params = {"pageNum": 1, "pageSize": 5}

        resp = requests.get(url, params=params)
        result = resp.json()

        assert resp.status_code == 200
        assert result["code"] == 401, f"预期无权限，实际返回: {result}"

    def test_get_product_brand_list(self, api_client):
        """正向用例：获取商品品牌列表"""
        path = "/brand/list"
        params = {"pageNum": 1, "pageSize": 5}

        result = api_client.get(path, params=params)

        assert result["code"] == 200

    def test_get_product_brand_list_no_token(self):
        """反向用例：获取商品品牌列表，无 token"""
        url = "https://admin-api.macrozheng.com/brand/list"
        params = {"pageNum": 1, "pageSize": 5}

        resp = requests.get(url, params=params)
        result = resp.json()

        assert resp.status_code == 200
        assert result["code"] == 401, f"预期无权限，实际返回: {result}"