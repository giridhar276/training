import gzip
import shutil

# GZIP is generally used to compress a single file.
# Here we compress students.txt into students.txt.gz.

with open("students.txt", "rb") as source_file:
    with gzip.open("students.txt.gz", "wb") as gzip_file:
        # Copy content from normal file to compressed gzip file
        shutil.copyfileobj(source_file, gzip_file)

print("GZIP file created successfully: students.txt.gz")


# Read gzip file directly without manually extracting
with gzip.open("students.txt.gz", "rt", encoding="utf-8") as gzip_file:
    content = gzip_file.read()

print("Content inside GZIP file:")
print(content)


# Extract gzip file back to normal text file
with gzip.open("students.txt.gz", "rb") as source_file:
    with open("students_extracted.txt", "wb") as output_file:
        shutil.copyfileobj(source_file, output_file)

print("GZIP file extracted successfully: students_extracted.txt")
