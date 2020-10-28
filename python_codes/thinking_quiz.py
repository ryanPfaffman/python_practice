
questions = ['\nCritical thinking concerns...\n\na. Determining the cause of our beliefs.\nb. Pinpointing the psychological basis of our beliefs\nc. Determining the quality of our beliefs\nd. Assessing the practical impact of our beliefs.\nType (a,b,c,d) and Press Enter','\n\nA belief is worth accepting if...\n\na. We have good reasons to accept it\nb. It is consistent with our needs\nc. It has not been proven wrong\nd. It is accepted by our peers\nType (a,b,c,d) and Press Enter','\n\nThe word critical in critical thinking refers to...\n\na. A fault-finding attitude\nb. Attempts to win an argument\nc. Using careful judgment or judicious evaluation\nd. A lack of respect for other people.','\n\nAccording to the text, critical thinking complements...\na. Our prejudices\nb. Our emotions\nc. Peer pressure\nd. Our unconscious desires']
answers = ['a','b','c','b']
user_answ = []

for x in questions:
    user_answ.append(input(x))

def get_points(lstA, userA):
    correct = 0
    total = len(lstA)
    for i in range(len(lstA)):
        if userA[i] == lstA[i]:
            correct += 1
    score = "Grade: " + str(int(round(correct/total*100,0))) + "%"
    return score
print(get_points(answers,user_answ))
