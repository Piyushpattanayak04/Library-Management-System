import pyttsx3
from tkinter import *
from PIL import ImageTk,Image


inventory={}
issued={}

def addbook():
    while True:
        serial=int(input("Enter The Serial No. Of The Book : "))
        if serial==0:
            break
        else:
            name=str(input("Enter The Name Of The Book : "))
            author=str(input("Enter The Author Of The Book : "))
            inventory[serial]=name,author
            print("Book Added To The Inventory Sucessfully :]")
            print(" ")

def issuebook():
    while True:
        serialissue=int(input("Enter Serial Number To Issue A Book : "))
        if serialissue==0:
            break
        else:
            person=str(input("Enter The Reciever Name : "))
            id=int(input("Enter Your Library Id :"))
            phonenumber=str(input("Enter The Contact Details : "))
            if len(phonenumber)==10:
                issued[id]=person,phonenumber,serialissue,inventory[serialissue]
                del inventory[serialissue]
                print("Book Issued Sucessfully :] ")
                print(" ")
            else:
                print("Invalid Phone Number")
                print(" ")
            

def returnbook():
    while True:
        serailreturn=int(input("Enter The Library Id : "))
        if serailreturn not in issued:
            break
        else:
            inventory.setdefault(issued[serailreturn][2],issued[serailreturn][3])
            del issued[serailreturn]
            print("Book Returned Sucessfully :] ")
            print(" ")

def deletebook():
    
    while True:
        serialdelete=int(input("Enter The Serial Of The Book To Be Deleted : "))
        if serialdelete==0:
            break
        else:
            print(inventory[serialdelete],"Has Been Deleted Sucessfully :] ")
            del inventory[serialdelete]
            print(" ")

def viewlibrarystats():
    print("The Books Available In The Inventory Are :")
    print(inventory)
    print(" ")
    print("The Books Issued Are : ")
    print(issued)
    print(" ")


def voice():
    engine = pyttsx3.init()
    voices=engine.getProperty("voices")
    engine.setProperty("rate", 125)
    engine.setProperty("voice", voices[1].id)
    engine.say("Welcome To The Ocean Of Books ")
    engine.say("Please Select Any Option To Continue ")
    engine.runAndWait()

def viewbook():
    print("Press 1 To Search Through Serial Number")
    print("Press 2 to Search Through Book Name")
    print("Press 3 To Search Through Author Name")
    
    while True:
        search=int(input("Enter Your Choice : "))
        if search==1:
            serailsearch=int(input("Enter The Serial Number : "))
            if serailsearch in inventory.keys():
                print("Book related To Your Search")
                print(inventory[serailsearch])
                print(" ")
            else:
                print("Invalid Serial Number :[ ")
                print(" ")
        elif search==2:
            bookname=str(input("Enter The Book Name : "))
            for i in inventory.keys():
                if bookname==inventory[i][0]:
                    print("Book related To Your Search ")
                    print(inventory[i])
                    print(" ")
        elif search==3:
            authorname=str(input("Enter Author Name : "))
            book=[]
            for i in inventory.keys():
                if authorname==inventory[i][1]:
                    book.append(inventory[i])
            if len(book)==0:
                print("Books Of ",authorname,"not found in inventory")
                print(" ")
            else:
                print("The Books Of ",authorname,"are as follows : ")
                print(book)
                print(" ")
        elif search==0:
            break        
        else:
            print("Invlaid Search Option :[")   
            print(" ")  


def quit():
    root.destroy()
    print(" ")
    print("*****************************************************************************************************************")
    print(" ")
    print("THANK YOU FOR VISITING OUR LIBRARY : ] ")
    print(" ")
    print("*****************************************************************************************************************")


root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")

# Take n greater than 0.25 and less than 5
same=True
n=0.25

# Adding a background image
background_image =Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="  Welcome to \n Ocean Of Books", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


btn1 = Button(root,text="Add Book Details",bg='black', fg='white',command=addbook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete Book",bg='black', fg='white',command=deletebook)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="Search Book",bg='black', fg='white',command=viewbook)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white',command=issuebook)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Return Book",bg='black', fg='white',command=returnbook)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

btn6= Button(root,text="View Library",bg='black', fg='white',command=viewlibrarystats)
btn6.place(relx=0.28,rely=0.9, relwidth=0.45,relheight=0.1)

btn7= Button(root,text="Quit",bg='white', fg='red',command=quit)
btn7.place(relx=0.85,rely=0.9, relwidth=0.1,relheight=0.1)

btn8=Button(root,text="Voice",bg='white', fg='red',command=voice)
btn8.place(relx=0.85,rely=0.8, relwidth=0.1,relheight=0.1)

root.mainloop()



            
            



