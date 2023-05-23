import os

N = 10

for i in range(N):
    os.makedirs(os.path.join("D:\Python\w3resouce\Basic 1", "folder name " + str(i)), exist_ok=True)