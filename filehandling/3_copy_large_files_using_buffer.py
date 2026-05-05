

# Copy large file using buffered reading and writing
#Copying large videos, backup files, database dumps, zip files, ISO files.

def copy_large_file(source_file, destination_file, buffer_size=1024 * 1024):
    # Open source in read-binary mode
    with open(source_file, "rb") as src:
        
        # Open destination in write-binary mode
        with open(destination_file, "wb") as dest:
            
            while True:
                # Read 1 MB at a time
                chunk = src.read(buffer_size)

                # Stop when file is completed
                if not chunk:
                    break

                # Write chunk to destination file
                dest.write(chunk)

    print("File copied successfully")


copy_large_file("large_video.mp4", "backup_video.mp4")