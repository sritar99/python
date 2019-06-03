easy_quiz = '___1___ is the language of the web. HTML ___2___ and ___3___ are good ways to make your code more readable to other programmers. While HTML is the structure, ___4___ is the style.'
easy_answers = ["HTML", "comments", "indenting", "CSS"]

medium_quiz = 'A directory can be removed in two ways: ___1___ and ___2___. Using a ___3___ and using the ___4___ are two methods of running pythons.'
medium_answers = ["rmdir", "rm -r", "text Editor", "Command Line"]

hard_quiz = "Under the list operation, ___1___ is like a procedure that is used like string while ___2___ introduces a new list. ___3___ works for so many other things other than list including strings. One of the advantages of having data with structure is that you can take advantage of that structure! One way you can do that is by directly looping through the elements of a list with what's called a ___4___"
hard_answers = ["append", "plus", "len", "for loop"]


blanks = ["__1__","__2__", "__3__"," __ 4__"]
answers = [easy_answers, medium_answers, hard_answers]


a_list = [1, 2, 3, 4]
index = 0
while index < len (a_list):
        index = index + 1
print 'Welcome to the Quiz!'
print " choose Easy, Medium or Hard, you certainly cannot fail all."




# Displays user's questions and answers for any option choosen
def difficulty():
  diff = raw_input()
  if diff == 'Easy':
    print 'Are you ready? Rock and Roll!! For the blank in the quiz below, fill in the correct answer.'
    print easy_quiz
    return easy_quiz, easy_answers

  elif diff =='Medium':
    print 'Are you ready? Rock and Roll!!  For the blank in the quiz below, fill in the correct answer. '
    print medium_quiz
    return medium_quiz, medium_answers

  elif diff == 'Hard':
    print 'Are you ready? Rock and Roll!!  For each blank in the quiz below, fill in what you believe is the correct answer. '
    print hard_quiz
    return hard_quiz, hard_answers



def process_question(questions):
    #replace the blanks in the questions
    list_of_words = questions.split()


def quiz(questions, answers):
    #confirms the answers to the questions
    index = 0
    max_index = 4
    replaced = []
    print (questions)

    for new_answer in blanks: #Try and call a different blank
        while True: #Creates an infinite loop if the user enters the wrong answer
            fill_blanks = raw_input("What is the answer of " + new_answer) # Ask a user to fill in the blank
            if fill_blanks == answers[index]: # Confirm if the user's answer match
                questions = questions.replace(new_answer, fill_blanks)
                index += 1 # If answer match, go to the next blank
                print "Correct! Yayy!!"
                if index == max_index:
                    print "YOU ARE AWESOME!!"
                else:
                    print questions
                break
            else:
                print "Think Again!"
                print questions


questions, answers = difficulty()

quiz(questions, answers)



def search_for(blanks, questions):
    for new_answer in blanks:
        if new_answer in questions:
            return new_answer
    return None
