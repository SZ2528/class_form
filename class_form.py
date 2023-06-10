from datetime import datetime,date
from root import Main
from flask import change_data
from time import sleep

"""课程总配置"""
start_list=[(7,20),(8,30),(9,20),(10,10),(11,5),(12,30),(13,0),(13,50),(14,45),(15,30),(16,45)]#每节课开始时间
end_list=[(8,0),(9,10),(10,0),(10,55),(11,45),(12,50),(13,40),(14,35),(15,25),(16,35),(18,45)]
class_list={0:'周一化数英语语物物体道英化',
    1:'周二英英生物体化道语数化数',
    2:'周三物英数道物语体语化语语',
    3:'周四数语数体化数英英数物物',
    4:'周五语英化语数英班跨自数英',
    5:'周六无无无无无无无无无无无',
    6:'周日无无无无无无一二三四晚'}

start_list=[(7,18),(8,28),(9,18),(10,8),(11,3),(12,28),(12,58),(13,48),(14,43),(15,33),(16,43)]



if __name__ == '__main__':
    window=Main()

    today=datetime.now()
    to_week=date(today.year,today.month,today.day).weekday()
    window.today_list=change_data(class_list[to_week])
    window.local=class_list[to_week]

    window.make()
    window.win_init()

    
    num=0

    while True:
        now=(datetime.now().hour,datetime.now().minute)

        if len(end_list)==1 and now>=end_list[0]:
            window.school()

        if len(start_list)>=1:
            if now>start_list[0]:
                del(start_list[0])
                window.window.attributes('-topmost',False)
                num+=1
                window.num+=1
            elif now==start_list[0]:
                del(start_list[0])
                num+=1

            if now>end_list[0]:
                del(end_list[0])
                window.window.attributes('-topmost',True)
            elif now==end_list[0]:
                del(end_list[0])
                window.window.attributes('-topmost',True)
                window.after()


        window.light(num)
        sleep(0.1)
