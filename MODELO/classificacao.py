import plotly.express as px
import pandas as pd

class Eletrodomesticos:
    def __init__(self):
        self.eletrodomesticos = []

    def inserir_dados(self):
        while True:
            nome_eletrodomestico = input("\nInforme o nome do eletrodoméstico (exemplo: Ar-condicionado), ou 'sair' para finalizar: ")
            
            if nome_eletrodomestico.lower() == 'sair':
                break
            
            try:
                potencia_watts = float(input("Informe a potência do eletrodoméstico em watts (W): "))
                horas_uso_dia = float(input("Informe o número de horas de uso diário: "))
                
                consumo_mensal_kwh = (potencia_watts * horas_uso_dia * 30) / 1000  
                
                limiar = 500  
                
                if consumo_mensal_kwh <= limiar:
                    categoria_consumo = "Eficiente"
                else:
                    categoria_consumo = "Ineficiente"
                
                self.eletrodomesticos.append({
                    "Nome": nome_eletrodomestico,
                    "Consumo Mensal (kWh)": consumo_mensal_kwh,
                    "Categoria": categoria_consumo
                })
            except ValueError:
                print("Erro: Por favor, insira valores válidos para potência e horas de uso.")
    
    def ver_dados_inseridos(self):
        if not self.eletrodomesticos:
            print("\nNenhum eletrodoméstico foi inserido.")
        else:
            df_eletrodomesticos = pd.DataFrame(self.eletrodomesticos)
            print("\nDados inseridos:")
            print(df_eletrodomesticos)

    def gerar_grafico(self):
        if not self.eletrodomesticos:
            print("\nNenhum dado para gerar gráfico. Insira pelo menos um eletrodoméstico.")
        else:
            df_eletrodomesticos = pd.DataFrame(self.eletrodomesticos)
            fig = px.bar(df_eletrodomesticos, 
                         x='Nome', 
                         y='Consumo Mensal (kWh)', 
                         color='Categoria',
                         title='Consumo Mensal dos Eletrodomésticos',
                         labels={'Nome': 'Eletrodoméstico', 'Consumo Mensal (kWh)': 'Consumo (kWh)', 'Categoria': 'Categoria de Consumo'})
            
            fig.show()

def menu():
    eletro = Eletrodomesticos()
    
    while True:
        print("\nMenu de Opções:")
        print("1. Inserir dados de um novo eletrodoméstico")
        print("2. Ver dados inseridos")
        print("3. Gerar gráfico comparativo de consumo")
        print("4. Sair")
        
        try:
            opcao = int(input("Escolha uma opção (1-4): "))
            
            if opcao == 1:
                eletro.inserir_dados()
            elif opcao == 2:
                eletro.ver_dados_inseridos()
            elif opcao == 3:
                eletro.gerar_grafico()
            elif opcao == 4:
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        except ValueError:
            print("Por favor, insira um número válido entre 1 e 4.")

menu()
