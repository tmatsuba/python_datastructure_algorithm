class Queue2Stacks(object):
    u"""stackを2つ使用して、queueを表現するクラス
    """
    def __init__(self):

        # Two Stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,element):

        self.stack1.append(element)

    def dequeue(self):


        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            return None

        return self.stack2.pop()











