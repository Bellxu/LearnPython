# 8-7 专辑：编写一个名为make_album()的函数，它创建一个描述音乐专辑的字典。
# 这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。
# 使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
# 给函数make_album()添加一个可选形参，以便能够存储专辑包含的歌曲数。
# 如果调用这个函数时指定了歌曲数，就将这个值添加到表示专辑的字典中。调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。

def make_album(singer_name,album_name,song_count=""):
    album={"歌手":singer_name,"专辑名":album_name}
    if song_count:
        album["歌曲数"]=song_count
    return album

print(make_album("周杰伦","范特西",10))