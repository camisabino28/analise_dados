import requests
import pandas as pd

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyMDE1LCJpYXQiOjE3NzQzNTAwMTUsImp0aSI6ImI3M2UyZGUyMmNkYTQ1ZWQ5ZmI2ZWZhYTAwZGM4N2I3IiwidXNlcl9pZCI6IjExNSJ9.BYwtttiHVt8EVA_653elnaGNcPAHdaWjlc9pusQLu7I"
resp = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2021-04-01"},
)

dados= resp.json()
df = pd.DataFrame(dados)
df2 = df[["ticker","roic","earning_yield"]]
df2["rank_roic"] = df2["roic"].rank()
df2["rank_earning_yield"] = df2["earning_yield"].rank()
df2["rank_final"] = (df2["rank_roic"] + df2["rank_earning_yield"] ) / 2
df3 = df2.sort_values("rank_final", ascending=True)

carteira = df3.head(20)["ticker"]


#tempo atual preco
import requests
import pandas as pd
carteira = list(df3.head(20)["ticker"])
lista_frames = []
for acao in carteira:
    params = {"ticker": acao, "data_ini": "2021-04-01", "data_fim": "2026-03-30"}
    resp = requests.get(
        f"{base_url}/preco/corrigido",
        headers={"Authorization": f"Bearer {token}"},
        params=params,
    )
    
    if resp.status_code == 200:
        dados = resp.json()
        if dados: # Verifica se não voltou vazio
            temp_df = pd.DataFrame(dados)
            temp_df["ticker"] = acao
            # Converte data para datetime para facilitar a manipulação
            temp_df["data"] = pd.to_datetime(temp_df["data"])
            lista_frames.append(temp_df)

df_precos_total = pd.concat(lista_frames)
df_pivot = df_precos_total.pivot(index="data", columns="ticker", values="fechamento")
# Convertendo o pivot para numérico para evitar o erro de string
df_pivot = df_pivot.apply(pd.to_numeric, errors='coerce')
df_pivot = df_pivot.ffill().dropna()

# 2. Cálculo do Rendimento Ponta a Ponta por Ação (Peso de 5% cada)
rendimentos_por_acao = (df_pivot.iloc[-1] / df_pivot.iloc[0]) - 1
rendimento_carteira = rendimentos_por_acao.mean()

print(f"Rendimento da Carteira (Equiponderada 5%): {rendimento_carteira:.2%}")
#Ibovespa 5 anos
import yfinance as yf
ibov5 = yf.download("^BVSP", start= "2021-04-01", end = "2026-03-30")
preco_fechamento_ibov5= ibov5["Close"]
rendimento_ibov = preco_fechamento_ibov5["^BVSP"].iloc[-1] / preco_fechamento_ibov5["^BVSP"].iloc[0] - 1
print(f"Rendimento: {rendimento_ibov:.2%}")



print(f"Rendimento da Carteira (Equiponderada 5%): {rendimento_carteira:.2%}")
print(f"Rendimento: {rendimento_ibov:.2%}")