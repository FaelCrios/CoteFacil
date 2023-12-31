import scrapy

class CodeQuestao2Spider(scrapy.Spider):
    name = "code_questao_2"
    allowed_domains = ['pedidoeletronico.servimed.com.br', 'peapi.servimed.com.br']
    start_urls = ["https://pedidoeletronico.servimed.com.br/login"]

    def start_requests(self):
        self.cookies = []

        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        self.cookies = response.headers.getlist('Set-Cookie')
        yield scrapy.FormRequest(
            url='https://pedidoeletronico.servimed.com.br/login',
            headers={'Cookie': ''.join(self.cookies)},
            formdata={
                'username': 'juliano@farmaprevonline.com.br',
                'password': 'a007299A'
            },
            callback=self.depois_de_logar
        )

    def depois_de_logar(self, response):
        if response.status == 200:
            self.log("Logado")
            self.log(response)
            yield scrapy.Request(
                url='https://pedidoeletronico.servimed.com.br/pedidos',
                headers={'Cookie': ''.join(self.cookies)},
                callback=self.pesquisa
            )

    def pesquisa(self, response):
        if response.status == 200:
            self.log("Na pagina de pedidos")
            self.log(response)

        pedido = response.xpath("//table[@class='table table-striped table-hover']/tbody/tr/td[1]//text()").get()
        yield {
            'pedido': pedido
        }
