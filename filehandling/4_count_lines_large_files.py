

# Count number of lines in a large file
# For huge files, we should not use file.readlines() because it loads all lines into memory.
#Counting rows in large CSV files, logs, audit files, and report files.


def count_lines(file_path):
    line_count = 0

    with open(file_path, "r", encoding="utf-8") as file:
        
        # Reads one line at a time
        for line in file:
            line_count += 1

    return line_count


total_lines = count_lines("large_log.txt")
print("Total lines:", total_lines)