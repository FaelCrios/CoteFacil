from webdriver_manager.chrome import ChromeDriverManager 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import json 

def questao6(nome_autor):
    navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        
        link = "http://quotes.toscrape.com/"
        navegador.get(link)
        navegador.find_elements('xpath', f'//small[@class="author" and contains(text(), "{nome_autor}")]')
        about = navegador.find_element('xpath', f'//small[@class="author" and contains(text(), "{nome_autor}")]/following-sibling::a[@href]')
        link_about = (about.get_attribute('href')) 

        navegador.get(link_about)
        
        nome_do_autor = navegador.find_element('xpath', f'//h3[@class="author-title"]').text
        nascimento = navegador.find_element('xpath', f'//span[@class="author-born-date"]').text
        local_nascimento = navegador.find_element('xpath', f'//span[@class="author-born-location"]').text
        descricao = navegador.find_element('xpath', f'//div[@class="author-description"]').text
        descricao = descricao[:200]

        
        conteudo_do_autor = {
            "author": {
                "name": nome_do_autor,
                "birth_date": nascimento,
                "birth_location": local_nascimento,
                "description": f'{descricao} ...'
            },
            "quotes": [
            ]
        }
        
        
        navegador.get(link)
        
        while (
            navegador.find_elements('xpath', f'//small[@class="author" and contains(text(), "{nome_autor}")]') and
            navegador.find_elements('xpath', '//li[@class="next"]/a')
        ):
            quotes = navegador.find_elements('xpath', f"//span[@class='text' and following-sibling::span/small[@class='author' and contains(text(), '{nome_autor}')]]")
            quotes_tags = navegador.find_elements('xpath', f"//span[./small[@class='author' and contains(text(), '{nome_autor}')]]/following-sibling::div[@class='tags']/a[@class='tag']")
            
            for quote_texto, tags in zip(quotes, quotes_tags):
                quote_texto_conteudo = quote_texto.text
                tags_conteudo = tags.text
                
                nova_citacao = {
                    "text": quote_texto_conteudo,
                    "tags": [tags_conteudo]
                }
                
                conteudo_do_autor["quotes"].append(nova_citacao)

            next_button = navegador.find_element('xpath', '//li[@class="next"]/a')
            next_button.click()
        
         
    finally:
        navegador.quit()
        
    return conteudo_do_autor
        
        


print(json.dumps(questao6("J.K. Rowling"), indent=2, ensure_ascii=False))

