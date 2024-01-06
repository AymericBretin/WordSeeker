import customtkinter
import os
from customtkinter import filedialog
import re
import mimetypes


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("800x480")
app.title('WordSeeker')
app.resizable(False, False)

def find():
    global dir_path
    dir_path = a
    global word
    word = entry_1.get()
    for file in os.listdir(dir_path):
        global cur_path
        cur_path = os.path.join(dir_path, file)
        mime_type, _ = mimetypes.guess_type(cur_path)
        if mime_type and mime_type.startswith('text'):
            if os.path.isfile(cur_path):
                with open(cur_path, 'r') as file:
                    content = file.read()
                    if re.search(rf'\b{re.escape(word)}\b', content):
                        print('Mot "', word,'" trouvé dans', cur_path)

def Next_Page():
    label_5.destroy()
    label_2 = customtkinter.CTkLabel(master=frame_right, text="Enter the word to search for", bg_color="#2b2b2b", font=("Helvetica", 30, "bold"))
    label_2.grid(row=0, column=0, pady=50, padx=10)
    button.destroy()
    label_4.destroy()
    global entry_1
    entry_1 = customtkinter.CTkEntry(master=frame_right, placeholder_text="CTkEntry", width=200, height=50, font=("Helvetica", 20, "bold"))
    entry_1.grid(row=1, column=0, padx=20, pady=30)
    button_start = customtkinter.CTkButton(master=frame_right, text="Start search", command=find, font=("Helvetica", 20, "bold"), width=200, height=50)
    button_start.grid(row=3, column=0, padx=20, pady=10)
    button_next.destroy()
    label_5.destroy()


def button_function():
    global a
    a = filedialog.askdirectory(
        initialdir="/home/ay",
        title="Open file",
    )
    global label_5
    label_5 = customtkinter.CTkLabel(master=frame_right, text=a, bg_color="#2b2b2b", font=("Helvetica", 20, "bold"))
    label_5.grid(row=2, column=0, pady=50, padx=20)

    global button_next
    button_next = customtkinter.CTkButton(master=frame_right, text="Next", command=Next_Page, font=("Helvetica", 15, "bold"), width=100, height=25)
    button_next.grid(row=3, column=0, padx=20, pady=35, sticky="e")

if __name__ == "__main__":
    global frame_left
    frame_left = customtkinter.CTkFrame(master=app, width=200, height=440)
    frame_left.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    
    global frame_right
    frame_right = customtkinter.CTkFrame(master=app, width=510, height=440)
    frame_right.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    global label_1
    label_1 = customtkinter.CTkLabel(master=frame_left, text="WordSeeker", bg_color="#2b2b2b", font=("Helvetica", 30, "bold"))
    label_1.grid(row=0, column=0, pady=20, padx=10)

    global label_2
    label_2 = customtkinter.CTkLabel(master=frame_right, text="Select Filepath", bg_color="#2b2b2b", font=("Helvetica", 30, "bold"))
    label_2.grid(row=0, column=0, pady=50, padx=150)

    global button
    button = customtkinter.CTkButton(master=frame_right, text="Select Folder", command=button_function, font=("Helvetica", 20, "bold"), width=200, height=50)
    button.grid(row=1, column=0, padx=20, pady=20)

    global label_4
    label_4 = customtkinter.CTkLabel(master=frame_right, text="No Filepath please select one", bg_color="#2b2b2b", font=("Helvetica", 20, "bold"))
    label_4.grid(row=2, column=0, pady=50, padx=20)

app.mainloop()
