# %% 
import sys
import json
import numpy as np
import random

# %%
def get_questions():
    with open('./resources/questions.json') as f:
        return json.load(f)

def get_answer():
    answer = input('\nWähle a, b, c oder d (bestätige mit ENTER, oder verlasse die App mit q/exit/quit). >>> ')
    return answer

def calculate_score(score_count, question_count):
    score = round(np.divide(score_count, question_count) * 100, 2)
    
    if score >= 95:
        print(f'\EPISCH! Deine Trefferquote ist: {score}%')
    elif score >= 80:
        print(f'\nSeht gut! Deine Trefferquote ist: {score}%')
    elif score >= 60:
        print(f'\nNicht schlecht, bleib dran! Deine Trefferquote ist: {score}%')
    else:
        print(f'\nEs gibt keine Niederlagen, wenn man immer wieder aufsteht - Weiter geht\'s!\nDeine Trefferquote ist: {score}%')

# %%
def run():

    """run the app"""
    
    # retireve data
    questions = get_questions()
    # shuffle questions
    random.shuffle(questions)

    # create vars to calculate answering precision of user
    score_count = 0.0
    question_count = 0.0

    for d in questions:

        print('\n\n' + d.get('question') + '\n')

        if d.get('image') is not None:
            print('https://www.elwis.de' + d.get('image') + '\n')

        # get the answer as a inidiv. dict
        # keys are a, b, c, d
        # use to check answers as answer a is always correct
        answers_dict = d.get('answers')

        # shuffle questions
        options = ['a', 'b', 'c', 'd']
        shuffled_answers = sorted(answers_dict.values(), key=lambda k: random.random())
        shuffled_answers_dict = dict(zip(options, shuffled_answers))

        # display shuffeled questions
        for option, answer in shuffled_answers_dict.items():
            print(option + ') ' + answer)

        # get user input
        user_answer = get_answer()

        # logic to check input
        if shuffled_answers_dict.get(user_answer) == answers_dict.get('a'):
            print('\nRichtig! +1')
            # add to the score count
            score_count += 1.0
        
        elif user_answer in ['quit', 'exit', 'q']:
            calculate_score(score_count, question_count)
            sys.exit('\nQuiting app ...')

        else:
            print('\nFalsch! Die Antwort ist:\n> ', answers_dict.get('a'))

        # add to the question count
        question_count += 1

    # if all questions are answered in one go
    # get score and quit the app
    print('\nNice! All-in one!')
    calculate_score(score_count, question_count)
    sys.exit('\nQuiting app ...')

if __name__ == '__main__':
    print('Starting App ...')
    run()