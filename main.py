from tkinter import *
from tkinter.colorchooser import askcolor
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageOps
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import sys
import matplotlib.font_manager
import os
from os.path import exists



window = Tk()
window.title('WATERMARK APP')
window.config(width=800, height=700)


canvas = Canvas(width=800, height=700, bg="#9DF1DF", highlightthickness=0)
canvas.grid(row=5, column=3)

canvas.create_rectangle(0, 50, 800, 50)
canvas.create_rectangle(0, 650, 800, 650)

#-----------Create ADD Button ---------
def create_add_button():
    add_button.config(
        text="Add Image",
        highlightthickness=0,
        highlightbackground="#9DF1DF",
        highlightcolor="white",
        foreground="#0014FF",
        command=_upload_image,
        state=DISABLED
    )
    add_button.place(x=300, y=12)


#---------Function to upload the Image ------------

def _upload_image():
    global img
    f_types = [('Jpg Files', '*.jpg'), ('Jpeg Files', '*.jpeg')]
    filename = filedialog.askopenfilename(filetypes=f_types)

    image = Image.open(filename)
    image_rs = image.resize((600, 350))
    image_rs.save('img.jpeg')
    image = ImageTk.PhotoImage(image_rs)
    label1.config(image=image)
    label1.image = image
    label1.place(x=90, y=150)
    remove_text.place(x=0, y=-300)
    add_center_button.destroy()
    next_button.config(state=NORMAL)
    clear_button.config(state=NORMAL, command=clear_app)
    create_add_button()
    add_center_button.destroy()
    clear_button.place(x=400, y=12)



label1 = Label(image="")

def _upload_image_with_text():

    image = Image.open('img_draw.jpeg').resize((600, 350))

    image_rs = image.resize((600, 350))
    image = ImageTk.PhotoImage(image_rs)
    label1.config(image=image)
    label1.image = image
    label1.place(x=90, y=150)
    remove_logo.place(x=0, y=-300)

# ----------Function to Clear the image uploaded---------

def clear_app():
    global label1, step
    step = 0
    label1.destroy()
    add_center_button = Button(
        text="Add Image",
        highlightthickness=0,
        highlightbackground="#9DF1DF",
        highlightcolor="white",
        foreground="#0014FF",
        command=add_image,
    )
    add_center_button.place(x=335, y=300)
    label1 = Label(image="")
    next_button.config(state=DISABLED)
    clear_button.config(state=DISABLED)
    add_center_button.destroy()
    add_button.config(state=NORMAL)
    file_exists = exists('img_draw.jpeg')
    file_exists2 = exists('img_with_logo.jpeg')
    if file_exists:
        os.remove('img_draw.jpeg')
    if file_exists2:
        os.remove('img_with_logo.jpeg')




#------- Function to Add an Image on Tkinter
def add_image():
    image = Image.open('img.jpeg').resize((600, 350))

    image_rs = image.resize((600, 350))
    image = ImageTk.PhotoImage(image_rs)
    label1.config(image=image)
    label1.image = image
    label1.place(x=90, y=150)
    remove_logo.place(x=0, y=-300)

#-----------Function going Back ----------
def back():
    global step
    text_add.place(x=400, y=-100)
    logo_add.place(x=400, y=-100)
    create_add_button()

    clear_button.place(x=400, y=12)
    back_button.place(x=400, y=-100)
    remove_text.place(x=-300, y=0)
    remove_logo.place(x=-300, y=0)
    step = 0





#------Function to close the app --------

def close_app():

    sys.exit()

#-----------FUNCTION TO SAVE THE FINAL RISULT----------
def save():
    sys.exit()





