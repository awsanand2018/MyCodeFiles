import csv,os,time,sys, inspect

import subprocess,shutil

from subprocess import Popen

import pandas as pd

class Employees:

    total_ppl=0

    sno=0

    count=0

    eno=[]

    def __init__(self,eid,fname,lname,age,pay,title,rep_mgr):

        self.eid=eid

        self.fname=fname

        self.lname=lname

        self.age=age

        self.pay=pay

        self.title=title

        self.rep_mgr=rep_mgr

        myfile_exists=os.path.isfile('Emp_Details.csv')

        if myfile_exists:

            with open("Emp_Details.csv","r",newline='') as f:

                csv_reader=csv.DictReader(f)

                Employees.sno = sum(1 for row in csv_reader)                

        Employees.sno+=1

        with open("Emp_Details.csv","a+",newline='') as f:

            csv_header=['S.No','Emp.ID','First Name','Last Name','Fullname','Email','Age','Pay','Title','Reporting Manager']

            csv_reader=csv.DictReader(f)

            csv_writer=csv.DictWriter(

                f,fieldnames=csv_header)

            if not myfile_exists:

                csv_writer.writeheader()

            csv_writer.writerow({'S.No':Employees.sno,'Emp.ID':self.eid,'First Name':self.fname[0].upper()+self.fname[1:].lower(),'Last Name':self.lname[0].upper()+self.lname[1:].lower(),'Fullname':self.fullname(),'Email':self.email(),'Age':self.age,'Pay':self.pay,'Title':self.title[0].upper()+self.title[1:].lower(),'Reporting Manager':self.rep_mgr[0].upper()+self.rep_mgr[1:].lower()})

    @staticmethod        

    def design():

        print("\n"+"*"*50+"\n")

    def fullname(self):

        return '{} {}'.format(self.fname[0].upper()+self.fname[1:].lower(),self.lname[0].upper()+self.lname[1:].lower())

    def email(self):

        return '{}.{}@example.com'.format(self.fname,self.lname)

                                                   

    @staticmethod

    def eid_checking(q):

          with open("Emp_Details.csv") as f:

            readfile=csv.DictReader(f)

            for emps in readfile:

              Employees.eno.append(emps['Emp.ID'])

            if q not in Employees.eno:

              if inspect.stack()[1][3]=='record_update' or inspect.stack()[1][3]=='emp_view' or inspect.stack()[1][3]=='delete_module':

                print("\nPlease enter the correct Employee ID")

              if inspect.stack()[1][3]=='record_update':

                record_update()

              elif inspect.stack()[1][3]=='emp_view':

                emp_view()

              elif inspect.stack()[1][3]=='record_creation':

                record_creation()

              elif inspect.stack()[1][3]=='delete_module':

                delete_module()

              else:

                print()

class Manager(Employees):

    def __init__(self,eid,fname,lname,age,pay,title,rep_mgr):

        super().__init__(eid,fname,lname,age,pay,title,rep_mgr)

        print("\nA Manager employee record created for {}".format(Employees.fullname(self)))

class Developer(Manager,Employees):

    def __init__(self,eid,fname,lname,age,pay,title,rep_mgr):

        Employees.__init__(self,eid,fname,lname,age,pay,title,rep_mgr)

        print("\nA Developer employee record created for {}".format(Employees.fullname(self)))

class Testing(Manager,Employees):

    def __init__(self,eid,fname,lname,age,pay,title,rep_mgr):

        Employees.__init__(self,eid,fname,lname,age,pay,title,rep_mgr)

        print("\nA Testing employee record created for {}".format(Employees.fullname(self)))

class Others(Manager,Employees):

    def __init__(self,eid,fname,lname,age,pay,title,rep_mgr):

        Employees.__init__(self,eid,fname,lname,age,pay,title,rep_mgr)

        print("\nOther employee record created for {}".format(Employees.fullname(self)))

