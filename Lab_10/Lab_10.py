from array import array
from ctypes import Array
from typing import Tuple


def binary_search(numbers: Array, value: int) -> Tuple[bool, int]:
    p=0
    k=len(numbers)-1
    while(p<=k):
        middle = int((p+k)/2)
        if value==numbers[middle]:
            return True,middle
        elif value>numbers[middle]:
            p+=1
        else:
            k-=1
    return False,-1

x = array('i',[0,4,7,11,55,99])
print(binary_search(x,2))
print(binary_search(x,55))