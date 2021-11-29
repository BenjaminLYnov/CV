import os

absFilePath = os.path.abspath(__file__)
path, filename = os.path.split(absFilePath)
os.system("cd " + path + " && git add * && git commit -m \"last commit\" && git push --set-upstream origin master")
input('\n\n\n\n\nAppuyer sur Entrée pour fermer...')
