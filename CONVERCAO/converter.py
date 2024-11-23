import pandas as pd
import unicodedata
import os

caminho = 'C:/Users/zenet/OneDrive/Desktop/GS_IA_IOT/PureEnergy-GsIAIOT/DADOS'

def normalizar_texto(texto):
    texto = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('utf-8')
    return texto

def normalizar_df(df):
    for coluna in df.select_dtypes(include='object').columns:
        df[coluna] = df[coluna].apply(lambda x: normalizar_texto(x) if isinstance(x, str) else x)
    return df

arquivos_csv = [
    "T_PE_COMODOS.csv",
    "T_PE_CONSUMO_MENSAL.csv",
    "T_PE_ELETRODOMESTICOS.csv",
    "T_PE_ENDERECOS.csv",
    "T_PE_PONTUACAO_USUARIO.csv",
    "T_PE_RESIDENCIAS.csv",
    "T_PE_USUARIOS.csv",
]


dataframes = {}


for arquivo in arquivos_csv:
    caminho_completo = os.path.join(caminho, arquivo)
    df = pd.read_csv(caminho_completo, encoding='latin1')  
    df = normalizar_df(df)  
    dataframes[arquivo] = df  

df_combined = (
    dataframes["T_PE_COMODOS.csv"]
    .merge(dataframes["T_PE_CONSUMO_MENSAL.csv"], on='ID_USUARIO', how='left')
    .merge(dataframes["T_PE_ELETRODOMESTICOS.csv"], on='ID_COMODO', how='left')
    .merge(dataframes["T_PE_ENDERECOS.csv"], on='ID_USUARIO', how='left')
    .merge(dataframes["T_PE_PONTUACAO_USUARIO.csv"], on='ID_USUARIO', how='left')
    .merge(dataframes["T_PE_RESIDENCIAS.csv"], on='ID_USUARIO', how='left')
    .merge(dataframes["T_PE_USUARIOS.csv"], on='ID_USUARIO', how='left')
)

print(df_combined.head())

df_combined.to_csv(f'{caminho}/dados_combinados.csv', index=False, encoding='utf-8')
