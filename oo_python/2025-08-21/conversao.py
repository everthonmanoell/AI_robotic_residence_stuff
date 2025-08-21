import sys

if len(sys.argv) > 3:
    print(f"Uso indetivo! python3 {sys.argv[0]} ESCALA(c2f, f2c) VALOR")

else:
    if sys.argv[1] == "c2f":

        # (0 °C × 9/5) + 32 = 32 °F c2f

        c = sys.argv[2]
        f = (c * 9 / 5) + 32
    else:
        # (0 °F − 32) × 5/9 = -17,78 °C f2c
        f = sys.argv[2]

        c = (f - 32) * 5 / 9
