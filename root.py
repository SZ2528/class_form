from tkinter import *
from time import sleep
from flask import move,pause,change_data


"""主课表"""
class Main():  
    def __init__(self):
        #变量配置
        self.classes=[]
        self.num=0
        self.useless=[]
        self.today_list=''
        self.local=''
        self.move_list=[]
        self.select_class=None
        self.select_label=None
        self.aft_cl=None

        #窗口配置
        self.window=Tk()
        self.screen_wid=self.window.winfo_screenwidth()
        self.width=840
        self.height=79
        self.class_height=0
        self.class_width=0
        self.leave=10


    """初始化窗口"""
    def win_init(self):
        self.window.geometry(str(self.width)+'x'+str(self.height)+'+'+str(int((self.screen_wid-self.width)/2))+'+5')#设置窗口位置及大小
        self.window.overrideredirect(True)#隐藏标题栏
        self.window.attributes('-topmost',True)#置顶
        self.window.attributes('-alpha',0.7)#透明度
        self.window.config(bg='black')#设置背景色
        self.window.update()


    """窗口课程渲染"""
    def make(self):
        #数据初始化
        self.move_list=[]
        self.classes=[]
        self.useless=[]
        self.width=840

        position=10#Label位置

        #组装Label
        for class_text in self.today_list:
            class_lab=Label(self.window,text=class_text,font=('幼圆',40),fg='white',bg='black')
            class_lab.place(x=position,y=10)
            class_lab.bind('<Double-Button-1>',self.select)
            if class_text=='|':
                self.useless.append(class_lab)
            else:
                self.classes.append(class_lab)
                self.move_list.append(position)
            position+=class_lab.winfo_reqwidth()

        #配置窗口
        self.class_width=class_lab.winfo_reqwidth()
        self.class_height=class_lab.winfo_reqheight()
        self.width=position+(self.leave)*2
        self.height=self.class_height+(self.leave)*2
        self.window.update()


    """高亮课程"""
    def light(self,num):
        if self.num!=num:
            self.num=num
            self.begin()
            self.window.attributes('-topmost',False)
            self.classes[self.num]['fg']='white'
            self.classes[self.num+1]['fg']='yellow'
            self.window.update()
        else:
            self.classes[self.num]['fg']='white'
            self.classes[self.num+1]['fg']='yellow'
            self.window.update()

        if self.aft_cl!=None:
            self.aft_cl.update()


    """下课动画"""
    def after(self):
        #配置下课窗口
        self.aft_cl=Tk()
        self.aft_cl.overrideredirect(True)#隐藏标题栏
        self.aft_cl.attributes('-topmost',True)#置顶
        self.aft_cl.attributes('-alpha',0.7)#透明度
        self.aft_cl.config(bg='black')

        #配置动画数据
        after_txt=Label(self.aft_cl,text='下课时间',font=('幼圆',40),fg='yellow',bg='black')
        label_width=after_txt.winfo_reqwidth()+20
        win_x=int((self.screen_wid-self.width-60-label_width)/2)
        aft_x=win_x+60+self.width
        self.aft_cl.geometry(str(label_width)+'x79+'+str(aft_x)+'+5')
        after_txt.place(x=10,y=10)

        #动画执行
        self.aft_cl.attributes('-alpha',0)

        if self.select_label!=None:
            self.select_label.destroy()
            self.select_label=None
            self.select_class=None
        for cl in self.classes:
            cl.unbind('<Double-Button-1>')
        pause([self.window,self.aft_cl],1)
        
        move([self.window],[self.width],[self.height],[win_x],[5])
        for t in range(8):
            self.aft_cl.attributes('-alpha',t/10)
            sleep(0.01)

        for cl in self.classes:
            cl.bind('<Double-Button-1>',self.select)


    """上课动画"""
    def begin(self):
        for cl in self.classes:
            cl.unbind('<Double-Button-1>')
        pause([self.window,self.aft_cl],1)
        if self.aft_cl!=None:
            self.aft_cl.destroy()
        move([self.window],[self.width],[self.height],[int((self.screen_wid-self.width)/2)],[5])
        for cl in self.classes:
            cl.bind('<Double-Button-1>',self.select)
        self.aft_cl=None

        #摧毁原有Label
        for class_text in self.classes:
            class_text.destroy()
        for class_text in self.useless:
            class_text.destroy()

        #配置动画数据
        begin_lab=Label(self.window,text="准备上课",font=('幼圆',40),fg='yellow',bg='black')
        class_lab=Label(self.window,text=self.local[self.num+1],font=('幼圆',40),fg='yellow',bg='black')
        label_width=begin_lab.winfo_reqwidth()

        #执行动画
        #第一步:缩至1格
        move([self.window],[self.class_width+20],[self.class_height+20],[int((self.screen_wid-self.width)/2+self.move_list[self.num+1])],[5])
        class_lab.place(y=self.leave,relx=0.5,anchor='n')
        begin_lab.place(y=self.leave+self.height,relx=0.5,anchor='n')
        self.window.update()
        pause([self.window],1)

        #第二步:放大
        move([self.window],[label_width+20],[self.height*2],[int((self.screen_wid-self.width)/2+self.move_list[self.num+1]-(label_width-self.class_width)/2)],[5])
        pause([self.window],30)

        #第三步:还原
        begin_lab.destroy()
        class_lab.destroy()
        move([self.window],[self.width],[79],[int((self.screen_wid-self.width)/2)],[5])
        self.make()



    """放学文字"""
    def school(self):
        for class_text in self.classes:
            class_text.destroy()
        for class_text in self.useless:
            class_text.destroy()

        class_text=Label(self.window,text='放学了',font=('幼圆',40),fg='yellow',bg='black')
        class_text.place(x=int((self.width-180)/2),y=10)
        self.window.update()
        self.window.mainloop()


    def select(self,event):
        #检测点击课程序号
        num=0
        for x in self.move_list:
            if event.x_root-self.window.winfo_x()>= x:
                num+=1

        if num>2 and num-1!=self.select_class:#如果是点击了新的课程那么就执行更新动画
            #全刷
            for lab in self.classes:
                lab['bg']='black'

            if self.select_class==None:#如果第一次就跳过还原动画
                self.classes[num-1]['bg']='grey'

                #创建选择label
                self.select_label=Label(self.window,text='语 数 英 物 化 体 自 跨 生 道 班',font=('幼圆',40),fg='white',bg='black')
                self.select_label.place(y=self.height+self.leave,relx=0.5,anchor='n')
                self.select_label.bind('<Double-Button-1>',self.change)
                self.window.update()

            else:#更新
                self.classes[num-1]['bg']='grey'

                #还原窗口
                move([self.window],[self.width],[self.height],[self.window.winfo_x()],[5])

            #扩展窗口
            move([self.window],[self.width],[self.height*2],[self.window.winfo_x()],[5])
            self.select_class=num-1

        else:
            self.classes[self.select_class]['bg']='black'
            self.select_class=None
            move([self.window],[self.width],[self.height],[self.window.winfo_x()],[5])
            self.select_label.destroy()
            self.select_label=None


    def change(self,event):
        num=0
        for x in range(11):
            if event.x_root-self.window.winfo_x()>=self.select_label.winfo_x()+(self.select_label.winfo_reqwidth()/11*x):
                num+=1
        self.classes[self.select_class]['bg']='black'
        self.classes[self.select_class]['text']='语数英物化体自跨生道班'[num-1]
        self.local=self.local[:self.select_class]+'语数英物化体自跨生道班'[num-1]+self.local[self.select_class+1:]
        self.today_list=change_data(self.local)
        self.window.update()
        move([self.window],[self.width],[self.height],[self.window.winfo_x()],[5])
        self.select_label.destroy()
        self.select_label=None
        self.select_class=None

