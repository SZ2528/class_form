from time import time,sleep
from math import exp

"""动画"""
def move(window,hopel,hopew,hopex,hopey):
    length=[]
    width=[]
    x=[]
    y=[]
    win=[]
    for b in range(len(window)):
        length.append(window[b].winfo_width())
        width.append(window[b].winfo_height())
        x.append(window[b].winfo_x())
        y.append(window[b].winfo_y())
        a=-5
        while a<5:
            length_now=-(length[b]-hopel[b])/(1+exp(-a))+length[b]
            width_now=-(width[b]-hopew[b])/(1+exp(-a))+width[b]
            x_now=-(x[b]-hopex[b])/(1+exp(-a))+x[b]
            y_now=-(y[b]-hopey[b])/(1+exp(-a))+y[b]
            win.append(str(int(length_now))+"x"+str(int(width_now))+"+"+str(int(x_now))+"+"+str(int(y_now)))
            a+=0.2
            
    b=1
    while b<50:        
        for a in range(len(window)):
            window[a].geometry(win[b+50*a])
            window[a].update()
        b+=1
        sleep(0.01)

def pause(windows,times):
    start=time()
    while time()<=start+times:
        for window in windows:
            if window!=None:
                window.update()

def change_data(data):
    return data[0:2]+'|'+data[2]+'|'+data[3:7]+'|'+data[7]+'|'+data[8:12]+'|'+data[12]
