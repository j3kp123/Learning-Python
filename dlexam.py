def correct_exam():
    print('The correct exam answers: ')
    correct_list = ['1. A', '2. C', '3. A', '4. A', '5. D', '6. B', '7. C', '8. A', '9. C', '10. B',
                    '11. A', '12. D', '13. C', '14. A', '15. D', '16. C', '17. B', '18. B', '19. D', '20. A']
    return correct_list

def student_answers():
    answer_list = []
    f = open('testfile.txt', 'r')
    for i in f:
        i = i.rstrip('\n')
        answer_list.append(i)
    return answer_list
    f.close()
    
def check(correct_list, answer_list):
    count = 0
    print(correct_list)
    print(answer_list)
    wrong_answers = []
    for i in range(20):
        if correct_list[i] == answer_list[i]:
            count += 1
        else:
            wrong_answers.append(i)
            count += 0
    if count < 15:
        print('\nI am sorry but you have failed the exam.')
    else:
        print('\nCongratulations! You passed.')
    print('\nThe number you answered correctly: ', count)
    print('\nThe number you answered incorrectly: ', 20 - count)
    print('\nThe questions you missed: ',
          wrong_answers)

def main():
    correct_list = correct_exam()
    answer_list = student_answers()
    check(correct_list, answer_list)

main()
