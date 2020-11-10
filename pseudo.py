student_answers = ['a', 'b', 'd']
answerKeyAnswers = ['b', 'c', 'd']

print('len')
print(len(student_answers))

correct_answers = 0
incorrect_answers = 0

index = 0
while (index < len(answerKeyAnswers)):
    if(student_answers[index] != ' '):
      if(student_answers[index] == answerKeyAnswers[index]):
          correct_answers += 1
      else:
        incorrect_answers += 1
    index += 1

print(correct_answers, incorrect_answers)