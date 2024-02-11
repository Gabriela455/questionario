import xml.etree.ElementTree as ET

def extrair_dados_xml(nome_arquivo):
    tree = ET.parse(nome_arquivo)
    root = tree.getroot()
    
    dados = {'dia': [], 'valor': []}
    
    for row in root.findall('row'):
        dia = int(row.find('dia').text)
        valor = float(row.find('valor').text)
        
        dados['dia'].append(dia)
        dados['valor'].append(valor)
    
    return dados

def calcular_metricas(faturamento_diario):
    valores_faturamento = faturamento_diario['valor']
    valores_com_faturamento = [valor for valor in valores_faturamento if valor > 0]
    
    menor_valor = min(valores_com_faturamento) if valores_com_faturamento else 0
    maior_valor = max(valores_faturamento)
    
    if valores_com_faturamento:
        media_mensal = sum(valores_com_faturamento) / len(valores_com_faturamento)
    else:
        media_mensal = 0
    
    dias_acima_da_media = sum(1 for valor in valores_com_faturamento if valor > media_mensal)
    
    return menor_valor, maior_valor, media_mensal, dias_acima_da_media

def main():
    nome_arquivo = "faturamento.xml"
    dados_xml = extrair_dados_xml(nome_arquivo)
    
    menor_valor, maior_valor, media_mensal, dias_acima_da_media = calcular_metricas(dados_xml)
    
    print("Menor valor de faturamento:", menor_valor)
    print("Maior valor de faturamento:", maior_valor)
    print("Média mensal de faturamento:", media_mensal)
    print("Número de dias com faturamento acima da média mensal:", dias_acima_da_media)

if __name__ == "__main__":
    main()