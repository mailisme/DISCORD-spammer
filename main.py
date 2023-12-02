import requests as req
import tkinter as tk

def click():
    token = entry1.get()
    url = entry2.get()
    text = entry3.get()
    i = 1177575105329400000
    headers = {
        'Authorization': token, 
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }
    while i<1900000000000000000:
        json = {
            "mobile_network_type": "unknow", 
            "content": text, 
            "nonce": i, 
            "tts": False, 
            "flags": 0
        }

        r = req.post(url=url, headers=headers, json= json)
        print(r.text)
        i = i +1

win = tk.Tk()
win.title('discord')

label1 = tk.Label(text='token')
label1.pack()
entry1 = tk.Entry()
entry1.pack()
label2 = tk.Label(text='url')
label2.pack()
entry2 = tk.Entry()
entry2.pack()
label3 = tk.Label(text='text')
label3.pack()
entry3 = tk.Entry()
entry3.pack()
btn = tk.Button(win, command=click, text='開始刷屏')
btn.pack()

win.mainloop()