import os


def createifnot(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def move(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")


if __name__ == '__main__':
    file = os.listdir()
    file.remove("Folder_Cleaner.py")

    createifnot('Images')
    createifnot('Videos')
    createifnot('Python')
    createifnot('Others')

    imgExist = [".png", ".jpg", ".ico", ".jpeg"]
    Images = [file for file in file if os.path.splitext(file)[
        1].lower() in imgExist]
    vdoExist = [".wmv", ".mp4", ".webm"]
    vdo = [file for file in file if os.path.splitext(
        file)[1].lower() in vdoExist]
    PythonExist = [".py"]
    Python = [file for file in file if os.path.splitext(
        file)[1].lower() in PythonExist]
    Others = []
    for file in file:
        ext = os.path.splitext(file)[1].lower()
        if(ext not in imgExist) or (ext not in vdoExist) or (ext not in PythonExist) or os.path.isfile(file):
            Others.append(file)
        move("Images", Images)
        move("Videos", vdo)
        move("Python", Python)
        move("Others", Others)
