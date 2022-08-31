import os
opcao = 0
lst_vazia = []
cada_despesa = []
cada_receita = []
def lin():
  print("-"*24) 

while opcao != 8:
    os.system('cls') # para windows use os.system('cls')
    print('### Controle de Finanças ###\n')
    lin()
    print("[1] Cadastrar Receitas")
    print("[2] Modificar Receitas")
    print("[3] Remover Receita")
    lin()
    print("[4] Cadastrar Despesas")
    print("[5] Modificar Despesas")
    print("[6] Remover Despesa")
    lin()
    print("[7] Gerar Relatório")
    print("[8] Sair")
    lin()
    lin()
    opcao = int(input("Digite a opção desejada: "))
    

    os.system('cls')
    if opcao == 1: # Casdastrar receita
      print("## Cadastro de Receitas\n")
      receita = float(input("Digite o valor da receita: "))
      cada_receita.append(receita)      

    if opcao == 2: # Modificar receita    
      print("Posições correspondentes a cada valor:")
      for r, elem in enumerate(cada_receita):
        print(r,": R$",elem)     
      posicao = int(input("Para modificar um valor digite a posição do mesmo: "))
      modificar = float(input("Novo valor: "))
      cada_receita[posicao] = modificar
      print("Receitas modificadas:")
      for mod_r in cada_receita:
        print("- R$",mod_r)

    if opcao == 3: # Remover receita
      print("#### Remover Receita ####\n")
      print("Receitas Atuais:")
      for antes_r in cada_receita:
        print("- R$",antes_r)
      remove_r = float(input("Insira o valor que deseja remover"))
      cada_receita.remove(remove_r)
      print("Receitas modificadas: ")
      for rem_r in cada_receita:
        print("- R$",rem_r)
    
    if opcao == 4: # Cadastrar despesa
      print("#### Cadastro de Despesa ####\n")
      despesa = float(input("Digite o valor da despesa: "))
      cada_despesa.append(despesa)

    if opcao == 5: # Modificar despesa
      print("#### Modificar Despesa ####\n")
      print("Posições correspondentes a cada valor:")
      for d, elem in enumerate(cada_despesa):
        print(d,": R$",elem)
      posicao_d = int(input("Para modificar um valor digite a posição do mesmo: "))
      modificar_d = float(input("Novo valor: "))
      cada_despesa[posicao_d] = modificar_d
      print("Despesas modificadas:")
      for mod_d in cada_despesa:
        print("- R$",mod_d)
    
    if opcao == 6: 
      print("#### Remover Despesa ####\n")
      print("Despesas Atuais:")
      for antes_d in cada_despesa:
        print("- R$",antes_d)
      remove_d = float(input("Insira o valor que deseja remover: "))
      cada_despesa.remove(remove_d)
      print("Despesas modificadas:")
      for rem_d in cada_despesa:
        print("- R$",rem_d)     
  
    if opcao == 7: # Gerar realtório
      # Receita total e despesa total:
      receita_total = sum(cada_receita)
      despesa_total = sum(cada_despesa)
      # Maior e menor receita:
      if cada_receita != lst_vazia:
        maior_receita = max(cada_receita)
        menor_receita = min(cada_receita)
      # Maior e menor despesa:
      if cada_despesa != lst_vazia:
        maior_despesa = max(cada_despesa)
        menor_despesa = min(cada_despesa)
      # Lucro ou prejuízo:
      total = receita_total-despesa_total
      print("#### Relatórios ####\n")  
      
      if cada_receita != lst_vazia:
        print("Receitas:")
        for recet in cada_receita:
          print("+ R$",recet)
        
        print("Maior receita: R$",maior_receita)
        print("Menor receita: R$",menor_receita)
        print()
        
      if cada_despesa != lst_vazia:
        print("Despesas:")
        for desp in cada_despesa:
          print("- R$",desp)     
        
        print("Maior despesa: R$",maior_despesa)
        print("Menor despesa: R$",menor_despesa)
        print()
      print("Total de receitas: R$",receita_total)
      print("Total de despesas: R$",despesa_total)
      
      if total > 0:
        print("Lucro total: R$",total)
      else:
        print("Prejuízo total: R$",total)
    input("Aperte 'ENTER' para continuar") 
print("Obrigado por usar o sistema!") 