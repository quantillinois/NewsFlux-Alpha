import os
"""

breaks up text files to be submitted to claude.ai

"""
def split_text_file(input_file, output_dir, max_file_size=99 * 1024):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open the input file for reading
    with open(input_file, 'r') as f:
        current_file_index = 1
        current_file_size = 0
        current_file = None

        for line in f:
            line_size = len(line.encode('utf-8'))

            # If the current file is None or adding the line exceeds the max size
            if current_file is None or current_file_size + line_size > max_file_size:
                if current_file:
                    current_file.close()
                current_file = open(os.path.join(output_dir, f'output_{current_file_index}.txt'), 'w')
                current_file_index += 1
                current_file_size = 0

            current_file.write(line)
            current_file_size += line_size

        # Close the last open file
        if current_file:
            current_file.close()

if __name__ == '__main__':
    input_file = './large_input.txt'  # Replace with the path to your input file
    output_directory = './output_files/'  # Replace with the desired output directory
    max_file_size = 99 * 1024  # Maximum file size in bytes (99 KB)

    split_text_file(input_file, output_directory, max_file_size)
