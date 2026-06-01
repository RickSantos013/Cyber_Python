import pandas as pd

#1. Dataframe a partir de um dicionário
data = {
    'Nome': ['Ana', 'João', 'Maria', 'Carlos'],
    'Idade': [23, 34, 29, 42],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
}
df = pd.DataFrame(data)

#2. Acessando colunas do dicionário
print("\nAcessando a coluna 'Nome':")
print("----------------------------")
print(df['Nome'])

#3. Acessando linhas por índice
print("\nAcessando a primeira linha: ")
print("------------------------------")
print(df.iloc[0])

#4. Adicionar nova coluna
df['Profissão'] = ['Engenheira', 'Médico', 'Designer', 'Professor']
print("\nDataframe com nova coluna 'Profissão':")
print(df)

#5. Filtrando dados: Selecionando pessoas com idade maior que 30
print("\nPessoas com idade maior que 30: ")
print(df[df['Idade'] > 30])

#6. Estatísticas básicas : Média de idade
print("\nMédia da idade: ")
print(df['Idade'].mean())

#7.Agrupando dados: Contagem de pessoas por cidade
print("\nContagem de pessoas por cidade: ")
print(df.groupby('Cidade').size())

#8. Salvando o Dataframe em um arquivo .csv
df.to_csv("pessoas.csv", index=False)
print("\nDataframe salvo como 'pessoas.csv'.")

#9. Carregando dados de um arquivo csv
df_carregado = pd.read_csv('pessoas.csv')
print("\nDataframe carregado de 'pessoas.csv':")
print(df_carregado)

