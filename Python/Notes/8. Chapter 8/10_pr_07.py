def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Miskatur is a good      "
n = remove_and_split(this, "Miskatur")
print(n)
# print(this)
# print(this.strip())
