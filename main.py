import numpy as np

sodukoFile = open("soduko.txt","r")
sodukoString = "".join(sodukoFile.readlines()).replace("\n","")
print(sodukoString)
sodukoMartix = np.matrix(sodukoString)
print(sodukoMartix)
# sodukoArray = np.array(sodukoMatrix)
# print(sodukoArray)


