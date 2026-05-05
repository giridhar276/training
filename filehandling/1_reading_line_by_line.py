

# Large file reading line by line
#Instead of loading the full file into memory, we read one line at a time.

def read_large_file_line_by_line(file_path):
    # with automatically closes the file
    with open(file_path, "r", encoding="utf-8") as file:
        
        # Reads one line at a time
        for line in file:
            print(line.strip())


read_large_file_line_by_line("large_log.txt")