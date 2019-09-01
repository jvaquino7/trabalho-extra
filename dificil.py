conta = float(input("INFORME SUA CONTA:"))
senha = float(input("INFORME SUA SENHA:"))
saque = float(input("INFORME SEU SAQUE:"))

if conta == 999 and senha ==456:
	print("BEM VINDO")
else:
	print("CONTA E/OU SENHA INCORRETAS")

dinheiro = 100 - saque

if saque > 100:
	print("SALDO INSUFICIENTE")
else:
	print("SEU SALDO E DE:","R$", dinheiro,"REAIS")
	print("VOCE TIROU:","R$", saque, "REAIS")