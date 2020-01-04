from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
import exceldatauser
flag=0
ib2=60
def homewindow():
    theLable.config(text="Instruction:\n1)Select the passage from above menu named passage to take a test won\n"
                            "2)Otherwise choose a text file from your desktop from above add file menu\n"
                            "3)There will be two level of exam first level will be 30word per minutes and level 2 will be 40 word per minutes \n"
                            "4) You need to cleared both level to pass the exam.")
    text.delete('1.0',END)
    text.config(state=DISABLED)
    thelable2.config(text="00 : " + str(ib)+"\nLevel1")


def timerfunc():
    print("timer start")
    global ib2
    ib2 = ib2 - 1
    thelable2.config(text="00 : " + str(ib2)+"\nLevel2")
    if ib2==0:
        txteror2()
        return True
    else:
        root.after(1000,timerfunc)
def Secondwindow():

    t=open('passage4.txt','r')
    t1=t.read()
    t3 = open('Temp.txt', 'w')
    t3.write(t1)
    theLable.config(text=t1)
    thelable2.config(text="01:00\nLevel2")
    text.delete('1.0',END)
    ans = messagebox.showwarning("Level 2", "do you want to start Level 2 click ok to start now")
    print(ans)
    if ans == 'ok':
        text.config(state=NORMAL)
        timerfunc()
def browseuserfile():
    open_return=filedialog.askopenfile(initialdir="/",title='select file to open',filetypes=(("text files","*.txt"),("all files","*.*")))
    for line in open_return:
        strr=line
    theLable.config(text=strr)
    f2 = open('Temp.txt', 'w')
    f2.write(strr)
    ans = messagebox.showwarning("warning", "do you want to start test now")
    print(ans)
    if ans == 'ok':
        text.config(state=NORMAL)
        timerloop()
def txteror2():
    print("start")
    str1 = open('Temp.txt', 'r').read()
    str2 = text.get("1.0", 'end-1c')
    list1 = list(str1.split(" "))
    list2 = list(str2.split(" "))
    print(list1)
    print(list2)

    i = 0
    j = 0
    m = 0
    s = 0
    c = 0
    c2 = 0
    try:
        while i in range(len(list1)):
            if list1[i] == list2[j]:
                c2=c2+1
                print(i, list1[i] + "=" + list2[j] + " correct1", j)
                i = i + 1
                j = j + 1

            elif list1[i] != list2[j]:
                m = m + 1
                print(i, list1[i] + "=" + list2[j] + " incorrect1", j)
                s = i
                i = i + 1
                while i in range(len(list1)):
                    if list2[j] == list1[i]:
                        c=c+1
                        print(i, list1[i]+"="+list2[j]+" correct2", j)
                        i = i + 1
                        j = j + 1
                        break
                    elif i + 1 >= len(list1):

                        i = s + 1
                        j = j + 1
                        break
                    else:
                        print(i, len(list1))
                        print(i, list1[i]+"="+list2[j]+" check incorrect2", j)
                        i = i + 1

            else:
                i = i + 1
                j = j + 1
    except Exception:
        print("ok")
    finally:
        missing = len(list1) - len(list2)
        correct = c +c2
        mistakes=len(list2)-correct
        speed=correct
        print("missing=", missing)
        print("mistake=", mistakes)
        print("correct=", correct)
        print("speed="+str(speed)+"wpm")

        top1=Toplevel()
        toplabel=Label(top1,text="missing words="+str(missing),font=('arial', 16),justify='right')
        toplabel2=Label(top1,text="mistakes="+str(m),font=('arial', 16))
        toplabel3=Label(top1,text="correct="+str(correct),font=('arial', 16))
        toplabel4=Label(top1,text="speed="+str(speed),font=('arial', 16))

        if speed>=25:
            resultf="pass"
        else:
            resultf="fail"
        # if resultf=="pass":
        #     btnr=Button(top1,width=20,text="Thank You",command=lambda:[top1.destroy(),homewindow()])
        #     btnr.pack()
        # else:
        #     btnexit = Button(top1, text="ok", command=lambda: [top1.destroy(), homewindow()])

        btnr=Button(top1,width=20,text="Thank You",command=lambda:[top1.destroy(),homewindow()])

        toplabel5=Label(top1,text="result="+resultf,font=('arial', 16))
        toplabel.pack()
        toplabel2.pack()
        toplabel3.pack()
        toplabel4.pack()
        toplabel5.pack()
        btnr.pack()
        top1.title("Final Result")
        top1.geometry("400x400+350+350")
    try:
        exceldatauser.myf(usernamefinal,correct, missing, mistakes, speed, resultf)
    except Exception:
        print("ok")


