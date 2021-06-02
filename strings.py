cad = "mY fiRst cAd"
print(cad)

#print(dir(cad)) #all properties and methods

print(cad.title()) #My First Cad

print(cad.upper()) #all chars to uppercase

print(cad.lower()) #all chars to lowercase

print(cad.swapcase()) #My FIrST CaD

print(cad.capitalize()) #My first cad

print(cad.replace("cAd", "py").upper()) #MY FIRST PY

print(cad.count("cA")) #1

print(cad.replace("cAd", "py").upper().count("Y")) #2

print(cad.startswith("mY ")) #True

print(cad.endswith("  cAd")) #False

print(cad.split(" ")) #List

print(cad.find("fi"))

print(len(cad))

print(cad.index("Y"))

print(cad.isnumeric())

print(cad[len(cad) - 1])

print(f"PLZ {cad}")

print("PLZ {0}, {1}".format(cad, cad + cad))