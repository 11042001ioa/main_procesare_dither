import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

GREYSCALE = True
ANTIALIAS = True
img_name = 'clinton.jpg'
# Read in the image, convert to greyscale.
img = Image.open(img_name)
if GREYSCALE:
    img = img.convert('L')

width, height = img.size

new_width = width
new_height = height
#new_width = 1280
#new_height = int(height * new_width / width)
#img = img.resize((new_width, new_height),ANTIALIAS)

def get_new_val(old_val, nc):
    """
    Get the "closest" colour to old_val in the range [0,1] per channel divided
    into nc values.

    """
    #return np.round(old_val)
    return np.round(old_val * (nc-1)) / (nc-1)

# For RGB images, the following might give better colour-matching.
#p = np.linspace(0, 1, nc)
#p = np.array(list(product(p,p,p)))
#def get_new_val(old_val):
#    idx = np.argmin(np.sum((old_val[None,:] - p)**2, axis=1))
#    return p[idx]
def newspaper(img):

    arr = np.array(img, dtype=float) / 255
    for ir in range(int(new_height/2)):
        for ic in range(int(new_width/2)):
            avg = arr[2*ir,2*ic]+arr[2*ir+1,2*ic]+arr[2*ir,2*ic+1]+arr[2*ir+1,2*ic+1]
            avg = avg/4
            if avg <0.2:
                arr[2*ir,2*ic]=0
                arr[2*ir+1,2*ic]=0
                arr[2*ir,2*ic+1]=0
                arr[2*ir+1,2*ic+1]=0
            else:
                if avg <0.4:
                    arr[2*ir,2*ic]=0
                    arr[2*ir+1,2*ic]=1
                    arr[2*ir,2*ic+1]=0
                    arr[2*ir+1,2*ic+1]=0
                else:
                    if avg <0.6:
                        arr[2*ir,2*ic]=0
                        arr[2*ir+1,2*ic]=1
                        arr[2*ir,2*ic+1]=1
                        arr[2*ir+1,2*ic+1]=0
                    else:
                        if avg <0.8:
                            arr[2*ir,2*ic]=0
                            arr[2*ir+1,2*ic]=1
                            arr[2*ir,2*ic+1]=1
                            arr[2*ir+1,2*ic+1]=1
                        else:
                            arr[2*ir,2*ic]=1
                            arr[2*ir+1,2*ic]=1
                            arr[2*ir,2*ic+1]=1
                            arr[2*ir+1,2*ic+1]=1

    carr = np.array(arr/np.max(arr, axis=(0,1))*255 , dtype=np.uint8)
    return Image.fromarray(carr)