def txteror():
    print("start")
    str1 = open('Temp.txt', 'r').read()
    str2 = text.get("1.0", 'end-1c')
    list1 = list(str1.split(" "))
    list2 = list(str2.split(" "))
    print(list1)
    print(list2)

    i = 0
    j = 0
    m = 0
    c = 0
    c2 = 0
    try:
        while i in range(len(list1)):
            if list1[i] == list2[j]:
                c2=c2+1
                print(i, list1[i] + "=" + list2[j] + " correct1", j)
                i = i + 1
                j = j + 1

            elif list1[i] != list2[j]:
                m = m + 1
                print(i, list1[i] + "=" + list2[j] + " incorrect1", j)
                s = i
                i = i + 1
                while i in range(len(list1)):
                    if list2[j] == list1[i]:
                        c=c+1
                        print(i, list1[i]+"="+list2[j]+" correct2", j)
                        i = i + 1
                        j = j + 1
                        break
                    elif i + 1 >= len(list1):

                        i = s + 1
                        j = j + 1
                        break
                    else:
                        print(i, len(list1))
                        print(i, list1[i]+"="+list2[j]+" check incorrect2", j)
                        i = i + 1

            else:
                i = i + 1
                j = j + 1
    except Exception:
        print("ok")
    finally:
        missing = len(list1) - len(list2)
        correct = c +c2
        mistakes=len(list2)-correct
        #speed=len(list2)/cb
        speed=correct
        print("missing=", missing)
        print("mistake=", mistakes)
        print("correct=", correct)
        print("speed="+str(speed)+"wpm")

        top=Toplevel()
        toplabel=Label(top,text="missing words="+str(missing),font=('Times', 16),justify='right')
        toplabel2=Label(top,text="mistakes="+str(m),font=('Times', 16))
        toplabel3=Label(top,text="correct="+str(correct),font=('Times', 16))
        toplabel4=Label(top,text="speed="+str(speed),font=('Times', 16))
        toplabel5=Label(top,text="Do you want to go for Level 2",font=('arial', 16))



        if speed>=20:
            resultf="cleared"
        else:
            resultf="Not cleared"

        toplabel6=Label(top,text="result="+resultf,font=('Times', 16))
        toplabel.pack()
        toplabel2.pack()
        toplabel3.pack()
        toplabel4.pack()
        toplabel6.pack()
        toplabel5.pack()
        if resultf=="cleared":
            btnr=Button(top,width=20,text="Yes",command=lambda:[Secondwindow(),top.destroy()])
            btnr.pack()

            btnexit1 = Button(top, width=20, text="NO", command=lambda: [top.destroy(), homewindow()])
            btnexit1.pack()

        else:
            btnexit2 = Button(top, width=20, text='better luck next time', command=lambda: [top.destroy(), homewindow()])

            btnexit2.pack()

        top.title("Result Level 1")
        top.geometry("400x400+350+350")



ib=60
cb=ib
def timerloop():
    print("timer start")
    global ib
    ib = ib - 1
    thelable2.config(text="00 : " + str(ib)+"\nLevel1")
    if ib==0:
        txteror()
        return True
    else:
        root.after(1000,timerloop)

    # txt_eror = threading.Timer(20.0, txteror)
    # txt_eror.start()

def passage1():
    f1 = open('Passage1.txt', 'r')

    l1 = f1.read()
    theLable.config(text=l1)
    f2 = open('Temp.txt', 'w')
    f2.write(l1)
    ans = messagebox.showwarning("warning", "do you want to start test now")
    print(ans)
    if ans == 'ok':
        text.config(state=NORMAL)
        timerloop()

    return flag
def passage2():
    f1 = open('Passage2.txt', 'r')
    l1 = f1.read()
    theLable.config(text=l1)
    f2 = open('Temp.txt', 'w')
    f2.write(l1)
    ans=messagebox.showwarning("warning","do you want to start test now")
    print(ans)
    if ans=='ok':
        text.config(state=NORMAL)
        timerloop()
    return flag
def username():
    usernameis=simpledialog.askstring("input string",'please enter you name',parent=root)
    print(usernameis)
    return usernameis


def getmeexit():
    exitmeout=messagebox.askyesno("warning",'Do you really want to exit?')
    if exitmeout==True:
        root.destroy()

root=Tk()
root.focus_force()
main_menu = Menu()              #to create a top level menu
root.config(menu=main_menu)     #display the menu
passage = Menu(main_menu)
exitme = Menu(main_menu)
fileopen= Menu(main_menu)
main_menu.add_cascade(label="passsage", menu=passage)   #it is used to create hierarchical
                                                        #menu to the parent menu
main_menu.add_cascade(label="Browse file", menu=fileopen)
main_menu.add_cascade(label="Exit", menu=exitme)

passage.add_command(label="passage1",command=passage1)     #it is used to add the menu item
                                                        # into the menu
passage.add_command(label="passage2",command=passage2)
exitme.add_command(label="Exit",command=getmeexit)
fileopen.add_command(label="browse file",command=browseuserfile)

left = Frame(root, borderwidth=2, relief="solid")
right = Frame(root, borderwidth=2, relief="solid")

theLable = Label(left, text="Instruction:\n1)Select the passage from above menu named passage to take a test on\n"
                            "2)Otherwise choose a text file from your desktop from above add file menu\n"
                            "3)There will be two level of exam first level will be 30word per minutes and level 2 will be 40 word per minutes \n"
                            "4) You need to cleared both level to pass the exam.", justify=LEFT, padx=10, anchor=NW, wraplength=750, relief='groove',
                            font=('arial', 16))
theLable.pack(fill=BOTH, side=LEFT)
text = Text(right,font=('arial',16),state=DISABLED)
left.pack(side="left", expand=True, fill="both")
right.pack(side="right", expand=True, fill="both")
text.pack(fill=BOTH, side=RIGHT)
thelable2=Label(left,justify=RIGHT,text="01:00 \nLevel1",anchor=NW,relief='groove',font=('arial',14))


thelable2.pack(fill=BOTH,side=LEFT)
width_value=root.winfo_screenwidth()
height_value=root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (width_value,height_value))
usernamefinal=username()
print(usernamefinal)
root.mainloop()
