import zipfile

# specify the path to the zip file you want to convert
zip_path = "path/to/your/zipfile.zip"

# specify the path to the text file you want to create
txt_path = "path/to/your/textfile.txt"

# open the zip file in read mode
with zipfile.ZipFile(zip_path, 'r') as myzip:

    # get the name of the first file in the zip archive
    first_file = myzip.namelist()[0]

    # extract the contents of the first file to a string variable
    file_contents = myzip.read(first_file).decode('utf-8')

    # write the contents of the file to a text file
    with open(txt_path, 'w') as outfile:
        outfile.write(file_contents)

# print a message to confirm that the conversion was successful
print("Conversion complete!")
