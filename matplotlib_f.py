#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
        # x = np.linspace(0,10,1000)
        # y = np.sin(x) + 1
        # z = np.cos(x**2) + 1
        #
        # plt.figure(figsize=(8,4))
        # plt.plot(x,y,label = '$sin x+1$',color = 'red',linewidth = 2)
        # plt.plot(x,z,'b--',label = '$\cosx^2+1$')
        # plt.xlabel('Time(s)')
        # plt.ylabel('Volt')
        # plt.title("A  Q")
        # plt.ylim(0,2.2)
        # plt.legend()
        # plt.show()
x = np.random.randn(1000)
plt.hist(x,10)
plt.show()
