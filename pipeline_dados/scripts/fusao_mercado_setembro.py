from processamento_dados import Dados

path_json = './data_raw/dados_empresaA.json'
path_csv = './data_raw/dados_empresaB.csv'


# Extract
dados_empresaA = Dados.leitura_dados(path_json, 'json')
dados_empresaB = Dados.leitura_dados(path_csv, 'csv')


# Transform

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
dados_fusao = Dados.join(dados_empresaA, dados_empresaB)


# Load
 
path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)

