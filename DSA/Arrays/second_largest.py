def get_second_largest(numbers: list[int]) -> int | None:
    # EDGE CASE 1: Array is too small
    if not numbers or len(numbers) < 2:
        return None 
        
    # Initialize the podium
    largest = float('-inf')
    second_largest = float('-inf') 

    for num in numbers:
        # If we find a new Gold Medalist
        if num > largest:
            second_largest = largest
            largest = num
            
        # If we find a new Silver Medalist 
        # (Must be smaller than Gold to avoid counting duplicates)
        elif num > second_largest and num != largest:
            second_largest = num
            
    # EDGE CASE 2: All elements were identical (e.g., [10, 10, 10])
    if second_largest == float('-inf'):
        return None
        
    return int(second_largest)


if __name__ == "__main__":
    # 1. Standard Case
    print(f"Standard: {get_second_largest([12, 35, 1, 10, 34, 1])}")  # Output: 34
    
    # 2. Strictly Decreasing
    print(f"Decreasing: {get_second_largest([80, 40, 20, 10])}")      # Output: 40
    
    # 3. All Duplicates (Edge Case)
    print(f"Duplicates: {get_second_largest([10, 10, 10])}")          # Output: None
    
    # 4. Too Small (Edge Case)
    print(f"Too Small: {get_second_largest([5])}")                    # Output: None
    
    # 5. Empty List (Edge Case)
    print(f"Empty: {get_second_largest([])}")                         # Output: None
    
    # 6. Negative Numbers
    print(f"Negatives: {get_second_largest([-10, -5, -20])}")         # Output: -10
