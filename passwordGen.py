from tkinter import  * 
import string 
import random 

ascii_characters = (string.ascii_letters   +  string.digits +   string.punctuation)

all_characters = list(ascii_characters)

print("This is the password generator program.")

window = Tk()
window.title("Password Generator/v.1")
window.geometry("500x250")

icon = PhotoImage(file = "temporarily_icon.png")
window.iconphoto(False, icon)
window.attributes("-alpha", 0.8)
window.configure(background="black")

label = Label(window , text="How many characters you wanna use: " , fg="white" ,background="black")
label.pack()

entry = Entry()
entry.pack()

n = entry.get()

while True:    
    
    n = input(" Give the number of characters for the password: ")
    if n.isdigit():
        
         def password_generator(num_dig , char_for_use):
            for char_for_use in range(int(n)):
              digit = random.choice(all_characters)
              print(digit, end= "")
            print()
            
            

         def main():
            
             print("This is your password:  " )
             password_generator(n, all_characters)
             
         main() 

    else:
        print("The number must be a digit")







