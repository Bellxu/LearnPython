guests = ["张三","李四","王五"]
mystr="邀请"+guests[0]+","+guests[1]+","+guests[2]+"参加宴席"
print(mystr)
cant=guests[1]
print(cant + "无法参加宴席")
guests[1]="赵六"
mystr="邀请"+guests[0]+","+guests[1]+","+guests[2]+"参加宴席"
print(mystr)
guests.insert(0,"孙七")
guests.insert(2,"周八")
guests.append("吴九")
# mystr="邀请"+guests.__str__+"参加宴席"
print(guests)
print(len(guests))
guests.pop()
guests.pop()
guests.pop()
guests.pop()
print(guests)
del guests[0]
del guests[0]
print(guests)

