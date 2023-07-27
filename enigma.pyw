import PIL.ImageTk
from tkinter import *
import tkinter.messagebox

def enigma(r1=0,r2=0,r3=0):
    turns = []
    file3 = open('encryption.txt','r')
    turns.append(r1)
    turns.append(r2)
    turns.append(r3)


    number  = [x for x in range(26)]
    alpabet = [chr(65+x) for x in range(26)]
    # list of no. and alpabet in order
    def rotator(n,lst):
        newlist = []
        for x in range(26):
            newlist.append(lst[(x+n)%26])
        return newlist

    rotor1=['J', 'H', 'G', 'E', 'F', 'M', 'O', 'S', 'C', 'W', 'R', 'Y', 'Q', 'I',
     'T', 'K', 'D', 'Z', 'N', 'P', 'X', 'U', 'B', 'V', 'A', 'L']
    rotor2=['C', 'Z', 'B', 'O', 'G', 'V', 'W', 'X', 'P', 'S', 'H', 'A', 'F', 'K',
    'U', 'T', 'J', 'N', 'Y', 'L', 'E', 'R', 'M', 'Q', 'I', 'D']
    rotor3=['P', 'K', 'S', 'G', 'J', 'H', 'C', 'I', 'X', 'D', 'M', 'V', 'A', 'L',
    'F', 'N', 'B', 'T', 'R', 'Y', 'E', 'Q', 'O', 'U', 'Z', 'W']
    rotor4=['C', 'X', 'S', 'Y', 'L', 'M', 'U', 'R', 'B', 'V', 'G', 'A', 'F', 'E',
    'W', 'I', 'Z', 'K', 'O', 'Q', 'T', 'D', 'N', 'H', 'P', 'J']
    rotor5=['V', 'J', 'U', 'A', 'C', 'P', 'Z', 'I', 'D', 'M', 'W', 'E', 'F', 'S',
    'K', 'T', 'O', 'Y', 'L', 'R', 'H', 'G', 'Q', 'N', 'B', 'X']
    rotors = [rotor1,rotor2,rotor3,rotor4,rotor5]


    for x in rotors:
        for y in range(len(x)):
            x[y] = alpabet.index(x[y])
    reflector = {0: 3, 3: 0, 1: 10, 10: 1, 2: 21, 21: 2, 4: 19, 19: 4, 5: 16,
     16: 5, 6: 13, 13: 6, 7: 9, 9: 7, 8: 11, 11: 8, 12: 15, 15: 12,
     14: 25, 25: 14, 17: 24, 24: 17, 18: 23, 23: 18, 20: 22, 22: 20}
    reflector2 = {0: 3, 3: 0, 1: 21, 21: 1, 2: 17, 17: 2, 4: 9, 9: 4, 5: 18, 18: 5}

    #selected rotors can be taken as select1,select2,selct3
    global result
    file2 = open('encrypted.txt','w')
    result = '                            Rotor setting '+str(r1)+'.'+str(r2)+'.'+str(r3)+'\n'+'\n'
    file2.write(result)
    for a in file3.readlines():
        result=''
        for x in a:
            if x.isalpha()==False:
                result+=x
                continue

            
            rotors[0] = rotator(turns[0],rotors[0])
            rotors[1] = rotator(turns[1],rotors[1])
            rotors[2] = rotator(turns[2],rotors[2])
            if x.islower():
                u=reflector[rotors[2][rotors[1][rotors[0][alpabet.index(x.upper())]]]]
                text = alpabet[rotors[0].index(rotors[1].index(rotors[2].index(u)))].lower()
                result+=text
                turns[0]=(turns[0]+1)%26
                if turns[0]%26==0:
                    turns[1] = (turns[1]+1)%26
                    if turns[1]%26==0:
                        turns[2]=(turns[2]+1)%26
            elif x.isupper():
                u=reflector[rotors[2][rotors[1][rotors[0][alpabet.index(x)]]]]
                text = alpabet[rotors[0].index(rotors[1].index(rotors[2].index(u)))]
                result+=text
                turns[0]=(turns[0]+1)%26
                if turns[0]%26==0:
                    turns[1] = (turns[1]+1)%26
                    if turns[1]%26==0:
                        turns[2]=(turns[2]+1)%26
        file2.write(result)
    file2.close()
    file3.close()
