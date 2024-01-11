from flask import Flask
import os
app = Flask(__name__)


@app.get('/path/<string:path>')
def get_path(path):
    print(path)
    existing_files = []
    os.system(f"find {path} -type f > files.txt")
    with open("files.txt", 'r') as file:
        files = file.read()
    for line in files.split("\n"):
        name = line.split("/")[-1]
        if name != '':
            existing_files.append(name)
    files_no = len(set(existing_files))
    os.remove("files.txt")
    return f"the number of files {files_no}"


app.run(host='127.0.0.1', port=5000)
