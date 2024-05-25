def recomendar_plano(consumo_mensal):
  if consumo_mensal <= 10:
    plano = "Plano Essencial Fibra - 50Mbps"
  elif consumo_mensal > 10 and consumo_mensal <= 20:
    plano = "Plano Prata Fibra - 100Mbps"
  else:
    plano = "Plano Premium Fibra - 300Mbps"
  return plano
consumo = float(input(""))
print(recomendar_plano(consumo))