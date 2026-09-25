import re

# 1. ANOTAÇÃO TEÓRICA APLICADA: Estrutura de Dados Composta (Lista de Dicionários)
# Simula uma base de dados bruta recebida por uma Inteligência Artificial
dados_brutos = [
    {"id": "usr_01", "mensagem": "Agendar reuniao para as 14h de amanha"},
    {"id": "usr_02", "mensagem": "Código de ativação: #99482"},
    {"id": "usr_03", "mensagem": "O resultado do teste deu 100% de sucesso!"},
    {"id": "usr_04", "mensagem": "Ola! Como posso te ajudar hoje?"}
]

# 2. ANOTAÇÃO TEÓRICA APLICADA: Funções e Regex Alfanumérico
def extrair_apenas_texto(texto):
    """
    Remove números e caracteres especiais, deixando apenas letras e espaços.
    Muito útil em PLN (Processamento de Linguagem Natural).
    """
    # Regex para manter apenas letras (a-z, A-Z) e espaços
    padrao_letras = r'[a-zA-Z\s]+'
    match = re.findall(padrao_letras, texto)
    
    # Junta os pedaços de texto encontrados
    texto_limpo = "".join(match).strip()
    return texto_limpo

# 3. ANOTAÇÃO TEÓRICA APLICADA: Funções e Regex Numérico
def extrair_apenas_numeros(texto):
    """
    Identifica e extrai qualquer sequência numérica dentro da mensagem.
    """
    padrao_numeros = r'\d+'
    numeros_encontrados = re.findall(padrao_numeros, texto)
    return numeros_encontrados

# 4. FUNÇÃO PRINCIPAL: Pipeline de Processamento
def processar_dados_ia(dataset):
    print("🤖 INICIANDO PIPELINE DE INTELIGÊNCIA ARTIFICIAL...\n")
    
    # Lista composta para armazenar o resultado final limpo
    dados_processados = []
    
    for dado in dataset:
        mensagem_original = dado["mensagem"]
        
        # Executa as funções de Regex para limpar os dados
        texto_filtrado = extrair_apenas_texto(mensagem_original)
        numeros_filtrados = extrair_apenas_numeros(mensagem_original)
        
        # Cria um novo dicionário com os dados tratados
        insight_ia = {
            "id": dado["id"],
            "texto_puro": texto_filtrado,
            "dados_numericos": numeros_filtrados if numeros_filtrados else "Nenhum número detectado"
        }
        
        dados_processados.append(insight_ia)
        
        # Exibe o progresso na tela
        print(f"📥 ID: {insight_ia['id']}")
        print(f"💬 Original: '{mensagem_original}'")
        print(f"✨ Texto Limpo: '{insight_ia['texto_puro']}'")
        print(f"🔢 Números Extraídos: {insight_ia['dados_numericos']}")
        print("-" * 50)
        
    return dados_processados

# Executa o código se este arquivo for o principal
if __name__ == "__main__":
    resultado_final = processar_dados_ia(dados_brutos)
    print("\n✅ Processamento concluído com sucesso! Dados prontos para o Modelo de IA.")
