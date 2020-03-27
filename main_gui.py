from tkinter import *
from main_logic import *
window = Tk()
window.title("Py ML Preprocessing")

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

PATH = glob.glob(
    "C:\\Users\\Varadh\\Documents\\GitHub\\PyProject_ML_Preprocessing\\Active_Workspace\\*.jpg")


def submit():
    set_path(path_entry.get())

    if var1 == 1:
        convert_filetype()

    if var2 == 1:
        img_resize(b_width.get(), b_height.get())

    if var3 == 1:
        img_to_grey()

    if var4 == 1:
        img_to_numpy_w_label(e.get(), f.get())


text2 = Label(window, text='Enter the Path')
text2.grid(row=1, column=0)
path_entry = Entry(window, width=50)

path_entry.grid(row=1, column=1)
# By default, the variable is set to 1 if the button is selected, and 0 otherwise.
a = Checkbutton(window, text='Images to JPG', variable=var1)
a.grid(row=2, column=0)

b = Checkbutton(window, text='Resize', variable=var2)
b.grid(row=3, column=0)
Label(window, text='Enter width and height').grid(row=3, column=1)
b_width = Entry(window)
b_width.grid(row=3, column=2)
b_height = Entry(window)
b_height.grid(row=3, column=3)

c = Checkbutton(window, text='Convert Images to Greyscale', variable=var3)
c.grid(row=4, column=0)

d = Checkbutton(window, text='Store Images in numpy array with extracted features', variable=var4)
d.grid(row=5, column=0)

Label(window, text='Extraction Parameters:').grid(row=6)
Label(window, text="Enter the feature separating symbol (E.g:- '_' or '-'):  ").grid(row=7, column=0)
e = Entry(window)
e.grid(row=7, column=1)

Label(window, text="Enter the offset of the separating symbol (i.e. after how many '_' or '-' to start extracting the features:  ").grid(row=8, column=0)
f = Entry(window)
f.grid(row=8, column=1)

g = Text(window, height=7, width=50, state='disabled')
g.configure(state='normal')
g.insert('end', 'This is a Log of the Program\n')
g.configure(state='disabled')
g.grid(row=9, column=0)

h = Button(window, text='Submit', command=submit)
h.grid(row=9, column=1)


window.mainloop()
