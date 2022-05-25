import json

import requests

URL = 'https://parallelum.com.br/fipe/api/v1/'


class ListTabelaFipe:

    @staticmethod
    def get_marca_carro():
        path = URL + 'carros/marcas'
        res = requests.get(path, headers={'User-Agent': 'XY'})
        return res.json()

    @staticmethod
    def get_modelo_carro():
        path = URL + 'carros/marcas/26/modelos'
        res = requests.get(path, headers={'User-Agent': 'XY'})
        return res.json()

    @staticmethod
    def get_ano_carro():
        path = URL + 'carros/marcas/26/modelos/4925/anos'
        res = requests.get(path, headers={'User-Agent': 'XY'})
        return res.json()

    @staticmethod
    def valor_carro():
        path = URL + 'carros/marcas/26/modelos/4925/anos/2010-1'
        res = requests.get(path, headers={'User-Agent': 'XY'})
        return [res.json()]


def main():
    tabela_fipe = ListTabelaFipe()
    list_marcas = tabela_fipe.get_marca_carro()
    list_modelo = tabela_fipe.get_modelo_carro()
    list_ano_carro = tabela_fipe.get_ano_carro()
    list_valor_carro = tabela_fipe.valor_carro()

    with open('valor-fipe.txt', 'w') as f:
        f.write(json.dumps(list_valor_carro))


print('Gerando arquivo...')

if __name__ == '__main__':
    main()
print('Arquivo gerado com sucesso!')
