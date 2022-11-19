# DialogueGetter gets dialogues from russian texts,
# clean them and write down to a dataset file <.txt>
# for use in nlp projects.
import datetime
import os
from loguru import logger
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from FileTreeOps.dir_preprocessor import pipeline

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
    else:
        logger.error('Input directory not found')


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

    # extract dialogues

    # clean dialogues

    # save to dataset file
    else:
        logger.error('Output directory not found')

# "[\s]*-[\s]*[А-Я]" find -This is a Test sentence.


if __name__ == '__main__':
    # Open main window
    root = Tk()
    root.title("Dialogues Getter RU")
    root.geometry('455x732')
    root.resizable(False, False)
    # Enter paths widgets
    heart_label = Label(root, text='. ..  ... ❦ ....    .....', font=("Helvetica", "27"))
    heart_label.grid(column=0, row=0, columnspan=3, pady=10)
    info_label = Label(root, text='Copy all  < .txt >  source-files in a separate directory.', font=("Helvetica", "12"))
    info_label.grid(column=0, row=1, columnspan=3, sticky=W, pady=10, padx=5)
    # info_label_1 = Label(root, text='Files in the directory will be RENAMED & utf-8 ENCODED.', font=("Helvetica", "12"))
    # info_label_1.grid(column=0, row=2, columnspan=3, sticky=W, pady=10, padx=5)
    entry_label_src = Label(root, text="Enter path to directory where literary sources are:", font=("Helvetica", "12"))
    entry_label_src.grid(column=0, row=2, columnspan=2, sticky=W, pady=10, padx=5)
    str_src = StringVar()
    entry_src = Entry(root, width=43, textvariable=str_src)
    entry_src.grid(column=0, row=3, columnspan=2, sticky=W, padx=5)
    path_src = Button(root, text="OK", command=lambda:input_src())
    path_src.grid(column=2, row=3, sticky=W)
    entry_label_dtset = Label(root, text="Enter path to directory to save dataset we`d make:", font=("Helvetica", "12"))
    entry_label_dtset.grid(column=0, row=4, columnspan=2, sticky=W, pady=10, padx=5)
    str_dtset = StringVar()
    entry_dtset = Entry(root, width=43, textvariable=str_dtset)
    entry_dtset.grid(column=0, row=5, columnspan=2, sticky=W, padx=5)
    path_dtset = Button(root, text="GO", command=lambda:input_dtset())
    path_dtset.grid(column=2, row=5, sticky=W)

    # from tkinter import *
    # root = Tk()
    # txt2 = Entry(root,width=20)
    # txt2.grid(column=0, row=0)
    # lbl2 = Label(root, text='Докладная о')
    # lbl2.grid(column=0, row=1)
    # btn = Button(root, text='click', command=lambda:change())
    # btn.grid(column=0, row=2, columnspan=2)
    # def change():
    # lbl2['text'] = f'Докладная о {txt2.get()}'
    # root.mainloop()
    # Execute Tkinter
    root.mainloop()
