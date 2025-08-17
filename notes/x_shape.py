def draw_x(n):
    for i in range(n):
        line = [' '] * n
        line[i] = '*'
        line[n - i - 1] = '*'
        print("".join(line))
        
if __name__ == "__main__":
    try:
        n = int(input("Enter number of lines for X shape: "))
        draw_x(n)
    except ValueError:
        print("Please enter a valid integer.")
