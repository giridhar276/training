import tarfile

# TAR.GZ means:
# TAR  -> bundle multiple files
# GZIP -> compress the bundled archive

with tarfile.open("sample_files.tar.gz", "w:gz") as tar_file:
    # Add multiple files into compressed TAR.GZ archive
    tar_file.add("students.txt")
    tar_file.add("sales.csv")
    tar_file.add("config.json")

print("TAR.GZ file created successfully: sample_files.tar.gz")


# Read file names inside TAR.GZ archive
with tarfile.open("sample_files.tar.gz", "r:gz") as tar_file:
    print("Files inside TAR.GZ:")
    for file_name in tar_file.getnames():
        print(file_name)


# Extract all files from TAR.GZ archive
with tarfile.open("sample_files.tar.gz", "r:gz") as tar_file:
    tar_file.extractall("targz_output")

print("TAR.GZ file extracted successfully into targz_output folder")
