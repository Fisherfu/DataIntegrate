'''
word_dic_DEV
'''


import tkinter as tk
import csv,os

def _hit1():
    myDict[entrY1.get()]=entrY2.get()
    entrY1.delete(0,tk.END)
    entrY2.delete(0,tk.END)

def _hit2():
    wiN1=tk.Toplevel(wiN)
    wiN1.title("Hello!!!")
    wiN1.geometry("400x600")
    btN1 = tk.Button(wiN1, text="回主選單", font=("Arial", 12), width=10, height=2, command=wiN1.destroy)
    btN1.pack() 
    sBar=tk.Scrollbar(wiN1)
    sBar.pack(side=tk.RIGHT,fill=tk.Y)
    
    listBox=tk.Listbox(wiN1, font=("Arial", 20),yscrollcommand=sBar.set,height=50,bg="lime")
    listBox.pack(side=tk.BOTTOM, fill=tk.BOTH)
    sBar.config(command=listBox.yview)
    
    for ii in myDict.items():
        listBox.insert(tk.END, str(ii))

def _hit3():
    if myDict.get(entrY1.get())==None:
        tk.messagebox.showerror("錯誤","找不到單字")
        entrY1.delete(0,tk.END)
    else:
        del myDict[entrY1.get()]
        entrY1.delete(0,tk.END)
        tk.messagebox.showeinfo("成功","刪除完成!!")
        


def _hit4():
    if myDict.get(entrY1.get())==None:
        tk.messagebox.showerror("錯誤","找不到單字")
        entrY1.delete(0,tk.END)
        
    else:   
        tk.messagebox.showinfo("中文是",myDict[entrY1.get()])
      #  entrY2.insert(tk.END,myDict[entrY1.get()])
      #  time.sleep(2)   
        entrY1.delete(0,tk.END)
      #  entrY2.delete(0,tk.END)

def _hit5():

    wiN1=tk.Toplevel(wiN)
    wiN1.title("Hello!!!")
    wiN1.geometry("400X300+100+100")
    lbL1 = tk.Label(wiN,text="中文",fg="white",bg="green", font=("Arial", 16), width=15, height=2)
    lbL1.pack()
    btN1 = tk.Button(wiN1, text="say 88", font=("Arial", 12), width=10, height=2, command=wiN1.destroy)
    btN1.pack()

def _hit6():
    qQ=tk.messagebox.askokcancel("提示","確定要結束程式嗎???")
    if qQ:
        csvFile=open("abc.csv","w",newline="",encoding="utf-8-sig")
        writeR=csv.writer(csvFile)
        for rowK,rowV in myDict.items():
            writeR.writerow([rowK,rowV])
        csvFile.close()    
        wiN.destroy()

if os.path.isfile("abc.csv"):
    csvFile=open("abc.csv","r",encoding="utf-8-sig")
    myDict=dict(csv.reader(csvFile))
else:    
    myDict=dict()

wiN = tk.Tk()

wiN.title("Welcome!!!")

wiN.geometry("600x600+600+200")

lbL1 = tk.Label(wiN,text="請輸入英文",fg="white",bg="green", font=("Arial", 16), width=15, height=2)
lbL1.pack()

entrY1=tk.Entry(wiN,font=("Arial",16),bd=5)
entrY1.pack()
lbL2 = tk.Label(wiN,text="請輸入中文",fg="white",bg="green", font=("Arial", 16), width=15, height=2)
lbL2.pack()
entrY2=tk.Entry(wiN,font=("Arial",16),bd=5)
entrY2.pack()

btN1 = tk.Button(wiN,bg="blue",fg="white", text="新增單字!!", font=("Arial", 16), width=10, height=2, command=_hit1)
btN1.pack() 
btN2 = tk.Button(wiN,bg="blue",fg="white", text="顯示單字!!", font=("Arial", 16), width=10, height=2, command=_hit2)
btN2.pack() 
btN3 = tk.Button(wiN,bg="blue",fg="white", text="刪除單字!!", font=("Arial", 16), width=10, height=2, command=_hit3)
btN3.pack() 
btN4 = tk.Button(wiN,bg="blue",fg="white", text="查詢單字!!", font=("Arial", 16), width=10, height=2, command=_hit4)
btN4.pack() 
btN5 = tk.Button(wiN,bg="blue",fg="white", text="英文測驗!!", font=("Arial", 16), width=10, height=2, command=_hit5)
btN5.pack() 
btN6 = tk.Button(wiN,bg="blue",fg="white", text="離開!!", font=("Arial", 16), width=10, height=2, command=_hit6)
btN6.pack() 


wiN.mainloop()

