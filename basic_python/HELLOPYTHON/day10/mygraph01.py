import matplotlib.pyplot as plt


fig = plt.figure()

ax = fig.gca(projection='3d')  # 보여줄 방식을 3d로 설정합니다.

ax.set_zlabel('Z')
ax.set_ylabel('Y')
ax.set_xlabel('X')


x = [0,0,0,0,0]
y = [0,1,2,3,4]
z = [1,2,1,2,1]


ax.plot(x, y, z)  


plt.show()





