import zipfile

zip_path = "path/to/your/zipfile.zip"

txt_path = "path/to/your/textfile.txt"

with zipfile.ZipFile(zip_path, 'r') as myzip:

    first_file = myzip.namelist()[0]

    file_contents = myzip.read(first_file).decode('utf-8')

    with open(txt_path, 'w') as outfile:
        outfile.write(file_contents)

print("Conversion complete!")
