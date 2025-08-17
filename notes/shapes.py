def draw_hollow_square(n):
    border = '*' * n
    middle = '*' + ' ' * (n - 2) + '*' if n > 1 else '*'
    print("\nHollow Square:")
    print(border)
    for _ in range(n - 2):
        print(middle)
    if n > 1:
        print(border)


def draw_x_in_hollow_square(n):
    print("\nX inside Hollow Square:")
    for i in range(n):
        line = []
        for j in range(n):
            if i in [0, n - 1] or j in [0, n - 1] or i == j or j == n - i - 1:
                line.append('*')
            else:
                line.append(' ')
        print("".join(line))


def draw_pascals_triangle(n):
    print("\nPascal's Triangle:")
    for i in range(n):
        print(" " * (n - i), end="")
        val = 1
        for j in range(i + 1):
            print(f"{val} ", end="")
            val = val * (i - j) // (j + 1)
        print()


def draw_rhombus(n):
    print("\nRhombus:")
    row = '*' * n
    for i in range(n):
        print(" " * (n - i - 1) + row)


if __name__ == "__main__":
    try:
        n = int(input("Enter the number of lines for the shapes: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            draw_hollow_square(n)
            draw_x_in_hollow_square(n)
            draw_pascals_triangle(n)
            draw_rhombus(n)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
