from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import matplotlib.pyplot as plt#matplotlib library used for plotting graphs
#import tkFont
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Notebook, Style

from tkinter.font import Font
 
window = Tk()
 
window.title("Welcome to GRAPH")
 
window.geometry('400x250')
 


def clicked():
 
    #messagebox.showinfo("GRAPHS ",selected.get())
    if selected.get()==1:
         messagebox.showinfo("GRAPHS ","You have selected linear equation")
         window = Tk()
         window.title("Linear equation")
 
         window.geometry('350x200')
 
         lbl11 = Label(window, text="Enter value of coefficient of x")
         lbl11.grid(column=0, row=0)

         
         atxt = Entry(window,width=10)
         atxt.grid(column=3, row=0)
        

         lbl12 = Label(window, text="Enter value of coefficient of y")
         lbl12.grid(column=0, row=2)

         
         btxt = Entry(window,width=10)
         btxt.grid(column=3, row=2)
         


         lbl13 = Label(window, text="Enter value of constant")
         lbl13.grid(column=0, row=4)

         
         ctxt = Entry(window,width=10)
         ctxt.grid(column=3, row=4)
         

         def clicked():
             a=int(atxt.get())
             b=int(btxt.get())
             c=int(ctxt.get())
              
             #messagebox.showinfo("xyz",type(a))
             x1=[]#list for storing x coordinates
             y1=[]#list for storing y coordinates
             if a==0:
                 for x in range(-10,10,5):
                     y=(a*x+c)/b
                     x1.append(x)
                     y1.append(y)
             elif b==0:
                for y in range(-10,10,5):
                    x=(b*y+c)/a
                    x1.append(x)
                    y1.append(y)
             else:
                 for y in range(-10,10,5):
                    x=(b*y+c)/a
                    x1.append(x)
                    y1.append(y)
             plt.plot(x1,y1,linewidth=4,marker="o",markerfacecolor="red",markersize=10,label="line")#statement for plotting graph linewidth is width of graph line marker denotes points
             plt.title("Linear Equation")#graph title
             plt.xlabel("x-axis")#x-axis label
             plt.ylabel("y-axis")#y-axis label
             plt.grid("True",color="green")
             plt.legend()
             plt.show()

         btn1 = Button(window, text="Show Graph", command=clicked)
 
         btn1.grid(column=1, row=5)
    elif selected.get()==2:
        
        messagebox.showinfo("GRAPHS ","You have selected parabola")
        window = Tk()
        window.title("Quadratic equation")
 
        window.geometry('350x200')
 
        lbl11 = Label(window, text="Enter value of coefficient of x square")
        lbl11.grid(column=0, row=0)

         
        atxt = Entry(window,width=10)
        atxt.grid(column=2, row=0)
        

        lbl12 = Label(window, text="Enter value of coefficient of x")
        lbl12.grid(column=0, row=1)

         
        btxt = Entry(window,width=10)
        btxt.grid(column=2, row=1)
         


        lbl13 = Label(window, text="Enter value of constant")
        lbl13.grid(column=0, row=2)

         
        ctxt = Entry(window,width=10)
        ctxt.grid(column=2, row=2)

        
        def clicked():
             a=int(atxt.get())
             b=int(btxt.get())
             c=int(ctxt.get())
             x1=[]#list for storing x coordinates

             y1=[]#list for storing y coordinates

             
             for x in range (-10,10):
                 x1.append(x)
                 y=(a*(x*x))+(b*x)+c
                 y1.append(y)
             plt.plot(x1,y1,linewidth=4,marker="o",markerfacecolor="red",markersize=10,label="line")

             plt.title("Quadratic equation")
             plt.xlabel("x-axis")
             plt.ylabel("y-axis")
             plt.grid("True",color="green")
             plt.legend()
             plt.show()
        btn1 = Button(window, text="show graph", command=clicked)
 
        btn1.grid(column=0, row=5)
            
                 















         
         
    elif selected.get()==3:
         messagebox.showinfo("GRAPHS ","You have selected line")
         
         window = Tk()
         window.title("Line Graph")
 
         window.geometry('350x200')
         lbl11 = Label(window, text="Enter first x coordinnate")
         lbl11.grid(column=0, row=0)

         
         atxt = Entry(window,width=10)
         atxt.grid(column=1, row=0)

         lbl12 = Label(window, text="Enter second x coordinate")
         lbl12.grid(column=0, row=1)

         
         btxt = Entry(window,width=10)
         btxt.grid(column=1, row=1)

         lbl13 = Label(window, text="Enter third x coordinate")
         lbl13.grid(column=0, row=2)

         
         ctxt = Entry(window,width=10)
         ctxt.grid(column=1, row=2)


         lbl14 = Label(window, text="Enter fourth x coordinate")
         lbl14.grid(column=0, row=3)

         
         dtxt = Entry(window,width=10)
         dtxt.grid(column=1, row=3)

         lbl15 = Label(window, text="Enter fifth x coordinate")
         lbl15.grid(column=0, row=4)

         
         etxt = Entry(window,width=10)
         etxt.grid(column=1, row=4)


         lbl16 = Label(window, text="Enter first y coordinate")
         lbl16.grid(column=0, row=5)

         
         ftxt = Entry(window,width=10)
         ftxt.grid(column=1, row=5)

         lbl17= Label(window, text="Enter second y coordinate")
         lbl17.grid(column=0, row=6)

         
         gtxt = Entry(window,width=10)
         gtxt.grid(column=1, row=6)


         lbl18 = Label(window, text="Enter third y coordinate")
         lbl18.grid(column=0, row=7)

         
         htxt = Entry(window,width=10)
         htxt.grid(column=1, row=7)


         lbl19 = Label(window, text="Enter fourth  y coordinate")
         lbl19.grid(column=0, row=8)

         
         itxt = Entry(window,width=10)
         itxt.grid(column=1, row=8)


         lbl110 = Label(window, text="Enter second x coordinate")
         lbl110.grid(column=0, row=9)

         
         jtxt = Entry(window,width=10)
         jtxt.grid(column=1, row=9)


         def clicked():
             a=int(atxt.get())
             b=int(btxt.get())
             c=int(ctxt.get())
             d=int(dtxt.get())
             e=int(etxt.get())
             f=int(ftxt.get())
             g=int(gtxt.get())
             h=int(htxt.get())
             i=int(itxt.get())
             j=int(jtxt.get())
             x1=[a,b,c,d,e]
             y1=[f,g,h,i,j]
             plt.plot(x1,y1,linewidth=4,marker="o",markerfacecolor="red",markersize=10,label="line")

             plt.title("Line graph")
             plt.xlabel("x-axis")
             plt.ylabel("y-axis")
             plt.grid("True",color="green")
             plt.legend()
             plt.show()
         btn1 = Button(window, text="show graph", command=clicked)
 
         btn1.grid(column=1, row=11)
            
    elif selected.get()==4:
        messagebox.showinfo("GRAPHS ","You have selected bar graph")
         
        window = Tk()
        window.title("Bar graph")
 
        window.geometry('350x200')


        lbl11 = Label(window, text="Enter first  label")

        lbl11.grid(column=0, row=0)

        atxt = Entry(window,width=10)
        atxt.grid(column=1, row=0)

        lbl12 = Label(window, text="Enter first height")
        lbl12.grid(column=0, row=1)

        btxt = Entry(window,width=10)
        btxt.grid(column=1, row=1)

        lbl13 = Label(window, text="Enter second label")
        lbl13.grid(column=0, row=2)

        ctxt = Entry(window,width=10)
        ctxt.grid(column=1, row=2)

        
        lbl14 = Label(window, text="Enter second height")
        lbl14.grid(column=0, row=3)

        dtxt = Entry(window,width=10)
        dtxt.grid(column=1, row=3)

        lbl15 = Label(window, text="Enter third label")
        lbl15.grid(column=0, row=4)

        etxt = Entry(window,width=10)
        etxt.grid(column=1, row=4)

        lbl16 = Label(window, text="Enter third  height")
        lbl16.grid(column=0, row=5)

        ftxt = Entry(window,width=10)
        ftxt.grid(column=1, row=5)

        lbl17= Label(window, text="Enter fourth  label")
        lbl17.grid(column=0, row=6)

        gtxt = Entry(window,width=10)
        gtxt.grid(column=1, row=6)
        
        lbl18 = Label(window, text="Enter fourth height")
        lbl18.grid(column=0, row=7)

        htxt = Entry(window,width=10)
        htxt.grid(column=1, row=7)

        lbl19 = Label(window, text="Enter fifth  label")
        lbl19.grid(column=0, row=8)

        itxt = Entry(window,width=10)
        itxt.grid(column=1, row=8)

        lbl10 = Label(window, text="Enter first  height")
        lbl10.grid(column=0, row=9)

        jtxt = Entry(window,width=10)
        jtxt.grid(column=1, row=9)

        def clicked():
            b=int(btxt.get())
            d=int(dtxt.get())
            f=int(ftxt.get())
            h=int(htxt.get())
            j=int(jtxt.get())
            a=(atxt.get())
            c=(ctxt.get())
            e=(etxt.get())
            g=(gtxt.get())
            i=(itxt.get())
            lbl=[a,c,e,g,i]
            height=[b,d,f,h,j]
            left = [10, 20, 30, 40, 50]
            plt.bar(left, height, tick_label = lbl , width = 1.0 , color = ['blue', 'red',"green"])
            plt.xlabel("x-axis")
            plt.ylabel("y-axis")
            plt.title("BarGraph")
            plt.show()

        btn1 = Button(window, text="show graph", command=clicked)
 
        btn1.grid(column=1, row=11)
            
            
    elif selected.get()==5:
        messagebox.showinfo("GRAPHS ","You have selected pie chart")
         
        window = Tk()
        window.title("Pie Chart")
 
        window.geometry('350x200')


        lbl11 = Label(window, text="Enter first  label")

        lbl11.grid(column=0, row=0)

        atxt = Entry(window,width=10)
        atxt.grid(column=1, row=0)

        lbl12 = Label(window, text="Enter first percentage")
        lbl12.grid(column=0, row=1)

        btxt = Entry(window,width=10)
        btxt.grid(column=1, row=1)

        lbl13 = Label(window, text="Enter second label")
        lbl13.grid(column=0, row=2)

        ctxt = Entry(window,width=10)
        ctxt.grid(column=1, row=2)

        
        lbl14 = Label(window, text="Enter second percentage")
        lbl14.grid(column=0, row=3)

        dtxt = Entry(window,width=10)
        dtxt.grid(column=1, row=3)

        lbl15 = Label(window, text="Enter third label")
        lbl15.grid(column=0, row=4)

        etxt = Entry(window,width=10)
        etxt.grid(column=1, row=4)

        lbl16 = Label(window, text="Enter third percentage")
        lbl16.grid(column=0, row=5)

        ftxt = Entry(window,width=10)
        ftxt.grid(column=1, row=5)

        lbl17= Label(window, text="Enter fourth  label")
        lbl17.grid(column=0, row=6)

        gtxt = Entry(window,width=10)
        gtxt.grid(column=1, row=6)
        
        lbl18 = Label(window, text="Enter fourth percentage")
        lbl18.grid(column=0, row=7)

        htxt = Entry(window,width=10)
        htxt.grid(column=1, row=7)

        lbl19 = Label(window, text="Enter fifth  label")
        lbl19.grid(column=0, row=8)

        itxt = Entry(window,width=10)
        itxt.grid(column=1, row=8)

        lbl10 = Label(window, text="Enter first  percentage")
        lbl10.grid(column=0, row=9)

        jtxt = Entry(window,width=10)
        jtxt.grid(column=1, row=9)

        def clicked():
            b=int(btxt.get())
            d=int(dtxt.get())
            f=int(ftxt.get())
            h=int(htxt.get())
            j=int(jtxt.get())
            a=(atxt.get())
            c=(ctxt.get())
            e=(etxt.get())
            g=(gtxt.get())
            i=(itxt.get())
            lbl=[a,c,e,g,i]
            sizes=[b,d,f,h,j]
            left = [10, 20, 30, 40, 50]
            fig1,ax1=plt.subplots()
            ax1.pie(sizes,labels=lbl,startangle=90,shadow="True")
            ax1.axis("equal")
            plt.title("Pie chart")
            plt.show()

            
        btn1 = Button(window, text="show graph", command=clicked)
 
        btn1.grid(column=1, row=11)
            

        

        
         
        
        
        
        
        
        
        
        
        
        
         

 
         
                      
        
    #lbl.configure(text= res)
#myfont= font(famly='Times',size=18)
 
btn = Button(window, text="Click Me",command=clicked)
#btn = tkFont.Font (family="Helvetica",size=10,weight="bold" )
 
btn.grid(column=2, row=5)
#print (txt.get())
#print("hello")
lbl = Label(window, text="Select graph type")
 
lbl.grid(column=2, row=0)
selected = IntVar()

rad1 = Radiobutton(window,text='Linear eqn', value=1,variable=selected)
 
rad2 = Radiobutton(window,text='Parabola', value=2,variable=selected)
 
rad3 = Radiobutton(window,text='Line Graph ', value=3,variable=selected)

rad4=Radiobutton(window,text="Bargraph",value=4,variable=selected)

rad5=Radiobutton(window,text="Pie chart",value=5,variable=selected)
 
rad1.grid(column=0, row=1)
 
rad2.grid(column=1, row=1)
 
rad3.grid(column=2, row=1)

rad4.grid(column=3,row=1)

rad5.grid(column=4,row=1)
 
 
window.mainloop()
