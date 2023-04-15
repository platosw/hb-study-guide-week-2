# Create your classes here
class Student:
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question:
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        answer = input(f'{self.question} > ')
        return answer == self.correct_answer


class Exam:
    def __init__(self, name):
        self.exam_name = name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def administer(self):
        total_question = len(self.questions)
        count_correct = 0
        for question in self.questions:
            evaluate = question.ask_and_evaluate()

            if evaluate == True:
                count_correct += 1

        tally_of_correct_answers = (100 / total_question) * count_correct

        return tally_of_correct_answers


class StudentExam(Student, Exam):
    def __init__(self, first_name, last_name, address, exam_name):
        Student.__init__(self, first_name, last_name, address)
        Exam.__init__(self, exam_name)

    def take_test(self):
        return Exam.administer(self)


class StudentQuiz(Student, Exam):
    def __init__(self, first_name, last_name, address, exam_name):
        Student.__init__(self, first_name, last_name, address)
        Exam.__init__(self, exam_name)

    def take_quiz(self):
        result = Exam.administer(self)

        if result >= 50:
            return 1
        else:
            return 0
