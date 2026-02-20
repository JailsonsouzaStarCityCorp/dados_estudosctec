import pandas as pd  
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

df = pd.read_csv("dados.csv")
print(df)

print(df.info)

#contador de coluna

contagem_cidade = df["cidade"].value_counts()

plt.figure(figsize=(8, 5))
contagem_cidade.plot(kind="bar")
plt.title('Quantidade de pessoas por cidade')
plt.xlabel("Cidade")
plt.ylabel("Total de pessoas")
plt.xticks(rotation=45)

plt.show()

#histograma

plt.figure(figsize=(8,5))
plt.hist(df["idade"], bins=8)
plt.title("Distribuição de idades")
plt.xlabel("Idade")
plt.ylabel("Frequencia")

plt.show()


#Idade média por cidade

plt.figure(figsize=(8,5))

media_idade = df.groupby("cidade")["idade"].mean().reset_index()
sb.barplot(data=media_idade, x="cidade", y="idade")
plt.title('Idade media por cidade')
plt.xlabel("Cidade")
plt.ylabel("Idade media")
plt.xticks(rotation=45)
plt.show()


#idade Media e menor media de idade


cidade_maior_media = media_idade.loc[media_idade["idade"].idxmax()]
cidade_menor_media = media_idade.loc[media_idade["idade"].idxmin()]

print(f"\nCidade com maior média de idade: {cidade_maior_media['cidade']} ({cidade_maior_media['idade']:.1f})")
print(f"Cidade com menor média de idade: {cidade_menor_media['cidade']} ({cidade_menor_media['idade']:.1f})")


#Heatmap

Tabela = pd.crosstab (df["cidade"], pd.cut(df["idade"], bins=5))
plt.figure(figsize=(8,5))
sb.heatmap(Tabela, annot=True, fmt="d", cmap="Blues")
plt.title("Distribuição de faixa etaria por cidade")
plt.show()