def newspaper3(img):

    arr = np.array(img, dtype=float) / 255
    for ir in range(int(new_height/3)):
        for ic in range(int(new_width/3)):
            avg = 0
            for i in range(3):
                for j in range(3):
                    avg = avg+arr[3*ir+i,3*ic+j]
            avg = avg/9
            if avg <0.1:
                arr[3*ir,3*ic]=0
                arr[3*ir,3*ic+1]=0
                arr[3*ir,3*ic+2]=0
                arr[3*ir+1,3*ic]=0
                arr[3*ir+1,3*ic+1]=0
                arr[3*ir+1,3*ic+2]=0
                arr[3*ir+2,3*ic]=0
                arr[3*ir+2,3*ic+1]=0
                arr[3*ir+2,3*ic+2]=0
            else:
                if avg <0.2:
                    arr[3*ir,3*ic]=0
                    arr[3*ir,3*ic+1]=0
                    arr[3*ir,3*ic+2]=0
                    arr[3*ir+1,3*ic]=0
                    arr[3*ir+1,3*ic+1]=1
                    arr[3*ir+1,3*ic+2]=0
                    arr[3*ir+2,3*ic]=0
                    arr[3*ir+2,3*ic+1]=0
                    arr[3*ir+2,3*ic+2]=0
                else:
                    if avg <0.3:
                        arr[3*ir,3*ic]=0
                        arr[3*ir,3*ic+1]=0
                        arr[3*ir,3*ic+2]=0
                        arr[3*ir+1,3*ic]=0
                        arr[3*ir+1,3*ic+1]=1
                        arr[3*ir+1,3*ic+2]=1
                        arr[3*ir+2,3*ic]=0
                        arr[3*ir+2,3*ic+1]=0
                        arr[3*ir+2,3*ic+2]=0
                    else:
                        if avg <0.4:
                            arr[3*ir,3*ic]=0
                            arr[3*ir,3*ic+1]=1
                            arr[3*ir,3*ic+2]=0
                            arr[3*ir+1,3*ic]=0
                            arr[3*ir+1,3*ic+1]=1
                            arr[3*ir+1,3*ic+2]=1
                            arr[3*ir+2,3*ic]=0
                            arr[3*ir+2,3*ic+1]=0
                            arr[3*ir+2,3*ic+2]=0
                        else:
                            if avg<0.5:
                                arr[3*ir,3*ic]=0
                                arr[3*ir,3*ic+1]=1
                                arr[3*ir,3*ic+2]=0
                                arr[3*ir+1,3*ic]=0
                                arr[3*ir+1,3*ic+1]=1
                                arr[3*ir+1,3*ic+2]=1
                                arr[3*ir+2,3*ic]=1
                                arr[3*ir+2,3*ic+1]=0
                                arr[3*ir+2,3*ic+2]=0
                            else:
                                if avg<0.6:
                                    arr[3*ir,3*ic]=0
                                    arr[3*ir,3*ic+1]=1
                                    arr[3*ir,3*ic+2]=0
                                    arr[3*ir+1,3*ic]=1
                                    arr[3*ir+1,3*ic+1]=1
                                    arr[3*ir+1,3*ic+2]=1
                                    arr[3*ir+2,3*ic]=1
                                    arr[3*ir+2,3*ic+1]=0
                                    arr[3*ir+2,3*ic+2]=0
                                else:
                                    if avg<0.7:
                                        arr[3*ir,3*ic]=0
                                        arr[3*ir,3*ic+1]=1
                                        arr[3*ir,3*ic+2]=0
                                        arr[3*ir+1,3*ic]=1
                                        arr[3*ir+1,3*ic+1]=1
                                        arr[3*ir+1,3*ic+2]=1
                                        arr[3*ir+2,3*ic]=1
                                        arr[3*ir+2,3*ic+1]=0
                                        arr[3*ir+2,3*ic+2]=1
                                    else:
                                        if avg<0.8:
                                            arr[3*ir,3*ic]=0
                                            arr[3*ir,3*ic+1]=1
                                            arr[3*ir,3*ic+2]=1
                                            arr[3*ir+1,3*ic]=1
                                            arr[3*ir+1,3*ic+1]=1
                                            arr[3*ir+1,3*ic+2]=1
                                            arr[3*ir+2,3*ic]=1
                                            arr[3*ir+2,3*ic+1]=0
                                            arr[3*ir+2,3*ic+2]=1
                                        else:
                                            if avg<0.9:
                                                arr[3*ir,3*ic]=1
                                                arr[3*ir,3*ic+1]=1
                                                arr[3*ir,3*ic+2]=1
                                                arr[3*ir+1,3*ic]=1
                                                arr[3*ir+1,3*ic+1]=1
                                                arr[3*ir+1,3*ic+2]=1
                                                arr[3*ir+2,3*ic]=1
                                                arr[3*ir+2,3*ic+1]=0
                                                arr[3*ir+2,3*ic+2]=1
                                            else:
                                                arr[3*ir,3*ic]=1
                                                arr[3*ir,3*ic+1]=1
                                                arr[3*ir,3*ic+2]=1
                                                arr[3*ir+1,3*ic]=1
                                                arr[3*ir+1,3*ic+1]=1
                                                arr[3*ir+1,3*ic+2]=1
                                                arr[3*ir+2,3*ic]=1
                                                arr[3*ir+2,3*ic+1]=1
                                                arr[3*ir+2,3*ic+2]=1

    carr = np.array(arr/np.max(arr, axis=(0,1))*255 , dtype=np.uint8)
    return Image.fromarray(carr)