#-------------- Function to the Next Step-----------
step = 0
def next_step():
    global step

    step += 1
    if step == 1:

        text_add.config(
                          text="Add Text",
                        highlightthickness=0,
                        highlightcolor="white",
                        foreground="#0014FF",
                        highlightbackground="#9DF1DF",



                          )

        text_add.place(x=300, y=12)


        add_button.place(x=400, y=-100)
        clear_button.place(x=400, y=-100)
        back_button.config(
            text="< Back",
            highlightthickness=0,
            highlightcolor="white",
            foreground="#00FFC6",
            highlightbackground="#9DF1DF",
            command=back
        )
        back_button.place(x=100, y=12)
    else:

        logo_add.config(
            text="Add Logo",
            highlightthickness=0,
            highlightcolor="white",
            foreground="#0014FF",
            highlightbackground="#9DF1DF",

        )
        logo_add.place(x=300, y=12)
        add_button.place(x=400, y=-100)
        clear_button.place(x=400, y=-100)

        back_button.config(
            text="< Back",
            highlightthickness=0,
            highlightcolor="white",
            foreground="#00FFC6",
            highlightbackground="#9DF1DF",
            command=back
        )
        back_button.place(x=100, y=12)
        text_add.place(x=0, y=-300)
        remove_text.place(x=0, y=-300)






#-------FUNCTION TO ADD TEXT TO THE IMAGE AND ALL PROPERTIES     --------------
color_got = ""


text_position = {"top_left": {"coord": (0, 10),
                              "m": "lt"},
                 "top_middle": {"coord": (300,10),
                                "m": "mt"},
                 "top_right": {"coord": (600,10),
                               "m": "rt"},
                 "mid_left": {"coord": (0, 175),
                              "m": "lm"},
                 "mid_middle": {"coord": (300, 175),
                                "m": "mm"},
                 "mid_right": {"coord": (600, 175),
                                "m": "rm"},
                 "bot_left": {"coord": (0, 350),
                              "m": "lb"},
                 "bot_middle": {"coord": (300, 350),
                                "m": "mb"},
                 "bot_right": {"coord": (600, 350),
                               "m": "rb"}}

#--------------ADD TEXT BUTTON FUNNCTIONALITY-----------------
def add_text():
    top = Toplevel(window)
    top.config(width=400, height=500)
    top.title('Properties')
    Label(top, text='Text',font=("Helvetica", 15, "bold")).place(x=10, y=50)
    text = StringVar(top)

    entry_txt = Entry(top, width=35, textvariable=text)
    entry_txt.place(x=60, y=50)

    remove_logo.place(x=0, y=-300)
    remove_text.config(
        text="Remove Text",
        highlightthickness=0,
        highlightcolor="white",
        foreground="#0014FF",
        highlightbackground="#9DF1DF",
        command=add_image
    )
    remove_text.place(x=400, y=12)




    def display_selected(choice):
        #---GET THE VALUE OF FONT-FAMILY THAT THE USER PICK----------
        choice = clicked.get()
        entry_txt.config(font=(f"{choice}",),)
        return choice

    system_fonts = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf', )
    list_fonts = [os.path.basename(os.path.normpath(n)) for n in system_fonts]

    clicked = StringVar()

    Label(top, text='Font', font=("Helvetica", 15, "bold")).place(x=10, y=120)
    drop = OptionMenu(top, clicked, *list_fonts, command=display_selected)
    drop.place(x=60, y=120)

    pos = StringVar()
    def select_position(position):
        #---GET THE VALUE OF POSITION THAT THE USER PICK----------
        position = pos.get()
        return position

    list_position = text_position.keys()

    Label(top, text='Select Position', font=("Helvetica", 15, "bold")).place(x=10, y=380)
    drop_position = OptionMenu(top, pos, *list_position, command=select_position)
    drop_position.place(x=130, y=380)



    def change_color():
        global color_got
        #-------OPEN ALL COLORS WINDOW AVAILABLE---------
        color = askcolor()
        entry_txt.config(foreground=color[1])
        color_got = color[1]


    Label(top, text='Color', font=("Helvetica", 15, "bold")).place(x=10, y=200)
    color_button = Button(top, text="Pick you color", command=change_color)
    color_button.place(x=60, y=200)


    def scale_sizing(scale):
        scale = int(size_scale.get())
        return scale
    Label(top, text='Size', font=("Helvetica", 15, "bold")).place(x=10, y=285)
    size_scale = Scale(top, from_=0, to=50, length=320, tickinterval=10, orient=HORIZONTAL, command=scale_sizing)
    size_scale.place(x=60, y=270)

    def confirm_text():

        image = Image.open('img.jpeg').resize((600, 350))
        image_rs = image.resize((600, 350))
        draw = ImageDraw.Draw(image_rs)
        e_text = text.get()
        get_position = pos.get()
        print(get_position)
        coord = text_position[get_position]['coord']
        margin = text_position[get_position]['m']

        got_font = clicked.get()


        scale = int(size_scale.get())
        font = ImageFont.truetype(f"{got_font}",scale)

        draw.text(coord,f"{e_text}", font=font, fill=f"{color_got}", align='right', anchor=f'{margin}')
        image_rs.save("img_draw.jpeg")

        image = Image.open('img_draw.jpeg')
        image_rs = image.resize((600, 350))
        image = ImageTk.PhotoImage(image_rs)
        label1.config(image=image)
        label1.image = image
        top.destroy()




    confirm_button = Button(top, text="Confirm", highlightthickness=0, background='white', fg="#0014FF", command=confirm_text)
    confirm_button.place(x=150, y=450)

