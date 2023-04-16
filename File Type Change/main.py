import os
os.getcwd()
#IMG_6049_00
#IMG_6049_00.jpeg


#Yeni klasör (2)

file_cont= os.listdir("C:\\Users\\d_ali\\Desktop\\KendiVerisetim2")
print(len(file_cont))
counter = 3041
collection = "C:\\Users\\d_ali\\Desktop\\KendiVerisetim2"

file_type=".txt"

for i, filename in enumerate(os.listdir(collection)):
    os.rename("C:\\Users\\d_ali\\Desktop\\KendiVerisetim2\\" + filename, "C:\\Users\\d_ali\\Desktop\\KendiVerisetim2\\" +str(counter)+file_type)
    counter = counter+1

print(counter)