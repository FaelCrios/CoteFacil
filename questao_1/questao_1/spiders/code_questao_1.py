import scrapy
import nacl


class CodeQuestao1Spider(scrapy.Spider):
    name = "code_questao_1"
    allowed_domains = ["www.compra-agora.com"]
    start_urls = ["https://www.compra-agora.com/loja/destaques/1458","https://www.compra-agora.com/loja/alimentos/800","https://www.compra-agora.com/loja/bazar/344","https://www.compra-agora.com/loja/bebidas/778","https://www.compra-agora.com/loja/bomboniere/183","https://www.compra-agora.com/loja/carnes-e-congelados/1321","https://www.compra-agora.com/loja/papelaria/926","https://www.compra-agora.com/loja/naturais-e-nutricao/1399","https://www.compra-agora.com/loja/papelaria/926"]

    

    def parse(self, response):
        yield scrapy.FormRequest(
            url='https://www.compra-agora.com/cliente/logar',
            formdata={
                'username': '04.502.445/0001-20',
                'password': '85243140'
            },
            callback=self.depois_de_logar
        )
    
    def depois_de_logar(self, response):
        if response.status == 200:
            self.log("Logado")
        
