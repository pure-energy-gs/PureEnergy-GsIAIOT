import pandas as pd
import unicodedata
import os

# Caminho para os arquivos CSV
caminho = 'C:/Users/zenet/OneDrive/Desktop/GS_IA_IOT/PureEnergy-GsIAIOT/DADOS'

# Função para normalizar strings (corrigir acentos e caracteres especiais)
def normalizar_texto(texto):
    # Remove acentos e caracteres especiais
    texto = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('utf-8')
    return texto

# Função para normalizar todo um DataFrame
def normalizar_df(df):
    for coluna in df.select_dtypes(include='object').columns:
        df[coluna] = df[coluna].apply(lambda x: normalizar_texto(x) if isinstance(x, str) else x)
    return df

# Lista de arquivos CSV
arquivos_csv = [
    "T_PE_COMODOS.csv",
    "T_PE_CONSUMO_MENSAL.csv",
    "T_PE_ELETRODOMESTICOS.csv",
    "T_PE_ENDERECOS.csv",
    "T_PE_PONTUACAO_USUARIO.csv",
    "T_PE_RESIDENCIAS.csv",
    "T_PE_USUARIOS.csv",
]

# Dicionário para armazenar os DataFrames normalizados
dataframes = {}

# Carregar, normalizar e armazenar cada CSV em memória
for arquivo in arquivos_csv:
    caminho_completo = os.path.join(caminho, arquivo)
    df = pd.read_csv(caminho_completo, encoding='latin1')  # Leitura com encoding apropriado
    df = normalizar_df(df)  # Normalização dos textos
    dataframes[arquivo] = df  # Armazenar o DataFrame normalizado em memória

# Realizar as junções (merge) com os DataFrames normalizados
df_combined = (
    dataframes["T_PE_COMODOS.csv"]
    .merge(dataframes["T_PE_CONSUMO_MENSAL.csv"], on='ID_USUARIO', how='left')
    .merge(dataframes["T_PE_ELETRODOMESTICOS.csv"], on='ID_COMODO', how='left')
    .merge(dataframes["T_PE_ENDERECOS.csv"], on='ID_USUARIO', how='left')
    .merge(dataframes["T_PE_PONTUACAO_USUARIO.csv"], on='ID_USUARIO', how='left')
    .merge(dataframes["T_PE_RESIDENCIAS.csv"], on='ID_USUARIO', how='left')
    .merge(dataframes["T_PE_USUARIOS.csv"], on='ID_USUARIO', how='left')
)

# Exibir o DataFrame combinado
print(df_combined.head())

# Salvar o DataFrame combinado em um novo arquivo CSV
df_combined.to_csv(f'{caminho}/dados_combinados.csv', index=False, encoding='utf-8')
