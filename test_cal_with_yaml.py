import pytest
import yaml
from code.calculator import Calculator

def get_datas():
    with open("./test_data.yml") as shuju:
        datas = yaml.safe_load(shuju)
        print(datas)
        # 获取文件中key为avalue&bvalue的数据
        avalue_test = datas["avalue"]
        bvalue_test = datas["bvalue"]
        # 获取文件中key为myids的数据
        ids_test = datas["myids"]
        return [avalue_test, bvalue_test, ids_test]

# @pytest.fixture()
# def befor():
#     print("\n【本次测试作业的计算测试开始.】")

class TestCalc:
    def setup_class(self):
        # 实例化类,生成类的对象
        self.calc = Calculator()

    #使用参数化
    @pytest.mark.parametrize("a", get_datas()[0], ids=get_datas()[2])
    @pytest.mark.parametrize("b", get_datas()[1], ids=get_datas()[2])
    # 测试add函数
    def test_add(self, a, b):
        expected = a + b
        # 调用add函数,返回的结果保存在result里面
        result = self.calc.add(a, b)
        # 判断result结果是否等于期望的值
        assert result == expected

    @pytest.mark.parametrize("a", get_datas()[0], ids=get_datas()[2])
    @pytest.mark.parametrize("b", get_datas()[1], ids=get_datas()[2])
    def test_sub(self, a, b):
        expected = a - b
        result = self.calc.sub(a, b)
        assert result == expected

    @pytest.mark.parametrize("a", get_datas()[0], ids=get_datas()[2])
    @pytest.mark.parametrize("b", get_datas()[1], ids=get_datas()[2])
    def test_mul(self, a, b):
        expected = a * b
        result = self.calc.mul(a, b)
        assert result == expected


    @pytest.mark.parametrize("a", get_datas()[0], ids=get_datas()[2])
    @pytest.mark.parametrize("b", get_datas()[1], ids=get_datas()[2])
    def test_div(self, a, b):
        if b != 0:
            expected = a / b
            result = self.calc.div(a, b)
            assert result == expected
        else:
            print(f'参数b为{b}，不能作为除数。')
            assert b == 0


