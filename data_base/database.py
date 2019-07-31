import time
import random as rn
import dbcontext as db
from models import Internship 
from models import Student
from prettytable import PrettyTable

def _get_new_id():
    t_obj = time.localtime()
    new_id = rn.randint(1000,9900) + (t_obj.tm_min + t_obj.tm_hour + t_obj.tm_sec)
    return new_id

def add_internship(iname,company,i_year):
    id = _get_new_id()
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("insert into internship(id,iname,company,i_year,status) values(?,?,?,?,?)",(id,iname,company,i_year,1))
            print(f"Internship is added successfully with id:{id}")
    except Exception as e:
        print(str(e))

def view_all_internships():
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("select id,iname,company,i_year,status from internship")
            rows = cursor.fetchall()
            intern_pro_lst = [Internship(*row) for row in rows]
            _view_internship_list(intern_pro_lst)
    except Exception as e:
        print(str(e))
def search_internship_by_name(name):
      try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("select all from intrship where ename:",(name,))
            row = cursor.fetchone()
            intern_pro_lst = [Internship(*row) ]
            _view_internship_list(intern_pro_lst)
      except Exception as e:
        print(str(e))
    
  
def change_status_internship(name):
      try:
          with db.DbContext() as connection:
            cursor = connection.cursor()
            stat = int(input("enter the status of the intership"))
            status = "completed" if stat==0 else "run"
            cursor.execute("update status where status =:(select iname from internship where iname :",(status,name,))
            row = cursor.fetchone()
            intern_pro_lst = [Internship(*row) ]
            _view_internship_list(intern_pro_lst)
      except Exception as e:
        print(str(e))
    


def delete_internship(name):
      try:
          with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("delete the intership where iname=: ",(name,))
         
      except Exception as e:
        print(str(e))

def add_student_internship(name,sem,usn,placed):
     iid = _get_new_id()
     try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("insert into student values(?,?,?,?)",(usn,name,sem,placed))
            print(f"student is added successfully with id:{iid}")
     except Exception as e:
        print(str(e))
def view_all_reg_student():
     try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("select id,iname,company,i_year,status from internship")
            rows = cursor.fetchall()
            intern_pro_lst = [Student(*row) for row in rows]
            _view_student_list(intern_pro_lst)
     except Exception as e:
        print(str(e))
def search_student_by_name(name):
     try:
        t=PrettyTable(['usn','name','sem','placed'])
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("select * from student where name=?",(name,))
            rows = cursor.fetchone()
            intern_pro_lst = [Student(*row) for row in rows ]
            for row in rows:
                t.add_row(row)
            print(t)
            _view_student_list(intern_pro_lst)
     except Exception as e:
        print(str(e))
    
def update_student(iid,sem):
    try:
       with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("update the student (iid,sem) values(?,?,?,?,?)",(iid,sem))
            row = cursor.fetchone()
            intern_pro_lst = [Student(*row)for row in row ]
            _view_student_list(intern_pro_lst)
       
    except Exception as e:
        print(str(e))

def delete_student(name):
     try:
          with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("delete the student where name=: ",(name,))
         
     except Exception as e:
        print(str(e))


def company_ws_count():
    pass
def student_ws_count():
    pass
def ws_student_reports():
    pass

def reg_stu_internship():
    pass

def update_stu_intership_status():
    pass


def _view_internship_list(lst):
    if lst and len(lst) > 0:
        table = PrettyTable()
        table.column_headers = ["ID", "NAME", "COMPANAY", "YEAR","STATUS"]
        for l in lst:
            status = "ComPleted" if l.status == 0 else "Going on" 
            table.append_row([l.id, l.iname, l.company, l.i_year,status])
        print(table)
    else:
        print(f"There are no Intership programms, yet to add...")

def _view_student_list(lst):
    if lst and len(lst) > 0:
        table = PrettyTable()
        table.column_headers = ["USN", "NAME", "SEM","STATUS"]
        for l in lst:
            table.append_row([l.iid, l.name, l.sem,l.placed])
        print(table)
    else:
        print(f"There are no student programms, to display..")