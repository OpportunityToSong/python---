import tkinter.messagebox
import os


class Thing:
    def __init__(self):
        self.thing_list = []
        self.read_file()

    def add_thing(self, thing_name, category, count, state='未使用', identity='无'):
        if category == '' or thing_name == '' or count == '':
            tkinter.messagebox.showinfo('提示', '请输入完整信息')
        else:
            dict1 = {}
            dict1['物资名称'] = thing_name
            dict1['物资类型'] = category
            dict1['物资数量'] = count
            dict1['状态'] = state
            dict1['借用人/组织'] = identity
            self.thing_list.append(dict1)
            self.write_file()
            tkinter.messagebox.showinfo('提示', '增加成功')

    def write_file(self):
        with open('物资信息.txt', 'w', encoding='utf-8') as f:
            for i in self.thing_list:
                f.write(str(i) + '\n')

    def read_file(self):
        if os.path.exists('物资信息.txt'):
            with open('物资信息.txt', 'r', encoding='utf-8') as f:
                for i in f.readlines():
                    self.thing_list.append(eval(i))

    def update(self, flag, name, identity='无'):
        if flag == 'T':
            for i in self.thing_list:
                if i.get('物资名称') == name:
                    i['状态'] = '正在借用'
                    i['借用人/组织'] = identity
                    break
            self.write_file()
        elif flag == 'F':
            for i in self.thing_list:
                if i.get('物资名称') == name:
                    i['状态'] = '未借走'
                    i['借阅人/组织'] = identity
                    break
            self.write_file()

        else:
            for i, j in enumerate(self.thing_list):
                if j.get('物资名称') == name:
                    del self.thing_list[i]
                    break
            self.write_file()
