import tkinter as tk
import requests

root = tk.Tk()
root.title("Home Page")
root.geometry("300x200")

root.configure(bg="grey")

label = tk.Label(root, text="Send")
label.place(x=10, y=10)

textbox = tk.Entry(root, width=30)
textbox.place(x=45,y=11)

label2 = tk.Label(root, text="Receive")
label2.place(x=10, y=35)

label3 = tk.Label(root, text="")
label3.place(x=60,y=35)

#send requests
def send_message():
    message = textbox.get()
    response = requests.post(
        "http://192.168.1.17:5000/send",
        json={"message": message }
    )
    print(response.text)

#receive requests
def get_message():
    msg = requests.get("http://192.168.1.17:5000/send")
    message = msg.text
    return message

# message="Hi"
def update_message():
    msg = get_message()
    label3.config(text=msg)
    root.after(1000,update_message)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.place(x=230,y=8)

update_message()

root.mainloop()