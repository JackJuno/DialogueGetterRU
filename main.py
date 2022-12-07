# DialogueGetter gets dialogues from russian texts,
# clean them and write down to a dataset file <.txt>
# for use in nlp projects.
import datetime
import os
from loguru import logger
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from FileTreeOps.dir_preprocessor import pipeline
from FileTreeOps.files_preprocessor import merge_files_in_directory
from TextOps.dialogue_extractor import extract_n_save_replicas

# vars
SRC_PATH = ''
DTSET_PATH = ''


# UI foos
def input_src():
    # save a path to var
    path = str_src.get()
    path = path.strip()
    # check if the dir exists
    if os.path.isdir(path):
        global SRC_PATH
        # save path to global var
        SRC_PATH = path
        logger.info('Input directory found')
        display_info_string_var.set('Current state: Work in progress')
    else:
        logger.error('Input directory not found')
        display_info_string_var.set('Current state: Input directory not found')


def input_dtset():
    # save input to var
    path = str_dtset.get()
    path = path.strip()
    # check if the dir exists
    if os.path.isdir(path):
        global SRC_PATH
        global DTSET_PATH
        # save path to global var
        DTSET_PATH = path
        logger.info('Output directory found')
        # pre-process files in src dir -> list of files ready to extract dialogues
        pipeline(SRC_PATH)
        # extract & save dialogues
        extract_n_save_replicas(SRC_PATH, DTSET_PATH)
        display_info_string_var.set('Current state: Work done')
    else:
        logger.error('Output directory not found')
        display_info_string_var.set('Current state: Output directory not found')


def merge_files():
    global DTSET_PATH
    path_to_merge_files = DTSET_PATH
    merge_files_in_directory(path_to_merge_files)
    display_info_string_var.set('Current state: All datasets are merged into all_in_one_dataset_file')


# delete autogenerated tmp files
if __name__ == '__main__':
    # Open main window
    root = Tk()
    root.title("Dialogues Getter RU")
    root.geometry('615x732')
    root.resizable(False, False)
    # Enter paths widgets
    heart_label = Label(root, text='. ..  ... ❦ ....    .....', font=("Helvetica", "27"))
    heart_label.grid(column=0, row=0, columnspan=3, pady=10)
    info_label = Label(root, text='At first copy all  < .txt >  source-files in a separate directory of your computer.', font=("Helvetica", "12"))
    info_label.grid(column=0, row=1, columnspan=3, sticky=W, pady=10, padx=5)
    entry_label_src = Label(root, text="Then enter path to the directory where the source-files were copied to:", font=("Helvetica", "12"))
    entry_label_src.grid(column=0, row=2, columnspan=3, sticky=W, pady=10, padx=5)
    str_src = StringVar()
    entry_src = Entry(root, width=63, textvariable=str_src)
    entry_src.grid(column=0, row=3, columnspan=2, sticky=W, padx=5)
    path_src = Button(root, text="OK", command=lambda:input_src())
    path_src.grid(column=2, row=3, sticky=E)
    entry_label_dtset = Label(root, text="Enter path to directory where you would like to put the datasets that will be created:", font=("Helvetica", "12"))
    entry_label_dtset.grid(column=0, row=4, columnspan=3, sticky=W, pady=10, padx=5)
    str_dtset = StringVar()
    entry_dtset = Entry(root, width=63, textvariable=str_dtset)
    entry_dtset.grid(column=0, row=5, columnspan=2, sticky=W, padx=5)
    path_dtset = Button(root, text="GO", command=lambda:input_dtset())
    path_dtset.grid(column=2, row=5, sticky=E)
    display_info_string_var = StringVar()
    display_info_string_var.set('Current state: Program is idle. Waiting for paths data.')
    display_info_label = Label(root, textvariable=display_info_string_var, font="Helvetica 12", foreground="red")
    display_info_label.grid(column=0, row=6, columnspan=3, sticky=W, pady=10, padx=5)
    # Create an instance of ttk Style Object to change font in a button
    style = Style()
    merge_files_btn = Button(root, text="Merge all datasets created in output directory into all-in-one big dataset file", style="big.TButton", command=lambda:merge_files())
    style.configure('big.TButton', font=('Helvetica', 12))
    merge_files_btn.grid(column=0, row=7, columnspan=3, sticky=EW, pady=5, padx=5)
    # Execute Tkinter
    root.mainloop()
