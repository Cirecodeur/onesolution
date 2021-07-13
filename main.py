import json
import random


class Questions:
    LISTESDEQUESTIONS = []

    def __init__(self, **list_questions):
        for attr_name, attr_value in list_questions.items():
            setattr(self, attr_name, attr_value)

    @classmethod
    def initialize_questions(cls):
        for list_questions in json.load(open("questions.json", encoding='utf-8')):
            question = Questions(**list_questions)
            # print(question.r1)
            # str(question))
            #print(dir(question))
            cls.LISTESDEQUESTIONS.append(question)
        random.shuffle(cls.LISTESDEQUESTIONS)

    @classmethod
    def shuffleQuestions(cls):
        random.shuffle(cls.LISTESDEQUESTIONS)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Questions.initialize_questions()
    Questions.shuffleQuestions()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
