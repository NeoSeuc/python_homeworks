from random import randint
from statistics import mean
from typing import List

generate_random_numbers = lambda count, min_value, max_value: [randint(min_value, max_value) for _ in range(count)]


def quick_sort(arr: List[int]) -> List[int]:
    """Sort a list using the QuickSort algorithm."""
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


separate_even_odd = lambda numbers: ([num for num in numbers if num % 2 == 0], [num for num in numbers if num % 2 != 0])
calculate_average = lambda numbers: mean(numbers) if numbers else 0


def main():
    """Main function to execute the program flow."""
    numbers = generate_random_numbers(100, 0, 1000)
    sorted_numbers = quick_sort(numbers)
    even_numbers, odd_numbers = separate_even_odd(sorted_numbers)
    even_avg = calculate_average(even_numbers)
    odd_avg = calculate_average(odd_numbers)

    print(f"Even average is {even_avg}")
    print(f"Odd average is {odd_avg}")


if __name__ == "__main__":
    main()
