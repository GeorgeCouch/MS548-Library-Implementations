# George Couch
# 6/2/2023
# This program uses various functions from within the Textblob api to perform actions on user entered text. It also
# displays this information within a GUI using various functions within tkinter.
# Time spent: 3 hours
# Time description: I unfortunately am turning this in late, but as for the time spent the main issues that I had were
# involved with learning the tkinter library. After I created the interface I had to rewrite some of my functions so
# that I could keep user input validation while inserting the text into my scrolling text box.

# imports
from textblob import TextBlob
from textblob import Word
import tkinter
from tkinter import *
from tkinter import scrolledtext


# Returns the definition of a word
def define_word_button(text: str):
    # Delete all contents in the scrolling text box
    resultsBox.delete("1.0", END)
    text = text.strip()
    if " " in text or len(text) == 0:
        resultsBox.insert(tkinter.INSERT, "INVALID: Please only enter a single word")
    else:
        resultsBox.insert(tkinter.INSERT, Word(text).define()[0])


# Returns a list of all words passed through text parameter
def get_all_words_as_list_button(text: str):
    # Delete all contents in the scrolling text box
    resultsBox.delete("1.0", END)
    if len(text) == 0:
        resultsBox.insert(tkinter.INSERT, "INVALID: No words were entered, please enter some words")
    else:
        text = TextBlob(text)
        resultsBox.insert(tkinter.INSERT, text.words)


# Returns a list of synonyms of a word
def get_synsets_for_word_button(text: str):
    # Delete all contents in the scrolling text box
    resultsBox.delete("1.0", END)
    text = text.strip()
    if " " in text or len(text) == 0:
        resultsBox.insert(tkinter.INSERT, "INVALID: Please only enter a single word")
    else:
        resultsBox.insert(tkinter.INSERT, str(Word(text).synsets))


# Returns three ngrams for the given text.
def get_ngrams_for_text_button(text: str):
    # Delete all contents in the scrolling text box
    resultsBox.delete("1.0", END)
    arrWords = text.split(" ")
    text = TextBlob(text)
    if len(arrWords) < 3:
        resultsBox.insert(tkinter.INSERT, "INVALID: Please enter at least three words")
    else:
        resultsBox.insert(tkinter.INSERT, text.ngrams())


# Closes the program
def close():
    window.quit()


# Create the GUI window
window = Tk()
window.title("Python GUI and TextBlob")
window.config(padx=20, pady=20)

# Create Frames so that GUI items can be organized within them using the grid system
optionsFrame = Frame(window)
optionsFrame.grid(row=0, column=0)

outputFrame = Frame(window)
outputFrame.grid(row=0, column=1, padx=10)

# Create Buttons and link them to their respective functions
defineButton = Button(optionsFrame, text="Define a word.", width=25,
                      command=lambda: define_word_button(userTextBox.get()))
defineButton.grid(row=0, column=0, sticky="W", pady=(50, 0))

wordListButton = Button(optionsFrame, text="Get all words entered as a list.", width=25,
                        command=lambda: get_all_words_as_list_button(userTextBox.get()))
wordListButton.grid(row=1, column=0, sticky="W")

synsetsButton = Button(optionsFrame, text="Get synsets for a word", width=25,
                       command=lambda: get_synsets_for_word_button(userTextBox.get()))
synsetsButton.grid(row=2, column=0, sticky="W")

ngramsButton = Button(optionsFrame, text="Get ngrams for a word", width=25,
                      command=lambda: get_ngrams_for_text_button(userTextBox.get()))
ngramsButton.grid(row=3, column=0, sticky="W")

exitButton = Button(optionsFrame, text="Exit", width=25, command=close)
exitButton.grid(row=5, column=0, sticky="W")

# Create user input box and results box
userTextLabel = Label(outputFrame, width=40, text="Enter Text Here!")
userTextLabel.grid(row=0, column=0)

userTextBox = Entry(outputFrame, width=40)
userTextBox.grid(row=1, column=0, pady=10)

resultsBox = scrolledtext.ScrolledText(outputFrame, width=40, height=10)
resultsBox.grid(row=2, column=0)

window.mainloop()
