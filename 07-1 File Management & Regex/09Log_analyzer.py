import os
import re
import unittest

# ----------------------- Core Functions -----------------------

def get_user_directory():
    path = input("Enter the directory path to scan for '.log' files (e.g., ./logs or C:/logs): ").strip()
    return path

def find_log_files(directory):
    log_files = []
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        return log_files

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.log'):
                full_path = os.path.join(root, file)
                log_files.append(full_path)
    return log_files

def count_errors_in_text(text):
    pattern = r'ERROR\s*(?<!\d)\d{4}(?!\d)'
    matches = re.findall(pattern, text, re.IGNORECASE)
    return len(matches)

def count_errors_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        return count_errors_in_text(content)
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            content = f.read()
        return count_errors_in_text(content)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return 0

def generate_summary(directory):
    log_files = find_log_files(directory)
    if not log_files:
        print("No '.log' files found in the specified directory.")
        return

    error_counts = {}
    for filepath in log_files:
        count = count_errors_in_file(filepath)
        filename = os.path.basename(filepath)
        error_counts[filename] = count

    total_errors = sum(error_counts.values())

    summery_path = os.path.join(os.getcwd(), 'summary.txt')
    try:
        with open(summery_path, 'w', encoding='utf-8') as f:
            f.write("Summery of Errors:\n")
            for filename, count in error_counts.items():
                f.write(f"{filename}: {count}\n")
            f.write(f"Total Errors: {total_errors}\n")
        print(f"Summery successfully written to {summery_path}.")
    except Exception as e:
        print(f"Failed to write summery: {e}")

def main():
    directory = get_user_directory()
    if directory:
        generate_summary(directory)


# ----------------------- Unit Tests (unittest) -----------------------

class TestAnalyzer(unittest.TestCase):
    def test_count_errors_basic(self):
        text = "This is an ERROR 4040 and another 5001 here."
        self.assertEqual(count_errors_in_text(text), 1)


    def test_count_errors_case_insensitive_and_no_space(self):
        text = "error 4040 and ERROR5001 and Error 2024"
        self.assertEqual(count_errors_in_text(text), 3)


    def test_count_errors_invalid_codes(self):
        # 3-digit, 5-digit, wrong keyword -> should not count
        text = "ERROR 404 (only 3 digits), ERROR 12345 (5 digits), INFO 9999, ERROR 12ab"
        self.assertEqual(count_errors_in_text(text), 0)


    def test_count_errors_multiline(self):
        text = "Line 1: ERROR 1111\nLine 2: ERROR 2222\nLine 3: Everything fine."
        self.assertEqual(count_errors_in_text(text), 2)


# -------------------------- Runner Logic --------------------------

if __name__ == "__main__":
    import sys

    # If the user passes 'test' as an argument, run unit tests.
    # Otherwise, run the main interactive program.
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        # Remove the 'test' argument so that unittest doesn't misinterpret it
        sys.argv = [sys.argv[0]]
        unittest.main()
    else:
        main()