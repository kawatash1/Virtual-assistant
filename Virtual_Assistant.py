import webbrowser as wb
import tkinter as tk
from Web_Search import Websearch


class App():
	root = tk.Tk()				


	root.title("Виртуальный дворецкий")    
	root.geometry("700x500")				
	root.config(bg="yellow")
	
	
	L1 = tk.Label(text="Hello, I'm Virtual assistant", 
				  font='Arial 30', fg="Blue", bg="yellow")
	L1.pack()							


	b1 = tk.Button(text="GOOGLE", command = Websearch.open_chrome)
	b1.pack(pady = 20)
	
	b2 = tk.Button(text="Close", command = root.destroy)
	b2.pack(pady = 20)

	editor = tk.Text(height=10, wrap = "char")
	editor.pack()

	root.mainloop()
