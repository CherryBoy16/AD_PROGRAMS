def sum_of_evens(n):
    if n <= 0:
        return "Please enter a positive integer greater than 0."

    even_sum = sum(i for i in range(2, n + 1, 2))
    return even_sum
try:
    n = int(input("Enter a positive integer: "))
    result = sum_of_evens(n)
    print(f"The sum of all even numbers between 1 and {n} is: {result}")
except ValueError:
    print("Please enter a valid positive integer.")