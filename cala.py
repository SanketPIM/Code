from tkinter import *
class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.wm_geometry('550x300+100+100')
       
        self.window.configure(bg ="light blue")
        self.text1 = Entry(master=self.window, text="")
        self.text1.place(x = 50,y=50,width = 100,height = 30)
        self.text2 = Entry(master=self.window, text="")
        self.text2.place(x = 200,y=50,width = 100,height = 30)
        self.output = Entry(master=self.window, )
        self.output.place(x=350, y=50, width=100, height=30)
        self.addButton = Button(master=self.window, text="add",command=self.add)
        self.addButton.place(x = 50,y=100,width = 100,height = 30)
        self.subButton = Button(master=self.window, text="sub",command=self.sub)
        self.subButton.place(x = 170,y=100,width = 100,height = 30)
        self.mulButton = Button(master=self.window, text="mul",command=self.mul)
        self.mulButton.place(x = 290,y=100,width = 100,height = 30)
        self.divButton = Button(master=self.window, text="div",command=self.div)
        self.divButton.place(x = 410,y=100,width = 100,height = 30)
        self.btnclr = Button(master=self.window,text = "CLEAR",
                        font = ('consolas',15,'bold'),command=self.clear)
        self.btnclr.place(x = 240,y = 170,width=150,height=30)
        self.window.mainloop()
    def add(self):
        n1 = int(self.text1.get())
        n2 = int(self.text2.get())
        n3 = n1 + n2 
        self.output.insert(0,n3)
    
    def sub(self):
        n1=int(self.text1.get())
        n2=int(self.text2.get())
        n3=n1-n2
        self.output.insert(0,n3)
        
    def mul(self):
        n1=int(self.text1.get())
        n2=int(self.text2.get())
        n3=n1*n2
        self.output.insert(0,n3)
        
    def div(self):
        n1=int(self.text1.get())
        n2=int(self.text2.get())
        n3=n1/n2
        self.output.insert(0,n3)
    def clear(self):
        self.output.configure(state='normal')
        self.output.delete(0,END)
        self.output.delete(0,END)
        self.output.config(state="readonly")
        
        
if __name__ == '__main__':
    g = GUI()
