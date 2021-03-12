from tkinter import *
import cv2
from PIL import ImageTk, Image 
from tkinter import filedialog 
from tkinter import messagebox
import numpy as np




# global variables declaration

global original_img_canvas
global edited_img_canvas

edited_image = 0 


# Function for intensity adjuster
def adjust_intensity(value):
    update_img_canvas()
    global imgs
    global edited_image
    img = imgs
    
    value = int(value)
  
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img = np.array(img, dtype = np.float64)
    
    img[:,:,1] = img[:,:,1]* (1 + value / 100)  
    img[:,:,1][img[:,:,1]>255]  = 255
    img = np.array(img, dtype = np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB) 
    
    im_pil = Image.fromarray(img)
    
    edited_image = im_pil

    width, height = im_pil.size
   
    if width > height:
        im_pil = im_pil.resize((550, 450), Image.ANTIALIAS) 
    elif width < height:
        im_pil = im_pil.resize((450, 550), Image.ANTIALIAS) 
    else:
        im_pil = im_pil.resize((500, 500), Image.ANTIALIAS) 
    
    photo = ImageTk.PhotoImage(im_pil) 
    img_canvas.image = photo
    img_canvas.itemconfig(blank_image_init,image = "")
    
    if width > height:
        img_canvas.create_image(310,120, image = photo, anchor = N)
    else:
         img_canvas.create_image(310,70, image = photo, anchor = N)
 
    
# Function for Brightness adjuster
def adjust_brightness(value):
    update_img_canvas()
    global imgs
    global edited_image
    img = imgs
    
    value = int(value)
  
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img = np.array(img, dtype = np.float64)
    
    img[:,:,2] = img[:,:,2]* (1 + value / 100)
    img[:,:,2][img[:,:,2]>255]  = 255
    img = np.array(img, dtype = np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB) 
    

    im_pil = Image.fromarray(img)
    edited_image = im_pil

    width, height = im_pil.size
   
    if width > height:
        im_pil = im_pil.resize((550, 450), Image.ANTIALIAS) 
    elif width < height:
        im_pil = im_pil.resize((450, 550), Image.ANTIALIAS) 
    else:
        im_pil = im_pil.resize((500, 500), Image.ANTIALIAS) 
    
    photo = ImageTk.PhotoImage(im_pil) 
    img_canvas.image = photo
    img_canvas.itemconfig(blank_image_init,image = "")
    
    if width > height:
        img_canvas.create_image(310,120, image = photo, anchor = N)
    else:
         img_canvas.create_image(310,70, image = photo, anchor = N)
    
    
def gamma_function(channel, gamma):
    
    invGamma = 1/gamma
    table = np.array([((i / 255.0) ** invGamma) * 255  for i in np.arange(0, 256)]).astype("uint8") 
    channel = cv2.LUT(channel, table)
    return channel

# Function for creating Summer Effect
def summer_effect(value):
    
    update_img_canvas()
    global imgs
    global edited_image
    value = int(value)
   
    img = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    img[:, :, 0] = gamma_function(img[:, :, 0], (1 - value / 100 + 0.001)) 
    img[:, :, 2] = gamma_function(img[:, :, 2], (1 + value / 100))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img[:, :, 1] = gamma_function(img[:, :, 1], 1.5) 

    img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
    

    im_pil = Image.fromarray(img)
    
    edited_image = im_pil

    width, height = im_pil.size
   
    if width > height:
        im_pil = im_pil.resize((550, 450), Image.ANTIALIAS) 
    elif width < height:
        im_pil = im_pil.resize((450, 550), Image.ANTIALIAS) 
    else:
        im_pil = im_pil.resize((500, 500), Image.ANTIALIAS) 
    
    photo = ImageTk.PhotoImage(im_pil) 
    img_canvas.image = photo
    img_canvas.itemconfig(blank_image_init,image = "")
    
    if width > height:
        img_canvas.create_image(310,120, image = photo, anchor = N)
    else:
         img_canvas.create_image(310,70, image = photo, anchor = N)
    
 
