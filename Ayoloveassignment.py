Questions = [["What is the chemical formula for Gold:", "A. Au, B. Ag, C. Zn.", "A."],

["The fastest animal on land is?:", "A. Goat, B. Cheetah, C. Dog.", "B."],

["The fastest animal on air is?:", "A. Sailfish, B. Cheetah, C. Peregrine Falcon.", "C."],

["Chicken evolved from.....?:", "A. Lion, B. Dinosaur, C. Fish.", "B."],

["The brain send message round the body through a network of?:", "A. Neurons, B. Brain power, C. Brain web", "A."]]


def ask_questions(a,b,c):

    user_answer = input(f"{question[0]}  {question[1]}:")

    if user_answer == question[2]:

        print("processing")

        return 2
    else:

        print("reprocessing")

        return 0


score = 0

for question in Questions:

    score = score + ask_questions(question[0],question[1],question[2])

print(f"{score}/10")