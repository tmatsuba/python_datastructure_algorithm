# --- coding: utf-8 ---

from unittest import TestCase
from stack_queue_deques.queue_two_stack import Queue2Stacks


class TestQueue2Stacks(TestCase):

    def test_queue2stacks(self):
        q = Queue2Stacks()
        for i in range(5):
            q.enqueue(i)

        for i in range(5):
            self.assertEqual(i, q.dequeue())

        qnone = Queue2Stacks()
        self.assertEqual(qnone.dequeue(), None)
