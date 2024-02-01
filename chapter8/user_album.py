# 8-8 用户的专辑：在为完成练习8-7编写的程序中，编写一个while循环，让用户输入一个专辑的歌手和名称。
# 获取这些信息后，使用它们来调用函数make_album()，并将创建的字典打印出来。在这个while循环中，务必要提供退出途径

def make_album(singer_name,album_name,song_count=""):
    album={"歌手":singer_name,"专辑名":album_name}
    if song_count:
        album["歌曲数"]=song_count
    return album

# 设置一个标志，指出调查是否继续
ablum={}
polling_active = True
while polling_active:
    print("我们将调查你最喜欢的专辑的相关信息,调查过程中输入q可以退出") 
    print("接下来清输入你最喜欢的专辑的相关信息")
    singer_name=input("\n歌手名是?")
    ablum_name=input("\n专辑名是?")
    song_count=input("\n专辑歌曲数量是?")
    ablum=make_album(singer_name,ablum_name,song_count)
    polling=input("\nZ输入yes退出?")
    polling_active=not (polling == "yes")
print(ablum)
    
