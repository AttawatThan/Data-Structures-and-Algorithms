from typing import List, Optional, Union

def binary_search(arrays: List[Union[int, float]], item) -> Optional[int]:
    low: int = 0
    high: int = len(arrays) - 1
    while low <= high:
        mid: int = (low + high) // 2
        guess: Union[int, float] = arrays[mid]
        
        if guess==item:
            return mid
        # Too High
        elif guess > item:
            high = mid - 1
        # Too Low
        elif guess < item:
            low = mid + 1
    return None

if __name__ == "__main__":
    # array must sorted
    arr = [1, 3, 5, 8, 9, 12, 16, 24]
    item = 50
    print(f"index of item: {item} in array: {arr} is: {binary_search(arr, item)}")