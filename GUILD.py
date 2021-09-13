# Made by @Saksham Solanki, Date: 18/06/2021 (DD/MM/YYYY), Time: 22:24 (24-hour-format)
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import ctypes
from tkinter.constants import W

import requests
from PIL import Image, ImageTk


ctypes.windll.shcore.SetProcessDpiAwareness(1)


class gui_properties:
    def get_color(element):
        # Returns HEX form of element RGB color (str)
        el_r = element["fills"][0]["color"]['r'] * 255
        el_g = element["fills"][0]["color"]['g'] * 255
        el_b = element["fills"][0]["color"]['b'] * 255

        return ('#%02x%02x%02x' % (round(el_r), round(el_g), round(el_b)))

    def get_line_color(element):
        # Returns HEX form of element RGB color (str)
        el_r = element["strokes"][0]["color"]['r'] * 255
        el_g = element["strokes"][0]["color"]['g'] * 255
        el_b = element["strokes"][0]["color"]['b'] * 255

        return ('#%02x%02x%02x' % (round(el_r), round(el_g), round(el_b)))

    def get_coordinates(element):
        # Returns element coordinates as x (int) and y (int)
        x = int(element["absoluteBoundingBox"]["x"])
        y = int(element["absoluteBoundingBox"]["y"])
        x = x + (x*25/100)
        y = y + (y*25/100)
        return int(x), int(y)

    def get_dimensions(element):
        # Return element dimensions as width (int) and height (int)
        height = int(element["absoluteBoundingBox"]["height"])
        width = int(element["absoluteBoundingBox"]["width"])
        width = width + (width*25/100)
        height = height + (height*25/100)
        return int(width), int(height)

    def get_dimensions_entrybox(entrybox):
        # Return dimensions of entrybox type element
        height = int(entrybox["absoluteBoundingBox"]["height"])
        width = int(entrybox["absoluteBoundingBox"]["width"])
        height = int((height*6)/100)
        width = int((width*12.45)/100)
        return int(width), int(height)

    def get_text_properties(element):
        # Return element font and fontSize (str)
        font = element["style"]["fontFamily"]
        fontSize = element["style"]["fontSize"]
        fontSize = str(int((int(fontSize)*78.75)/100))

        return font, fontSize

    def get_alignment(element):
        align = element["style"]["textAlignHorizontal"]
        if align == 'LEFT':
            return 'left'
        elif align == 'RIGHT':
            return 'right'
        elif align == 'CENTER':
            return 'center'
        elif align == 'JUSTIFIED':
            return "none"


