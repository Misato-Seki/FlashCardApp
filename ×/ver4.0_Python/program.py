import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import Style

if __name__ == '__main__':

    # Create the main GUI window
    root = tk.Tk()
    root.title('Flashcards App')
    root.geometry('500*400')

    # Apply styling to the GUI elements
    style = Style(theme='superhero')
    style.configure('TLabel', font=('TkDefaultFont', 18))
    style.configure('TButtun', font=('TkDefaultFont', 16))

    # Set up variables for storing user input
    set_name_var = tk.StringVar()
    word_var = tk.StringVar()
    definition_var = tk.StringVar()

    #Create a notebook widget to manage tabs
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # Create the "Create Set" tab and its content
    create_set_frame = ttk.Frame(notebook)
    notebook.add(create_set_frame, text='Create Set')

    # Label and Entry widgets for entering set name, word and definition
    ttk.Label(create_set_frame, text='Set Name:').pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=set_name_var, width=30).pack(padx=5, pady=5)

    ttk.Label(create_set_frame, text='Word:').pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=set_name_var, width=30).pack(padx=5, pady=5)

    ttk.Label(create_set_frame, text='Definition:').pack(padx=5, pady=5)
    ttk.Entry(create_set_frame, textvariable=set_name_var, width=30).pack(padx=5, pady=5)

    # Button to add a word to the set (command = add_word) => for the next part
    ttk.Button(create_set_frame, text='Add Word').pack(padx=5, pady=10)

    # Button to save the set (command = create_set)
    ttk.Button(create_set_frame, text='Save Set').pack(padx=5, pady=10)

    # Create the "Select Set" tab and its content
    select_set_frame = ttk.Frame(notebook)
    notebook.add(select_set_frame, text='Select Set')

    # Combobox widget for selecting existing flashcard sets
    sets_combobox = ttk.Combobox(select_set_frame, state='readonly')
    sets_combobox.pack(padx=5, pady=5)

    # Button to select a set (command = select_set)
    ttk.Button(select_set_frame, text='Select Set').pack(padx=5, pady=5)

    # Button to delete a set (command = delete_selected_set)
    ttk.Button(select_set_frame, text='Delete Set').pack(padx=5, pady=5)

    # Create the "Learn mode" tab and its content
    flashcard_frame = ttk.Frmae(notebook)
    notebook.add(flashcard_frame, text='Learn Mode')

    # Initialize variable for tracking card index and current cards
    card_index = 0
    current_tabs = []

    # Label to display the word on flashcards
    word_label = ttk.Label(flashcard_frame, text='', font=('TkDefaultFont', 24))
    word_label.pack(padx=5, pady=40)

    # Label to display the definition on flashcards
    definition_label = ttk.Label(flashcard_frame, text='')
    definition_label.pack(padx=5, pady=5)

    # Button to flip the flashcard (command = flip_card)
    ttk.Button(flashcard_frame, text='Flip').pack(side='left', padx=5, pady=5)

    # Button to view the next flashcard (command = next_card)
    ttk.Button(flashcard_frame, text='Next').pack(side='right', padx=5, pady=5)

    # Button to view the previous flashcard (command = prev_card)
    ttk.Button(flashcard_frame, text='Previous').pack(side='right', padx=5, pady=5)

    # 


    root.mainloop()