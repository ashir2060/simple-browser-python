import tkinter as tool

# Tool Kit Window Setup
window = tool.Tk() #Toolkit
window.title("My Python Tool-Kit App") # Assign title
window.geometry("400x300") # size

#Title label for text box
title_label1 = tool.Label(window, text="Add Student", font=("Arial", 10))
title_label1.pack(pady=5)
title_label1.pack(anchor="w")

#Text box
student_entry = tool.Entry(window, width=30, font=("Arial",10))
student_entry.pack(pady=0)
student_entry.pack(anchor="w")

#Title label for text box
title_label2 = tool.Label(window, text="Add Student ID", font=("Arial", 10))
title_label2.pack(pady=5)
title_label2.pack(anchor="w")

#Text box
student_ID_entry = tool.Entry(window, width=30, font=("Arial",10))
student_ID_entry.pack(pady=0)
student_ID_entry.pack(anchor="w")

window.mainloop() # begin loop