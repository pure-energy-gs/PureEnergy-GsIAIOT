import oracledb
import json
import pandas as pd
from datetime import datetime


def criar_conexao():
    try:
        
        dsnStr = oracledb.makedsn("oracle.fiap.com.br", 1521, "ORCL")
        
        
        conn = oracledb.connect(
            user="rm553621",
            password="051102",
            dsn=dsnStr
        )
        
        print("Conexão estabelecida com sucesso.")
        return conn
    
    except oracledb.DatabaseError as e:
        print("Erro ao conectar ao banco:", e)
        return None


def converter_datetime(dados):
    for tabela in dados:
        for i, registro in enumerate(dados[tabela]):
            for chave, valor in registro.items():
                if isinstance(valor, datetime):  
                    registro[chave] = valor.strftime('%Y-%m-%d %H:%M:%S')  
    return dados


def exportar_para_json():
    conn = criar_conexao()
    
    if conn is None:
        return

   
    tabelas = [
        "T_PE_USUARIOS",
        "T_PE_ENDERECOS",
        "T_PE_RESIDENCIAS",
        "T_PE_COMODOS",
        "T_PE_ELETRODOMESTICOS",
        "T_PE_CONSUMO_MENSAL",
        "T_PE_PONTUACAO_USUARIO"
    ]
    
    dados = {}

    try:
        cursor = conn.cursor()
        
        
        for tabela in tabelas:
            query = f"SELECT * FROM {tabela}"
            cursor.execute(query)
            colunas = [col[0] for col in cursor.description]  
            registros = cursor.fetchall()  

            # Converte os dados em um dicionário
            dados[tabela] = [dict(zip(colunas, registro)) for registro in registros]
        
        
        dados = converter_datetime(dados)
        

        with open('dados_exportados.json', 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
        
        print("Dados exportados para JSON com sucesso.")

    except oracledb.DatabaseError as e:
        print("Erro ao exportar dados:", e)
    
    finally:
        cursor.close()
        conn.close()

exportar_para_json()
