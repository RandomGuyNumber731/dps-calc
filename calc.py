from tkinter import *

def calc():
    try:
        try:
            a=float(_sta.get())                                                 # no explanation think urself ¯\_(ツ)_/¯
        except:
            a=_sta.get()
            pass
        try:
            b=float(_aps.get())
        except:
            b=_aps.get()
            pass
        try:
            c=float(_dph.get())
        except:
            c=_dph.get()
            pass
        
        if type(a) is not str:
            rate = 1/float(a)
        else:
            rate = float(b)
        dps = float(rate)*float(c)
        out = Label(root, text=f"ur DPS is {round(dps, 3)}!!")
        out.pack()
        out.after(3000, out.destroy)
    except Exception as e:
        print (e)
        out = Label(root, text="hmm i think u forgot smth...", fg="grey")
        out.pack()
        out.after(1500, out.destroy)
    if a == '': sta.set("seconds to attack")
    if b == '': aps.set("attack per second")
    if c == '': dph.set("damage per hit")

root = Tk()
root.title("DPS calculator by mimi")                                         #                                               .   '  .
root.geometry("400x230")                                                     #                                             .    ....  .   
#                                                                            #                                            . .... ...  .   
sta = StringVar()                                                            #                                            .   .  .`   .   
sta.set("seconds to attack")                                                 #                                               *'.. "   .   
aps = StringVar()                                                            #              '    '  .               ..     .   . .    .   
aps.set("attack per second")                                                 #           .....  .....                .     ..  .'.   '`.  
dph = StringVar()                                                            #           ...           .                .    '']$*'..`.   
dph.set("damage per hit")                                                    #           .,:'....."^'..'                  .   '... ''     
#                                                                            #          . .*..' .'"". '.                    .   .'.       
Label(root, text="a small thiny calcuator i made for calculations").pack()   #            ..  .  ....  .                     .            
#                                                                            #                : _      .                     :            
frametxt = Frame(root)                                                       #                ...     `                       .           
frametxt.pack()                                                              #          .   '^@@l'. .''                        :          
#                                                                            #          .. . `z@~...^`                         .          
Label(root, text="\"seconds to attack\" or \"attack per second\"").pack()    #          '...'. . ..'`                          .          
#                                                                            #             `.'...'`                            .          
frame1 = Frame(root)
frame1.pack()
frame2 = Frame(root,padx=5,pady=5)
frame2.pack()
Label(frametxt, text="either input ").grid(row=1)
Label(frametxt, text="ONE ", fg="RED", font="bold").grid(row=1,column=1)
Label(frametxt, text="of").grid(row=1,column=2)
_sta = Entry(frame1, textvariable=sta, borderwidth=3, justify=CENTER)
_aps = Entry(frame1, textvariable=aps, borderwidth=3, justify=CENTER)
_dph = Entry(frame2, textvariable=dph, borderwidth=3, justify=CENTER)
_sta.grid(row=1,column=0,padx=5)
_aps.grid(row=1,column=1,padx=5)
_dph.grid()
Button(frame2, text="Calculate!",command=lambda: calc(),).grid(pady=5)
root.mainloop()
