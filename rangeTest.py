# 4-3
# for number in range(1,21):
# 4-4
numbers=[number for number in range(1,1000001)]
# for number in numbers:
#     print(number)
# print(numbers)
# 4-5
print(max(numbers))
print(min(numbers))
print(sum(numbers))
# 4-6
# numbers=list(range(1,20,2))
# print(numbers)
# 4-7
# numbers=[]
# for number in range(1,11):
#     numbers.append(number*3)
# for number in numbers:
#     print(number)
# 4-8
# numbers=[]
# for number in range(1,11):
#     numbers.append(number**3)
# for number in numbers:
#     print(number)
# 4-9
numbers=[number**3 for number in range(1,11)]
for number in numbers:
    print(number)

# 4-10
print(numbers[:3])
miadde_len=(int)(len(numbers)/2)
print(miadde_len)
print(numbers[miadde_len-3:miadde_len])
print(numbers[-3:])