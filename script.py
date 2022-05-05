from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pesquisa = input("Digite sua pesquisa: ")

driver = webdriver.Chrome() #Abrir o Chrome
driver.get("https://www.google.com")

campo = driver.find_element_by_xpath("//input[@aria-label='Pesquisar']") # Acha o campo de pesquisa - Propriedade e valor da bara de pesquisa precisam estar bem especificados
campo.send_keys(pesquisa) # Método para digitar a pesquisa 
campo.send_keys(Keys.ENTER) # Aperta o Enter