def newspaperht2(img):

    arr = np.array(img, dtype=float) / 255
    for ir in range(int(new_height/8)):
        for ic in range(int(new_width/8)):
            avg = 0
            for j in range (8):
                for i in range (8):
                    avg = avg + arr[8*ir+i,8*ic+j]
            avg = avg/64
            if avg<0.111:
                for i in range(8):
                    for j in range(8):
                        arr[8*ir+i, 8*ic+j] = 0
            else:
                if avg<0.222:
                    for i in range(8):
                        for j in range(8):
                            arr[8*ir+i, 8*ic+j] = 0
                    arr[8*ir+4, 8*ic+4] = 1
                else:
                    if avg<0.333:
                        for i in range(8):
                            for j in range(8):
                                arr[8*ir+i, 8*ic+j] = 0
                        arr[8*ir+4, 8*ic+4] = 1
                        arr[8*ir+3, 8*ic+3] = 1
                        arr[8*ir+4, 8*ic+3] = 1
                        arr[8*ir+3, 8*ic+4] = 1
                    else:
                        if avg<0.444:
                            for i in range(8):
                                for j in range(8):
                                    arr[8*ir+i, 8*ic+j] = 0
                            for k in range(3):
                                for l in range(3):
                                    arr[8*ir+3+k, 8*ic+3+l] = 1
                        else:
                            if avg<0.555:
                                for i in range(8):
                                    for j in range(8):
                                        arr[8*ir+i, 8*ic+j] = 0
                                for k in range(4):
                                    for l in range(4):
                                        arr[8*ir+2+k, 8*ic+2+l] = 1
                            else:
                                if avg<0.666:
                                    for i in range(8):
                                        for j in range(8):
                                            arr[8*ir+i, 8*ic+j] = 0
                                    for k in range(5):
                                        for l in range(5):
                                            arr[8*ir+1+k, 8*ic+1+l] = 1
                                else:
                                    if avg<0.777:
                                        for i in range(8):
                                            for j in range(8):
                                                arr[8*ir+i, 8*ic+j] = 0
                                        for k in range(6):
                                            for l in range(6):
                                                arr[8*ir+1+k, 8*ic+1+l] = 1
                                    else:
                                        if avg<0.888:
                                            for i in range(8):
                                                for j in range(8):
                                                    arr[8*ir+i, 8*ic+j] = 0
                                            for k in range(7):
                                                for l in range(7):
                                                    arr[8*ir+1+k, 8*ic+1+l] = 1
                                        else:

                                            for i in range(8):
                                                for j in range(8):
                                                    arr[8*ir+i, 8*ic+j] = 1


    carr = np.array(arr/np.max(arr, axis=(0,1))*255 , dtype=np.uint8)
    return Image.fromarray(carr)

def newspaperht6(img):

    arr = np.array(img, dtype=float) / 255
    for ir in range(int(new_height/6)):
        for ic in range(int(new_width/6)):
            avg = 0
            for j in range (6):
                for i in range (6):
                    avg = avg + arr[6*ir+i,6*ic+j]
            avg = avg/36
            if avg<0.166:
                for i in range(6):
                    for j in range(6):
                        arr[6*ir+i, 6*ic+j] = 0
            else:
                if avg<0.333:
                    for i in range(6):
                        for j in range(6):
                            arr[6*ir+i, 6*ic+j] = 0
                    arr[6*ir+3, 6*ic+3] = 1
                else:
                    if avg<0.5:
                        for i in range(6):
                            for j in range(6):
                                arr[6*ir+i, 6*ic+j] = 0
                        arr[6*ir+4, 6*ic+4] = 1
                        arr[6*ir+3, 6*ic+3] = 1
                        arr[6*ir+4, 6*ic+3] = 1
                        arr[6*ir+3, 6*ic+4] = 1
                    else:
                        if avg<0.666:
                            for i in range(6):
                                for j in range(6):
                                    arr[6*ir+i, 6*ic+j] = 0
                            for k in range(3):
                                for l in range(3):
                                    arr[6*ir+2+k, 6*ic+2+l] = 1
                        else:
                            if avg<0.832:
                                for i in range(6):
                                    for j in range(6):
                                        arr[6*ir+i, 6*ic+j] = 0
                                for k in range(4):
                                    for l in range(4):
                                        arr[6*ir+1+k, 6*ic+1+l] = 1
                            else:

                                for i in range(6):
                                    for j in range(6):
                                        arr[6*ir+i, 6*ic+j] = 1



    carr = np.array(arr/np.max(arr, axis=(0,1))*255 , dtype=np.uint8)
    return Image.fromarray(carr)

