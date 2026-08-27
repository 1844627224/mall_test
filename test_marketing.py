import requests

class TestMarketing:

    def test_get_brand_recommend_list(self, api_client):
        """正向用例：获取品牌推荐列表"""
        path = "/home/brand/list"
        params = {"pageNum": 1, "pageSize": 5}

        result = api_client.get(path, params=params)

        assert result["code"] == 200

    def test_get_brand_recommend_list_no_token(self):
        """反向用例：品牌推荐列表，无 token"""
        url = "https://admin-api.macrozheng.com/home/brand/list"
        params = {"pageNum": 1, "pageSize": 5}

        resp = requests.get(url, params=params)
        result = resp.json()

        assert resp.status_code == 200
        assert result["code"] == 401, f"预期无权限，实际返回: {result}"

    # ==================== 秒杀活动 ====================

    def test_get_flash_list(self, api_client):
        """正向用例：获取秒杀活动列表"""
        path = "/flash/list"
        params = {"pageNum": 1, "pageSize": 5}

        result = api_client.get(path, params=params)

        assert result["code"] == 200

    def test_get_flash_list_no_token(self):
        """反向用例：秒杀活动列表，无 token"""
        url = "https://admin-api.macrozheng.com/flash/list"
        params = {"pageNum": 1, "pageSize": 5}

        resp = requests.get(url, params=params)
        result = resp.json()

        assert resp.status_code == 200
        assert result["code"] == 401, f"预期无权限，实际返回: {result}"

    # ==================== 优惠券列表 ====================

    def test_get_coupon_list(self, api_client):
        """正向用例：获取优惠券列表"""
        path = "/coupon/list"
        params = {"pageNum": 1, "pageSize": 10}

        result = api_client.get(path, params=params)

        assert result["code"] == 200

    def test_get_coupon_list_no_token(self):
        """反向用例：优惠券列表，无 token"""
        url = "https://admin-api.macrozheng.com/coupon/list"
        params = {"pageNum": 1, "pageSize": 10}

        resp = requests.get(url, params=params)
        result = resp.json()

        assert resp.status_code == 200
        assert result["code"] == 401, f"预期无权限，实际返回: {result}"

    # ==================== 新品推荐 ====================

    def test_get_new_product_list(self, api_client):
        """正向用例：获取新品推荐列表"""
        path = "/home/newProduct/list"
        params = {"pageNum": 1, "pageSize": 5}

        result = api_client.get(path, params=params)

        assert result["code"] == 200

    def test_get_new_product_list_no_token(self):
        """反向用例：新品推荐列表，无 token"""
        url = "https://admin-api.macrozheng.com/home/newProduct/list"
        params = {"pageNum": 1, "pageSize": 5}

        resp = requests.get(url, params=params)
        result = resp.json()

        assert resp.status_code == 200
        assert result["code"] == 401, f"预期无权限，实际返回: {result}"

    # ==================== 人气推荐 ====================

    def test_get_recommend_product_list(self, api_client):
        """正向用例：获取人气推荐列表"""
        path = "/home/recommendProduct/list"
        params = {"pageNum": 1, "pageSize": 5}

        result = api_client.get(path, params=params)

        assert result["code"] == 200

    def test_get_recommend_product_list_no_token(self):
        """反向用例：人气推荐列表，无 token"""
        url = "https://admin-api.macrozheng.com/home/recommendProduct/list"
        params = {"pageNum": 1, "pageSize": 5}

        resp = requests.get(url, params=params)
        result = resp.json()

        assert resp.status_code == 200
        assert result["code"] == 401, f"预期无权限，实际返回: {result}"

    # ==================== 专题推荐 ====================

    def test_get_recommend_subject_list(self, api_client):
        """正向用例：获取专题推荐列表"""
        path = "/home/recommendSubject/list"
        params = {"pageNum": 1, "pageSize": 5}

        result = api_client.get(path, params=params)

        assert result["code"] == 200

    def test_get_recommend_subject_list_no_token(self):
        """反向用例：专题推荐列表，无 token"""
        url = "https://admin-api.macrozheng.com/home/recommendSubject/list"
        params = {"pageNum": 1, "pageSize": 5}

        resp = requests.get(url, params=params)
        result = resp.json()

        assert resp.status_code == 200
        assert result["code"] == 401, f"预期无权限，实际返回: {result}"

    # ==================== 广告列表 ====================

    def test_get_advertise_list(self, api_client):
        """正向用例：获取广告列表"""
        path = "/home/advertise/list"
        params = {"pageNum": 1, "pageSize": 5}

        result = api_client.get(path, params=params)

        assert result["code"] == 200

    def test_get_advertise_list_no_token(self):
        """反向用例：广告列表，无 token"""
        url = "https://admin-api.macrozheng.com/home/advertise/list"
        params = {"pageNum": 1, "pageSize": 5}

        resp = requests.get(url, params=params)
        result = resp.json()

        assert resp.status_code == 200
        assert result["code"] == 401, f"预期无权限，实际返回: {result}"