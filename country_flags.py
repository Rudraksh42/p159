from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image

root=Tk()
root.title("Country Flags")
root.geometry("600x400")
root.configure(background="lightblue")

get_input = Entry(root)
show_label = Label(root)

india_map = ImageTk.PhotoImage(Image.open ("India.jpg"))
america_map = ImageTk.PhotoImage(Image.open ("America.jpg"))
australia_map = ImageTk.PhotoImage(Image.open ("Australia.png"))
philippines_map = ImageTk.PhotoImage(Image.open ("Philippines.png"))
japan_map = ImageTk.PhotoImage(Image.open ("Japan.jpg"))

maps_dictionary = { "India" : india_map , 
                    "America" : america_map ,
                    "Australia" : australia_map ,
                    "Philippines" : philippines_map,
                    "Japan" : japan_map,}

def showMaps():
    try:
        map_name = get_input.get()
        s = map_name.capitalize()
        print(str(s))
        show_label['image'] = maps_dictionary[s]
    except:
        messagebox.showinfo("Invalid Code!","The country flag is not avaible in our system")
        
    

btn = Button(root , text="Show Map", bg="green", command=showMaps)
get_input.place(relx=0.5, rely=0.1, anchor=CENTER)
btn.place(relx=0.5, rely=0.2, anchor=CENTER)
show_label.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()