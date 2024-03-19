from tkinter import *
from functools import partial
def hello():

    def bonil():

        f=open("C:/Users/bonil/Desktop/record.txt","r")
        f.read()


       # C = Tk()
       # C.geometry("2000x820")
       # C.title("STOCK")
        #frame3=Frame(C, borderwidth=6, bg="yellow", relief=SUNKEN)
        #frame3.pack()

        #b6= Button(frame3, fg="red", text="MY STOCKS",font="comicsansms 25 bold", relief=SUNKEN)
        #b6.pack(pady=10)


        #C.mainloop()
    
    def tapan():
        
        def buy(stock_name, quantity):
            stock_name = stock_name.get()
            quantity = quantity.get()
            with open("C:/Users/bonil/Desktop/record.txt","a+") as f:
                f.write('\n')
                f.write(f"{stock_name,quantity}")

        D = Tk()
        D.geometry("600x600")
        D.title("BUYING STOCK")
        #frame5=Frame(D, borderwidth=6, bg="grey", relief=SUNKEN)
        #frame5.pack(fill=X, pady=20)
    
        #label5=Label(frame5, text="BUY STOCK", bg="black" , fg="white" , font="comicsansms 50 bold", borderwidth=5, relief=SUNKEN )
        #label5.pack(fill=X)
        #frame6=Frame(D, borderwidth=6, bg="grey", relief=SUNKEN)
        #frame6.pack(fill=X, pady=20)
        user= Label(D, text="Stock Name: ", font="comicsansms 15 bold")
        value=Label(D, text="Quantity: ", font="comicsansms 15 bold")
        user.grid(row=1, column=2)
        value.grid(row=2, column=2)

        uservalue = StringVar()
        passvalue = StringVar()


        userentry = Entry(D, textvariable = uservalue)
        passentry = Entry(D, textvariable = passvalue)
        userentry.grid(row=1,column=3)
        passentry.grid(row=2,column=3)
        b7= Button(D, fg="red", text="BUY", font="comicsansms 10 bold", relief=SUNKEN, command=partial(buy,stock_name=userentry, quantity=passentry)) 
        b7.grid(row=3,column=2)


        D.mainloop()
    
    
        
    
    def utsav():
        def smit():
            def graph(stock_name):
                import threading
                import matplotlib.pyplot as plt
                from datetime import datetime
                import time as t

                try:
                    from urllib.request import urlopen
                except ImportError:
                    from urllib2 import urlopen

                import json 


                time = []
                price = []

                def datastream(url, stock_name):
    
                    response = urlopen(url)
                    data = response.read().decode("utf-8")
                    data = json.loads(data)
    
                    price.append(data['price'])
    
                    print(time, price)
                    d = datetime.strptime(data['updated_at'], '%Y-%m-%d %H:%M:%S')    
    
                    time.append(d.hour * 3600 + d.minute * 60 + d.second)
    
                    plt.figure(figsize=(20, 10))
                    plt.plot(time, price)
                    plt.gca().legend((stock_name),prop={'size': 20})
                    #plt.xticks(dates, dates, rotation=60)
                    plt.grid(True)
                    mng = plt.get_current_fig_manager()
                    mng.full_screen_toggle()
                    plt.show(block=False)
                    plt.pause(1)
                    plt.close()
    
                    return data

                if __name__ == '__main__':
                    x = str(stock_name.get())
                    url = ("https://financialmodelingprep.com/api/company/real-time-price/" + x.strip()+"?datatype=json")

                    while(True):
                        datastream(url, x)
                        #t.sleep(2)
                        #plt.close('all')
                  
            E = Tk()
            E.geometry("600x600")

            E.title("GRAPH")
            user1= Label(E, text="Stock Name: ", font="comicsansms 15 bold")
            user1.grid(row=1, column=2)
            user1value = StringVar()
            user1entry = Entry(E, textvariable = user1value)
            user1entry.grid(row=1,column=3)
            b8= Button(E, fg="red", text="GRAPH", font="comicsansms 10 bold", relief=SUNKEN, command=partial(graph,stock_name=user1entry))
            b8.grid(row=3,column=2)
            E.mainloop()

        def adit():
            def fenil( stock_name, date1, date2):
                from yahoofinancials import YahooFinancials
                import matplotlib.pyplot as plt

                stock_name = stock_name.get()
                date1 = date1.get()
                date2 = date2.get()
                yahoo_financials = YahooFinancials(stock_name)
                data = yahoo_financials.get_historical_price_data(date1, date2, "daily")

                prices = [price_dict['close'] for price_dict in data[stock_name]['prices']]
                dates = [data_dict['formatted_date'] for data_dict in data[stock_name]['prices']]

                list(zip(dates, prices))

                plt.figure(figsize=(20, 10))
                plt.plot(dates, prices)
                plt.gca().legend(stock_name, prop={'size': 20}, loc=1)
                plt.xticks(dates, dates, rotation=60)
                plt.grid(True)
                plt.show()

                
            D = Tk()
            D.geometry("600x600")
            D.title("BUYING STOCK")
            stock=Label(D, text="STOCK NAME: ", font="comicsansms 15 bold")
            user= Label(D, text="Start DATE: ", font="comicsansms 15 bold")
            value=Label(D, text="End DATE: ", font="comicsansms 15 bold")
            stock.grid(row=1, column=2)
            user.grid(row=2, column=2)
            value.grid(row=3, column=2)
            
            stockvalue = StringVar()
            uservalue = StringVar()
            passvalue = StringVar()

            stockentry = Entry(D, textvariable = stockvalue)
            userentry = Entry(D, textvariable = uservalue)
            passentry = Entry(D, textvariable = passvalue)
            
            stockentry.grid(row=1,column=3)
            userentry.grid(row=2,column=3)
            passentry.grid(row=3,column=3)
            
            b7= Button(D, fg="red", text="GRAPH", font="comicsansms 10 bold", relief=SUNKEN, command=partial(fenil, stock_name=stockentry, date1=userentry, date2=passentry)) 
            b7.grid(row=4,column=2)

            D.mainloop()

        def karan():
            def graph1(stock_name1, stock_name2):
                import threading
                import matplotlib.pyplot as plt
                from datetime import datetime
                import time as t

                try:
                    from urllib.request import urlopen
                except ImportError:
                    from urllib2 import urlopen

                import json 


                time = []
                price = []
                price1=[]

                def datastream(url, url1,  stock_name1,stock_name2):
    
                    response = urlopen(url)
                    data = response.read().decode("utf-8")
                    data = json.loads(data)
                
                    response = urlopen(url1)
                    data1 = response.read().decode("utf-8")
                    data1 = json.loads(data1)

                    price.append(data['price'])
                    price1.append(data1['price'])
    
                    print(time, price, price1)
                    d = datetime.strptime(data['updated_at'], '%Y-%m-%d %H:%M:%S')    
    
                    time.append(d.hour * 3600 + d.minute * 60 + d.second)
    
                    plt.figure(figsize=(20, 10))
                    plt.plot(time, price)
                    plt.plot(time, price1)
                    plt.gca().legend((stock_name1,stock_name2),prop={'size': 20})
                    #plt.xticks(dates, dates, rotation=60)
                    plt.grid(True)
                    mng = plt.get_current_fig_manager()
                    mng.full_screen_toggle()
                    plt.show(block=False)
                    plt.pause(1)
                    plt.close()

    
                    return data

                if __name__ == '__main__':
                    x = str(stock_name1.get())
                    y = str(stock_name2.get())
                    url = ("https://financialmodelingprep.com/api/company/real-time-price/" + x.strip()+"?datatype=json")
                    url1 = ("https://financialmodelingprep.com/api/company/real-time-price/" + y.strip()+"?datatype=json")

                    while(True):
                        datastream(url, url1, x, y)
                        #t.sleep(2)
                        #plt.close('all')
            G = Tk()
            G.geometry("600x600")

            G.title("GRAPH")
            user= Label(G, text="Stock Name 1: ", font="comicsansms 15 bold")
            value=Label(G, text="Stock name 2: ", font="comicsansms 15 bold")
            user.grid(row=1, column=2)
            value.grid(row=2, column=2)

            uservalue = StringVar()
            passvalue = StringVar()


            userentry = Entry(G, textvariable = uservalue)
            passentry = Entry(G, textvariable = passvalue)
            userentry.grid(row=1,column=3)
            passentry.grid(row=2,column=3)
            b7= Button(G, fg="red", text="COMPARE", font="comicsansms 10 bold", relief=SUNKEN, command=partial(graph1,stock_name1=userentry,stock_name2=passentry)) 
            b7.grid(row=3,column=2)

            G.mainloop()

        B = Tk()
        B.geometry("2000x820")
        B.title("STOCKS")
    
        frame1=Frame(B, borderwidth=6, bg="grey", relief=SUNKEN)
        frame1.pack(fill=X, pady=20)
    
        label1=Label(frame1, text="Choose Your Option", bg="black" , fg="white" , font="comicsansms 50 bold", borderwidth=5, relief=SUNKEN )
        label1.pack(fill=X)

        frame2=Frame(B, borderwidth=6, bg="yellow", relief=SUNKEN)
        frame2.pack()

        b5= Button(frame2, fg="red", text="REAL TIME PRICE",font="comicsansms 25 bold", relief=SUNKEN, command=smit)
        b5.pack(pady=10)

        b2= Button(frame2, fg="red", text="DATE WISE PRICE",font="comicsansms 25 bold", relief=SUNKEN, command=adit)
        b2.pack(pady=10)

        b8= Button(frame2, fg="red", text="COMPARE TWO STOCK",font="comicsansms 25 bold", relief=SUNKEN, command=karan)
        b8.pack(pady=10)

        B.mainloop()  
        
    

    
    B = Tk()
    B.geometry("2000x820")
    B.title("STOCKS")
    
    frame1=Frame(B, borderwidth=6, bg="grey", relief=SUNKEN)
    frame1.pack(fill=X, pady=20)
    
    label1=Label(frame1, text="Choose Your Option", bg="black" , fg="white" , font="comicsansms 50 bold", borderwidth=5, relief=SUNKEN )
    label1.pack(fill=X)

    frame2=Frame(B, borderwidth=6, bg="yellow", relief=SUNKEN)
    frame2.pack()

    b5= Button(frame2, fg="red", text="MY STOCKS",font="comicsansms 25 bold", relief=SUNKEN, command=bonil)
    b5.pack(pady=10)

    b2= Button(frame2, fg="red", text="BUY STOCK",font="comicsansms 25 bold", relief=SUNKEN, command=tapan)
    b2.pack(pady=10)

    b3= Button(frame2, fg="red", text="STOPLOSS",font="comicsansms 25 bold", relief=SUNKEN)
    b3.pack(pady=10)

    b4= Button(frame2, fg="red", text="SREARCH STOCK",font="comicsansms 25 bold", relief=SUNKEN, command=utsav)
    b4.pack(pady=10)

    B.mainloop()

A = Tk()
A.geometry("2000x830")
A.title("Stock Analysis")
menubar= Menu(A)
m1 = Menu(menubar,tearoff=0)
m1.add_command(label="Privious Page")
m1.add_command(label="Home Page")
A.config(menu=menubar)
menubar.add_cascade(label="GO",menu=m1)

m2 = Menu(menubar,tearoff=0)
m2.add_command(label="Privious Page")
m2.add_command(label="Home Page")
A.config(menu=menubar)
menubar.add_cascade(label="Exit",menu=m2)

label=Label(text="STOCK ANALYSIS", bg="black" , fg="white" , font="comicsansms 50 bold", borderwidth=5, relief=SUNKEN )
label.pack(fill=X)

frame=Frame(A, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=BOTTOM)
b1= Button(frame, fg="red", text="START",font="comicsansms 25 bold", command=hello)
b1.pack()

A.mainloop()
