import datetime
import locale
import math

locale.setlocale(locale.LC_ALL)

user = input("Usuario do discord (ex: @xpto#123): ")
name = input("Nome do Personagem: ")
prod = input("Produção por dia do seu tier (só numero) (Young: 25, Adult: 50, Ancient: 100, Legendary: 200): ")
desc = input("Descrição do que esta produzindo: ")
cost = input("Custo de produção (Apenas numero em PO): ")
date = datetime.datetime.now()
days = math.ceil(float(cost)/float(prod))
cool = math.ceil(float(cost)/float(prod)/2)

#print("Eu: "+user+"como: "+name+"Estou produzindo: "+desc+"Valor para construção completa: "+cost+" PO"+"Data e horário de início: "+date+"Data e horário de término: "+"Data e horário de término do CD: ")
ct = datetime.datetime.now()
endprod = ct.replace(day=ct.day+days)
endcd = endprod.replace(day=endprod.day+cool)


print("Eu: " + user)
print("Como: "+ name)
print("Estou produzindo: "+ desc)
print("Valor para construção completa: "+ cost)
print("Data e horário de início: "+ date.strftime('%d/%m %A %H:%M'))
print("Data e horário de término: "+ endprod.strftime('%d/%m %A %H:%M'))
print("Data e horário de término do CD: "+ endcd.strftime('%d/%m %A %H:%M'))
