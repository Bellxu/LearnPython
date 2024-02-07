# 创建一个名为test_cities.py的程序，对刚编写的函数进行测试（别忘了，你需要导入模块unittest以及要测试的函数）。
# 编写一个名为test_city_country()的方法，核实使用类似于'santiago'和'chile'这样的值来调用前述函数时，得到的字符串是正确的。
# 运行test_cities.py，确认测试test_city_country()通过了。

import unittest
from city_functions import city_inform

class CityCountryTestCase(unittest.TestCase):
    def test_city_and_country(self):
        """"可以这样测试吗"""
        city_inform_=city_inform("beijing","china")
        self.assertEqual(city_inform_,"Beijing,China")

unittest.main()