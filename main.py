from tkinter import *
import sqlite3
import time
import webbrowser
import login

connection7=sqlite3.connect('PythonMarshal.db')
c7=connection7.cursor()

try:
    c7.execute('create table PythonMarshal(teacher varchar(10), DOS varchar(20), class varchar(10), team_no varchar(10) primary key, topic varchar(100), descrip varchar(200), team_members1 varchar(10), team_no1 int(4), team_members2 varchar(10), team_no2 int(2), team_members3 varchar(10), team_no3 int(2), team_members4 varchar(10), team_no4 int(2), grade float(10), documentation varchar(30), highlights varchar(20),Status varchar(20))')
except:
    pass


Name = ''


def menu():
    global menu_screen
    global upload
    global view_table
    global search
    global Name

    name1= " Logined as : " + Name

    menu_screen=Tk()
    menu_screen.title("PROJECT MARSHALAR")
    menu_screen.geometry('640x400')
    menu_screen.geometry('+320+90')
    L=Label(menu_screen,text="Menu")
    L.config(font=("Arial",20))
    L.pack()
    L1=Label(menu_screen,text=name1)
    L1.pack()
    
    Label(menu_screen,text="").pack()
    Label(text="").pack()
    Button(menu_screen,text="UPLOAD PROJECT",width=15,height=1,command=upload).pack()
    Label(text="").pack()   
    Button (menu_screen,text="VIEW TABLE",width=15,height=1,command=dashboard).pack()
    Label(text="").pack()
    Button(menu_screen,text="SEARCH TABLE",width=15,height=1,command=search_table).pack()
    Label(text="").pack()
    Button(menu_screen,text="CLASS STATUS",width=15,height=1,command=class_status).pack()
    Label(text="").pack()
    Button(menu_screen,text="LOGOUT",width=15,height=1,command=Log_out).pack()


def upload():
    menu_screen.destroy()
    global upload_screen
    upload_screen=Tk()
    upload_screen.title("UPLOAD")
    upload_screen.geometry("1600x900")

    global Class_section
    global Team_no
    global Topic
    global Short_Note 
    global Name_Member1
    global Name_Member2
    global Name_Member3
    global Name_Member4
    global Name_Member1
    global Roll_no_Member1
    global Roll_no_Member2
    global Roll_no_Member3
    global Roll_no_Member4
    global Grade
    global Doc
    global Remarks
    global Status
    #global DOS
    Class_section= StringVar()
    Team_no = StringVar()
    Short_Note = StringVar()
    Name_Member1= StringVar()
    Name_Member2= StringVar()
    Name_Member3= StringVar()
    Name_Member4= StringVar()
    Roll_no_Member1= StringVar()
    Roll_no_Member2= StringVar()
    Roll_no_Member3= StringVar()
    Roll_no_Member4= StringVar()
    Grade= StringVar()
    Doc= StringVar()
    Remarks= StringVar()
    Status= StringVar()
    
    Class_section = Label(upload_screen, text="Class and section (format:12A7)")
    Class_section.pack()
    Class_section = Entry(upload_screen,textvariable=Class_section)
    Class_section.pack()

    Team_no = Label(upload_screen, text="Team_no (format:<yearclassteamno>)")
    Team_no.pack()
    Team_no = Entry(upload_screen,textvariable=Team_no)
    Team_no.pack()
    
    Topic= Label(upload_screen, text="Topic")
    Topic.pack()
    Topic= Entry(upload_screen, textvariable=Topic)
    Topic.pack()
    
    Short_Note = Label(upload_screen, text="Short note on topic ")
    Short_Note.pack()
    Short_Note = Entry(upload_screen, textvariable=Short_Note)
    Short_Note.pack()
    
    Name_Member1=Label(upload_screen, text="Name of Member1")
    Name_Member1.pack()
    Name_Member1=Entry(upload_screen, textvariable=Name_Member1)
    Name_Member1.pack()
    
    Roll_no_Member1=Label(upload_screen, text="Roll_no_Member1")
    Roll_no_Member1.pack()
    Roll_no_Member1=Entry(upload_screen, textvariable=Roll_no_Member1)
    Roll_no_Member1.pack()
    
    Name_Member2=Label(upload_screen, text="Name of Member2")
    Name_Member2.pack()
    Name_Member2=Entry(upload_screen, textvariable=Name_Member2)
    Name_Member2.pack()
    
    Roll_no_Member2=Label(upload_screen, text="Roll no of Member2")
    Roll_no_Member2.pack()
    Roll_no_Member2=Entry(upload_screen, textvariable=Roll_no_Member2)
    Roll_no_Member2.pack()
    
    Name_Member3=Label(upload_screen, text="Name of Member3")
    Name_Member3.pack()
    Name_Member3=Entry(upload_screen, textvariable=Name_Member3)
    Name_Member3.pack()

    Roll_no_Member3=Label(upload_screen, text="Roll no of Member3")
    Roll_no_Member3.pack()
    Roll_no_Member3=Entry(upload_screen, textvariable=Roll_no_Member3)
    Roll_no_Member3.pack()

    Name_Member4=Label(upload_screen, text="Name of Member4")
    Name_Member4.pack()
    Name_Member4=Entry(upload_screen, textvariable=Name_Member4)
    Name_Member4.pack()

    Roll_no_Member4=Label(upload_screen, text="Roll no of Member4")
    Roll_no_Member4.pack()
    Roll_no_Member4=Entry(upload_screen, textvariable=Roll_no_Member4)
    Roll_no_Member4.pack()

    Grade= Label(upload_screen, text="Grade")
    Grade.pack()
    Grade= Entry(upload_screen, textvariable=Grade)
    Grade.pack()
    
    Doc= Label(upload_screen, text="Doc")
    Doc.pack()
    Doc= Entry(upload_screen, textvariable=Doc)
    Doc.pack()

    Remarks= Label(upload_screen, text="Remarks")
    Remarks.pack()
    Remarks= Entry(upload_screen, textvariable=Remarks)
    Remarks.pack()

    Status= Label(upload_screen, text="Status(Late/Ontime)")
    Status.pack()
    Status= Entry(upload_screen, textvariable=Status)
    Status.pack()
    
    

    
    Label(upload_screen, text="").pack()
    Button(upload_screen, text="UPLOAD", width=10, height=1, command = up).pack()
    
    
