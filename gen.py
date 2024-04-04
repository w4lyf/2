
def print_before_after(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@print_before_after
def generate_even_numbers(n):
    for i in range(2, n+1, 2):
        yield i

if __name__ == "__main__":
    n = int(input("Enter the limit for even numbers: "))
    print("Generated even numbers:")
    for num in generate_even_numbers(n):
        print(num)
