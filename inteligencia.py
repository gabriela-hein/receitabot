


import google.generativeai as genai

def detectar_ingredientes(chave, imagem):
    genai.configure(api_key=chave)
    modelo = genai.GenerativeModel('gemini-1.5-flash')
    prompt = '''Liste quais são os ingredientes desta imagem.
    Os ingredientes devem ser apresentados em uma lista separados por vígula, como no exemplo
    a seguir. Nenhum texto adicional deve ser gerado como resposta além dos próprios ingredientes.
    #exemplo de saída
    arroz, feijão, frango'''
    resposta = modelo.generate_content([prompt, imagem])
    ingredientes=resposta.text.split(",")
    return ingredientes


def possiveis_receitas(chave, ingredientes):
    genai.configure(api_key=chave)
    modelo = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f'''Considerando a seguinte lista de ingredientes, gere uma lista
    de receitas culinárias que os utilizem. 
    As receitas devem tentar incluir a maior parte dos ingredientes.
    Gere apenas uma lista com o nome das receitas separado por vírgula.
    #lista de ingredientes
    {ingredientes}
    #exemplo de saída
    receita1, receita2, receita3
    '''
    resposta = modelo.generate_content(prompt)
    receitas=resposta.text.split(",")
    return receitas


def receita_completa(chave, ingredientes, receitas):
    genai.configure(api_key=chave)
    modelo = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f'''Crie a receita para o prato "{receitas}"
    inclua a maior quantidade possível de ingredientes da lista de ingredientes
    
    #lista de ingredientes
    {ingredientes}
    '''
    resposta = modelo.generate_content(prompt)
    return resposta.text

