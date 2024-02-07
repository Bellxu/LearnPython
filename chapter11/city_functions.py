# 11-1 城市和国家：编写一个函数，它接受两个形参：一个城市名和一个国家名。
# 这个函数返回一个格式为City,Country的字符串，如Santiago,Chile。将这个函数存储在一个名为city_functions.py的模块中。

# 11-2 人口数量：修改前面的函数，使其包含第三个必不可少的形参population，并返回一个格式为City,Country-population xxx的字符串，如Santiago,Chile-population 5000000。
# 运行test_cities.py，确认测试test_city_country()未通过。修改上述函数，将形参population设置为可选的。再次运行test_cities.py，确认测试test_city_country()又通过了。
def city_inform(city,country,population=""):
    if population:
        return city.title()+","+country.title()+"-"+str(population)
    else:
        return city.title()+","+country.title()

