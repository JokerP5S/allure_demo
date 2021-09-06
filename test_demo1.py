import allure
import pytest



@allure.feature("测试allure")
class TestAllure():
    @pytest.mark.parametrize("code",[200,400,500])
    def test_login(self,code):
        assert code==200


