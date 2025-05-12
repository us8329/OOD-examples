'''
Purpose: Define a family of interchangeable algorithms, encapsulate each one, and make them interchangeable at runtime.
Key Points:
    1. Context holds a reference to a Strategy interface
    2. Concrete strategies implement the algorithm

modify or extend behavior of class without changing it 

Follow Open-Closed Principle 
'''

from abc import ABC, abstractmethod

class FilterStrategy(ABC):

    @abstractmethod
    def removeValue(self,val):
        pass


class RemoveNegativeStrategy(FilterStrategy):
    def removeValue(self, val):
        return val<0

class RemoveOddStrategy(FilterStrategy):
    def removeValue(self, val):
        return abs(val) % 2
    
    
class Values:
    def __init__(self,vals):
        self.vals = vals
    
    def filter(self,strategy):
        res = []
        for n in self.vals:
            if not strategy.removeValue(n):
                res.append(n)
        return sorted(res)

values = Values([-7,-5,-4,0,19,-2,56,3,2,8])

print(values.filter(RemoveNegativeStrategy()))
print(values.filter(RemoveOddStrategy()))