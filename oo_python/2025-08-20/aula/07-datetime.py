from datetime import datetime, timedelta

agora = datetime.now()
# print(agora)
vespera_natal_2015 = datetime(2015,12,24,21,30,00)
print(vespera_natal_2015)
print(type(vespera_natal_2015))
print(vespera_natal_2015.year)

aniversario_tamyres = datetime(2025,10,1,23,37,50)
if agora < aniversario_tamyres: 
    print('ainda não chegou a hora de cantar parabéns')
else:
    print('o bolo já era')

diferenca = aniversario_tamyres - agora
print(f'Faltam {diferenca.days} dias para o aniversário de Tamyres.')


print('---')
inicio = aniversario_tamyres
print(inicio, type(inicio))
doze_dias_depois = timedelta(days=12,seconds=37, hours=2)
print(doze_dias_depois, type(doze_dias_depois))
fim_ferias = inicio + doze_dias_depois
print(f'O fim das férias será em {fim_ferias.strftime('%d/%m/%Y %H:%M:%S')}')
str_fim_ferias = '14/10/2025 01:38:27'
print(str_fim_ferias, type(str_fim_ferias))
data_fim_ferias = datetime.strptime(str_fim_ferias,'%d/%m/%Y %H:%M:%S')
print(data_fim_ferias, type(data_fim_ferias))