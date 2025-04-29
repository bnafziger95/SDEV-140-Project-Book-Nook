# add books window

# import libraries: tkinter, json
# window title: "Add Book"
# labels: "Title", "Author", "Genre" (dropdown), "Rating" (1-5), Status (Want to Read, Currently Reading, Finished)
# entry fields for title, author, rating
# drop down for genre: "Fiction", "Non-Fiction", "Romance", "Sci-Fi", "Fantasy", "Other"
# button: "Add Book" --> adds book to library.json
# button: "Back to Main" --> closes add book window and returns to main window
# functions:
# open_add_book_window() --> creates add book window
# submit_book() --> adds book to library.json, validate input, show success/error message
# back_to_main() --> closes add book window and returns to main window


# start of add_book.py
# import libraries
import tkinter as tk
from tkinter import messagebox, ttk  # for message boxes and dropdowns
import json

# import utility functions from util.py
from utils import load_library, save_library, validate_input, show_message, get_genre_options, get_status_options, get_rating_options

# create add book window
