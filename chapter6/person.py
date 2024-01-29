
# 6-1 人：使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。该字典应包含键first_name、last_name、age和city。将存储在该字典中的每项信息都打印出来。
person={"first_name":"Bell","last_name":"Xu","age":30,"city":"ZhengJiang"}
print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])

# 6-7 人：在为完成练习6-1而编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为people的列表中。遍历这个列表，将其中每个人的所有信息都打印出来。
person2={"first_name":"Candy","last_name":"Xu","age":23,"city":"ZhengJiang"}
person3={"first_name":"Dell","last_name":"Wang","age":40,"city":"Shanghai"}
people=[person,person2,person3]
for item in people:
    print(item)