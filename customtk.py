import customtkinter as ctk
from tkinter import messagebox


def main():
    def show_error_message(message):
        messagebox.showerror("Error", message)

    def printen():
        try:
            key = int(keyentry.get())
        except:
            show_error_message("The key must be an integer")
            return
        entext = encrypt(textentry.get(), key)
        outtext.delete(1.0, ctk.END)
        outtext.insert(ctk.END, entext)
    def printde():
        try:
            key = int(keyentry.get())
        except:
            show_error_message("The key must be integer")
            return
        entext = decrypt(textentry.get(), key)
        outtext.delete(1.0, ctk.END)
        outtext.insert(ctk.END, entext)

    def clear():
        outtext.delete("1.0", ctk.END)
        textentry.delete(0, ctk.END)
        keyentry.delete(0, ctk.END)

    app = ctk.CTk()
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("dark-blue")
    app.geometry("600x500")
    app.title("Caeser cipher")

    #lable
    label = ctk.CTkLabel(master=app, text="Hello world\n This is caeser cipher encrypter and decrypter", font=("Verdana", 18))
    label.place(relx=0.5, y=40, anchor="center")

    #text lable
    textlabel = ctk.CTkLabel(master=app, text="Text", font=("Verdana",17))
    textlabel.place(y=100, x=50)

    #text entry
    textentry = ctk.CTkEntry(master=app, width=400, height=30, placeholder_text="Alphabetical letters only", placeholder_text_color="gray", font=("Verdana",17), border_color="black")
    textentry.place(y=100, x=100)

    #key label
    keylabel = ctk.CTkLabel(master=app, text="Key", font=("Verdana",17))
    keylabel.place(y=150, x=50)

    #key entry
    keyentry = ctk.CTkEntry(master=app, height=30, width=150, placeholder_text="Integer only", placeholder_text_color="gray", font=("Verdana",17), border_color="black")
    keyentry.place(y=150, x=100)

    #encryption button
    enbutton = ctk.CTkButton(master=app, text="Encrypt", width=100, corner_radius=12, fg_color="transparent", border_color="black", border_width=2, hover_color="black", font=("Verdana", 16), command=printen)
    enbutton.place(y=220, x=100)

    #decryption button
    debutton = ctk.CTkButton(master=app, text="Decrypt", width=100, corner_radius=12, fg_color="transparent", border_color="black", border_width=2, hover_color="black", font=("Verdana", 16), command=printde)
    debutton.place(y=220, x=240)

    #clear button
    clearbutton = ctk.CTkButton(master=app, text="Clear all", width=100, corner_radius=12, fg_color="transparent", border_color="black", border_width=2, hover_color="black", font=("Verdana", 16), command=clear)
    clearbutton.place(y=220, x=380)

    #ouput label
    outlabel = ctk.CTkLabel(master=app, text="Your message", font=("Verdana", 17), corner_radius=12, fg_color="transparent")
    outlabel.place(y=335, x=50)

    #output text
    outtext = ctk.CTkTextbox(master=app, width=300, height=100, corner_radius=12, border_width=2, border_color="black", fg_color="transparent", font=("Verdana",17))
    outtext.place(y=300, x=200)


    app.mainloop()

def show_error_message(message):
        messagebox.showerror("Error", message)


def encrypt(text, n):
    if any(not letter.isalpha() and not letter.isspace() for letter in text):
        show_error_message("Can only decrypt and encrypt alphabetical letters")
        return
    entext = ''
    for letter in text:
        if letter.isspace():
            entext += letter
        
        if letter.isupper():
            dvalue = ord(letter)
            if n > 26:
                n -= 26
            dvalue += n
            if dvalue > ord("Z"):
                dvalue -= 26
            entext += chr(dvalue)
        elif letter.islower():
            dvalue = ord(letter)
            if n > 26:
                n -= 26
            dvalue += n
            if dvalue > ord("z"):
                dvalue -= 26
            entext += chr(dvalue)
    return entext


def decrypt(text, n):
    if any(not letter.isalpha() and not letter.isspace() for letter in text):
        show_error_message("Can only decrypt and encrypt alphabetical letters")
        return
    entext = ''
    for letter in text:
        if letter.isspace():
            entext += letter
        if letter.isupper():
            dvalue = ord(letter)
            if n > 26:
                n -= 26
            dvalue -= n
            if dvalue < ord("A"):
                dvalue += 26
            entext += chr(dvalue)
        elif letter.islower():
            dvalue = ord(letter)
            if n > 26:
                n -= 26
            dvalue -= n
            if dvalue < ord("a"):
                dvalue += 26
            entext += chr(dvalue)
    return entext


if __name__=="__main__":
    main()