def up():
    Date=str(time.ctime(time.time()))
    month = Date[4:7]
    if 'Jan' in month:
        month = 1
    elif 'Fe' in month:
        month = 2
    elif 'Mar' in month:
        month = 3
    elif 'Ap' in month:
        month = 4
    elif 'May' in month:
        month = 5
    elif 'Jun' in month:
        month = 6
    elif 'Jul' in month:
        month = 7
    elif 'Au' in month:
        month = 8
    elif 'S' in month:
        month = 9
    elif 'Oc' in month:
        month = 10
    elif 'N' in month:
        month = 11
    elif 'Dec' in month:
        month = 12
    Date = Date[8:10] + ':' + str(month) + ':' + Date[-4:]
    Classec=Class_section.get()
    Teamno = Team_no.get()                     
    Topicinfo = Topic.get()
    Shortnote= Short_Note.get()
    NameMember1= Name_Member1.get()
    RollnoMember1= Roll_no_Member1.get()
    NameMember2= Name_Member2.get()
    RollnoMember2= Roll_no_Member2.get()
    NameMember3= Name_Member3.get()
    RollnoMember3= Roll_no_Member3.get()
    NameMember4= Name_Member4.get()
    RollnoMember4= Roll_no_Member4.get()
    Gradeinfo= Grade.get()
    Docinfo= Doc.get()
    Remarksinfo= Remarks.get()
    Statusinfo= Status.get()
    
    uplist=[Name,Date,Classec,Teamno,Topicinfo,Shortnote,NameMember1,RollnoMember1, NameMember2,RollnoMember2,NameMember3,RollnoMember3,NameMember4,RollnoMember4,Gradeinfo,Docinfo,Remarksinfo,Statusinfo]
    qery=""
    for i in uplist:
        qery = qery + '\"' + i + '\"' + ','
    qery = qery[:-1]
    query = 'INSERT INTO PythonMarshal VALUES(' + qery + ')'
    #c7.execute(query)
    #connection7.commit()
    try:
        c7.execute(query)
        connection7.commit()
        
    except:
        global uperror_screen
        uperror_screen=Tk()
        uperror_screen.title("ERROR")
        l= Label(uperror_screen, text="ERROR : REDUNTANT DATA")
        l.config(font=("Arial", 50))
        l.pack()
        
        
     
    

    upload_screen.destroy()
    menu()