def fs_dither(img, nc):
    """
    Floyd-Steinberg dither the image img into a palette with nc colours per
    channel.

    """
    arr = np.array(img, dtype=float) / 255
    #print(arr)
    for ir in range(new_height):
        for ic in range(new_width):
            # NB need to copy here for RGB arrays otherwise err will be (0,0,0)!
            old_val = arr[ir, ic].copy()
            new_val = get_new_val(old_val, nc)
            arr[ir, ic] = new_val
            err = old_val - new_val
            # In this simple example, we will just ignore the border pixels.
            if ic < new_width - 1:
                arr[ir, ic+1] += err * 7/16
            if ir < new_height - 1:
                if ic > 0:
                    arr[ir+1, ic-1] += err * 3/16
                arr[ir+1, ic] += err * 5/16
                if ic < new_width - 1:
                    arr[ir+1, ic+1] += err / 16

    carr = np.array(arr/np.max(arr, axis=(0,1))*255 , dtype=np.uint8)
    #print(arr)
    return Image.fromarray(carr)


def process_images():
    try:
        image1 = Image.open(img_name)

        img_dither = entry1.get()
        img_bits = entry2.get()

        dim = fs_dither(img, int(img_bits)+1)

        if img_dither == "2x2":
            dim = newspaper(dim)
        if img_dither == "hd3x3":
            dim = newspaper3(dim)
        if img_dither == "6x6":
            dim = newspaperht6(dim)
        if img_dither == "8x8":
            dim = newspaperht2(dim)
        dim.save('dim-{}.jpg'.format(img_bits))
        image2 = Image.open('dim-{}.jpg'.format(img_bits))

        # Open and process images

        #image2 = Image.open(img_path2)

        # Resize images to fit in the window (adjust size as needed)
        if height>500:
            h = 400
            w = int(width * h / height)
            image1 = image1.resize((w,h))
            image2 = image2.resize((w,h))

        # Convert images to Tkinter PhotoImage objects
        photo1 = ImageTk.PhotoImage(image1)
        photo2 = ImageTk.PhotoImage(image2)

        # Update output labels with the processed images
        label_output1.config(image=photo1)
        label_output1.image = photo1  # Keep a reference
        label_output2.config(image=photo2)
        label_output2.image = photo2  # Keep a reference

    except Exception as e:
        # Display error if an exception occurs
        print("Error:", e)

# Create the main window
root = tk.Tk()
root.title("Image Processing")

# Input fields
label1 = tk.Label(root, text="size of dither block:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="2^x bits sampling:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

# Button to process images
process_button = tk.Button(root, text="Process Images", command=process_images)
process_button.pack()

# Output images
label_output1 = tk.Label(root)
label_output1.pack()

label_output2 = tk.Label(root)
label_output2.pack()

root.mainloop()


#for nc in (2,3,4):
 #   print('nc =', nc)
  #  dim = fs_dither(img, nc)
   # dim = newspaperht2(dim)
    #dim.save('dim-{}.jpg'.format(nc))



# de adaugat parcurgere asemanatoare cu floyd warshal cu aproximare pt mini matrici de 3x3
