#WEB CRAWLER

#IMPORT MODULES

from tkinter import *
import requests
from PIL import Image,ImageTk
from bs4 import BeautifulSoup
from tkinter import messagebox
import webbrowser
import winsound

#FORMING WINDOW

google="http:/google.com"

while True:
    f=5000
    dr=1000

    root=Tk()

    root.title("ALPHA.OS MUSIC v1.0.1  Powered By ALPHA.OS")
    root.iconbitmap(r'icon.ico')
    root.configure(bg="#ffecd2")
    image=Image.open("newicon.png")
    photo2=ImageTk.PhotoImage(image)

    def quit():
        exit()

    l1=Label(root,image=photo2,bg="#ffecd2")
    l1.pack(pady=30)
    #b1=Button(root,text="ENTER",command=quit)
    #b1.pack()
    l2=Label(root, text="powered by", bg="#ffecd2", fg="black")
    l3=Label(root,text = "ALPHA.OS", font="Cambria 20", height=1,width=24, bg="#ffecd2", fg="black")
    l3.pack(side=BOTTOM)
    l2.pack(side=BOTTOM)
    winsound.Beep(f,dr)
    messagebox.showinfo("ALPHA.OS", "ALPHA.OS INITIATNG... YOU CAN NOW CLOSE THIS WINDOW")
    root.mainloop()

    break

window=Tk()
messagebox.showinfo("ALPHA.OS","WEB SPIDER INITIATED...")
messagebox.showinfo("ALPHA.OS","COMMANDS AND INPUT WILL BE TAKEN IN SHELL WINDOW. "
                               "CONTINUE TO FOLLOW THE ON SCREEN INSTRUCTIONS")
print("WELCOME TO ALPHA.OS WEB CRAWLER v1.0.1")

window.title("ALPHA.OS   WEBCRAWLER v1.0.1")
window.iconbitmap(r'icon.ico')
image=Image.open("background1.png")
photo=ImageTk.PhotoImage(image)
image1=Image.open("osicon.png")
photo2=ImageTk.PhotoImage(image1)
image2 = Image.open("google.png")
photo3 = ImageTk.PhotoImage(image2)
#window.iconbitmap(r'icon.ico')

messagebox.showinfo("ALPHA.OS","CHOOSE THEME DARK/LIGHT IN THE SHELL WINDOW")
q=input("ENTER YOUR THEME CHOICE (DARK/LIGHT) HERE=")

if q == "light" or q == "LIGHT":
    window.configure(bg="white")
elif q == "dark" or q == "DARK":
    window.configure(bg="grey")
else:
    messagebox.showerror("ALPHA.OS","YOU ENTERED AN INVALID CHOICE !")
    window.configure(bg="white")

fr=1000
d=100

#MAIN FUNCTIONING

a=int(input("enter number of websites to be searched"))

i=1
while i<=a:

    n=0
    def search():
        global n
        n=n+1
        if n==1:
            winsound.Beep(fr,d)
            messagebox.showinfo("ALPHA.OS","ENTER THE WEBSITE TO BE CRAWLED IN THE SELL WINDOW")
            website = input("ENTER WEBSITE TO BE CRAWLED...")
            url = 'https://'+website +'.com'
            w= url+"  IS NOW BIENG CRAWLED."
            messagebox.showinfo("ALPHA.OS",w)
            r = requests.get(url)
            htmlcont = r.content
            soup = BeautifulSoup(htmlcont, 'html.parser')
            title = soup.title
            anchor = soup.find_all('a')
            all_links=set()
            #for links in anchor:
                #print(links.get('href'))
            para = soup.find_all('p')
            for link in anchor:
                if (link.get('href') != '#'):


                    link = url+link.get('href')
                    all_links.add (link)
                    print(title.string)
                    print(link)
                    #messagebox.showinfo("BEAST.OS",link)
                else:
                    pass
            messagebox.showinfo("ALPHA.OS",link)
            messagebox.showinfo("ALPHA.OS","SCRAPING COMPLETED...")
            messagebox.showinfo("ALPHA.OS","CHECK THE SHELL FOR ALL THE LINKS. LINKS CAN BE COPIED , "
                                           "PASTED IN THE BROWSER TO VISIT THE WEBSITE ON THE TARGET LOCATION")
            messagebox.showinfo("ALPHA.OS","OPENING WEBSITE HOMEPAGE. ENTER 'YES' TO CONTINUE")

            u=input("ENTER YOUR CHOICE - ")
            u1="visiting " + url
            if u == "yes" or u == "YES":
                messagebox.showinfo("ALPHA.OS",u1)
                webbrowser.open(url)
            else:
                messagebox.showinfo("ALPHA.OS","CONNECTION TERMINATED")

    x=0
    def Exit():
        global x
        x=x+1
        if x==1:
            winsound.Beep(fr, d)
            window.quit()

    y=0
    def search2():
        global y
        y=y+1
        if y==1:
            winsound.Beep(fr, d)
            b=input("ARE YOU SURE TO MOVE TO ANOTHER WEBSITE...")
            messagebox.showinfo("ALPHA.OS", "PREVIOUS CONNECTION TERMINATED")
            if b == "y" or b=="Y":
                website = input("ENTER WEBSITE TO BE CRAWLED...")
                url = 'https://'+website +'.com'
                e=url+" IS NOW BIENG CRAWLED"
                messagebox.showinfo("ALPHA.OS",e)
                r = requests.get(url)
                htmlcont = r.content
                soup = BeautifulSoup(htmlcont, 'html.parser')
                title = soup.title
                anchor = soup.find_all('a')
                all_links=set()
                #for links in anchor:
                    #print(links.get('href'))
                para = soup.find_all('p')
                for link in anchor:
                    if (link.get('href') != '#'):
                        link = url +link.get('href')
                        all_links.add (link)
                        print(title.string)
                        print(link)
                    else:
                        pass
                messagebox.showinfo("ALPHA.OS", link)
                messagebox.showinfo("ALPHA.OS", "SCRAPING COMPLETED...")
                messagebox.showinfo("ALPHA.OS","CHECK THE SHELL FOR ALL THE LINKS. LINKS CAN BE COPIED , "
                                               "PASTED IN THE BROWSER TO VISIT THE WEBSITE ON THE TARGE LOCATION")
                messagebox.showinfo("ALPHA.OS", "OPENING WEBSITE HOMEPAGE. ENTER 'YES' TO CONTINUE")

                s = input("ENTER YOUR CHOICE - ")
                s1="visiting " + url
                if s == "yes" or s == "YES":
                    messagebox.showinfo("ALPHA.OS", s1)
                    webbrowser.open(url)
                else:
                    messagebox.showinfo("ALPHA.OS", "CONNECTION TERMINATED")
            else:
                pass

    def g():
        webbrowser.open(google)

    i+=1

