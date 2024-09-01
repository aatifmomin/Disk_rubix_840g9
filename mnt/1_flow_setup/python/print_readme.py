#Ask the user for input
title = input("Please enter header line:")
contain = input("Comment:")
contain_2 = contain.split(".")

file_name = "README"

title = "\n---------------------------------------------------------------------------------\n"+title+"\n--------------------------------------------------------------------------------\n"

with open(file_name, "a") as file:
    file.write(title)
    for index, item in enumerate(contain_2,start=1):
        file.write(f"{index}. {item}")
        file.write(".\n")


