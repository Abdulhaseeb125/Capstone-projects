import customtkinter as ctk
import pandas as pd

window = ctk.CTk()
window.geometry("500x500")
window.config(bg='#20262E')
window.title("Login Page")

def action():
    data = pd.read_csv("login.csv")
    if user_entry.get()==data["Username"][0] and password_entry.get()==data["Password"][0]:
        window.quit()


# Label
login_label = ctk.CTkLabel(text="Log In", master=window, font=("Arial", 40),bg_color="#20262E")
login_label.place(relx=0.5, rely=0.3, anchor=ctk.CENTER )
# Email/Username Entry
user_entry = ctk.CTkEntry(master=window,width=200,placeholder_text="Username")
user_entry.place(relx=0.5, rely=0.5, anchor=ctk.CENTER )
# Password Entry
password_entry = ctk.CTkEntry(master=window,width=200,placeholder_text="Password")
password_entry.place(relx=0.5, rely=0.6, anchor=ctk.CENTER )

# login button
login_button = ctk.CTkButton(text="Log in", master=window,command=action)
login_button.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)


window.mainloop()
