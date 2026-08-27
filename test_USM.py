import requests

class TestUms:

    # ==================== 用户列表 ====================

    def test_get_admin_list(self, api_client):
        """正向用例：获取管理员用户列表"""
        path = "/admin/list"
        params = {"pageNum": 1, "pageSize": 5}

        result = api_client.get(path, params=params)

        assert result["code"] == 200

    def test_get_admin_list_no_token(self):
        """反向用例：管理员列表，无 token"""
        url = "https://admin-api.macrozheng.com/admin/list"
        params = {"pageNum": 1, "pageSize": 5}

        resp = requests.get(url, params=params)
        result = resp.json()

        assert resp.status_code == 200
        assert result["code"] == 401, f"预期无权限，实际返回: {result}"

    # ==================== 角色列表（全部） ====================

    def test_get_role_list_all(self, api_client):
        """正向用例：获取所有角色列表"""
        path = "/role/listAll"

        result = api_client.get(path)

        assert result["code"] == 200

    def test_get_role_list_all_no_token(self):
        """反向用例：获取所有角色列表，无 token"""
        url = "https://admin-api.macrozheng.com/role/listAll"

        resp = requests.get(url)
        result = resp.json()

        assert resp.status_code == 200
        assert result["code"] == 401, f"预期无权限，实际返回: {result}"

    # ==================== 角色列表（分页） ====================

    def test_get_role_list(self, api_client):
        """正向用例：获取角色列表（分页）"""
        path = "/role/list"
        params = {"pageNum": 1, "pageSize": 5}

        result = api_client.get(path, params=params)

        assert result["code"] == 200

    def test_get_role_list_no_token(self):
        """反向用例：角色列表（分页），无 token"""
        url = "https://admin-api.macrozheng.com/role/list"
        params = {"pageNum": 1, "pageSize": 5}

        resp = requests.get(url, params=params)
        result = resp.json()

        assert resp.status_code == 200
        assert result["code"] == 401, f"预期无权限，实际返回: {result}"

    # ==================== 菜单列表 ====================

    def test_get_menu_list(self, api_client):
        """正向用例：获取菜单列表"""
        # 截图显示路径为 /menu/list/0，通常 0 代表根节点或全部
        path = "/menu/list/0"

        result = api_client.get(path)

        assert result["code"] == 200

    def test_get_menu_list_no_token(self):
        """反向用例：获取菜单列表，无 token"""
        url = "https://admin-api.macrozheng.com/menu/list/0"

        resp = requests.get(url)
        result = resp.json()

        assert resp.status_code == 200
        assert result["code"] == 401, f"预期无权限，实际返回: {result}"

    # ==================== 资源分类列表（全部） ====================

    def test_get_resource_category_list_all(self, api_client):
        """正向用例：获取所有资源分类列表"""
        path = "/resourceCategory/listAll"

        result = api_client.get(path)

        assert result["code"] == 200

    def test_get_resource_category_list_all_no_token(self):
        """反向用例：获取所有资源分类列表，无 token"""
        url = "https://admin-api.macrozheng.com/resourceCategory/listAll"

        resp = requests.get(url)
        result = resp.json()

        assert resp.status_code == 200
        assert result["code"] == 401, f"预期无权限，实际返回: {result}"

    # ==================== 资源列表（分页） ====================

    def test_get_resource_list(self, api_client):
        """正向用例：获取资源列表"""
        path = "/resource/list"
        params = {"pageNum": 1, "pageSize": 5}

        result = api_client.get(path, params=params)

        assert result["code"] == 200

    def test_get_resource_list_no_token(self):
        """反向用例：获取资源列表，无 token"""
        url = "https://admin-api.macrozheng.com/resource/list"
        params = {"pageNum": 1, "pageSize": 5}

        resp = requests.get(url, params=params)
        result = resp.json()

        assert resp.status_code == 200
        assert result["code"] == 401, f"预期无权限，实际返回: {result}"