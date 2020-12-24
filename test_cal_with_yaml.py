import pytest
import yaml
from code.calculator import Calculator


def setup_module():
    # 打印测试开始的提醒
    print('\n----->自动化测试脚本开始运行.')


def teardown_module():
    # 打印测试结束的提醒
    print('\n----->自动化测试脚本运行结束.')


def get_datas():  # 打开yaml数据文件取值
    with open("./test_data.yml") as shuju:
        datas = yaml.safe_load(shuju)
        # 获取文件中key为avalue&bvalue的数据
        avalue_test = datas["avalue"]
        bvalue_test = datas["bvalue"]
        # 获取文件中key为myids的数据
        ids_test = datas["myids"]
        return [avalue_test, bvalue_test, ids_test]


class TestCalc:
    def setup_class(self):
        # 打印类测试开始的提醒
        print("\n---->开始进行TestCalc类的测试.")
        # 实例化类,生成类的对象
        self.calc = Calculator()

    def teardown_class(self):
        # 打印类测试结束的提醒
        print("\n---->TestCalc类的测试已经结束.")

    # 使用参数化（下同）
    @pytest.mark.parametrize("a", get_datas()[0], ids=get_datas()[2])
    @pytest.mark.parametrize("b", get_datas()[1], ids=get_datas()[2])
    # 测试add函数（下同）
    def test_add(self, a, b):
        # 即时生成预期值（想不到其他办法了）（下同）
        expected = a + b
        # 调用add函数,返回的结果保存在result里面（下同）
        result = self.calc.add(a, b)
        # 判断result结果是否等于期望的值（下同）
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
        # 由于除数不能0，这里做了判断
        # b非0则正常判断
        if b != 0:
            expected = a / b
            result = self.calc.div(a, b)
            assert result == expected
        # b为负数是捕捉错误信息后再进行断言
        else:
            #使用pytest.raises来捕捉除数不能为0的异常信息
            with pytest.raises(ZeroDivisionError) as errorinfo:
                    a / b
            # 对异常信息类型进行断言
            assert errorinfo.type == ZeroDivisionError
            # 对异常信息的值进行断言
            assert "division by zero" in str(errorinfo.value)
