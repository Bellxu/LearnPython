import matplotlib.pyplot as plt
x_vaules=list(range(1,1001))
y_vaues=[x**2 for x in x_vaules]
# plt.scatter(x_vaules,y_vaues,c='red',edgecolors=None,s=40)
# plt.scatter(x_vaules,y_vaues,c=[0,0,0.8],edgecolors=None,s=40)
plt.scatter(x_vaules,y_vaues,c=y_vaues,cmap=plt.cm.Blues,edgecolors=None,s=40)
plt.title("Square Number",fontsize=14)
plt.xlabel("Vaule",fontsize=14)
plt.ylabel("Square of Vaule",fontsize=14)
plt.tick_params(axis="both",which="major",labelsize=14)
plt.axis([0,1100,0,1100000])
plt.show()


