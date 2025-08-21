nota = float(input("Digite uma nota:"))

if nota >= 9 and nota <= 10:
    print("Conceito A")
elif nota >= 8 and nota <= 9:
    print("Conceito B")
elif nota >= 7 and nota <= 8:
    print("Conceito C")
else:
    print("Conceito D (reprovado)")