class conversion:
    def background(element, file_id, token, gen_dir):
        x, y = gui_properties.get_coordinates(element)
        item_id = element["id"]

        response = requests.get(
            f"https://api.figma.com/v1/images/{file_id}"
            f"?ids={item_id}&use_absolute_bounds=true",
            headers={"X-FIGMA-TOKEN": f"{token}"})

        image_link = requests.get(response.json()["images"][item_id])

        with open(f"{gen_dir}background.png", "wb") as file:
            file.write(image_link.content)

        lines.extend(['\n\n# Background of window (bg.png should be in same folder as this file)',
                      'img = Image.open("background.png")',
                      'bg_image = img.resize((int(img.width+(img.width*25/100)), int(img.height+(img.height*25/100))))',
                      'bg_image = ImageTk.PhotoImage(bg_image)',
                      f'tk.Label(window, image=bg_image, borderwidth=0, relief="solid").place(x={x},y={y})'])

    def picture(element, elements, file_id, token, gen_dir):
        count_1
        x, y = gui_properties.get_coordinates(element)
        item_id = element["id"]

        response = requests.get(
            f"https://api.figma.com/v1/images/{file_id}"
            f"?ids={item_id}&use_absolute_bounds=true",
            headers={"X-FIGMA-TOKEN": f"{token}"})

        image_link = requests.get(response.json()["images"][item_id])

        with open(f"{gen_dir}picture_{count_1}.png", "wb") as file:
            file.write(image_link.content)
        bg = "#FFFFFF"
        for ele in elements:
            if ele["name"] == "Picture_color_"+element["name"][-1:]:
                bg = gui_properties.get_color(ele)
        lines.extend(['\n\n# Picutre (image should be in same folder as this file)',
                      f'img_{count_1} = Image.open("picture_{count_1}.png")',
                      f'img_{count_1} = img_{count_1}.resize((int(img_{count_1}.width+(img_{count_1}.width*25/100)), int(img_{count_1}.height+(img_{count_1}.height*25/100))))',
                      f'pic_{count_1} = ImageTk.PhotoImage(img_{count_1})',
                      f'tk.Label(window, image=pic_{count_1}, bg="{bg}",borderwidth=0, relief="solid").place(x={x},y={y})'])

    def menubutton(element, elements):
        x, y = gui_properties.get_coordinates(element)
        element_color = gui_properties.get_color(element)
        for ele in elements:
            if ele["name"] == "Menubox_text_"+element["name"][-1:]:
                text = ele["characters"]
                color = gui_properties.get_color(ele)
                font, fontSize = gui_properties.get_text_properties(ele)
        lines.extend(['\n\n# MenuBox',
                      f'\nMenuBox_{count_4} = tk.Menubutton(window, text="{text}", font=("{font}", {fontSize}), bg="{element_color}", fg="{color}", activebackground="{element_color}", activeforeground="{color}")',
                      f'MenuBox_{count_4}.place(x={x}, y={y})',
                      f'MenuBox_{count_4}.menu = tk.Menu(MenuBox_{count_4}, tearoff=0)',
                      f'MenuBox_{count_4}["menu"] = MenuBox_{count_4}.menu'],
                     )
        for value in elements:
            if value["name"] == "Menubox_list_"+element["name"][-1:]:
                vals = value["characters"]
                vals = vals.splitlines()
                vals2 = [line.replace(" ", "_") for line in vals]
                for menu_val in vals2:
                    lines.extend([f'{menu_val} = tk.IntVar()',
                                 f'MenuBox_{count_4}.menu.add_checkbutton(label="{menu_val}", variable={menu_val})'])

    def text(element, elements):
        bg = "#FFFFFF"
        ele_name = element["name"].split("_")
        suffix = ele_name[1]
        for color in elements:
            if "Text_color_"+suffix in color["name"]:
                bg = gui_properties.get_color(color)
        text = element["characters"]
        x, y = gui_properties.get_coordinates(element)
        color = gui_properties.get_color(element)
        font, fontSize = gui_properties.get_text_properties(element)
        align = gui_properties.get_alignment(element)
        text = text.replace("\n", "\\n")
        if align == "none":
            lines.extend(['\n\n# Text'
                          f'\ntk.Label(window, text="{text}", font=("{font}", {fontSize}), bg="{bg}",fg="{color}").place(x={x}, y={y})'])
        else:
            lines.extend(['\n\n# Text'
                          f'\ntk.Label(window, text="{text}", font=("{font}", {fontSize}), justify="{align}", bg="{bg}",fg="{color}").place(x={x}, y={y})'])

    def frames(element):
        width, height = gui_properties.get_dimensions(element)
        x, y = gui_properties.get_coordinates(element)
        element_color = gui_properties.get_color(element)

        lines.extend(['\n\n# Frame',
                      f'tk.Frame(window, bg="{element_color}", width={width}, height={height}).place(x={x}, y={y})'])

    def entryBox(element, elements):
        width, height = gui_properties.get_dimensions_entrybox(element)
        x, y = gui_properties.get_coordinates(element)
        color = gui_properties.get_color(element)
        y = str(int(y) + 5)
        text = ""
        for txt in elements:
            if "Entrybox_text_"+element["name"][-1:] == txt["name"]:
                text = txt["characters"]
                text_color = gui_properties.get_color(txt)
                font, fontsize = gui_properties.get_text_properties(txt)
        if len(text) > 0:
            lines.extend(['\n\n# Entrybox',
                          f'entrybox_{count_2} = tk.Text(window, width={width}, height={height}, bg="{color}", fg="{text_color}", font=("{font}", {fontsize}))',
                          f'entrybox_{count_2}.insert(1.0, "{text}")',
                          f'entrybox_{count_2}.place(x={x}, y={y})'])
        else:
            lines.extend(['\n\n# Entrybox',
                          f'entrybox_{count_2} = tk.Text(window, width={width}, height={height}, bg="{color}")',
                          f'entrybox_{count_2}.place(x={x}, y={y})'])

    def line(element):
        width, height = gui_properties.get_dimensions(element)
        x, y = gui_properties.get_coordinates(element)
        color = gui_properties.get_line_color(element)
        if int(width) == 0:
            width = 1

        lines.extend(['\n\n# Line',
                      f'tk.Frame(window, width={width}, height={height}, bg="{color}").place(x={x}, y={y})'])

    def button(element, elements, token, file_id, gen_dir):
        Type = element["name"].split('_')[1]
        if Type == 'NR':
            x, y = gui_properties.get_coordinates(element)
            color = gui_properties.get_color(element)
            text = ""
            for ele in elements:
                if ele["name"] == "B_"+element["name"][-1:]:
                    text = ele["characters"]
                    font, fontsize = gui_properties.get_text_properties(ele)
                    text_color = gui_properties.get_color(ele)
            lines.extend(['\n\n# Button',
                          f'button_{count_3} = tk.Button(window, text="{text}", bg="{color}", fg="{text_color}", activebackground="{color}", activeforeground="{text_color}", relief="flat", command=lambda:[placeholder()], font=("{font}", {fontsize}))',
                          f'button_{count_3}.place(x={x}, y={y})'])
        if Type == 'R':
            item_id = element["id"]

            response = requests.get(
                f"https://api.figma.com/v1/images/{file_id}"
                f"?ids={item_id}&use_absolute_bounds=true",
                headers={"X-FIGMA-TOKEN": f"{token}"})

            image_link = requests.get(response.json()["images"][item_id])

            with open(f"{gen_dir}button_{count_3}.png", "wb") as file:
                file.write(image_link.content)
            color = "#ffffff"
            for ele in elements:
                if ele["name"] == "BR_color_"+element["name"][-1:]:
                    color = gui_properties.get_color(ele)
            x, y = gui_properties.get_coordinates(element)
            lines.extend(['\n\n# Button',
                          f'img_b_{count_3} = Image.open("button_{count_3}.png")',
                          f'img_b_{count_3} = img_b_{count_3}.resize((int(img_b_{count_3}.width+(img_b_{count_3}.width*25/100)), int(img_b_{count_3}.height+(img_b_{count_3}.height*25/100))))',
                          f'pic_b_{count_3} = ImageTk.PhotoImage(img_b_{count_3})',
                          f'button_{count_3} = tk.Button(window, image = pic_b_{count_3}, activebackground="{color}", bg="{color}", relief="flat", command=lambda:[placeholder()])',
                          f'button_{count_3}.place(x={x}, y={y})'])

    def save(gen_dir):
        lines.extend(['window.resizable(False, False)', 'window.mainloop()'])
        final_code = [line + "\n" for line in lines]

        with open(f"{gen_dir}window.py", 'w+', encoding='utf-8') as py_file:
            py_file.writelines(final_code)
        messagebox.showinfo("Converted", "The code has been generated")

    def main():  # sourcery no-metrics
        token = entrybox_0.get('1.0', tk.END)
        link = entrybox_1.get('1.0', tk.END)
        token = token.splitlines()[0]
        link = link.splitlines()[0]
        file = filedialog.askdirectory(parent=window, initialdir="/")
        generated_dir = file + "/output/"
        global lines
        lines = []
        lines.extend(['import tkinter as tk\nimport ctypes\nfrom PIL import Image, ImageTk\n\nctypes.windll.shcore.SetProcessDpiAwareness(1)\n\n',
                      'def placeholder():',
                      '    print("Your function comes here")\n\n',
                      '# Window Initialization',
                      'window = tk.Tk()',
                      'window.title("Window")'])

        def find_between(s, first, last):
            try:
                start = s.index(first) + len(first)
                end = s.index(last, start)

                return s[start:end]

            except ValueError:
                return ""

        token = token.strip()
        file_url = link.strip()

        file_id = find_between(file_url, "file/", "/")
        try:
            response = requests.get(
                f"https://api.figma.com/v1/files/{file_id}", headers={"X-FIGMA-TOKEN": token})
        except ValueError:
            messagebox.showerror(
                "Value Error", "Either token or the file seems to be wrong")

        except requests.ConnectionError:
            messagebox.showerror(
                "No Connection", "No Internet connection detected")

        elements = response.json()
        try:
            fig_window = elements["document"]["children"][0]["children"][0]

            try:
                os.mkdir(generated_dir)

            except FileExistsError:
                messagebox.showinfo(
                    "File Exists", "Existing Files will be overwritten.")

            except PermissionError:
                messagebox.showerror(
                    "Permission Error", "Change directory or directory permissions.")

        except KeyError:
            messagebox.showerror(
                "Error", "Invalid Input. Please check your input and try again.")

        except IndexError:
            messagebox.showerror(
                "Error", "Invalid design file. Does your file contain a Frame?")

        window_width, window_height = gui_properties.get_dimensions(fig_window)

        try:
            window_bg_hex = gui_properties.get_color(fig_window)

        except Exception as e:
            print(e)
            window_bg_hex = "#FFFFFF"

        lines.extend([f'window.geometry("{window_width}x{window_height}")',
                      f'window.configure(bg = "{window_bg_hex}")'])

        # Getting Elements inside Window

        window_elements = fig_window["children"]
        global count_1, count_2, count_3, count_4
        count_1 = 0
        count_2 = 0
        count_3 = 0
        count_4 = 0

        for element in window_elements:
            if element["name"] == "Background":
                conversion.background(element, file_id, token, generated_dir)
            elif element["name"] == "Frame":
                conversion.frames(element)
            elif "Picture" in element["name"] and "color" not in element["name"]:
                conversion.picture(element, window_elements,
                                   file_id, token, generated_dir)
                count_1 += 1
            elif "Text" in element["name"] and "color" not in element["name"]:
                conversion.text(element, window_elements)
            elif "Entrybox" in element["name"] and "text" not in element["name"]:
                conversion.entryBox(element, window_elements)
                count_2 += 1
            elif "Menubox" in element["name"] and "text" not in element["name"] and "list" not in element["name"]:
                conversion.menubutton(element, window_elements)
                count_4 += 1
            elif element["name"] == "Line":
                conversion.line(element)
            elif "Button" in element["name"]:
                conversion.button(element, window_elements,
                                  token, file_id, generated_dir)
                count_3 += 1
        conversion.save(generated_dir)


