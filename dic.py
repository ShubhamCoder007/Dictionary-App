import json
from difflib import get_close_matches
from tkinter import *
from time import sleep

data=json.load(open("data.json"))

def translate_command():
	list1.delete(0, END)
	result = translate(word_text.get())
	if type(result) == list:
		for line in result:
			list1.insert(END, line)
	else:
		list1.insert(END, result)
		
def exit_command():
	list1.delete(0, END)
	list1.insert(END, "Thank you for using!")
	sleep(1)
	window.destroy()
	
def translate(word):
	word=word.lower().lstrip(" ").rstrip(" ").rstrip(".")
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif len(get_close_matches(word,data.keys()))>0:
		list1.delete(0, END)
		list1.insert(END,"Did you mean %s :"%get_close_matches(word,data.keys())[0])
		#choice=input("press y for yes, n for no: ").lower()
		if(option_text.get().lower()=="y"):
			return data[get_close_matches(word,data.keys())[0]]
		elif(option_text.get().lower()=="n"):
			return "Sorry! The word doesn't exists"
		else:
			return "Sorry! I didn't understand your query"
	else:
		return "Sorry! The word doesn't exist"
		
		
def creator():
	list1.delete(0,END)
	list1.insert(END,"Created by Shubham Banerjee!")


window = Tk()
window.wm_title("My dictionary SB")

l1 = Label(window, text = "Enter the word")
l1.grid(row = 0, column = 0, columnspan = 2)

l2 = Label(window, text = "Does your query match?")
l2.grid(row = 1, column = 0)

l3 = Label(window, text = "Results")
l3.grid(row = 2, column = 0)

word_text = StringVar()
e1 = Entry(window, textvariable = word_text)
e1.grid(row = 0, column = 3, columnspan = 2)

option_text = StringVar()
e2 = Entry(window, textvariable = option_text)
e2.grid(row = 1, column = 3, columnspan = 2)

list1 = Listbox(window, height = 6, width = 40)
list1.grid(row = 4, column = 0, columnspan = 2, rowspan = 6)

sb1 = Scrollbar(window)
sb1.grid(row = 4, column = 3, rowspan = 6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

b1 = Button(window, text = "Search", width = 15, command = translate_command)
b1.grid(row = 4, column = 4)

b2 = Button(window, text = "Creator", width = 15, command = creator)
b2.grid(row = 10, column = 4)

b2 = Button(window, text = "Exit", width = 15, command = exit_command)
b2.grid(row = 6, column = 4)


window.mainloop()
			