# Usage
Each element in Figma has a name, whether its text or a simple rectangle. This program creates all elements solely based on names. It cannot define a name on its own, due to which it’s important to follow the naming system. You can find all element names over here:

![Image](https://github.com/saksham-lussqvx/images/blob/master/img_fig_names.png)

## Naming System
This is how each element should be named

1. Text - To create text type element you have to write Text_ + corresponding number such as = Text_1, Text_2, etc. Also, in the text, if the background has non-white color then you need to draw a small rectangle which you can embed into the background and name it as - Text_color_ + corresponding text element number such as = Text_color_1, Text_color_2, etc.

2. Rectangles/Frames - To create a rectangle-type element you have to write Frame (Only one color should be used as the background color).

3. Button - To create a button type element you have to write Button_+ type of button + _ + corresponding number such as = Button_R_1 (for rounded type button) or Button_NR_1 (for non-rounded type button) (only two are supported for now), also you need to write Button Text too which should be written in the format - B_ + corresponding button number such as B_1, B_2, etc. Here the text number should be same as the number of buttons to which you want to bind it.

4. Picture - To create picture type element you have to write Picture if your picture doesn't have any rounded corners or is without a background, else you need to write it as Picture_ + corresponding number such as = Picture_1 and its background should be a rectangle whose color is what the color of your background it and it should be named as Picture_bg_ + the corresponding number such as = Picture_bg_1.

5. Background - To create a background type element you have to write Background. If you're planning to use a gradient color-based background then it’s best to choose this type and not Frame.

6. Entrybox - To create entrybox type element you have to write Entrybox, and if you want to add pre-loaded text in it then you can do it by writing Entrybox_ + corresponding number such as = Entrybox_1 and to add text = Entrybox_text_1.

7. Line - To create a line type element you have to write Line. For now, only straight lines are supporting, you cannot use lines other than at the angle of 90/-90 degrees.

8. Menubox - To create a Menubox type element you have to write Menubox_ + corresponding number such as = Menubox_1 and after that, it’s important to create two more elements which are Menubox Text and a Menubox elements List such as = Menubox_1(a rectangle), Menubox_text_1(text type element) and Menubox_list_1 (a list which contains names to add such as element1, element2, etc.).

# Creating each element

## Text
I'll show you two methods to create text, both are although same, just a bit of difference in naming.
1. Texts with the same background-color

Step 1: Give the frame color and then create a small rectangle of name = Text_color_1 and the same color and place it where you'll place your text.

![Image](https://github.com/saksham-lussqvx/images/blob/master/tutorial_2.png)


Step 2: Create a text element and give it the name Text_1

![Image](https://github.com/saksham-lussqvx/images/blob/master/tutorial_3.png)


Step 3: Here now you can use the name rectangle if your background has to be of the same color and the name should be the same as the previous one.

![Image](https://github.com/saksham-lussqvx/images/blob/master/tutorial_4.png)


2. Texts with different background-color

All the steps here are the same, just one key difference is that, according to the name, the colors are used.

![Image](https://github.com/saksham-lussqvx/images/blob/master/tutorial_5.png)


## Frames/Rectangles

Step 1: Create a rectangle with the name Frame and it’s done.

![Image](https://github.com/saksham-lussqvx/images/blob/master/tutorial_6.png)


## Buttons

There are two types of buttons. The first is the Non-rounded button and the second is the rounded button. Remember one thing, your button will be as bigger as your text, its sides may decrease if your text is small and the rectangle is big.

1. ROUNDED BUTTONS

Step 1: Create a rectangle and name it Button_NR_1.

![Image](https://github.com/saksham-lussqvx/images/blob/master/tutorial_7.png)


Step 2: Create a text element and name it B_1.

![Image](https://github.com/saksham-lussqvx/images/blob/master/tutorial_8.png)


2. NON-ROUNDED BUTTONS

Step 1: Create a rectangle, also reduce the corner in corner properties.

![Image](https://github.com/saksham-lussqvx/images/blob/master/tutorial_9.png)


Step 2: Create a text element and don't name it anything(you can also use a picture and fit it inside the button).

![Image](https://github.com/saksham-lussqvx/images/blob/master/tutorial_10.png)


Step 3: Group the text/picture and the button rectangle and rename it whole as Button_R_1

![Image](https://github.com/saksham-lussqvx/images/blob/master/tutorial_11.gif)


## Pictures
Pictures are one of the most used elements when it comes to GUI, as you can make any graphical elements with it and include them. NOTE: do not use this type for the background as a separate function exists for that. Also, one more thing, if your picture has shape other than square and rectangle or it is background-less, then use 2nd type of function or in Tkinter, borders will show white color.

1. Picture without matching background

Step 1: Create a rectangle named Picture (You can also use Figma elements like pictures, such as rounded corner rectangles).

Step 2: Copy the picture from its source and paste it in the rectangle or if the Figma element is used then skip this step.

![Image](https://github.com/saksham-lussqvx/images/blob/master/tutorial_11.png)


2. Picture with matching background

Step 1: Create a rectangle named Picture_bg_1 which will have the color same as the background(or whatever it is displayed upon) and then create another rectangle with the name Picture_1. Remember to create the bg rectangle first or it will overlay onto other elements.

![Image](https://github.com/saksham-lussqvx/images/blob/master/tutorial_12.png)


Step 2: Copy the picture from its source and paste it in the rectangle or if the Figma element is used then skip this step.


## Background
You can create background very easily and you can even have more than 1 background in a single slide. Also, you can create gradient color frames and then use them as background.

Step 1: Create a rectangle and name it Background, then, if it’s a photo, copy-paste it into the rectangle or change its color.

![Image](https://github.com/saksham-lussqvx/images/blob/master/tutorial_13.png)


## Entrybox/Input Field
There are two ways in which an Entrybox can be created. For now, only non-rounded corner entryboxes are supported.

1. Simple Entrybox

Step 1: Create a rectangle and name it Entrybox and it’s done.

![Image](https://github.com/saksham-lussqvx/images/blob/master/tutorial_14.png)


2. Entrybox with text

Step 1: Create a rectangle and name it Entrybox_1, after that create a text type element and name it Entrybox_text_1.

![Image](https://github.com/saksham-lussqvx/images/blob/master/tutorial_15.png)


Step 2: Change the colors of the text or the entrybox and remember to make the entrybox rectangle a bit bigger as when converted, it gets a bit small.


![Image](https://github.com/saksham-lussqvx/images/blob/master/tutorial_16.png)


## Line

Step 1: Create a line element and then rotate it to either -90 degrees or 90 degrees.

![Image](https://github.com/saksham-lussqvx/images/blob/master/tutorial_17.png)

## Menu button
This element is a little more complex to create as it requires three elements.

Step 1: Create a rectangle (its size doesn't matter but its position should be accurate and color too) and name it Menubox_1.

![Image](https://github.com/saksham-lussqvx/images/blob/master/tutorial_18.png)


Step 2: Create a text and name it as Menu_text_1 (this text's font size will decide the size of the menu button so modify it accordingly).

![Image](https://github.com/saksham-lussqvx/images/blob/master/tutorial_19.png)


Step 3: Create another text element and put it anywhere in the frame (best to place under the Menubox) and name it as Menu_list_1 and break down each word or whatever your elements are into lines.

![Image](https://github.com/saksham-lussqvx/images/blob/master/tutorial_20.png)


Step 4: Modification of colors of the list is useless so just modify colors of Menubox and Menubox_text.

![Image](https://github.com/saksham-lussqvx/images/blob/master/tutorial_21.png) ![Image](https://github.com/saksham-lussqvx/images/blob/master/tutorial_22.png)
