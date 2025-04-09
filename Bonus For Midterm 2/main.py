import re

def get_unique_words(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the file content
            content = file.read()
            
            # Check if the file is empty
            if not content.strip():
                print("The file is empty.")
                return
            
            # Split the content into words and normalize to lowercase
            words = re.findall(r'\b\w+\b', content.lower())
            
            # Get unique words using a set
            unique_words = set(words)
            
            # Display the unique words
            print("Unique words found in the file:")
            for word in sorted(unique_words):
                print(word)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Specify the file path
    file_path = input("Hello Please Enter the path to the text file that you would like read: ")
    
    # Strip any leading or trailing quotation marks
    file_path = file_path.strip('"').strip("'")
    
    # Call the function
    get_unique_words(file_path)

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")