# Function for creating Winter Effect
def winter_effect(value):
    
    update_img_canvas()
    global imgs
    global edited_image
    
    value = int(value)
   
    img = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    img[:, :, 0] = gamma_function(img[:, :, 0], 1 + value / 100) 
    img[:, :, 2] = gamma_function(img[:, :, 2], 1 - value / 100 + 0.001)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img[:, :, 1] = gamma_function(img[:, :, 1], 1.5) 
    img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
    
    im_pil = Image.fromarray(img)
    edited_image = im_pil

    width, height = im_pil.size
   
    if width > height:
        im_pil = im_pil.resize((550, 450), Image.ANTIALIAS) 
    elif width < height:
        im_pil = im_pil.resize((450, 550), Image.ANTIALIAS) 
    else:
        im_pil = im_pil.resize((500, 500), Image.ANTIALIAS) 
    
    photo = ImageTk.PhotoImage(im_pil) 
    img_canvas.image = photo
    img_canvas.itemconfig(blank_image_init,image = "")
    
    if width > height:
        img_canvas.create_image(310,120, image = photo, anchor = N)
    else:
         img_canvas.create_image(310,70, image = photo, anchor = N)


# Function for creating oil painting effect  
def oil_paint():
    

    global imgs
    global edited_image
    
   
    img = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    

    img1 = cv2.medianBlur(img, 5) 
 
  
    median_painted = cv2.xphoto.oilPainting(img1, 5 +2 , 5 + 4)
        
    median_painted = cv2.cvtColor(median_painted, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(median_painted)
    
    edited_image = im_pil

    width, height = im_pil.size

        
    if width > height:
        im_pil = im_pil.resize((550, 450), Image.ANTIALIAS) 
    elif width < height:
        im_pil = im_pil.resize((450, 550), Image.ANTIALIAS) 
    else:
        im_pil = im_pil.resize((500, 500), Image.ANTIALIAS) 
    
    photo = ImageTk.PhotoImage(im_pil) 
    img_canvas.image = photo
    img_canvas.itemconfig(blank_image_init,image = "")
    
    if width > height:
        img_canvas.create_image(310,120, image = photo, anchor = N)
    else:
         img_canvas.create_image(310,70, image = photo, anchor = N)
        
        
# Function for crating pencil sketch
def pencil_sketch():
    

    global imgs
    global edited_image
   
    
    img = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    

    dst_gray, dst_color = cv2.pencilSketch(img, sigma_s= (5 * 15), sigma_r= (5 /50), shade_factor= 0.04) 
        
  
    dst_gray = cv2.cvtColor(dst_gray, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(dst_gray)
    edited_image = im_pil
    
    width, height = im_pil.size
   
    if width > height:
        im_pil = im_pil.resize((550, 450), Image.ANTIALIAS) 
    elif width < height:
        im_pil = im_pil.resize((450, 550), Image.ANTIALIAS) 
    else:
        im_pil = im_pil.resize((500, 500), Image.ANTIALIAS) 
    
    photo = ImageTk.PhotoImage(im_pil) 
    img_canvas.image = photo
    img_canvas.itemconfig(blank_image_init,image = "")
    
    if width > height:
        img_canvas.create_image(310,120, image = photo, anchor = N)
    else:
         img_canvas.create_image(310,70, image = photo, anchor = N)
         
    
# Function for creating water color effect
def water_color():
    

    global imgs
    global edited_image
   
    
    img = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
   
    water_color = cv2.bilateralFilter(img, 8, 64, 64)
    water_color = cv2.pyrMeanShiftFiltering(water_color, 30, 40)
   
        
    water_color = cv2.cvtColor(water_color, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(water_color)
    edited_image = im_pil
    
    width, height = im_pil.size
   
    if width > height:
        im_pil = im_pil.resize((550, 450), Image.ANTIALIAS) 
    elif width < height:
        im_pil = im_pil.resize((450, 550), Image.ANTIALIAS) 
    else:
        im_pil = im_pil.resize((500, 500), Image.ANTIALIAS) 
    
    photo = ImageTk.PhotoImage(im_pil) 
    img_canvas.image = photo
    img_canvas.itemconfig(blank_image_init,image = "")
    
    if width > height:
        img_canvas.create_image(310,120, image = photo, anchor = N)
    else:
         img_canvas.create_image(310,70, image = photo, anchor = N)
    

# Function for creating cartoon effect
def cartoon():
    
  
    global imgs
    global edited_image

    img = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
   
        

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3) 
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 11)
    img = cv2.bilateralFilter(img, 6, 64, 64)
    dst = cv2.edgePreservingFilter(img, flags=2, sigma_s= 150, sigma_r=0.5) 
    cartoon = cv2.bitwise_and(dst, dst, mask=edges) 
        
    
    cartoon = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(cartoon)
    
    edited_image = im_pil
    
    width, height = im_pil.size
   
    if width > height:
        im_pil = im_pil.resize((550, 450), Image.ANTIALIAS) 
    elif width < height:
        im_pil = im_pil.resize((450, 550), Image.ANTIALIAS) 
    else:
        im_pil = im_pil.resize((500, 500), Image.ANTIALIAS) 
    
    photo = ImageTk.PhotoImage(im_pil) 
    img_canvas.image = photo
    img_canvas.itemconfig(blank_image_init,image = "")
    
    if width > height:
        img_canvas.create_image(310,120, image = photo, anchor = N)
    else:
         img_canvas.create_image(310,70, image = photo, anchor = N)
        
    


def enable_button():
    
    brightness_btn.config(state = NORMAL)
    Intensity_btn.config(state = NORMAL)
    summer_btn.config(state = NORMAL)
    winter_btn.config(state = NORMAL)
    cartooning_btn.config(state = NORMAL)
    oilpainter_btn.config(state = NORMAL)
    WaterColor_btn.config(state = NORMAL)
    Pencil_btn.config(state = NORMAL)
    
    
def scale(e):
    
    scale_handler()
    
    if e == 1: 
        slider.config(from_ = -100, to = 100,command = adjust_brightness)
        slider.place(x = 330, y =300)
        slider_label.config(text = "Brightness Adjuster")
        slider_label.place(x = 330, y = 275)
       
    if e == 2: 
        slider.config(from_ = -100, to = 100, length = 300,command = adjust_intensity)
        slider.place(x = 330, y = 300)
        slider_label.config(text = "Intensity Adjuster")
        slider_label.place(x = 330, y = 275)
 
    if e == 3: 
        slider.config(from_ = 0, to = 100,command = summer_effect)
        slider.place(x = 330, y =300)
        slider_label.config(text = "Summer Effect")
        slider_label.place(x = 330, y = 275)
    
    if e == 4: 
        slider.config(from_ = 0, to = 100, command = winter_effect)
        slider.place(x = 330, y =300)
        slider_label.config(text = "Winter Effect")
        slider_label.place(x = 330, y = 275)
    
      


# Function for open the image from local drive
def open_image():
    
    global imgs
    global edited_image
 
    path = filedialog.askopenfilename()
    
    if path:
        
        image = Image.open(path)
    else:
        return
    
    cv2_img = np.array(image)
    cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_RGB2BGR)
    
    height,width,_ = cv2_img.shape
   
   
    if height > 1000 and width > 1000:
        
        if height > width:
         
            cv2_img = cv2.resize(cv2_img, (1000 , 1200))
            
        elif height < width:
            cv2_img = cv2.resize(cv2_img, (1200 , 1000))
          
        else:
            cv2_img = cv2.resize(cv2_img, (1000 , 1000))
 
    
    width, height = image.size
   
    if width > height:
        image = image.resize((550, 450), Image.ANTIALIAS) 
    elif width < height:
        image = image.resize((450, 550), Image.ANTIALIAS) 
    else:
        image = image.resize((500, 500), Image.ANTIALIAS) 
    
    photo = ImageTk.PhotoImage(image) 
    img_canvas.image = photo
    img_canvas.itemconfig(blank_image_init,image = "")
    
    if width > height:
        img_canvas.create_image(310,120, image = photo, anchor = N)
    else:
         img_canvas.create_image(310,70, image = photo, anchor = N)

    
    imgs = cv2_img
    
    edited_image = 0
    enable_button()
    scale_handler()
    
    show_imgs = Image.open("logo/show_img.png")
    resized_show_imgs = show_imgs.resize((298,40),Image.ANTIALIAS)
    show_imgs = ImageTk.PhotoImage(resized_show_imgs) 
    
    original_img_button = Button(editor,image = show_imgs, bg = "#7FDBFF", relief= RAISED, borderwidth = 4, command = show_original_img)
    original_img_button.image = show_imgs
    original_img_button.place(x = 330, y = 560)
    #original_img_button
    

