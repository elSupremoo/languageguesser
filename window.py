from tkinter import ttk
from tkinter import *
from logic import get_page
from data import languages_dict

current_phrase = ''
global current_lang

current_lang = '' 

root = Tk()
root.geometry('800x200')
root.title('Guess the Language')
main_frame = ttk.Frame(root, padding=10)
main_frame.pack()

content = StringVar()
correct_answer = StringVar()

current_values = get_page()

current_phrase = current_values[0]
current_lang = current_values[1]

content.set(current_phrase)
correct_answer.set('The correct answer will appear here!')

print(current_lang)

text = ttk.Label(main_frame, textvariable=content)
text.pack()

correct_answer_box = ttk.Label(main_frame, textvariable=correct_answer)
correct_answer_box.pack()

score = IntVar()
score.set(0)

def change_lang():

    global current_lang, current_phrase, score
    user_answer =  answer_box.get()

    print('you entered' , user_answer)
    print('the answer is',languages_dict[current_lang])

    correct_answer.set('It was '+ languages_dict[current_lang])

    answer_box.delete(0, END)
    
    if user_answer.lower() in languages_dict[current_lang].lower():
        score.set(score.get() + 1)

    current_values = get_page()

    current_phrase = current_values[0]
    current_lang = current_values[1]

    content.set(current_phrase) 
    if content.get() == 'None':
        change_lang()

answer_box = ttk.Entry(root, width=80)
answer_box.pack()

score_counter = ttk.Label(main_frame, textvariable=score)
score_counter.pack()

quit_button = ttk.Button(main_frame, text="Quit", command=root.destroy)
quit_button.pack(side = 'right', expand=True)

guess_button = ttk.Button(main_frame, text="Guess", command=change_lang)
guess_button.pack(side='left', expand=True)

def enter_pressed(event):
    change_lang()

root.bind('<Return>', enter_pressed)

root.mainloop()

