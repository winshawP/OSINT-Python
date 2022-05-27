from googlesearch import search # =>Necessário instalar biblioteca do Google. comando: pip install google

#Dork utilizada: "cpf|cnpj|email|rg|contato" ext:xls "SEU_ALVO"
def pegar_cpf():

        cpf1=str(input("digite o numero do cpf, cnpj, email ou RG para pesquisa:\nuse como base o exemplo: xxx.xxx.xxx-xx\n=>"))
        return cpf1



cpf1=pegar_cpf()



query = '"'  + "cpf|cnpj|email|rg|contato " + '"'+ "ext:xls " + '"' + cpf1 + '"' #Aqui é onde monto a dork para ser utilizada.
print("Resultados encontrados:\n")
#dork: "cpf|cnpj|email|rg|contato" ext:xls "SEU_ALVO"
for link in search(query, tld="com", num=10, stop=10, pause=2):
    print(link)
