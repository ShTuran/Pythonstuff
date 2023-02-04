# quiz 

y_or_n=input("Are you ready for the quiz? ")

if y_or_n.lower() != "yes":
    print("How sad :( ")
    quit()
    
print("***Let's begin***")
score = 0
Questions = {
    "When was the first known use of the word 'quiz'": [
        "1781", "1771", "1871", "1881"
    ],
    "Which built-in function can get information from the user": [
        "input", "get", "print", "write"
    ],
    "Which keyword do you use to loop over a given list of elements": [
        "for", "while", "each", "loop"
    ],
    "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
}


for question, alternatives in Questions.items():
    correct_answer = alternatives[0]
    sorted_alternatives = sorted(alternatives)
    for label, alternative in enumerate(sorted_alternatives):
        print(f"  {label} ) {alternative}")
    
    answer_label = int(input(f"{question}? "))
    answer = sorted_alternatives[answer_label]

    if answer == correct_answer:
        print("Correct!")
        score+=1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        

print("Your score is", score ,"point.")       