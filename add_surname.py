# Kai Geller
# GitHub Username
# 5/4/2022
# This is trying to find the names that start with K and add Kardashian to the end of them
def add_surname(names):
    """This function will find which names start with K and add Kardashian as their surname"""
    new_names=[]
    for i in range(len(names)):
        if names[i][0] == "K":
            new_names.append(names[i]+" Kardashian")
    return (new_names)
