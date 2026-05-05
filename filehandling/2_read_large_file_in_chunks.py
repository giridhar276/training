

#C#hunk reading means reading fixed-size data, like 1 KB or 4 KB, at a time.
#Useful when reading very large text files, large reports, or exported data files.

# Read large file in chunks

def read_file_in_chunks(file_path, chunk_size=1024):
    with open(file_path, "r", encoding="utf-8") as file:
        
        while True:
            # Read fixed-size chunk
            chunk = file.read(chunk_size)

            # If no data left, stop loop
            if not chunk:
                break

            print(chunk)


read_file_in_chunks("large_log.txt", 1024)