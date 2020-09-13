#!/usr/bin/env python

import eel
import os
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror


# make the top level window and hide it
root = Tk()
root.overrideredirect(1)
root.withdraw()
# Make it almost invisible - no decorations, 0 size, top left corner.
root.overrideredirect(True)
root.geometry('0x0+0+0')

@eel.expose
def open_file_dialog():
    # Show window again and lift it to top so it can get focus,
    # otherwise dialogs will end up behind the terminal.
    # root.deiconify()
    # root.lift()
    # root.focus_force()
    root.wm_attributes('-topmost', 1)
    fname = askopenfilename(initialdir = "/",title = "Select file",filetypes=(("Markdown File", "*.md"),
                                           ("HTML files", "*.html;*.htm"),
                                           ("All files", "*.*") ))
    if fname:
        try:
            # print("""here it comes: self.settings["template"].set(fname)""")
            eel.load_html(open_file(fname))
        except:                     # <- naked except is a bad idea
            showerror("Open Source File", "Failed to read file\n'%s'" % fname)
        return

def open_file(filename):
    content=""
    with open(filename,'r') as f:
        content=f.read()
    return content

@eel.expose
def save_file_as_markdown(filename="document1.md",content:str=""):
    with open(filename,'w',encoding='utf-8') as f:
        f.write(content)
    print("saved file")

@eel.expose
def exit():
    os._exit(0)

if __name__ == "__main__":
    eel.init('web')

    try:
        eel.start('ui.main.html')
        # eel.start('ui.main.html',size=(650, 612))
        # eel.start('ui.main.html', mode='chrome', port=8080, cmdline_args=['--start-fullscreen', '--browser-startup-dialog'])
    except (SystemExit, MemoryError, KeyboardInterrupt):
    # We can do something here if needed
    # But if we don't catch these safely, the script will crash
        pass