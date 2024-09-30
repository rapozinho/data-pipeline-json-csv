
import json
import csv

class Dados:
    
    # Método construtor
    def __init__(self, dados):
        self.dados = dados
        self.nome_colunas = self.__get_columns()
        self.tamanho_dados = self.__size_data()
                
    # Leitura e armazenamento do arquivo JSON
    def __leitura_json(path):
        dados_json = []
        with open(path, 'r') as file:
            dados_json = json.load(file)
        return dados_json

    # Leitura e armazenamento do arquivo CSV
    def __leitura_csv(path):
        dados_csv = []
        with open(path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv

    # Função para identificar e armazenar os dados dentro da lista dados
    @classmethod
    def leitura_dados(cls, path, tipo_dados):
        dados = []

        if tipo_dados == 'csv':
            dados = cls.__leitura_csv(path)
        
        elif tipo_dados == 'json':
            dados = cls.__leitura_json(path)

        return cls(dados)
           
    # Função para pegar o nome das colunas
    def __get_columns(self):
        return list(self.dados[-1].keys())
 
    # Função para renomear o nome das colunas
    def rename_columns(self, key_mapping):
        new_dados = []

        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_dados.append(dict_temp)
        self.dados = new_dados
        self.nomes_colunas = self.__get_columns()
        
    # Função para retornar o numero de linhas 
    def __size_data(self):
        return len(self.dados)     
    
    # Função para unir os dois dados
    def join(dadosA, dadosB):
        combined_list = []
        combined_list.extend(dadosA.dados) 
        combined_list.extend(dadosB.dados)
        
        return Dados(combined_list) 
    
    # Função para transformar os dados
    def __transformando_dados_tabela(self):
        dados_combinados_tabela = [self.nome_colunas]

        for row in self.dados:
            linha = []
            for coluna in self.nome_colunas:
                linha.append(row.get(coluna, "Indisponível"))
            dados_combinados_tabela.append(linha)
        return dados_combinados_tabela
  
    # Função para salvar os dados
    def salvando_dados(self, path):
        dados_combinados_tabela = self.__transformando_dados_tabela()
        
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)   

    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    