"""
Context:
    This file contains all the UI and game logic. I am using tkinter to draw the window and the UI.
    The game logic is pretty simple. 
"""

# importing the necessary files and libraries
from tkinter import ttk
from tkinter import *
from logic import get_page
from data import languages_dict

# initializing some important varibales
current_phrase = ''
global current_lang
current_lang = '' 

# creating a tkinter window of mentioned dimensions and title
root = Tk()
root.geometry('800x200')
root.title('Guess the Language')

# adding a frame as a child to the root window
main_frame = ttk.Frame(root, padding=10)
main_frame.pack()

#initializing objects that are mutables on the fly
content = StringVar()
correct_answer = StringVar()

# calling the request method to get the first set of values
current_values = get_page()

# assigning those values, current phrase is the question displayed to the player, current lang the answer
current_phrase = current_values[0]
current_lang = current_values[1]

# setting the values to mutables objects initialized before
content.set(current_phrase)
correct_answer.set('The correct answer will appear here!')

# creating a Lable object to display the question in the window
text = ttk.Label(main_frame, textvariable=content)
text.pack()

# creating a Lable object to display the correct answer in the window
correct_answer_box = ttk.Label(main_frame, textvariable=correct_answer)
correct_answer_box.pack()

# counter to keep track of current score
score = IntVar()
score.set(0)

"""
This method gets called when user pressed the enter key or the guess button. It first checks 
if the user input answer is correct. Then it requests a new question and displays it. It also
shows the correct answer to the last question right underneath. Score goes up by 1 if correct
and stays the same if not.
"""
def change_lang():

    # the varibales
    global current_lang, current_phrase, score

    # getting the users answer
    user_answer =  answer_box.get()

    # getting the full answer from data dict
    correct_answer.set('It was '+ languages_dict[current_lang])

    # clearing the answer box for the next question, the aruguemts mean clear everything
    answer_box.delete(0, END)
    
    # checking if the users answer is correct
    if user_answer.lower() in languages_dict[current_lang].lower():
        score.set(score.get() + 1)

    # gets the new set of question and answer
    current_values = get_page()

    # assings them
    current_phrase = current_values[0]
    current_lang = current_values[1]

    # displaying the new question
    content.set(current_phrase) 

    # calling again if empty
    if content.get() == None:
        change_lang()

# answer box UI
answer_box = ttk.Entry(root, width=80)
answer_box.pack()

# score counter UI
score_counter = ttk.Label(main_frame, textvariable=score)
score_counter.pack()

# quit button UI
quit_button = ttk.Button(main_frame, text="Quit", command=root.destroy)
quit_button.pack(side = 'right', expand=True)

#guess button UI
guess_button = ttk.Button(main_frame, text="Guess", command=change_lang)
guess_button.pack(side='left', expand=True)

# pressing enter calls guess
def enter_pressed(event):
    change_lang()
root.bind('<Return>', enter_pressed)

root.mainloop()