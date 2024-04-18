import re
import sys

def parse_text_file(file_path):
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            for line in file:
                # Use regular expression to find the pattern 'N Failures'
                matches = re.findall(r'\b\d+ Failures\b', line)
                for match in matches:
                    failures_count = int(match.split()[0])
                    if failures_count == 0:
                        print("Success! No failures detected.")
                    else:
                        print(f"Error! {failures_count} failures detected.")
                        return False
        return True
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return False

# Example usage:
if __name__ == "__main__":
    file_path = sys.argv[1] # Replace with your file path
    result = parse_text_file(file_path)
    if result:
        print("File parsed successfully.")
    else:
    	raise Exception("Error encountered during file parsing.")

