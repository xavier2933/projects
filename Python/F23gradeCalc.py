############################################################################################
"""
Final grade calculator for my fall 2023 semester
"""
############################################################################################

class gradeCalc:
    
    def __init__(self, classNumber):
        if classNumber == "1":
            print("Aerodynamics grader\/\/\/\/\/\/\/")
            exam1Score = input("input exam  1 score: > ")
            exam3Score = input("input exam  3 score: > ")
            finalScore = float(((float(exam1Score) + float(exam3Score) + 85)/300)*100)
            print("Final score: ", finalScore)
            self.weights = {
                "Exam 1": (15, exam1Score), # (weight, score)
                "Exam 2": (15, 85),
                "Exam 3": (15, exam3Score),
                "Final": (25, str(finalScore)),
                "Homework": (10, 100),
                "Quizzes": (10, 98),
                "Clicker": (10, 81.48)
            }

        elif classNumber == "2":
            print("Structures grader\/\/\/\/\/\/\/")
            finalGrade = input("input final grade: > ")
            self.weights = {
                "Clicker": (10, 85),
                "Quizzes": (10, 100),
                "Homework": (10, 100),
                "Exams": (20, 104),
                "Final": (50, finalGrade)
            }

        elif classNumber == "3":
            print("Thermo grader\/\/\/\/\/\/\/")
            examGrade = input("input exam 3 score: > ")
            finalGrade = input("input final grade: > ")
            self.weights = {
                "Quizzes": (20, 100),
                "Homework": (20, 92.78),
                "Exam1": (12, 78.25),
                "Exam2": (13, 88.25),
                "Exam3": (15, examGrade),
                "Final": (20, finalGrade)
            }

        elif classNumber == "4":
            print("Systems Grader/\/\/\/\/\/\/\/")
            examGrade = input("input exam grade: > ")
            self.weights = {
                "Labs": (42, 92.667),
                "Exams": (48, examGrade),
                "Quiz": (10, 96.833)
            }

        else:
            print("Invalid")
            exit()

    def calc(self):
        grade = 0
        for i in self.weights:
            grade += self.weights[i][0] * (float(self.weights[i][1]) * 0.01)

        print("Grade is: ", grade)


if __name__ == "__main__":
    inputStr = input("Enter last number of class code: > ")
    gc = gradeCalc(inputStr)
    gc.calc()
    exit()
