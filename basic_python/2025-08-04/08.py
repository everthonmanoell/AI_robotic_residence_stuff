lunch_out = int(input("Quantas vezes por semana você almoça fora? "))
lunch_price = float(input("Qual o preço de um almoço, na média? "))
market_per_week = float(input("Quanto gasta de feira em supermercado na semana? "))

print("=" * 3, "GASTO MÉDIO", "=" * 3)

lunch_week = lunch_price * lunch_out
all_sum = lunch_week + market_per_week

print(f"Diário: R${(lunch_week / 7):.1f}")
print(f"Semanal: R${all_sum}")
