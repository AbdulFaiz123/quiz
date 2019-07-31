from openpyxl import Workbook
import openpyxl as pyxl

l_s_map= {"s":9,":s":10,"A":8,"B":7,"C":6,"D":5,"E":4,"F":0}
class Student:
    def __init__(self,name,usn):
        self.name=name
        self.usn=usn
        self.subject=[]

    def show_sgpa_info(self):
        g_c=0
        s_c=0
        for s in self.subject:
            g_c+=s["C"]*l_s_map[s["G"]]
            s_c+=s["C"]
        si=g_c/s_c
        print(f"name:{self.name} {si}")


wb= pyxl.load_workbook("Result.xlsx")
sheet = wb.active
Students=[]
for row in sheet.iter_rows(min_rows=3,min_cols=2,max_col=2):
    if row:
        data = [c.value for c in row]
        stu = data[:2]
        sub_1= data[5:7]
        sub_2=data[-2:]
        student=Student(*stu)
        student.subject.append({"C":sub_1[0],"G":sub_1[1]})
        student.subject.append({"C":sub_2[0],"G":sub_2[1]})
        Students.append(student)


