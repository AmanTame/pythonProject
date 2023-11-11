def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print('-------------------------')
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input('Enter(A,B,C or D): ')
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses,guesses)
def check_answer(answer, guess):
    if answer == guess:
        print('Correct')
        return 1
    else:
        print('Wrong!')
        return 0
def display_score(correct_guesses,guesses):
    print('----------------')
    print('Results')
    print('----------------')
    print('Answers: ', end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print('Guesses:', end="")
    for i in guesses:
        print(i,end=" ")
    print()
    score = (correct_guesses/len(questions))*100
    print('Your score is: ' + str(score)+'%')
def play_again():
    response = input('Do you want to play again yes/no?')
    response.upper()
    if response == 'yes':
        return True
    else:
        return False
# Dictionary
questions = {
    'who created python ?': 'A',
    'what year was python created?': 'B',
    'python is tributed to which comedy group?': 'C',
    'is the earth round?': 'A'
}
# 2D List
options = [
    ['A.Gid', 'B.gate', 'C.Mark', 'Ali'],
    ['A.1999', 'B.2000', 'C.2001', 'D.2002'],
    ['A.Messi', 'B.Ronaldo', 'C.Neymar', 'D.Kaka'],
    ['A.True', 'B.False', 'C.Sometimes', 'D.What is earth?']
]
new_game()
while play_again():
    new_game()
print('bye!')