def dashboard():
    # Python program to create a table
  
    class Table:
        def __init__(self,root):
            # code for creating table
            for i in range(total_rows):
                for j in range(total_columns):
                    self.e = Entry(root, width=13, fg='blue',
                                   font=('Arial',16,'bold'))
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j])
    # take the data
    c7.execute('select class,DOS,team_no,topic,descrip,team_members1,team_members2,team_members3,team_members4,grade,documentation from PythonMarshal') #class, team_no, topic, short note, namex4, grade
    data = c7.fetchall()
    lst = [("Class","DOS","Team No","Topic","Description","Member1","Member2","Member3","Member4","Grade","Documentation") ]
    lst=lst+data
    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])
    # create root window
    root = Tk()
    t = Table(root)
    root.mainloop()
    menu()


def search_table():
    menu_screen.destroy()
    global search_screen
    search_screen=Tk()
    search_screen.title("SEARCH TABLE")

    global Team_no

    Team_no= StringVar()

    Team_no = Label(search_screen, text="Team_no (format(eg):<202012A704>)")
    Team_no.pack()
    Team_no = Entry(search_screen,textvariable=Team_no)
    Team_no.pack()

    Label(text="").pack()
    Button (search_screen,text="SEARCH TABLE", width=15,height=1,command=search).pack()

def search():
    global content_for_opening_documentation
    Teamno = Team_no.get()
    
    in_put="SELECT * FROM PythonMarshal "
    c7.execute(in_put)
    out_put=c7.fetchall()
    data1=""
    
    for i in out_put:
        if i[3]== Teamno:
            data1=i
        

    content_for_opening_documentation = [Teamno, data1[15]]
    global out_screen
    out_screen=Tk()
    out_screen.title("Result")
    out_screen.geometry("1600x900")
    if data1=="":
            Label(out_screen,text="NO SUCH TEAM").pack()
            
    else:
        for i in range(0,len(data1)+1):
            if i==0:
                pass
            elif i==1:
                q=Label(out_screen,text="DOS: "+str(data1[i]))
                q.config(font=("Arial", 15))
                q.pack()
            elif i==2:
                Label(out_screen,text="").pack()
                w=Label(out_screen,text="Class: "+str(data1[i]))
                w.config(font=("Arial",15))
                w.pack()
            elif i==3:
                Label(out_screen,text="").pack()
                e=Label(out_screen,text="Team_no: "+str(data1[i]))
                e.config(font=("Arial", 15))
                e.pack()
            elif i==4:
                Label(out_screen,text="").pack()
                e=Label(out_screen,text="Topic: "+str(data1[i]))
                e.config(font=("Arial", 20))
                e.pack()
            elif i==5:
                
                r=Label(out_screen,text="Short Note: "+str(data1[i]))
                r.config(font=("Arial", 15))
                r.pack()
            elif i==6:
                Label(out_screen,text="").pack()
                r=Label(out_screen,text="Member 1: "+str(data1[i]))
                r.config(font=("Arial", 15))
                r.pack()
            elif i==7:
                
                r=Label(out_screen,text="Roll no: "+str(data1[i]))
                r.config(font=("Arial", 15))
                r.pack()
            elif i==8:
                Label(out_screen,text="").pack()
                r=Label(out_screen,text="Member 2: "+str(data1[i]))
                r.config(font=("Arial", 15))
                r.pack()
            elif i==9:
                
                r=Label(out_screen,text="Roll no: "+str(data1[i]))
                r.config(font=("Arial", 15))
                r.pack()
            elif i==10:
                Label(out_screen,text="").pack()
                r=Label(out_screen,text="Member 3: "+str(data1[i]))
                r.config(font=("Arial", 15))
                r.pack()
            elif i==11:
                
                r=Label(out_screen,text="Roll no: "+str(data1[i]))
                r.config(font=("Arial", 15))
                r.pack()
            elif i ==12:
                Label(out_screen,text="").pack()
                r=Label(out_screen,text="Member 4: "+str(data1[i]))
                r.config(font=("Arial", 15))
                r.pack()
            elif i==13:
                
                r=Label(out_screen,text="Roll no: "+str(data1[i]))
                r.config(font=("Arial", 15))
                r.pack()
            elif i==14:
                Label(out_screen,text="").pack()
                r=Label(out_screen,text="Grade: "+str(data1[i]))
                r.config(font=("Arial", 20))
                r.pack()
            elif i==16:
                
                r=Label(out_screen,text="Remarks: "+str(data1[i]))
                r.config(font=("Arial", 15))
                r.pack()
            elif i==17:
                
                r=Label(out_screen,text="Status: "+str(data1[i]))
                r.config(font=("Arial", 15))
                r.pack()
            elif i == 18:
                Label(text="").pack()
                Button (out_screen,text="View Documentation", width=15,height=1,command=view_documentation).pack()
                
    Label(out_screen,text="").pack()
    Button (out_screen,text="CLOSE", width=15,height=1,command=Close).pack()
    search_screen.destroy()
    
