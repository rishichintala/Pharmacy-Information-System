from tkinter import*
import tkinter.messagebox
import backend


def main():
    root=Tk()
    app = Window1(root)

class Window1:
    def __init__(self,master):
        self.master = master
        self.master.title("LOGIN SYSTEM")
        self.master.geometry('1350x750+0+0')
        self.frame=Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()



        self.lblTitle=Label(self.frame,text='LOGIN SYSTEM',font=('arial',50,'bold'),bd=20)
        self.lblTitle.grid(row=0,column=0,columnspan=2,pady=20)

        self.LoginFrame1=Frame(self.frame,width=1010,height=300,relief='ridge',bd=20)
        self.LoginFrame1.grid(row=1,column=0)

        self.LoginFrame2=Frame(self.frame,width=1000,height=100,relief='ridge',bd=20)
        self.LoginFrame2.grid(row=2,column=0)

        self.LoginFrame3=Frame(self.frame,width=1000,height=200,relief='ridge',bd=20)
        self.LoginFrame3.grid(row=3,column=0,pady=2)
        #====================================================================================================================
        self.lblUsername=Label(self.LoginFrame1,text='Username',font=('arial',30,'bold'),bd=22)
        self.lblUsername.grid(row=0,column=0)
        self.txtUsername=Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,textvariable=self.Username)
        self.txtUsername.grid(row=0,column=1)

        self.lblPassword=Label(self.LoginFrame1,text='Password',font=('arial',30,'bold'),bd=22,)
        self.lblPassword.grid(row=1,column=0)
        self.txtPassword=Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=22,show='*',textvariable=self.Password)
        self.txtPassword.grid(row=1,column=1)   
        #====================================================================================================================

        self.btnLogin =Button(self.LoginFrame2, text='LOGIN', width=17,font=('arial',20,'bold'),command= self.Login_System)
        self.btnLogin.grid(row=0,column=0)
        
        self.btnReset =Button(self.LoginFrame2, text='RESET', width=17,font=('arial',20,'bold'),command=self.Reset)
        self.btnReset.grid(row=0,column=1)
        
        self.btnExit =Button(self.LoginFrame2, text='EXIT', width=17,font=('arial',20,'bold'),command=self.iExit)
        self.btnExit.grid(row=0,column=2)
        #====================================================================================================================
        self.btnPharmacy=Button(self.LoginFrame3,text="PHARMACY INFORMATION SYSTEM",state=DISABLED,command=self.pharmacy_window)
        self.btnPharmacy.grid(row=0,column=0,pady=8,padx=22)
        #====================================================================================================================
    def Login_System(self):
        u=(self.Username.get())
        p=(self.Password.get())
        if (u==str(12345) and p==str(12345)):
            self.btnPharmacy.config(state=NORMAL)
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()
            self.btnLogin.config(state=DISABLED)
        
        else:
            tkinter.messagebox.showerror("ERROR","Too Bad,Invalid Login Details")
            self.btnPharmacy.config(state=DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    def Reset(self):
        self.btnPharmacy.config(state=DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()
        self.btnLogin.config(state=NORMAL)
        tkinter.messagebox.showinfo("Info","The DATA HAS BEEN CLEARED")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Confirm","ARE YOU SURE?  YOU WANT TO EXIT")
        if self.iExit > 0:
            self.master.destroy()
            return
        #====================================================================================================================        

    def pharmacy_window(self): 
        self.newWindow=Toplevel(self.master)
        self.app=Window2(self.newWindow)

class Window2:
    def __init__(self,master):
        self.master =master
        self.master.title("PHARMACY INFORMATION SYSTEM")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg="cadet blue")
        self.frame=Frame(self.master)
        self.frame.pack()
        #======================================================================================================================
        MedId = StringVar()
        MedName= StringVar()
        DoM = StringVar()
        DoE = StringVar()
        Prices = StringVar()
        

        #=========================================function======================================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("Confirm","ARE YOU SURE? YOU WANT TO EXIT")
            if iExit > 0:
                master.destroy()
                return
     
        def clearData():
            self.txtMedId.delete(0,END)
            self.txtMedName.delete(0,END)
            self.txtDoM.delete(0,END)
            self.txtDoE.delete(0,END)
            self.txtPrices.delete(0,END)
            self.txtMedId.focus()
            
            
            
        
        def addData():
            if(len(MedId.get())!= 0 ):
                backend.addMedRec(MedId.get(),MedName.get(),DoM.get(),DoE.get(),Prices.get())
                medicinelist.delete(0,END)
                medicinelist.insert(END,(MedId.get(),MedName.get(),DoM.get(),DoE.get(),Prices.get()))
                self.txtMedId.focus()


        def DisplayData():
            medicinelist.delete(0,END)
            for row in backend.viewData():
                medicinelist.insert(END,row,str(""))
                self.txtMedId.focus()
        
            
        
        def MedicineRec(event):
            global md
            searchMed = medicinelist.curselection() [0]
            md=medicinelist.get(searchMed)


            self.txtMedId.delete(0,END)
            self.txtMedId.insert(END,md[1])
            self.txtMedName.delete(0,END)
            self.txtMedName.insert(END,md[2])
            self.txtDoM.delete(0,END)
            self.txtDoM.insert(END,md[3])
            self.txtDoE.delete(0,END)
            self.txtDoE.insert(END,md[4])
            self.txtPrices.delete(0,END)
            self.txtPrices.insert(END,md[5])
            

        def DeleteData():
            if(len(MedId.get())!=0 ):
                backend.deleteRec(md[0])
                clearData()
                DisplayData()
                


        def searchDataBase():
            medicinelist.delete(0,END)
            for row in backend.searchData(MedId.get(),MedName.get(),DoM.get(),DoE.get(),Prices.get()):
                medicinelist.insert(END,row,str(""))
               

        def update():
            if(len(MedId.get())!=0 ):
                backend.deleteRec(md[0])
            if(len(MedId.get())!=0 ):
                backend.addMedRec(MedId.get(),MedName.get(),DoM.get(),DoE.get(),Prices.get())
                medicinelist.delete(0,END)
                medicinelist.insert(END,(MedId.get(),MedName.get(),DoM.get(),DoE.get(),Prices.get()))
            

               

        #=====================================================FRAMES========================================================================
        MainFrame = Frame(self.frame, bg="cadet blue")
        MainFrame.grid()

        TitFrame =Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame,font=('arial',47,'bold'),text="Pharmacy Information System",bg="Ghost White")
        self.lblTit.grid(sticky=W)

        ButtonFrame =Frame(MainFrame,bd=2,width=1350,height=70,padx=18,pady=10,bg="Ghost White",relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame,bd=1,width=1300,height=400,padx=20,pady=20,relief=RIDGE,bg="cadet blue")
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT =LabelFrame(DataFrame,bd=1,width=1000,height=600,padx=20,relief=RIDGE,bg="Ghost White",
                                  font=('arial',20,'bold'),text="Medicine Information\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT=LabelFrame(DataFrame,bd=1,width=400,height=300,padx=31,pady=3,relief=RIDGE,bg="Ghost White",
                                  font=('arial',20,'bold'),text="Medicine Details\n")
        DataFrameRIGHT.pack(side=RIGHT)
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Labels and entry widget ###########################################################

        self.lblMedId = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Medicine Id",padx=2,pady=2,bg="Ghost White")
        self.lblMedId .grid(row=0, column=0, sticky=W)
        self.txtMedId = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=MedId,width=30)
        self.txtMedId .grid(row=0, column=1)

        self.lblMedName = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Medicine Name",padx=2,pady=2,bg="Ghost White")
        self.lblMedName .grid(row=1, column=0, sticky=W)
        self.txtMedName = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=MedName,width=30)
        self.txtMedName .grid(row=1, column=1)

        self.lblDoM = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Date Of Manufacture",padx=2,pady=2,bg="Ghost White")
        self.lblDoM .grid(row=2, column=0, sticky=W)
        self.txtDoM = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=DoM,width=30)
        self.txtDoM .grid(row=2, column=1)

        self.lblDoE = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Date Of Expiry",padx=2,pady=2,bg="Ghost White")
        self.lblDoE .grid(row=3, column=0, sticky=W)
        self.txtDoE = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=DoE,width=30)
        self.txtDoE .grid(row=3, column=1)

        self.lblPrices = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Price per sheet(10 units)",padx=2,pady=2,bg="Ghost White")
        self.lblPrices .grid(row=4, column=0, sticky=W)
        self.txtPrices = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=Prices,width=30)
        self.txtPrices .grid(row=4, column=1)

       
        #=========================LISTBOX AND SCROLLBAR Widget ===============================================================

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        medicinelist=Listbox(DataFrameRIGHT,width=41,height=16,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
        medicinelist.bind('<<ListboxSelect>>',MedicineRec)
        medicinelist.grid(row=0,column=0,padx=8)
        scrollbar.config(command = medicinelist.yview)
        #=============================================Button Widget===========================================================

        self.btnAddData =Button(ButtonFrame,text="Add New",font=('arial',20,'bold'),height=1,width=10,bd=4,command=addData)
        self.btnAddData.grid(row=0,column=0)

        self.btnDisplayData =Button(ButtonFrame,text="Display",font=('arial',20,'bold'),height=1,width=10,bd=4,command=DisplayData)
        self.btnDisplayData.grid(row=0,column=1)

        self.btnClearData =Button(ButtonFrame,text="Clear",font=('arial',20,'bold'),height=1,width=10,bd=4,command=clearData)
        self.btnClearData.grid(row=0,column=2)

        self.btnDeleteData =Button(ButtonFrame,text="Delete",font=('arial',20,'bold'),height=1,width=10,bd=4,command=DeleteData)
        self.btnDeleteData.grid(row=0,column=3)

        self.btnSearchData =Button(ButtonFrame,text="Search",font=('arial',20,'bold'),height=1,width=10,bd=4,command=searchDataBase)
        self.btnSearchData.grid(row=0,column=4)

        self.btnUpdateData =Button(ButtonFrame,text="Update",font=('arial',20,'bold'),height=1,width=10,bd=4,command=update)
        self.btnUpdateData.grid(row=0,column=5)

        self.btnExitData =Button(ButtonFrame,text="Exit",font=('arial',20,'bold'),height=1,width=10,bd=4,command=iExit)
        self.btnExitData.grid(row=0,column=6)

        

       

if __name__ == '__main__':
    main()

