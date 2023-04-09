from deq import DEQUEUE 

class pal:
    def __init__(self):
        self.deq = DEQUEUE()

    def __repr__(self):
        return str(self.deq)
    
    def is_pal(self, word):
        for c in word:
            self.deq.add_rear(c)

    
    # def check(self):
    #     while self.deq:
    #         front = self.deq.remove_front()
    #         back = self.deq.remove_rear()

    #         print(front)
    #         print(back)

    #         if front != back:
    #             return False
    #         return True