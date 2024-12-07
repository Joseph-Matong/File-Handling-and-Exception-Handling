def read_and_modify_file(input_filename, output_filename):
    """
    Reads content from an input file, modifies it, and writes to an output file.

    Parameters:
    - input_filename (str): Name of the file to read from.
    - output_filename (str): Name of the file to write the modified content to.
    """
    try:
        # Read the content of the file
        with open(input_filename, 'r') as infile:
            content = infile.readlines()

        # Modify the content (e.g., adding line numbers)
        modified_content = [
            f"{index + 1}: {line.strip()}\n" for index, line in enumerate(content)
        ]

        # Write the modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)

        print(f"Modified content successfully written to {output_filename}.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError as e:
        print(f"An IOError occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to prompt the user for filenames and call the read-and-modify function.
    """
    print("File Read & Write Challenge 🖋️")
    input_filename = input("Enter the name of the file to read: ")
    output_filename = input("Enter the name of the file to write modified content to: ")

    # Perform the read and write operation
    read_and_modify_file(input_filename, output_filename)

if __name__ == "__main__":
    main()
