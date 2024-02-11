# Faturamento estado
faturamento_sp = 67836.43
faturamento_rj = 36678.66
faturamento_mg = 29229.88
faturamento_es = 27165.48
faturamento_outros = 19849.53

# total
faturamento_total = faturamento_sp + faturamento_rj + faturamento_mg + faturamento_es + faturamento_outros

# Calcular percentuais
percentual_sp = (faturamento_sp / faturamento_total) * 100
percentual_rj = (faturamento_rj / faturamento_total) * 100
percentual_mg = (faturamento_mg / faturamento_total) * 100
percentual_es = (faturamento_es / faturamento_total) * 100
percentual_outros = (faturamento_outros / faturamento_total) * 100

# Resultados
print("Percentual de representação de cada estado:")
print("SP:", round(percentual_sp, 2), "%")
print("RJ:", round(percentual_rj, 2), "%")
print("MG:", round(percentual_mg, 2), "%")
print("ES:", round(percentual_es, 2), "%")
print("Outros:", round(percentual_outros, 2), "%")