# read, edit a file
def separate_odd_even(input_file, odd_file='odd.txt', even_file='even.txt'):
    try:
        with open(input_file, 'r') as infile, \
             open(odd_file, 'w') as odds, \
             open(even_file, 'w') as events:

            for line in infile:
                line = line.strip()
                if not line:
                    continue
                try:
                    num = int(line)
                    if num % 2 == 0:
                        events.write(str(num) + "\n")
                    else:
                        odds.write(str(num) + "\n")
                except ValueError:
                    print(f"{line} is not valid, ignored.")
        print("Numbers separated successfully.")
    except FileNotFoundError:
        print(f"{input_file} is not found. Please run '01Generate-File' first.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"Unexpected error: {e}")

separate_odd_even('data.txt')