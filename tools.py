# This module will contain all stuff that isn't directly connected to selling fish, but is used for doing that

from typing import List, Union
from pyclbr import Function

class Functions: # Functions that will be used for different classes
    def sorted_by_function(arr: List[object], comparator: Function, left: int = 0, right: int = -1) -> List[object]: # comparator(x: object, y: object) must return True only if <x> must be considered as smaller then <y>
        # Function uses MergeSort algorithm
        if right == -1:
            right = len(arr)-1
        if left == right:
            return [arr[left]]
        mid = (left + right) >> 1
        lft = Functions.sorted_by_function(arr, comparator, left, mid)
        rght = Functions.sorted_by_function(arr, comparator, mid+1, right)
        res = []
        i = 0
        j = 0
        while i < len(lft) or j < len(rght):
            if i < len(lft) and j < len(rght):
                if comparator(lft[i], rght[j]):
                    res.append(lft[i])
                    i += 1
                else:
                    res.append(rght[j])
                    j += 1
            else:
                if i < len(lft):
                    res.append(lft[i])
                    i += 1
                else:
                    res.append(rght[j])
                    j += 1
        return res