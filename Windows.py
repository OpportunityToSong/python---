import tkinter as tk
import os
from Book import Thing
from tkinter import ttk
import tkinter.messagebox


class windows:
    def __init__(self, master):
        self.master = master
        self.student = ''  # 学生
        self.thing = Thing()  # 物资类
        self.lbl = tk.Label(self.master, text='欢迎使用物资管理系统', font=('microsoft yahei', 15),
                            fg='DarkViolet')
        self.lbl.place(x=100, y=0)
        self.f1 = None
        self.flag = ''
        self.identity() # 选择身份

    def identity(self):
        """选择身份"""
        if self.f1:
            self.f1.destroy()
        self.f1 = tk.Frame(self.master)
        self.f1['width'] = 400
        self.f1['height'] = 300
        self.lf = tk.LabelFrame(self.f1, text='选择身份')
        # 单选按钮
        self.vSex = tk.StringVar()  # 创建StringVar对象，性别
        self.vSex.set('管理员')  # 设置初始值：男性
        self.radioSexM = tk.Radiobutton(self.lf, text="管理员", value='管理员', variable=self.vSex)  # 单选按钮
        self.radioSexF = tk.Radiobutton(self.lf, text="学生", value='学生', variable=self.vSex)
        self.radioSexM.pack()
        self.radioSexF.pack()
        self.btn = tk.Button(self.lf, text='确定', width='5', command=self.log)
        self.btn.pack()
        self.lf.place(x=170, y=40)
        self.f1.place(x=0, y=80)

    def log(self):
        """登录"""
        if self.f1:
            self.f1.destroy()
        if self.vSex.get() == '管理员':    # 如果是管理员，则为账号
            text = '账号'
            self.flag = '管理员'
            self.f1 = tk.Frame(self.master)
            self.f1['width'] = 400
            self.f1['height'] = 300
            self.lf = tk.LabelFrame(self.f1, text='登录')
            self.lbl1 = tk.Label(self.lf, text=text)
            self.lbl1.pack()
            self.entry1 = tk.Entry(self.lf)
            self.entry1.pack()
            self.lbl2 = tk.Label(self.lf, text='密码')
            self.lbl2.pack()
            self.entry2 = tk.Entry(self.lf, show='*')
            self.entry2.pack()
            self.btn1 = tk.Button(self.lf, text='返回', command=self.identity)
            self.btn1.pack(side='left')
            self.btn1 = tk.Button(self.lf, text='登录', command=lambda: self.m_s1(self.entry1.get(), self.entry2.get()))
            self.btn1.pack(side='right')
            self.lf.place(x=130, y=40)
            self.f1.place(x=0, y=100)
        else:                             # 如果是学生，则为学号
            text = '学号'
            self.flag = '学生'
            self.f1 = tk.Frame(self.master)
            self.f1['width'] = 400
            self.f1['height'] = 300
            self.lf = tk.LabelFrame(self.f1, text='登录')
            self.lbl1 = tk.Label(self.lf, text=text)
            self.lbl1.pack()
            self.entry1 = tk.Entry(self.lf)
            self.entry1.pack()
            self.lbl2 = tk.Label(self.lf, text='姓名')
            self.lbl2.pack()
            self.entry2 = tk.Entry(self.lf, show='')
            self.entry2.pack()
            self.btn1 = tk.Button(self.lf, text='返回', command=self.identity)
            self.btn1.pack(side='left')
            self.btn1 = tk.Button(self.lf, text='登录', command=lambda: self.m_s2(self.entry1.get(), self.entry2.get()))
            self.btn1.pack(side='right')
            self.lf.place(x=130, y=40)
            self.f1.place(x=0, y=100)

    def m_s1(self, x, y):
        """主界面"""
        if x != 'sgh' or y != '2020':
            tk.messagebox.showinfo("提示", "请重新输入账号或密码")
        else:
            if self.f1:
                self.f1.destroy()
            self.f1 = tk.Frame(self.master)
            self.f1['width'] = 400
            self.f1['height'] = 300
            if self.flag == '管理员':
                self.btn1 = tk.Button(self.f1, text='查询物资', font=('microsoft yahei', 12),
                                      width=23, fg='DarkViolet', command=self.show_things)
                self.btn1.place(x=80, y=0)
                self.btn2 = tk.Button(self.f1, text='增加物资', font=('microsoft yahei', 12),
                                      width=23, fg='DarkViolet', command=self.add_thing)
                self.btn2.place(x=80, y=50)
                self.btn3 = tk.Button(self.f1, text='删除物资', font=('microsoft yahei', 12),
                                      width=23, fg='DarkViolet', command=self.delete_thing)
                self.btn3.place(x=80, y=100)
                self.btn4 = tk.Button(self.f1, text='返回登陆', font=('microsoft yahei', 12),
                                      width=23, fg='DarkViolet', command=self.identity)
                self.btn4.place(x=80, y=150)

            else:
                self.student = x
                self.btn5 = tk.Button(self.f1, text='借阅物资', font=('microsoft yahei', 12),
                                      width=23, fg='DarkViolet', command=self.borrow_thing)
                self.btn5.place(x=80, y=0)
                self.btn6 = tk.Button(self.f1, text='归还物资', font=('microsoft yahei', 12),
                                      width=23, fg='DarkViolet', command=self.return_thing)
                self.btn6.place(x=80, y=50)
                self.btn7 = tk.Button(self.f1, text='返回登陆', font=('microsoft yahei', 12),
                                      width=23, fg='DarkViolet', command=self.identity)
                self.btn7.place(x=80, y=100)
            self.f1.place(x=0, y=100)
        
    def m_s2(self, x, y):
        """主界面"""
        if x == '' or y == '':
            tk.messagebox.showinfo("提示", "请输入学号姓名")
        else:
            if self.f1:
                self.f1.destroy()
            self.f1 = tk.Frame(self.master)
            self.f1['width'] = 400
            self.f1['height'] = 300
            if self.flag == '管理员':
                self.btn1 = tk.Button(self.f1, text='查询物资', font=('microsoft yahei', 12),
                                      width=23, fg='DarkViolet', command=self.show_things)
                self.btn1.place(x=80, y=0)
                self.btn2 = tk.Button(self.f1, text='增加物资', font=('microsoft yahei', 12),
                                      width=23, fg='DarkViolet', command=self.add_thing)
                self.btn2.place(x=80, y=50)
                self.btn3 = tk.Button(self.f1, text='删除物资', font=('microsoft yahei', 12),
                                      width=23, fg='DarkViolet', command=self.delete_thing)
                self.btn3.place(x=80, y=100)
                self.btn4 = tk.Button(self.f1, text='返回登陆', font=('microsoft yahei', 12),
                                      width=23, fg='DarkViolet', command=self.identity)
                self.btn4.place(x=80, y=150)

            else:
                self.student = x
                self.btn5 = tk.Button(self.f1, text='借用物资', font=('microsoft yahei', 12),
                                      width=23, fg='DarkViolet', command=self.borrow_thing)
                self.btn5.place(x=80, y=0)
                self.btn6 = tk.Button(self.f1, text='归还物资', font=('microsoft yahei', 12),
                                      width=23, fg='DarkViolet', command=self.return_thing)
                self.btn6.place(x=80, y=50)
                self.btn7 = tk.Button(self.f1, text='返回登陆', font=('microsoft yahei', 12),
                                      width=23, fg='DarkViolet', command=self.identity)
                self.btn7.place(x=80, y=100)
            self.f1.place(x=0, y=100)

    def show_things(self):
        """显示物资信息"""
        if self.f1:
            self.f1.destroy()
        self.f1 = tk.Frame(self.master)
        self.f1['width'] = 400
        self.f1['height'] = 300

        self.lf = tk.LabelFrame(self.f1, text='物资信息')
        # 显示text
        self.text = tk.Text(self.lf, width=56, height=18)
        self.str1 = ''
        if os.path.exists('物资信息.txt'):
            with open('物资信息.txt', 'r', encoding='utf-8') as f:
                for i in f.readlines():
                    self.str1 += i
        self.text.insert(0.0, self.str1)
        self.text.pack()
        self.btn = tk.Button(self.lf, text='返回', command=lambda: self.m_s1('sgh', '2020'))
        self.btn.pack()
        self.lf.pack()
        self.f1.place(x=0, y=100)

    def add_thing(self):
        """添加物资信息"""
        if self.f1:
            self.f1.destroy()
        self.f1 = tk.Frame(self.master)
        self.f1['width'] = 400
        self.f1['height'] = 300
        self.lf = tk.LabelFrame(self.f1, text='添加物资信息')
        self.name = tk.Label(self.lf, text='物资名字')
        self.name.pack()
        self.name_entry = tk.Entry(self.lf)
        self.name_entry.pack()
        self.category = tk.Label(self.lf, text='物资类型')
        self.category.pack()
        self.category_entry = tk.Entry(self.lf)
        self.category_entry.pack()
        self.count = tk.Label(self.lf, text='物资数量')
        self.count.pack()
        self.count_entry = tk.Entry(self.lf)
        self.count_entry.pack()

        def cmd1():
            self.thing.add_thing(self.name_entry.get(), self.category_entry.get(), self.count_entry.get())
            self.category_entry.delete(0, 'end')
            self.name_entry.delete(0, 'end')
            self.count_entry.delete(0, 'end')

        self.btn1 = tk.Button(self.lf, text='返回', command=lambda: self.m_s1('sgh', '2020'))
        self.btn1.pack(side='left')
        self.btn2 = tk.Button(self.lf, text='确定', command=cmd1)
        self.btn2.pack(side='right')
        self.lf.place(x=130, y=40)
        self.f1.place(x=0, y=80)

    def borrow_thing(self):
        """借物资"""
        if self.f1:
            self.f1.destroy()
        self.f1 = tk.Frame(self.master)
        self.f1['width'] = 400
        self.f1['height'] = 300
        self.lf = tk.LabelFrame(self.f1, text='借用物资')
        self.cbox = ttk.Combobox(self.lf)
        self.cbox['values'] = [i['物资名称'] for i in self.thing.thing_list if i['状态'] != '正在借用']
        self.cbox.pack()

        def cmd2():
            self.thing.update('T', self.cbox.get(), self.student)
            tk.messagebox.showinfo('提示', '已成功借用{}物资'.format(self.cbox.get()))
            self.cbox.set('')
            self.cbox['values'] = [i['物资名称'] for i in self.thing.thing_list if i['状态'] != '正在借用']

        self.btn1 = tk.Button(self.lf, text='返回', command=lambda: self.m_s2(self.student, '1'))
        self.btn1.pack(side='left')
        self.btn2 = tk.Button(self.lf, text='借用', command=cmd2)
        self.btn2.pack(side='right')
        self.lf.place(x=130, y=40)
        self.f1.place(x=0, y=80)

    def return_thing(self):
        """归还物资"""
        if self.f1:
            self.f1.destroy()
        self.f1 = tk.Frame(self.master)
        self.f1['width'] = 400
        self.f1['height'] = 300
        self.lf = tk.LabelFrame(self.f1, text='归还物资')
        self.cbox = ttk.Combobox(self.lf)
        self.cbox['values'] = [i['物资名称'] for i in self.thing.thing_list if i['状态'] == '正在借用'
                               and i['借用人/组织'] == self.student]
        self.cbox.pack()

        def cmd3():
            self.thing.update('F', self.cbox.get())
            tk.messagebox.showinfo('提示', '已归还{}物资'.format(self.cbox.get()))
            self.cbox.set('')
            self.cbox['values'] = [i['物资名称'] for i in self.thing.thing_list if i['状态'] == '正在借用']

        self.btn1 = tk.Button(self.lf, text='返回', command=lambda: self.m_s2(self.student, '1'))
        self.btn1.pack(side='left')
        self.btn2 = tk.Button(self.lf, text='归还', command=cmd3)
        self.btn2.pack(side='right')
        self.lf.place(x=130, y=40)
        self.f1.place(x=0, y=80)

    def delete_thing(self):
        """删物资"""
        if self.f1:
            self.f1.destroy()
        self.f1 = tk.Frame(self.master)
        self.f1['width'] = 400
        self.f1['height'] = 300
        self.lf = tk.LabelFrame(self.f1, text='删除物资')
        self.cbox = ttk.Combobox(self.lf)
        self.cbox['values'] = [i['物资名称'] for i in self.thing.thing_list]
        self.cbox.pack()

        def cmd4():
            self.thing.update('D', self.cbox.get())
            tk.messagebox.showinfo('提示', '已删除{}物资'.format(self.cbox.get()))
            self.cbox.set('')
            self.cbox['values'] = [i['物资名称'] for i in self.thing.thing_list]

        self.btn1 = tk.Button(self.lf, text='返回', command=lambda: self.m_s1('sgh', '2020'))
        self.btn1.pack(side='left')
        self.btn2 = tk.Button(self.lf, text='删除', command=cmd4)
        self.btn2.pack(side='right')
        self.lf.place(x=130, y=40)
        self.f1.place(x=0, y=80)