def view_documentation():
    global content_for_opening_documentation
    #content_for_opening_documentation = [Teamno, doculink]
    t = content_for_opening_documentation
    webbrowser.open(t[1], new = 2)


    
def Close():
    
    out_screen.destroy()
    menu()

    



def class_status():
    try:
        menu_screen.destroy()
    except:
        pass
    global status_screen
    status_screen=Tk()
    status_screen.title("Status")

    global Class
    global Total_no_of_teams

    Class= StringVar()
    Total_no_of_teams=int()

    Class = Label(status_screen, text="Class (format(eg):12A7)")
    Class.pack()
    Class = Entry(status_screen,textvariable=Class)
    Class.pack()

    Total_no_of_teams = Label(status_screen, text="Total No of Teams")
    Total_no_of_teams.pack()
    Total_no_of_teams = Entry(status_screen,textvariable=Total_no_of_teams)
    Total_no_of_teams.pack()

    Label(text="").pack()
    Button (status_screen,text="Check", width=15,height=1,command=Checkstat).pack()
    


def Checkstat():
    
    Classinfo= Class.get()
    Total_no_of_teamsinfo=Total_no_of_teams.get()
    wrongclass_info=True

    try :
        tno=int(Total_no_of_teamsinfo)
    except:
        tno=0
        wrongclass_info=False
        class_status()
    
    
    q=" select * from PythonMarshal"
    c7.execute(q)
    count_late = 0
    count_ontime=0
    for i in c7.fetchall():
        if Classinfo in i:
            if i[17]== "Late": #17 in the table in highlights
                count_late += 1
            else:
                count_ontime += 1
               
    if count_late ==0 and count_ontime==0:
        global error_screen
        error_screen=Tk()
        error_screen.title("Status")

        Label(error_screen,text="NO SUCH CLASS ").pack()
        wrongclass_info= False

            
    count_total = count_late + count_ontime
    status_data = []
    status_data.append(Total_no_of_teamsinfo)
    status_data.append(str(count_total))
    status_data.append(str(count_ontime))
    status_data.append(str(count_late))
    status_data.append(str(tno - count_total))

    class Table:
        def __init__(self,root):
            # code for creating table
            for i in range(total_rows):
                for j in range(total_columns):
                    self.e = Entry(root, width=13, fg='blue',
                                   font=('Arial',16,'bold'))
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j])
                    
    # take the data
    lst = [("Total no of teams","NO. SUBMITTED","ONTIME","LATE","NOT Submitted")]
    lst.append(status_data)
    # find total number of rows and
    # columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])
    if wrongclass_info==True:
        # create root window
        root = Tk()
        t = Table(root)
        root.mainloop()
    
        
        
    menu()








def Log_out():
    time.sleep(1)
    rav = open('Name.txt', 'w')
    rav.write('')
    loginTrue = open('loginTrue.txt', 'w')
    loginTrue.write('')
    menu_screen.destroy()
    ini()






def ini():
    global Name
    loginTrue = open('loginTrue.txt', 'r')
    if loginTrue.read() == 'True':
        jai = open('Name.txt', 'r')
        Name = jai.read()
        menu()
    else:
        print('Please Login')
        login.main_account_screen()
        ini()

ini()