def update_img_canvas():
    global imgs
    
    im_pil = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(im_pil)
    
    edited_image = im_pil
    
    width, height = im_pil.size
       
    if width > height:
        im_pil = im_pil.resize((550, 450), Image.ANTIALIAS) 
    elif width < height:
        im_pil = im_pil.resize((450, 550), Image.ANTIALIAS) 
    else:
        im_pil = im_pil.resize((500, 500), Image.ANTIALIAS) 
    
    photo = ImageTk.PhotoImage(im_pil) 
    img_canvas.image = photo
    img_canvas.itemconfig(blank_image_init,image = "")
    
    if width > height:
        img_canvas.create_image(310,120, image = photo, anchor = N)
    else:
         img_canvas.create_image(310,70, image = photo, anchor = N)
     
  
def show_original_img():
    
    global imgs
    global photo
    img = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)

    orginal = Image.fromarray(img)
    
    width, height = orginal.size
   
    if width > height:
        im_pil = orginal.resize((550, 450), Image.ANTIALIAS) 
    elif width < height:
        im_pil = orginal.resize((450, 550), Image.ANTIALIAS) 
    else:
        im_pil = orginal.resize((500, 500), Image.ANTIALIAS) 
    
    
 
    photo = ImageTk.PhotoImage(im_pil) 
    
    second_window = Toplevel()
    second_window.title("Original Image")
    window_icon = PhotoImage(file = "logo/camera.png")
    second_window.iconphoto(False, window_icon)
    second_window.resizable(width = False, height = False) 
    second_window.configure(background= '#7FDBFF', borderwidth = 6,relief="raised")
    
    
    org_logo_image = Image.open("logo/org_img_logo.png")
    resized_blank_image  = org_logo_image.resize((590,45),Image.ANTIALIAS)
    org_logo_image = ImageTk.PhotoImage(resized_blank_image) 
    org_img_label = Label(second_window, image = org_logo_image,borderwidth = 5, relief="groove")
    org_img_label.pack(pady = 10,padx = 10)
    
    img_label = Label(second_window, image = photo)
    img_label.pack(pady = 10)
    second_window.mainloop()
    
    
