# 8-3 T恤：编写一个名为make_shirt()的函数，它接受一个尺码以及要印到T恤上的字样。这个函数应打印一个句子，
# 概要地说明T恤的尺码和字样。使用位置实参调用这个函数来制作一件T恤；
# 再使用关键字实参来调用这个函数。

def make_shirt(size="L",text="I love Python"):
    print("这件T恤衫的尺码是"+size+"字体样式是"+text)

make_shirt("M","黑体")
make_shirt(text="宋体",size="XL")

# 8-4 大号T恤：修改函数make_shirt()，使其在默认情况下制作一件印有字样“I love Python”的大号T恤。
# 调用这个函数来制作如下T恤：一件印有默认字样的大号T恤、一件印有默认字样的中号T恤和一件印有其他字样的T恤（尺码无关紧要）。

make_shirt()
make_shirt("M")
make_shirt(text="是的吗")