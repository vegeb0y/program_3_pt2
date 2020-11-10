#josh Vegetabile
#Program 3

def main():
    test_list = open('rawTests.txt', 'r')
    student_list = open('students.txt', 'r')
    datasheet = open('gradeData.txt', 'w')
    answer_key = get_answers(test_list.readline())
    for student in test_list:
        student_score = student_scores(student, answer_key)
        letter_grade = assign_letter_grade(student_score)
        stud_id = student_id_num(student)
        print(stud_id,'\t',student_score,'\t',letter_grade,'\t')

def get_answers(array_answers):

    answer_key_answers = array_answers.split(';')[1]
    return list(answer_key_answers)

def student_scores(array_answers, answer_key):
    student_answers = get_answers(array_answers)
    correct_count = 0
    incorrect_count = 0
    index = 0
    while (index < len(answer_key)):
        if student_answers[index] != ' ':
            if(student_answers[index] == answer_key[index]):
                correct_count += 1
            else:
                incorrect_count += 1
        index += 1 
    score = (correct_count) - (incorrect_count * .25)
    return score
def assign_letter_grade(score):

    if score > 46:
        grade = "A"
    elif score >= 44:
        grade = "A-"
    elif score >= 42:
        grade = "B+"
    elif score >= 40:
        grade = "B"
    elif score >= 38:
        grade = "B-"
    elif score >= 36:
        grade = "C+"
    elif score >= 34:
        grade = "C"
    elif score >= 32:
        grade = "C-"
    elif score >= 30:
        grade = "D"
    elif score < 30:
        grade = "F"
    return grade

def student_id_num(id):
    stud_id = id.split(';')[0]
    return (stud_id)

    
main()
