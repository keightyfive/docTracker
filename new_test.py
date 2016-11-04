import tkinter as tk
from tkinter import W, E, N, S, END, Label
import cw2

root = tk.Tk()

#root.master.title("Document Tracker")
root.grid()

"""
tab
"""
#tab for parsing the document_id

w = Label(root, text="document_id:")
w.grid(row=0, column=0)
tab = tk.Entry(root, width=30)
tab.grid(row=1, column=0)

w2 = Label(root, text="visitor_id:")
w2.grid(row=2, column=0)
tab2 = tk.Entry(root, width=30)
tab2.grid(row=3, column=0)


"""
Buttons
"""

"""
TASK 2.a) button for countries of viewers
"""
# button for countries
countriesBtn = tk.Button(root, text="2a) countries", command=lambda: cw2.show_histo(cw2.task2a(tab.get())))
countriesBtn.grid(row=0, column=1, sticky=W+E+N+S)

"""
TASK 2.b) button for continents of viewers
"""
# button for continents
continentsBtn = tk.Button(root, text="2b) continents", command=lambda: cw2.show_histo(cw2.task2b(tab.get())))
continentsBtn.grid(row=1, column=1, sticky=W+E+N+S)

"""
TASK 3.a) button for all browsers
"""
# button for continents
allBrowsersBtn = tk.Button(root, text="3a) all browsers", command=lambda: cw2.show_histo(cw2.task3a()))
allBrowsersBtn.grid(row=2, column=1, sticky=W+E+N+S)

"""
TASK 3.b) button only the main browser name
"""
# button for continents
mainBrowserBtn = tk.Button(root, text="3b) main browsers", command=lambda: cw2.show_histo(cw2.task3b()))
mainBrowserBtn.grid(row=3, column=1, sticky=W+E+N+S)

"""
TASK 4.) button for reader profiles: identifying the most avid readers
"""
# button for continents
avidReadersBtn = tk.Button(root, text="4) avid readers", command=lambda: insertList(cw2.task4()))
avidReadersBtn.grid(row=4, column=1, sticky=W+E+N+S)

"""
TASK 5.a) button for all visitor ids
"""
visitorsIdsBtn = tk.Button(root, text="5a) visitor ids", command=lambda: insertList(cw2.task5a(tab.get())))
visitorsIdsBtn.grid(row=5, column=1, sticky=W+E+N+S)

"""
TASK 5.b) button for document ids
"""
documentIdsBtn = tk.Button(root, text="5b) document ids", command=lambda: insertList(cw2.task5b(tab2.get())))
documentIdsBtn.grid(row=6, column=1, sticky=W+E+N+S)

"""
TASK 5.c) button for also liked documents list
"""
alsoLikesBtn = tk.Button(root, text="5c) also likes", command=lambda: insertList(cw2.task5c(tab.get(), tab2.get(), None)))
alsoLikesBtn.grid(row=7, column=1, sticky=W+E+N+S)

"""
TASK 5.d) button for sorting function based on readership profile
"""
sortFunctProfBtn = tk.Button(root, text="5d) sort based on readership", command=lambda: insertList(cw2.task5c(tab.get(), tab2.get(), cw2.task5d)))
sortFunctProfBtn.grid(row=8, column=1, sticky=W+E+N+S)

"""
TASK 5.e) button for sorting function based on readers in same document
"""
sortFunctDocBtn = tk.Button(root, text="5e) sort based on doc", command=lambda: insertList(cw2.task5c(tab.get(), tab2.get(), cw2.task5e)))
sortFunctDocBtn.grid(row=9, column=1, sticky=W+E+N+S)

"""
Listbox
"""
Listbox1 = tk.Listbox(root, width=60)
Listbox1.grid(row=10, column=1, sticky=W+E+N+S)

def insertList(listvalues):
	Listbox1.delete(0, END)
	for i in listvalues:
		Listbox1.insert(END, i)

root.mainloop()