import zipfile

# ZIP is used to store and compress multiple files together.
# Here we are adding students.txt, sales.csv, and config.json into one ZIP file.

with zipfile.ZipFile("sample_files.zip", "w", compression=zipfile.ZIP_DEFLATED) as zip_file:
    # Add students.txt into the ZIP file
    zip_file.write("students.txt")

    # Add sales.csv into the ZIP file
    zip_file.write("sales.csv")

    # Add config.json into the ZIP file
    zip_file.write("config.json")

print("ZIP file created successfully: sample_files.zip")


# Read files inside ZIP
with zipfile.ZipFile("sample_files.zip", "r") as zip_file:
    print("Files inside ZIP:")
    for file_name in zip_file.namelist():
        print(file_name)


# Extract all files from ZIP into a folder
with zipfile.ZipFile("sample_files.zip", "r") as zip_file:
    zip_file.extractall("zip_output")

print("ZIP file extracted successfully into zip_output folder")