#--------------ADD LOGO BUTTON FUNNCTIONALITY-----------------

def add_logo():
    top = Toplevel(window)
    top.config(width=400, height=500)
    top.title('Properties')

    def select_logo(logo_pick):
        #---GET THE VALUE OF POSITION THAT THE USER PICK----------
        user_logo = logo_pick.get()
        return user_logo

    remove_logo.config(
        text="Remove Logo",
        highlightthickness=0,
        highlightcolor="white",
        foreground="#0014FF",
        highlightbackground="#9DF1DF",
        command=_upload_image_with_text
    )
    remove_logo.place(x=400, y=12)

    image1 = PhotoImage(width=5, height=5, file="logo/logo0.png")
    image2 = PhotoImage(width=5, height=5, file="logo/logo1.png")
    image3 = PhotoImage(width=5, height=5, file="logo/logo2.png")
    image4 = PhotoImage(width=5, height=5, file="logo/logo3.png")
    image5 = PhotoImage(width=5, height=5, file="logo/logo4.png")
    image6 = PhotoImage(width=5, height=5, file="logo/logo5.png")
    image7 = PhotoImage(width=5, height=5, file="logo/logo6.png")

    images = {"logo1": image1, "logo2": image2, "logo3": image3, "logo4": image4, "logo5": image5, "logo6": image6,
              "logo7": image7, }
    #-------------OPEN IMAGES---------------
    image1_open = Image.open("logo/logo0.png").resize((100, 100))
    image2_open = Image.open("logo/logo1.png").resize((100, 100))
    image3_open = Image.open("logo/logo2.png").resize((100,100))
    image4_open = Image.open("logo/logo3.png").resize((100,100))
    image5_open = Image.open("logo/logo4.png").resize((100,100))
    image6_open = Image.open("logo/logo5.png").resize((100,100))
    image7_open = Image.open("logo/logo6.png").resize((100,100))

    images_open = {"logo1": image1_open, "logo2": image2_open, "logo3": image3_open, "logo4": image4_open, "logo5": image5_open,
                   "logo6": image6_open, "logo7": image7_open, }

    logo = StringVar(value="logo1")
    om = OptionMenu(top, logo, "logo1", "logo2", "logo3", "logo4", "logo5", "logo6", "logo7")
    menu = om.nametowidget(om.menuname)
    for label, image in images.items():
        menu.entryconfigure(label, image=images[label], compound="left")

    om.place(x=120, y=53)

    Label(top, text='Select Logo', font=("Helvetica", 15, "bold")).place(x=10, y=50)

    #------------BUILDING LOGO POSITION------------------
    image = Image.open('car.jpeg').resize((600, 350))
    logo_name = logo.get()
    image_to_paste = images_open[logo_name]
    watermark_width, watermark_height = image_to_paste.size

    x, y = image.size

    margin = 10

    logo_position = {"top-left": (0 + margin, 0 + margin),
                     "top-right": (x - margin - watermark_width, 0 + margin),
                     "bot_left": (0 + margin, y - margin - watermark_height),
                     "bot-right": (x - margin - watermark_width, y - margin - watermark_height)
                     }

    pos = StringVar()

    def select_position(position):
        # ---GET THE VALUE OF POSITION THAT THE USER PICK----------
        position = pos.get()
        return position

    list_position = logo_position.keys()

    Label(top, text='Select Position', font=("Helvetica", 15, "bold")).place(x=10, y=100)
    drop_position = OptionMenu(top, pos, *list_position, command=select_position)
    drop_position.place(x=150, y=100)


    #---------------- ADD BUTTON SAVE -------------
    next_button.place(x=0, y=-300)
    save_button.config(
        text="Save",
        highlightthickness=0,
        highlightbackground="#9DF1DF",
        highlightcolor="white",
        foreground="#00FFC6",
        state=NORMAL,
        command=save
    )
    save_button.place(x=700, y=12)

    def confirm_logo_button_fun():
        get_position = pos.get()
        position = logo_position[get_position]

        image = Image.open('img_draw.jpeg').resize((600, 350))

        logo_name = logo.get()
        print(logo_name)
        image_to_paste = images_open[logo_name]
        image.paste(image_to_paste, position, mask=image_to_paste)
        image.save('logo/img_saved/img_with_logo.jpeg')
        window.update()

        image = Image.open('logo/img_saved/img_with_logo.jpeg')
        image_rs = image.resize((600, 350))
        image = ImageTk.PhotoImage(image_rs)
        label1.config(image=image)
        label1.image = image
        remove_text.place(x=0, y=-300)



        top.destroy()


    confirm_logo = Button(top, text="Confirm", highlightthickness=0, background='white', fg="#0014FF",
                            command=confirm_logo_button_fun)
    confirm_logo.place(x=150, y=450)






