import pytest
import yaml
from code.calculator import Calculator

def setup_module():
    # 打印测试开始的提醒
    print('\n【本次测试作业的计算测试开始.】')

def teardown_module():
    # 打印测试结束的提醒
    print('【本次测试作业的计算测试结束.】')

def get_datas():
    with open("./test_data.yml") as shuju:
        datas = yaml.safe_load(shuju)
        print(datas)
        # 获取文件中key为datas的数据
        datas_test = datas["datas"]
        # 获取文件中key为myids的数据
        ids_test = datas["myids"]
        return [datas_test, ids_test]
print(888)
print(get_datas()[0])
print("666")
print(get_datas()[1])

# class TestCalc:
#     def setup_class(self):
#         # 实例化类,生成类的对象
#         self.calc = Calculator()
#
#     #  使用参数化
#     @pytest.mark.parametrize("a", get_datas()[0][0], ids=get_datas())
#     @pytest.mark.parametrize("b", get_datas()[0][1], ids=get_datas())
#     # @pytest.mark.parametrize(expected = get_datas()[0] + get_datas()[1])
#     # 测试add函数
#     def test_add(self, a, b):
#         expected = a + b
#         print(expected)
#         # 调用add函数,返回的结果保存在result里面
#         result = self.calc.add(a, b)
#         # 判断result结果是否等于期望的值
#         assert result == expected
    #
    # @pytest.mark.parametrize("a,b,expected", [(66, 22, 44), (-11, -19, 8), (-6, 9, -15), (8.5, 5.5, 3)],
    #                          ids=("Posi", "Nega", "Posi&Nega", "Float"))
    # def test_sub(self, a, b, expected):
    #     result = self.calc.sub(a, b)
    #     assert result == expected
    #
    # @pytest.mark.parametrize("a,b,expected", [(3, 7, 21), (-3, -8, 24), (14, -6, -84), (0.5, 9.6, 4.8)],
    #                          ids=("Posi", "Nega", "Posi&Nega", "Float"))
    # def test_mul(self, a, b, expected):
    #     result = self.calc.mul(a, b)
    #     assert result == expected
    #
    # @pytest.mark.parametrize("a,b,expected", [(20, 5, 4), (-24, -2, 12), (36, -9, -4), (8.8, 1.6, 5.5)],
    #                          ids=("Posi", "Nega", "Posi&Nega", "Float"))
    # def test_div(self, a, b, expected):
    #     result = self.calc.div(a, b)
    #     assert result == expected