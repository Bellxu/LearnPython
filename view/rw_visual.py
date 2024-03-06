import matplotlib.pylab as plt
from random_walk import RandomWalk


while True:
    plt.figure(dpi=128,figsize=(10,6))
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_numbers=list(range(rw.number_points))
    plt.scatter(rw.x_vaules,rw.y_vaules,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=15)
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_vaules[-1],rw.y_vaules[-1],c='red',edgecolors='none',s=100)
    # 隐藏坐标轴
    plt.axis('off')
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    plt.show()
    keeprunning = input("Make another walk ?(y/n) :")
    if keeprunning == 'n':
        break