#---------------- BUTTONS ---------------#



close_button = Button(
    text="Close App",
    highlightthickness=0,
    highlightbackground="#9DF1DF",
    highlightcolor="white",
    foreground="#0014FF",
    command=close_app,
)
close_button.place(x=5, y=12)

add_button = Button()
back_button = Button()
text_add = Button(command=add_text)
logo_add = Button(command=add_logo)
remove_text = Button()
remove_logo = Button()
save_button = Button()

clear_button = Button(
    text="Clear",
    highlightthickness=0,
    highlightbackground="#9DF1DF",
    highlightcolor="white",
    foreground="#0014FF",
    state=DISABLED,
)
clear_button.place(x=350, y=12)


next_button = Button(
    text="Next Step",
    highlightthickness=0,
    highlightbackground="#9DF1DF",
    highlightcolor="white",
    foreground="#00FFC6",
    state=DISABLED,
    command=next_step
)
next_button.place(x=700, y=12)



add_center_button = Button(
    text="Add Image",
    highlightthickness=0,
    highlightbackground="#9DF1DF",
    highlightcolor="white",
    foreground="#0014FF",
    command=lambda :_upload_image(),
)
add_center_button.place(x=335, y=300)



#----------Copyright Label ---------#


label = Label(
    text="@ Copyright Damiano Manzillo",
    background="#9DF1DF",
    highlightcolor="white",
)
label.place(x=300, y=665)




window.mainloop()
