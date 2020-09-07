"""
Solution to WEEKLY CODE BATTLE - WEEK 14.

NOTE: This 'app.py' file, contains the following-
        1] Solution:- To the WEEKLY CODE BATTLE:- WEEK 14, A Water Mark on Image.
        and has few OS dependent feature w.r.t FONT FAMILY [ i.e, 'VeraSe.ttf' is FONT FAMILY type (for my system- MANJARO) ]
        2] Code & Explaination:- to the written code, line-by-line as comments.
        3] Example Output

1] Solution-
    a] We have made use of 'pillow' a Imaging Library for Python.
       Command to install this, 
            pip install pillow
    b] We are getting the SOURCE image from the SYSTEM Arguments from user.
    c] User, while executing the script at position sys.arg[1], he'll pass
    with its extension.
    d] We have maintained few Dictionaries and Tuple for our ease of writting script
    e] The dictionaries are,
        e1] "pos_dict" Diictionary for different region/co-ordinates on the image
        e2] "water_mark" Diictionary for RELEASE | Don't RELEASE Hostage
    f] We have a Tuple 'EXTENSION', which holds the file extension types for image.
    (Currently we have 2 types, '.jpg' and '.png')
    g] User just have to follow the menu driven CONSOLE,
    to get the WATERMARK on the source image & now the file name
    of the Image will be 'after_watermark_images.jpg' | 'after_watermark_images.png'

2] Code & Explaination-
"""

#importing sys module for ARGUMENT Parsing
import sys
#from PIL package (pillow) importing Image, ImageDraw, ImageFont
from PIL import Image, ImageDraw, ImageFont


def main():
    """
    It'll process the SYSTEM Arguments, selected the from console.

    it accepts 1 dependant SYSTEM Argument from console
    :images.jpg - this is the source image file with EXTENSION (i.e, .jpg | .png)   
    
    Embedding inside the try-catch block
    """  
    try:
        if len(sys.argv) == 0:
            print("""Example , you have to run the script by providing
            python app.py \'input_image \'""")
            sys.exit()
        else:
            filename = sys.argv[1]
        #We are maintaining a Diictionary "pos_dict" for different region/co-ordinates on the image
        pos_dict = {'1': 'topleft', '2':'topright', '3':'bottomleft', '4': 'bottomright', '5':'center', '6':'topcenter'}

        user_pos = input("""\nSelect the respective position no. from the below,
[ Example: If your water mark should appear at 'AtCenter' of Image
    Select number 5, from the list]\n
    1] TopLeft
    2] TopRight
    3] BottomLeft
    4] BottomRight
    5] AtCenter
    6] TopCenter\n""")

        #If user select's other No. from the console
        #we are displaying proper message to user
        #So that he can rectifiy
        if user_pos not in pos_dict:
            print("Sorry! It was a wrong choice.\nPlease select the proper 'position no.' from menu")
            exit()
        else:
            pos = pos_dict[user_pos]
            uwater_mark = input("""\nSelect the respective water mark no. from the below
    1] Release!
    2] Don't Release!\n""")
            #We are maintaining a Diictionary "water_mark"
            water_mark = {'1':'Release, Hostage! (c) 2020 LetsUpgrade','2':"Don't Release, Hostage! (c) 2020 LetsUpgrade"}
            #If user select's other No. from the console
            #we are displaying proper message to user
            #So that he can rectifiy    
            if uwater_mark not in water_mark:
                print("Sorry! It was a wrong choice.\nPlease select the proper 'water mark no.' from menu")
                exit()            
            else: 
                water_text = water_mark[uwater_mark]
                #Calling the 'add_watermark()' and passing necessary dependant Arguments
                add_watermark(water_text, pos, filename)

    except Exception as e:
        print(e)


def add_watermark(water_text, pos, filename):
    """
    It'll add a text watermark to the selected image from console.
    
    it accepts the 3 dependant Arguments-
    :water_text - the text that'll be displayed on the image
    :pos - the region on the image which above water_text will be displayed
    :filename - the source file on which all the operation'll takes place

    Embedding inside the try-catch block
    """  
    try:
        #Tuple 'EXTENSION', which holds the file extension types for image.
        #Currently we have 2 types, '.jpg' and '.png')
        EXTENSION = ('.jpg', '.png')

        if any([filename.lower().endswith(ext) for ext in EXTENSION]):
            image = Image.open(filename)
            #Getting the width & height of the Image
            imageWidth = image.width
            imageHeight = image.height
        #NOTE: 'VeraSe.ttf' is FONT FAMILY type (for my system- MANJARO)
        # FONT FAMILY type is DEPENDANT of OS or SYSTEM,
        # on which this SCRIPT will run
        # at the end the WaterMark's FONT'll appear 
        # with the mentioned Font Properties          
            font = ImageFont.truetype("VeraSe.ttf", 20)
            draw = ImageDraw.Draw(image)        
            textWidth, textHeight = draw.textsize(water_text, font=font)
            #RGBA colour distribution
            # here we are initializing a 'color' Tuple represents 
            # [ R - 255, G -255, B -255 ] => 'white' & A - 255

            color = (255, 255, 255, 255)

            #If user has selected the right 'pos' no. from the menu
            #one of the If condition will execute

            if pos == 'topleft':                
                draw.text((0,0), water_text, fill=color, font=font)
                
            elif pos == 'topright':
                draw.text(((imageWidth - textWidth), 0), water_text, fill=color, font=font)

            elif pos == 'topcenter':
                draw.text(((imageWidth - textWidth)/2, 0), water_text, fill=color, font=font)

            elif pos == 'bottomleft':
                draw.text((0, imageHeight - textHeight), water_text, fill=color, font=font)

            elif pos == 'bottomright':
                draw.text((imageWidth - textWidth, imageHeight - textHeight), water_text, fill=color, font=font)

            elif pos == 'center':
                draw.text(((imageWidth - textWidth)/2, (imageHeight - textHeight)/2), water_text, fill=color, font=font)
            
            #At last, we save the changes made to the image file
            image.save('after_watermark_' + filename)
            print("Watermark addition was Successful!\nIn current folder you can find the image with file name '{}'".format('after_watermark_' + filename))
        else:
            print("Please provide the proper source file Image\n with extension '.jpg' or '.png'.")
    #If any unexpected may error occur
    #these exceptions will handle
    #and will notifiy the user respectively
    except Exception as e:
        print(e)

#Program Execution starts from here
if __name__ == "__main__":
    main()

"""
3] Example Output -

At Console run the following command,

python app.py images.jpg

Select the respective position no. from the below,
[ Example: If your water mark should appear at 'AtCenter' of Image
    Select number 5, from the list]

    1] TopLeft
    2] TopRight
    3] BottomLeft
    4] BottomRight
    5] AtCenter
    6] TopCenter
6

Select the respective water mark no. from the below
    1] Release!
    2] Don't Release!
1

Watermark addition was Successful!
In current folder you can find the image with file name 'after_watermark_images.jpg'.

"""