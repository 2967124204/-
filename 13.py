import tkinter as tk
import random
import threading
import time

def dow():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0,width)
    b = random.randrange(0,height)
    window.title('亲爱的')
    window.geometry(f'220x50+{a}+{b}')
    tk.Label(window,
             text='我爱你',
             bg='pink',
             font=('楷体',18),
             width=25,
             height=4
             ).pack()
    window.mainloop()

threads = []
for i in range(400):
    t = threading.Thread(target=dow)
    threads.append(t)
    t.start()
    time.sleep(0.01)