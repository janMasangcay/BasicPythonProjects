import os

def getAllTxt():
    fPath = os.listdir('C:\\Users\\Student\\Desktop\\pythonCourse\\BasicPythonProjects\\fileIO')
    for txt in fPath:
        if txt.endswith('.txt'):
            print('\nFile name: {}\nFile mTime: {}'.format(txt, os.path.getmtime(txt)))


if __name__ == '__main__':
    getAllTxt()
