from zipfile import ZipFile


with ZipFile("./data.zip", 'r') as zObject:
    zObject.extractall(
        path="./data")