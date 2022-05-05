from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pesquisa = input("Digite sua pesquisa: ")

driver = webdriver.Chrome() #Abrir o Chrome
driver.get("https://www.google.com")

campo = driver.find_element_by_xpath("//input[@aria-label='Pesquisar']") # Acha o campo de pesquisa - Propriedade e valor da bara de pesquisa precisam estar bem especificados
campo.send_keys(pesquisa) # Método para digitar a pesquisa 
campo.send_keys(Keys.ENTER) # Aperta o Enter

resultados = driver.find_element_by_xpath("//div[@id='result-stats']").text #Pega o texto de resultados
print(resultados) # printa resultados encontrados
numero_resultados = int(resultados.split("Aproximadamente ")[1].split(' resultados')[0].replace('.','')) # Função paraecortar resultados
maximo_paginas = numero_resultados / 10
print("Número de páginas: %s" % (maximo_paginas))

url_pagina = driver.find_element_by_xpath("//a[@aria-label='Page 2']").get_attribute("href") # Pegar a propriedade e o atributo href

# Estrutura de repetição - passando para a próxima página
pagina_atual = 0
start = 10 # Pois são 10 resultados por pág
while pagina_atual <=10: 
    if not pagina_atual == 0:
        url_pagina = url_pagina.replace("start = %s" % start, "start = %s" % (start+10)) # substitui a url_pagina por +10
        start += 10 # Soma mais 10 no start da página atual
    pagina_atual += 1 # Página atual
    driver.get(url_pagina) #Abrindo a próxima pág