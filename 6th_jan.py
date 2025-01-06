a = "python"
b = "java"
c = "c++"
d = "c#"
e = "react"
f = "javascript"

print("Concatenation")
print(a + " and " + b)
print(c + " or " + d)

print("Length")
print(len(a))
print(len(e))

print("Repetition")
print(f * 2)
print(a * 3)

print("Indexing and Slicing")
print(b[1])
print(e[0:3])
print(f[-4:])

print("lower()")
print(a.lower())
print(f.lower())

print("Upper()")
print(e.upper())
print(b.upper())

print("Strip")
print("   python programming   ".strip())
print("\t learn react now!   ".strip())

print("Replace")
print(a.replace("python", "ruby"))
print(d.replace("c#", "java"))

print("Split")
print(f.split(" "))
print(e.split("e"))

print("Find")
print(c.find("+"))
print(b.find("v"))
print(a.find("z"))

print("Join")
print("-".join(e))
print(" ".join(f))
