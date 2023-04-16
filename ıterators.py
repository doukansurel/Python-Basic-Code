"""
list = [1,2,3,4,5,6,7,8,9,10]

iterator = iter(list)

while True : 
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break

"""

class example:
    def ___init__(self,start,stop):
        self.start = start
        self.stop = stop 
    def __iter__(self):
        return self

    def __next__(self):
        if self. start <= self.stop:
            x = self.start
            self.start += 1 
            return x 
        else :
            raise StopIteration("Iterator Exception")
    

list = example(10,20)