try:

  def final_code():

    time.sleep(1)

    q1=input("\nAre you done with your records? [yes | y] ")

    if q1.lower()=='yes' or q1.lower()=='y':

      print('\nOkay!')

      Employees.design()        

      q=input("\nDo you want me to launch the file for you, just in case you want to review? [yes | y] ")

      if q.lower()=='yes' or q.lower()=='y':

          print("Launching the file...")

          # subprocess.Popen(r'C:\Program Files\Microsoft Office\Office15\EXCEL.EXE Emp_Details.csv') 

          # Use the above line of code with the right path of excel program on your computer

          sys.exit()

      else:

          print("\n\nAlright. Bye for now! :-)\n\n")

          sys.exit()

    else:

      first_code()

  def nodata():

    print("\n\nYou didn't provide any/right data. Did you? That's not good :-) \nLet me start over the app for you....")

    first_code() 

  def delete_module():

    dq=input("\nPlease enter the Employee ID of the person to delete his/her record [Enter 0 to skip]")

    if dq.isdigit() and int(dq)!=0:

      Employees.eid_checking(dq)

    else:

      print("\nPlease make sure you are entering only digits for Employee ID")

      delete_module()

    if int(dq)==0:

      final_code()

    

    fn=['S.No','Emp.ID','First Name','Last Name','Fullname','Email','Age','Pay','Title','Reporting Manager']

    with open('Emp_Details.csv','r') as inputfile, open('output.csv','w') as outputfile:

      r=csv.DictReader(inputfile,fieldnames=fn)

      w=csv.DictWriter(outputfile,fieldnames=fn)

      for lines in r:

          if not dq==lines['Emp.ID']:

              w.writerow(lines)

    shutil.move('output.csv','Emp_Details.csv') 

    print("\nEmployee record {} of {} is deleted\n".format(dq,lines['Fullname']))

    final_code()

  def record_creation():

      tot=int(input("\nHow many employee records do you want to create? [ Enter 0 to skip ]"))

      if tot==0:

          print("\nAlright! ")

      

      n=1

      eno=[]

      while n<=tot:

          print("\nPlease enter the details for employee {}".format(n))

          Employees.design()

          def other_inputs(eid):

            fn=input("What's the employee's first name? ")

            ln=input("What's the employee's last name? ")

            e_age=input("What's his/her age? ")

            if e_age.isdigit()==False:

              print("Please make sure you are entering only digits for age")

              e_age=int(input("What's his/her age? "))

            if int(e_age)<18:

                e_age=input("\nAll employees must be at least or more than 18 years old\nIf you have made a typo, please re-enter the correct age ")

            e_pay=int(input("What's his/her pay? "))

            e_title=input("What's his/her title? [ Manager | Developer | Testing | Others ] ")

            if e_title.lower()=='manager':

                mq=input("Is he/she a Senior manager? [ yes | y] ")

                if mq.lower()=='yes' or mq.lower()=='y':

                    mgr1=Manager(eid,fn,ln,e_age,e_pay,"Senior Manager","Corp")

                else:

                    mq1=input("Who is your reporting manager? ")

                    mgr1=Manager(eid,fn,ln,e_age,e_pay,e_title,mq1)

            elif e_title.lower()=='developer':

                mq1=input("Who is your reporting manager? ")

                dev1=Developer(eid,fn,ln,e_age,e_pay,e_title,mq1)

            elif e_title.lower()=='testing':

                mq1=input("Who is your reporting manager? ")

                test1=Testing(eid,fn,ln,e_age,e_pay,e_title,mq1)

            elif e_title.lower()=='others':

                other=input("Please enter your line of work ")

                mq1=input("Who is your reporting manager? ")

                other1=Others(eid,fn,ln,e_age,e_pay,other,mq1)

            else:

                print("\nPlease check the spellings of your title and re-enter it. Starting over the record creation to have a clean record")

                other_inputs(eid)

          def eid_check():

            empid=input("\nEnter the Employee ID: ")

            if empid.isdigit():

                myfile_exists=os.path.isfile('Emp_Details.csv')

                with open("Emp_Details.csv","a+",newline='') as f:

                    csv_header=['S.No','Emp.ID','First Name','Last Name','Fullname','Email','Age','Pay','Title','Reporting Manager']

                    csv_writer=csv.DictWriter(f,fieldnames=csv_header)

                    if not myfile_exists:

                      csv_writer.writeheader()

                    csv_reader=csv.DictReader(f)

                Employees.eid_checking(empid)    

                if empid in Employees.eno:

                  print("\nThe Employee ID {} you entered already exists.\nPlease enter a different Employee ID. ".format(empid))

                  eid_check()

                else:

                  eid=empid

                  other_inputs(eid)

            else:

              print("Please make sure you are entering only digits for Employee ID")

              eid_check()

          eid_check()        

          n+=1

      final_code()

  def record_update():

      q=input("\nPlease enter the Employee ID of the person for who you want to review/update the details ")

      if q.isdigit():

        Employees.eid_checking(q)

      else:

        print("\nPlease make sure you are entering only digits for Employee ID")

        record_update()

      

      q1=input("\nWhat detail you want to update for this employee?\n\nFirst Name\nLast Name\nAge\nPay\nTitle\nReporting Manager\n( Not case sensitive )\n\n")

      with open('Emp_Details.csv','r+') as f:

          r=csv.DictReader(f)

          df=pd.read_csv('Emp_Details.csv')

          for rows in r:

              if q==rows['Emp.ID']:

                  if q1.lower()=='firstname' or q1.lower()=='first name':

                      q1=rows['First Name']

                      fq='First Name'

                  if q1.lower()=='lastname' or q1.lower()=='last name':

                      q1=rows['Last Name']

                      fq='Last Name'

                  if q1.lower()=='age':

                      q1=rows['Age']

                      fq='Age'

                  if q1.lower()=='pay':

                      q1=rows['Pay']

                      fq='Pay'

                  if q1.lower()=='title':

                      q1=rows['Title']

                      fq='Title'

                  if q1.lower()=='reportingmanager' or q1.lower()=='reporting manager':

                      q1=rows['Reporting Manager']

                      fq='Reporting Manager'

                  q2=input('\nJust to make sure, you want to update the {} for the employee {}, who works as a {} in {}\'s team ? [yes | y]'.format(fq,rows['Fullname'],rows['Title'],rows['Reporting Manager']))

                  if q2.lower()=='yes' or q2.lower()=='y':

                      q3=input("Okay. The {} of employee {} currently is {}.\nPlease enter the new data now ".format(fq,rows['Fullname'],q1))   

                  else:

                    cq=int(input("\nAlright. I can do one of two things.\n\n\t1. Restart the app\n\t2. Restart only the record update module\t[Enter 1 or 2] "))

                    if cq==1:

                      first_code()

                    if cq==2:

                      record_update()

                    else:

                      nodata()

                  df.loc[df['Emp.ID']==int(q),fq]=q3[0].upper()+q3[1:].lower()

                  df.loc[df['Emp.ID']==int(q),'Fullname']=df['First Name']+ ' '+df['Last Name']

                  df.loc[df['Emp.ID']==int(q),'Email']=df['First Name']+ '.'+df['Last Name']+'@example.com'

                  df.to_csv("Emp_Details.csv", index=False)

                  print("Record updated...")

      final_code()  

    

  def tree_view():

      mgrs1=[]

      devs=[]

      tests=[]

      others=[]

      t=0

      m=d=te=o=0

      overview=input("\nWould you like to see an overview of employees? [yes | y] ")

      

      if overview.lower()=='yes' or overview.lower()=='y':

          with open("Emp_Details.csv") as f:

              csv_reader=csv.DictReader(f)

              for l in csv_reader:

                  t+=1

                  if l['Title'].lower()=='manager' or l['Title'].lower()=='senior manager':

                      m+=1

                      mgrs1.append(l['Fullname'])

                  elif l['Title'].lower()=='developer':

                      d+=1

                      devs.append(l['Fullname'])

                  elif l['Title'].lower()=='testing':

                      te+=1

                      tests.append(l['Fullname'])

                  else:

                      o+=1

                      others.append(l['Fullname'])

          print("\nThere are totally {} employees. Out of {} employees, there are {} managers, {} developers, {} testers and {} other employees\n\n".format(t,t,m,d,te,o))

          time.sleep(1)

          print("#"*50)

          print('\nManagers : {}\n\nDevelopers : {}\n\nTesters : {}\n\nOthers : {}\n\n'.format(mgrs1,devs,tests,others))

          print("#"*50)

          time.sleep(1)

          mgr_view()

      else:

          print("Okay!")

          final_code()

  def emp_view():

    eq=input("\nIf you would like to see an Employee's record, please enter the Employee ID [ Enter 0 to skip ] ")

    if eq.isdigit():

      if int(eq)==0:

        final_code()

      else:

          Employees.eid_checking(eq)

          with open("Emp_Details.csv") as f:

            csv_reader1=csv.DictReader(f)

            print()

            for r1 in csv_reader1:

              if int(eq)==int(r1['Emp.ID']):

                for k,v in r1.items():

                  print(k,' - ',v)

            final_code()

    else:

      print("\nPlease make sure you are entering only digits for Employee ID")

      emp_view()

  def mgr_view():     

    mgr_names=[]

      

    with open("Emp_Details.csv") as f:

          csv_reader=csv.DictReader(f)

          for r in csv_reader:

              if r['Title'].lower()=='manager' or r['Title'].lower()=='senior manager':

                  mgr_names.append(r['Fullname'].lower())

          mq=input('\n\nName of the managers in the directory at this time :{}\n\nPlease enter the name of the manager to see their reportees: [Enter any number to skip]'.format(mgr_names))

          if mq.isdigit():

              emp_view()

          if mq not in mgr_names and mq.isdigit()==False:

              print("\nPlease check the spellings and re-enter the manager name correctly ")

              mgr_view()

          if mq in mgr_names and mq.isdigit()==False:

              tree_view1(mgr_names,mq)

  def tree_view1(mgr_names,mq):

      rep=[]

      i=1

      print("\nManager {} has the following reportees : \n".format(mq[0].upper()+mq[1:].lower()))

      with open("Emp_Details.csv") as f:

          csv_reader=csv.DictReader(f)

          for r in csv_reader:

              if mq==r['Reporting Manager'].lower():

                  rep.append(r['Fullname'])

                  print(i,r['Fullname']+' - '+r['Title'])   

                  i+=1 

      emp_view()

  Employees.design()

  print("\t\tWelcome!")

  Employees.design()

  def first_code():

      fq=input("\nPlease select one of the options below\n\n\t1. Create New Employee Records\n\n\t2. Update Existing Employee Records\n\n\t3. Organization/Employee Records View\n\n\t4. Delete Record \n\n\t5. Exit\n\n[ Enter a digit between 1-5 ] ")

      if fq.isdigit():

        if int(fq)==1:

            record_creation()

        elif int(fq)==2:

            record_update()

        elif int(fq)==3:

            tree_view()

        elif int(fq)==4:

            delete_module()

        elif int(fq)==5:

          sys.exit("\nOkay. I will be here when you need me. Bye!")

        else:

            print("\nPlease enter a digit between 1-5")

            first_code()

      else:

        print("\nPlease enter a digit. No letters are allowed")

        first_code()

  first_code()

  Employees.design()

except Exception as e:

  print("\nYou either made a typo and didn't provide the data when asked.\nStarting over the application for you....")

  print(e)

  first_code()               

