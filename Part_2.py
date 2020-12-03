from tkinter import *
from tkinter.ttk import *
import csv

Dic = {}
Contact = {}

with open("base.csv", "r", newline = "") as base:
    reader = csv.reader(base)
    for e in reader:
        if e[0] != "Name":
            Dic[e[0]] = int(e[1])
            Contact[e[0]] = e[2]
base.close()
sorted_dict = {}
sorted_keys = sorted(Dic, reverse = True, key=Dic.get)

for w in sorted_keys:
    sorted_dict[w] = Dic[w]

window = Tk()
window.title("Innova™ Reader®©")

lb = Label(window, text = "")

Label(window, text = "Identification | Score").pack()
lb['text'] = '\n'.join('{} | {}'.format(k, d) for k, d in sorted_dict.items())
lb.pack()
window.mainloop()
