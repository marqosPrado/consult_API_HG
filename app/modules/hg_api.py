import requests, json


class Hg_api:
    key = None
    error = False

    def __init__(self, key):
        if len(key) == 8:
            self.key = key
            self.error = False
        else:
            self.warning = "Erro! chave inválida, vá até a pasta 'config' entre no arquivo 'config.py'\ne adicione uma chave válida."
            self.error = True


    def get_url(self, endpoint):
        self.URL = requests.get(f"https://api.hgbrasil.com/{endpoint}?format=json&key={self.key}")
        self.tx = self.URL.text
        self.data = json.loads(self.tx)
        return self.data


    def dolar_quotations(self):
        data = self.get_url("finance/quotations")

        if len(data) != 0:
            return data['results']['currencies']['USD']

        else:
            print("Erro ao pegar os dados da API")
