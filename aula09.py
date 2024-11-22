frase = "Curso em Video python"
print(frase.upper().count("O"))

print("""
Python é uma linguagem de programação de alto nível, interpretada, 
de propósito geral e bastante popular entre desenvolvedores por sua simplicidade e legibilidade.
 Ela foi criada por Guido van Rossum e lançada em 1991.
""")
print(frase.split())
print(len(frase))
#Mandando trocar pyhton por android
print(frase.replace("python", "Java"))
print("Curso" in frase)
print(frase.find("Video"))

frase2= "Curso em Video Android"
dividido = frase2.split()
print(dividido[2] [3])