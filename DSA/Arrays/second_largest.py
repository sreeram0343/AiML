from typing import List, Optional

def get_second_largest(numbers: List[int]) -> Optional[int]:
    """
    Finds the second largest distinct integer in an array.
    Returns None if no second largest exists.
    """
    if len(numbers) < 2:
        return None 
        
    largest = float('-inf')
    second_largest = float('-inf') 

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
            
    if second_largest == float('-inf'):
        return None
        
    return second_largest

# Testing the bulletproof code
print(get_second_largest([10, 20, 40, 80]))  # Output: 40
print(get_second_largest([10, 10, 10]))      # Output: None
print(get_second_largest([5]))               # Output: None