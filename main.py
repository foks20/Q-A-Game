
def new_game():
    score = 0
    counter = 0
    user_guesses = []
    for key in questions_answers:
        print(key)
        for options in choices[counter]:
            print(options)
            
            user_input = input("please select a choice")
            user_input = user_input.capitalize()
            print(user_input)
            user_guesses.append(user_input)
            print(questions_answers[key])
            score += check_answer(questions_answers[key],user_input)     
        counter+=1
    display_result(score)
    play_again()
    
def check_answer(correct_answer,user_answer):
    if correct_answer == user_answer:
        return 1
    else:
        return 0
        
def display_result(score):
    print(score)
    
def play_again():
    print("play again")
    user_input = input("Play again? Yes/No")
    if user_input =="Yes":
        new_game()
    else:
        return False
        


questions_answers ={
    "What's my favorite color": "A","Do you like to fly": "B"
}

choices = [["A) Green B) Blue C) Purple D) Black"],["A) No B) Yes C) Maybe D) N/A"]]

new_game()
