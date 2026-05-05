

import zipfile

# Create a ZIP file
# ZIP can store multiple files together
with zipfile.ZipFile("sample_files.zip", "w", compression=zipfile.ZIP_DEFLATED) as zip_file:

    # Add students.txt into zip
    zip_file.write("students.txt")

    # Add sales.csv into zip
    zip_file.write("sales.csv")

    # Add config.json into zip
    zip_file.write("config.json")

print("ZIP file created successfully")