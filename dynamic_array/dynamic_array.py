import sys

class DynamicArray(object):
    
    def __init__(self):
        
        self.n = 0
        self.A = self.make_array(1)
        
    def __len__(self):
        return self.n
    
    def __getitem__(self, k):
        
        if not 0 <= k < self.n:
            return IndexError('K is out of bounds!')
        
        return self.A[k]
    
    def __sizeof__(self):
         return (sys.getsizeof(self.A) - 64) /  8
    
    def append(self, ele):
        if self.n == self.__sizeof__() :
            self._resize(2* self.__sizeof__()) # 2x if capacity isn't enough
            
        self.A[self.n] = ele
        self.n += 1
        
    def _resize(self, new_cap):
        
        B = self.make_array(new_cap)
        
        for k in range(self.n):
            B[k] = self.A[k]
            
        self.A = B
        
    def make_array(self, new_cap):

        return [0] * int(new_cap)
