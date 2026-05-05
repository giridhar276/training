import tarfile

# TAR is used to bundle multiple files into one archive.
# TAR by itself does not compress unless we use tar.gz.

with tarfile.open("sample_files.tar", "w") as tar_file:
    # Add multiple files into TAR archive
    tar_file.add("students.txt")
    tar_file.add("sales.csv")
    tar_file.add("config.json")

print("TAR file created successfully: sample_files.tar")


# Read file names inside TAR archive
with tarfile.open("sample_files.tar", "r") as tar_file:
    print("Files inside TAR:")
    for file_name in tar_file.getnames():
        print(file_name)


# Extract all files from TAR archive
with tarfile.open("sample_files.tar", "r") as tar_file:
    tar_file.extractall("tar_output")

print("TAR file extracted successfully into tar_output folder")