#main_____________________
if __name__ =='__main__':
    enig = Tk()
    enig.geometry('950x440')
    enig.resizable(False,False)
    enig.title('Enigma Machine')
    enig.config(background='whitesmoke')
    machine=Frame(enig)
    machine.config(background='whitesmoke')
    machine.grid()
    im1 = PIL.Image.open('enigma-box-left2.png')
    im2 = im1.resize((100,100))
    photo = PIL.ImageTk.PhotoImage(im2)
    imgsrc = Label(machine,image=photo)
    Title = Label(machine,text='Enigma Machine',font=('Times', 30, 'bold'),justify=CENTER,
    border=2,background='whitesmoke')
    Title.place(x =300 ,y =10)
    dummmy1 = Label(machine,text='',font=('Helvetica', 30, 'bold'),justify=LEFT,border=2,
    background='whitesmoke')
    dummmy1.grid(row = 0,column =0)
    imgsrc.place(x=600,y=3)

    #Rotors ___________________
    rotorsetting1=StringVar()
    rotorsetting2=StringVar()
    rotorsetting3=StringVar()

    sidetext = Label(machine,text='Rotors Number:',font=('Helvetica', 16, 'italic'),border=2,
    justify =LEFT,height=1,background='whitesmoke')
    sidetext.place(x = 70,y=70)
    rotor1 = Listbox(machine,width=2,font=('Helvetica', 16, 'bold'),justify='center',height=1,
    listvariable=rotorsetting1)
    rotor1.place(x =239,y=70)
    scrollbar = Scrollbar(machine,orient='vertical',command=rotor1.yview)
    scrollbar.place(x=265,y=66)
    rotor1['yscrollcommand'] = scrollbar.set
    for i in range(0,26):
        rotor1.insert(END,str(i))
    rotor1.config(background='black',fg = 'white')
    scrollbar.config()

    rotor2 = Listbox(machine,width=2,font=('Helvetica', 16, 'bold'),justify='center',height=1,
    listvariable=rotorsetting1 )
    rotor2.place(x =281,y=70 )
    scrollbar2 = Scrollbar(machine,orient='vertical',command=rotor2.yview)
    scrollbar2.place(x=307,y=66)
    rotor2['yscrollcommand'] = scrollbar2.set
    for i in range(26):
        rotor2.insert(END,str(i))
    rotor2.config(background='black',fg = 'white')
    scrollbar2.config()

    rotor3 = Listbox(machine,width=2,font=('Helvetica', 16, 'bold'),justify='center',height=1,
    listvariable=rotorsetting1 )
    rotor3.place(x=325,y=70)
    scrollbar3 = Scrollbar(machine,orient='vertical',command=rotor3.yview)
    scrollbar3.place(x=351,y=66)
    rotor3['yscrollcommand'] = scrollbar3.set
    for i in range(26):
        rotor3.insert(END,str(i))
    rotor3.config(background='black',fg = 'white')
    scrollbar3.config()
    dummmy3= Label(machine,text='     ',font=('Helvetica', 16, 'bold'),border=2,justify =LEFT,
    height=1,background='whitesmoke').grid(row=1,column=400)
    #internal functioning of rotors____
    def selction_of_setting(event):
        global rotorno1
        rotorno1=0
        value = rotor1.curselection()
        if len(value)!=0:
            rotorno1 = value[0]%26
        rotoring1 = Button(text =str(rotorno1),relief='sunken',width = 3,
        borderwidth=1).place(x=459,y=90)
    def selction_of_setting2(event):
        global rotorno2
        rotorno2=0
        value = rotor2.curselection()
        if len(value)!=0:
            rotorno2 = value[0]%26
        rotoring2 = Button(text =str(rotorno2),relief='sunken',width = 3,
        borderwidth=1).place(x=485,y=90)
    def selction_of_setting3(event):
        global rotorno3
        rotorno3 = 0
        value = rotor3.curselection()
        if len(value)!=0:
            rotorno3 = value[0]%26
        rotoring3 = Button(text =str(rotorno3),relief='sunken',width = 3,
        borderwidth=1).place(x=510,y=90)
    def get_input():
        global encryption
        global encrypted_text
        encrypted_text = orignal.get('1.0','end-1c')
        print(encrypted_text)
        file = open('encryption.txt','w')
        file.write(encrypted_text)
        file.close()
        try:
            enigma(rotorno1,rotorno2,rotorno3)
        except:
            enigma()
        file4 = open('encrypted.txt','r')
        encoding =file4.read()
        encryption.destroy()
        encryption=Text(machine,borderwidth=2,wrap= 'char',relief='groove',
        font =('Helvetica', 13, 'italic'),width = 50,height= 12,background='whitesmoke' )
        encryption.insert(END,encoding)
        encryption.configure(state='disabled')
        encryption.grid(row = 2 ,column = 1,padx = (33,0),sticky=S)
        scrolllabel = Scrollbar(machine,orient='vertical',command=encryption.yview)
        xscrolllabel = Scrollbar(machine,orient='horizontal',command=encryption.xview)
        scrolllabel.grid(row=2,column=2,sticky=N+S+W,pady=(30,0))
        encryption['yscrollcommand']=scrolllabel.set
        encryption['xscrollcommand']=xscrolllabel.set

        file4.close()
    rotor1.bind('<Button-1>',  selction_of_setting)
    rotor2.bind('<Button-1>',  selction_of_setting2)
    rotor3.bind('<Button-1>',  selction_of_setting3)
    rotor1.bind('<Button-2>',  selction_of_setting)
    rotor2.bind('<Button-2>',  selction_of_setting2)
    rotor3.bind('<Button-2>',  selction_of_setting3)
    textvar= StringVar()

    orignal=Text(machine,width = 50,height= 15,borderwidth=2,wrap ='char',relief='groove',
    background='whitesmoke')
    ScrollText = Scrollbar(machine,orient='vertical',command=orignal.yview)
    ScrollText.grid(row =2,column = 1,sticky=N+S+W,pady=(29,0))

    orignal['yscrollcommand']=ScrollText.set

    orignal.grid(row = 2 ,column = 0,pady = (30,3),padx = (20,0),sticky=E)
    processs = Button(machine,text = 'Procced',command = lambda :get_input())
    processs.grid(row =3,column = 0)
    encryption=Label(machine,text='Encryption',borderwidth=2,relief='groove',
    background='whitesmoke',font =('Helvetica', 13, 'italic'),justify=LEFT,width = 45,height= 12 )
    encryption.grid(row = 2 ,column = 2,padx=16,sticky=S)
    border1 = Frame(machine,background='black',highlightthickness=2,bd =0
    ,highlightbackground='black').place(x=507,y=97)
    border2 = Frame(machine,background='black',highlightthickness=2,bd =0,
    highlightbackground='black').place(x=483,y=97)
    border3 = Frame(machine,background='black',highlightthickness=2,bd =0,
    highlightbackground='black').place(x=459,y=97)
    rotoring1 = Button(machine,bd=0,text =str(0),relief='sunken',width = 3,
    borderwidth=1).place(x=510,y=90)
    rotoring2 = Button(machine,bd=0,text =str(0),relief='sunken',width = 3,
    borderwidth=1).place(x=485,y=90)
    rotoring3 = Button(machine,bd=0,text =str(0),relief='sunken',width = 3,
    borderwidth=1).place(x=459,y=90)
    #rotor no (mButtony not)___________
    #useless menubar
    def iExit():
        iExit = tkinter.messagebox.askyesno("Live Long Hitler",
                                            " HE IS ALREADY DEAD FOR GOOD")
        if iExit>0:
            enig.destroy()
            return
    def cut():
        orignal.event_generate(('<<Cut>>'))
    def copy():
        orignal.event_generate(('<<Copy>>'))
    def paste():
        orignal.event_generate(('<<Paste>>'))
    def about():
        t = Tk()
        t.geometry('850x280')
        t.title('ABOUT')
        f = Frame(t)
        f.grid()
        text = '''                                Virtual Enigma Machine\n
        The Enigma machine is a cipher device developed and used in the early to \n 
        mid- 20th century to protect commercial, diplomatic and military communication. It \n
        was employed extensively by Nazi Germany during World War II, in all \n
        branches of the German military. The Enigma machine was considered so\n
         secure that it was used to encipher the most top-secret messages.'''
        maintxt = Label(f,text=text,background='whitesmoke',font=('Times',15,'bold'),
        justify=LEFT,width = 70,height= 12)

        maintxt.grid(row=0,column=0)
        t.mainloop()
    menubar = Menu(machine)
    filemenu = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = 'File', menu = filemenu)
    filemenu.add_command(label = "Exit", command = iExit)

    editmenu = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label = 'Edit', menu = editmenu)
    editmenu.add_command(label = "Cut",command=cut)
    editmenu.add_command(label = "Copy",command=copy)
    editmenu.add_separator()
    editmenu.add_command(label = "Paste",command=paste)

    editmenu.add_command(label = "About",command=about)

    enig.configure(menu =menubar)






    enig.mainloop()
    
    '''k = alpabet
    rotor1 = list()
    a=0
    while(True):
        t = random.choice(k)
        if k.index(t) != a:
            print(t,a)
            if t not in rotor1:
                rotor1.append(t)
                a+=1
        if len(rotor1)==26:
            break
    print(rotor1)'''
    #program of reflector

    '''reflector = dict()
    for c in range(13):
        s = number.pop(0)
        a = random.choice(number)
        number.pop(number.index(a))
        reflector[s] = a
        reflector[a] = s
    print(reflector)'''