def scale_handler():
    
    global slider
    global slider_label
    slider.destroy()
    slider = Scale(editor,length = 300,font =('Merkin',13,'bold'),fg = '#39569e', bg = "#7FDBFF",relief = "raised", borderwidth = 4,resolution = 1, orient = HORIZONTAL)
    slider_label.destroy()
    slider_label = Label(editor,borderwidth = 4, width = 30, relief="raised",bg = "#7FDBFF", font =('Merkin',13,'bold',"italic"),fg = '#39569e')
    slider.focus_set()                            
    
# Function for save edited image in local drive  
def save_image():
    
    global edited_image
    if edited_image == 0:
        messagebox.showerror("Error", " No Edited Image Found!")
    
    else:
        
        filename = filedialog.asksaveasfile(mode='wb', defaultextension=".png", filetypes=(("PNG file", "*.png"),("JPG file", "*.jpg"),("JPEG file", "*.jpeg"),("All Files", "*.*") ))
        if filename:
           edited_image.save(filename)
        else:
            return

 
#--------------------------------- GUI PART--------------------------------------------------------



    

# Main Window

editor = Tk()
editor.title("Image Editor")
editor.geometry("1300x740")
editor.configure(background= '#7FDBFF', borderwidth = 6,relief="raised")
editor.resizable(width = False, height = False) 

window_icon = PhotoImage(file = "logo/camera.png")
editor.iconphoto(False, window_icon)

# Heading logo

heading_logo  = Image.open("logo/logo.png")
resized_logo  = heading_logo.resize((522,94),Image.ANTIALIAS)
logo = ImageTk.PhotoImage(resized_logo) 
heading = Label(editor, image = logo, borderwidth = 8, relief="ridge")
heading.place(x = 20, y = 10)


# Style Filters Canvas 

style_frame = Canvas(editor, relief=GROOVE, borderwidth= 8, height = 250, width = 280, bg = "#7FDBFF").place(x = 20, y = 170)

# Style filters label  and logo
style_logo  = Image.open("logo/style.png")
resized_style_logo = style_logo.resize((280,40),Image.ANTIALIAS)
style_logo = ImageTk.PhotoImage(resized_style_logo)
style_label = Label(style_frame, borderwidth = 4, relief="groove", image = style_logo).place(x = 24, y = 175)



# Style filters button
brightness_btn = Button(style_frame,state = DISABLED,relief= RAISED,command = lambda:[update_img_canvas(),scale(1)], width = 20,borderwidth = 4,text = "Brightness Adjuster",font =('MERKIN',12,'bold'),fg = '#39569e',bg = "#7FDBFF")
brightness_btn.place(x = 60, y = 250)
Intensity_btn = Button(style_frame,state = DISABLED,relief= RAISED,command = lambda:[update_img_canvas(),scale(2)],width = 20,borderwidth = 4, text = "Intensity Adjuster",font =('MERKIN',12,'bold'),fg = '#39569e',bg = "#7FDBFF")
Intensity_btn.place(x = 60, y = 295)
summer_btn = Button(style_frame,state = DISABLED,relief= RAISED,command = lambda:[update_img_canvas(),scale(3)],width = 20,borderwidth = 4, text = "Summer Effect",font =('MERKIN',12,'bold'),fg = '#39569e',bg = "#7FDBFF")
summer_btn.place(x = 60, y = 340)
winter_btn = Button(style_frame, state = DISABLED,relief= RAISED,command = lambda:[update_img_canvas(),scale(4)],width = 20,borderwidth = 4,text = "Winter Effect",font =('MERKIN',12,'bold'),fg = '#39569e',bg = "#7FDBFF")
winter_btn.place(x = 60, y = 385)


