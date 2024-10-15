import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import sv_ttk # Cool theme called Sun-Valley for tkinter
import darkdetect
import pywinstyles as winstyle
import sys
from case import main

app = ctk.CTk()
app.geometry('720x480')
app.title('Case Converter')


# Creates the main window


# Detects theme windows has set
sv_ttk.set_theme(darkdetect.theme()) 

# Function to specifically apply theme to titlebar (NOT MY CODE | CREDIT: rdbebde/Sun-Valley-ttk-theme)
def apply_theme_to_titlebar(app):
    version = sys.getwindowsversion()
    if version.major == 10 and version.build >= 22000:
        winstyle.change_header_color(app, '#1c1c1c' if sv_ttk.get_theme() == 'dark' else '#fafafa')
    elif version.major == 10:
        winstyle.apply_style(app, 'dark' if sv_ttk.get_theme() == 'dark' else 'normal')
        app.wm_attributes('-alpha', 0.99)
        app.wm_attributes('-alpha', 1)


# Call the function to apply the theme to the title bar
apply_theme_to_titlebar(app)

# Button to test theme
def button_event():
    main()


button = ctk.CTkButton(app, text="CTkButton", command=button_event)
# Start the Tkinter main loop
app.mainloop()
button_event()