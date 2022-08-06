import os
import shutil
extensions = []
pdf = []
txt = []
exe = []
vid = []
img = []
mode = 0o666

os.chdir("C:\\Users\\thwan\\Downloads")
extensions.append(os.listdir(os.getcwd()))


for f_names in os.listdir(os.getcwd()):
    if f_names.endswith('.pdf'):
        pdf.append(f_names)
    elif f_names.endswith('.txt'):
        txt.append(f_names)
    elif f_names.endswith(".exe"):
        exe.append(f_names)
    elif f_names.endswith(".mp4" or ".mov"):
        vid.append(f_names)
    elif f_names.endswith(".jpg" or ".png" or ".psd"):
        img.append(f_names)
    else:
        pass

for i in img:
    try:
        folder = "D://Pictures"
        name = "Download"
        path = os.path.join(folder, name)
        os.mkdir(path, mode)
        shutil.move(os.getcwd()+"//"+i, "D://Pictures"+"//"+name)
    except:
        name = "Download"
        shutil.move(os.getcwd() + "//" + i, "D://Pictures" + "//" + name)

for i in exe:
    try:
        shutil.move(os.getcwd() + "//" + i, "D://Row")
    except:
        print("Error while moving the exe list")

for i in vid:
    try:
        shutil.move(os.getcwd() + "//" + i, "D://Video")
    except:
        print("error while moving the video files")

for i in pdf:
    try:
        os.mkdir("pdf")
        shutil.move(os.getcwd()+"//"+i, os.getcwd()+"//"+"pdf"+"//"+i)
    except:
        shutil.move(os.getcwd() + "//" + i, os.getcwd() + "//" + "pdf" + "//" + i)

for i in txt:
    try:
        os.mkdir("text files")
        shutil.move(os.getcwd() + "//" + i, os.getcwd() + "//" + "text files" + "//" + i)

    except:
        shutil.move(os.getcwd() + "//" + i, os.getcwd() + "//" + "text files" + "//" + i)























