ano_nascimento = int(input("Em que ano você nasceu?"))

print(f"Sua idade ao final de 2025: {2025 - ano_nascimento}")
altura = float(input("Qual a sua altura (m) "))
peso = float(input("Qual o seu peso? "))

print(f"Seu IMC é peso/altura: {(peso / (altura ** 2)):.2f}")