# Fun Filters Canvas
fun_frame = Canvas(editor, relief=GROOVE, borderwidth= 8, height = 250, width = 280, bg = "#7FDBFF").place(x = 20, y = 450)


# Fun filters label and logo
fun_logo  = Image.open("logo/fun.png")
resized_fun_logo  = fun_logo.resize((280,40),Image.ANTIALIAS)
fun_logo = ImageTk.PhotoImage(resized_fun_logo) 
fun_label = Label(style_frame, borderwidth = 4, relief="groove", image = fun_logo).place(x = 24, y = 455)

# Fun filters Button
cartooning_btn = Button(style_frame,relief= RAISED,state = DISABLED,command =lambda:[scale_handler(),cartoon()] , width = 20, borderwidth = 4,text = "Cartoon Effect", font =('MERKIN',12,'bold'),fg = '#39569e',bg = "#7FDBFF")
cartooning_btn.place(x = 60, y = 525)
oilpainter_btn = Button(style_frame,state = DISABLED,relief= RAISED,command = lambda:[scale_handler(),oil_paint()],width = 20,borderwidth = 4, text = "Oil Painter Effect",font =('MERKIN',12,'bold'),fg = '#39569e',bg = "#7FDBFF")
oilpainter_btn.place(x = 60, y = 570)
WaterColor_btn = Button(style_frame,state = DISABLED,relief= RAISED,command = lambda:[scale_handler(),water_color()], width = 20, borderwidth = 4,text = "WaterColor Effect",font =('MERKIN',12,'bold'),fg = '#39569e',bg = "#7FDBFF")
WaterColor_btn.place(x = 60, y = 615)
Pencil_btn = Button(style_frame,state = DISABLED,relief= RAISED,command =  lambda:[scale_handler(),pencil_sketch()],width = 20,borderwidth = 4, text = "Pencil Sketch",font =('MERKIN',12,'bold'),fg = '#39569e',bg = "#7FDBFF")
Pencil_btn.place(x = 60, y = 660)
 

# Image Canvas

img_canvas =  Canvas(editor, height = 620, width =600, bg = "#7FDBFF", relief=GROOVE , borderwidth= 8)
img_canvas.place(x = 650, y = 10)

# image box logo
img_box_logo  = Image.open("logo/img_box.png")
resized_img_box_logo  = img_box_logo.resize((600,45),Image.ANTIALIAS)
img_box_logo = ImageTk.PhotoImage(resized_img_box_logo) 
imgbox_label = Label(img_canvas, borderwidth = 5,relief="groove", image = img_box_logo)
imgbox_label.place(x = 5, y = 5)

#Image box image
blank_image = Image.open("logo/blank.png")
resized_blank_image  = blank_image.resize((500,400),Image.ANTIALIAS)
blank_image = ImageTk.PhotoImage(resized_blank_image) 

blank_image_init = img_canvas.create_image(310,140, image = blank_image, anchor = N)


# Upload Button and logo

upload_logo  = Image.open("logo/upload.png")
resized_upload_logo  = upload_logo.resize((50,50),Image.ANTIALIAS)
upload_logo = ImageTk.PhotoImage(resized_upload_logo) 
open_image_btn = Button(editor, image = upload_logo, command = open_image,borderwidth = 0,bg = "#7FDBFF", relief=RAISED)
open_image_btn.place(x = 850, y = 664)


# Download Button and logo

download_logo  = Image.open("logo/download.png")
resized_download_logo  = download_logo.resize((50,50),Image.ANTIALIAS)
download_logo = ImageTk.PhotoImage(resized_download_logo) 
download_image_btn = Button(editor, state = NORMAL,borderwidth= 0,image = download_logo, bg = "#7FDBFF", relief=RAISED, command = save_image)
download_image_btn.place(x = 1050, y = 664)


# Label of Slider
slider = Scale(editor)
slider_label = Label(editor, borderwidth = 4, width = 30, relief="ridge",bg = "light green", font =('Times',13,'bold'),fg = 'green')
 

editor.mainloop()