if __name__ == '__main__':
    # Window Initialization
    window = tk.Tk()
    window.title("Window")
    window.geometry("1250x625")
    window.configure(bg = "#ffffff")


    # Background of window (bg.png should be in same folder as this file)
    img = Image.open("background.png")
    bg_image = img.resize((int(img.width+(img.width*25/100)), int(img.height+(img.height*25/100))))
    bg_image = ImageTk.PhotoImage(bg_image)
    tk.Label(window, image=bg_image, borderwidth=0, relief="solid").place(x=0,y=0)


    # Frame
    tk.Frame(window, bg="#ffffff", width=1125, height=525).place(x=62, y=58)


    # Text
    tk.Label(window, text="GUI", font=("Comic Sans MS", 23), justify="left", bg="#FFFFFF",fg="#000000").place(x=72, y=58)


    # Text
    tk.Label(window, text="LD", font=("Comic Sans MS", 23), justify="left", bg="#FFFFFF",fg="#2b2bff").place(x=151, y=58)


    # Text
    tk.Label(window, text="WELCOME TO GRAPHICAL\nUSER INTERFACE\nLAYOUT DESIGNER", font=("Roboto", 23), justify="left", bg="#FFFFFF",fg="#000000").place(x=121, y=145)


    # Text
    tk.Label(window, text="Build eye pleasing GUI’s under minutes with\nsimple drag and drop interface of your\nproject without any hastle of debugging and\nmodifying code again and again!", font=("Courier New", 11), justify="left", bg="#FFFFFF",fg="#000000").place(x=121, y=342)


    # Picutre (image should be in same folder as this file)
    img_0 = Image.open("picture_0.png")
    img_0 = img_0.resize((int(img_0.width+(img_0.width*25/100)), int(img_0.height+(img_0.height*25/100))))
    pic_0 = ImageTk.PhotoImage(img_0)
    tk.Label(window, image=pic_0, bg="#FFFFFF",borderwidth=0, relief="solid").place(x=705,y=123)


    # Line
    tk.Frame(window, width=1, height=415, bg="#000000").place(x=656, y=110)


    # Text
    tk.Label(window, text="Token ID:", font=("Roboto", 15), justify="left", bg="#3f3f3f",fg="#7e7e7e").place(x=755, y=210)


    # Text
    tk.Label(window, text="File  Link:", font=("Roboto", 15), justify="left", bg="#3f3f3f",fg="#7e7e7e").place(x=755, y=287)


    # Entrybox
    entrybox_0 = tk.Text(window, width=18, height=1, bg="#ffffff")
    entrybox_0.place(x=901, y=216)


    # Entrybox
    entrybox_1 = tk.Text(window, width=18, height=1, bg="#ffffff")
    entrybox_1.place(x=901, y=293)


    # Button
    img_b_0 = Image.open("button_0.png")
    img_b_0 = img_b_0.resize((int(img_b_0.width+(img_b_0.width*25/100)), int(img_b_0.height+(img_b_0.height*25/100))))
    pic_b_0 = ImageTk.PhotoImage(img_b_0)
    button_0 = tk.Button(window, image = pic_b_0, activebackground="#3f3f3f", bg="#3f3f3f", relief="flat", command=lambda:[conversion.main()])
    button_0.place(x=828, y=396)
    window.resizable(False, False)
    window.mainloop()