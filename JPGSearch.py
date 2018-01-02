import os

list_jpg = []

for root, dirs, files in os.walk("c:/****/******/"):
    for file in files:
        if file.endswith(".jpg"):
             #print(os.path.join(file))
             list_jpg.append(file.title())

for file in list_jpg:
    if file.startswith('Un'):
        print(file)