import os
import sys

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

sys.path.append(PATH('../games/templates/'))
from base_class import BaseClass

class ParentalAccess(BaseClass):
    
    def parental_access(self, question):
        
        question1 =  self.get_text(question)
        question = question1.split(' ')
        answer = None
        if question[1] == 'x':
            answer = (int(question[0])) * (int(question[2]))
        elif question[1] == '+':
            answer = (int(question[0])) + (int(question[2]))
        elif question[1] == '-':
            answer = (int(question[0])) - (int(question[2]))
        else:
            print 'Math operation unidentified'
            
        print 'Answer for ' + question1 + ' ' + str(answer)
        ans = str(answer)
        keys = self.altdriver.find_elements('Text')
        
        for j in range(len(ans)):
            for i in range(len(keys)):
                try:
                    if ans[j] == keys[i].get_text():
                        keys[i].tap()
                except:
                    break

