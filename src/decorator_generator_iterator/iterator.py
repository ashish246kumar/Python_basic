class MyRange:
# Constructor to initialize the range with start and end values
    def __init__(self,start,end):
        self.start=start
        self.end=end
# This method makes the object iterable
    def __iter__(self):
        return self
# This method is used to return the next value in the range
    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        self.start+=1
        return self.start-1

my_range=MyRange(1,5)
# Iterate through the range and print each value
for i in my_range:
    print(i)