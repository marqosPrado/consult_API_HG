import platform, os
from app.modules import hg_api
from app.config import config
from time import sleep


while True:
    sO = platform.system()
    if sO == "Linux" or sO == "macOS":
        os.system("clear")
    if sO == "Windows":
        os.system("cls")


    app = hg_api.Hg_api(config.chave())

    def menu():
        print("="*50)
        print(" "*18 + "Mercado Financeiro")
        print("="*50)

    def cotacao():
        cotation = app.dolar_quotations()
        print("Moeda: " + config.color_white() + "USD/BRL" + config.reset())
        print("Valor de Compra: ", config.color_white(), cotation['buy'], config.reset())

        if cotation['variation'] < 0:
            print("Variação:", config.color_red(), cotation['variation'], config.reset())
        else:
            print("Variação:", config.color_green(), cotation['variation'], config.reset())

    if app.error == False:
        menu()
        cotacao()
        sleep(config.ATUALIZACAO)
    else:
        print(app.warning)
        break