#LABELLING AND BUTTON DEFINING

if q == "light" or q == "LIGHT":

    l1=Label(window, image=photo, pady=10, width=700, bg="white")
    l1.pack(pady=10)

    l2=Label(window, text = "ALPHA.OS      WEB CRAWLER", font="Cambria 40", height=1,width=24,bg="white",
             fg="black", pady=10)
    l2.pack(pady=10)

    b3=Button(window,image=photo3,width=100,bg="white",activebackground="white",activeforeground="black",
              command=g, borderwidth=5, font="calibri")
    b3.pack(pady=5)

    b1=Button(window,text="SEARCH THE WEB", activebackground="white",activeforeground="black",borderwidth=5,
              width=100,bg='black',fg='white', font="calibri",command=search)
    b1.pack(pady=5)

    b2=Button(window,text="SEARCH THE WEB FOR ANOTHER WEBSITE ",activebackground="white",activeforeground="black",
              width=100, pady=3,bg='black',fg='white', borderwidth=5, font="calibri" ,command=search2)
    b2.pack()

    b4=Button(window,text="EXIT",width=100,bg='black',fg='red',activebackground="white",activeforeground="black",
              command=Exit, borderwidth=5, font="calibri")
    b4.pack(pady=5)

    l3=Label(window, text="powered by", bg="white", fg="black")

    l4=Label(window,text = "ALPHA.OS", font="Cambria 20", height=1,width=24, bg="white", fg="black")
    l4.pack(side=BOTTOM)
    l3.pack(side=BOTTOM)

    l5=Label(window, image=photo2, bg="white")
    l5.pack(side=BOTTOM)

else:

    l1 = Label(window, image=photo, pady=10, width=700, bg="grey")
    l1.pack(pady=10)

    l2 = Label(window, text="ALPHA.OS      WEB CRAWLER", font="Cambria 40", height=1, width=24, bg="grey",
               fg="black",pady=10)
    l2.pack(pady=10)

    b3=Button(window,image=photo3,width=100,bg="black",activebackground="white",activeforeground="black",
              command=g, borderwidth=5, font="calibri")
    b3.pack(pady=5)

    b1 = Button(window, text="SEARCH THE WEB", activebackground="cyan",activeforeground="black",borderwidth=5,
                width=80, bg='black', fg='white', font="calibri",command=search)
    b1.pack(pady=5)

    b2 = Button(window, text="SEARCH THE WEB FOR ANOTHER WEBSITE ", activebackground="cyan",activeforeground="black",
                width=80, pady=3, bg='black', fg='white',borderwidth=5, font="calibri", command=search2)
    b2.pack()

    b4 = Button(window, text="EXIT", width=80, bg='black', activebackground="cyan",activeforeground="black",fg='red',
                command=Exit, borderwidth=5, font="calibri")
    b4.pack(pady=5)

    l3 = Label(window, text="powered by", bg="grey", fg="black")

    l4 = Label(window, text="ALPHA.OS", font="Cambria 20", height=1, width=24, bg="grey", fg="black")
    l4.pack(side=BOTTOM)
    l3.pack(side=BOTTOM)

    l5 = Label(window, image=photo2, bg="grey")
    l5.pack(side=BOTTOM)

#ENDING/CLOSING LOOP
window.mainloop()
