import pyperclip
import pyshorteners 
from tkinter import *


def urlshort():
    urladdress= url.get()
    url_short= pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.delete(0, END)
    url_address.insert(0, url_short)

def copyurl():
    url_short= url_address.get()
    pyperclip.copy(url_short)

root = Tk()
root.geometry("400x300")
root.title("URL Shortener")
Label (root, text="My URL Shortener", font= "poppins 16 bold").pack(pady=10) 
url= Entry(root,width=30, font=("Arial", 14))
url.pack(pady=5)
Button(root, text="Generate Short URL", command=urlshort).pack(pady=7)
Label(root, text="Your URL After Short ",font="poppins 16 bold").pack(pady=10)
url_address= Entry(root,width=30, font=("Arial", 16))
url_address.pack(pady=7)
Button(root,text="Copy URL", command=copyurl).pack(pady=7)
root.mainloop()
