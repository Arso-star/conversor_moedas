def converter(valor, taxa):
    """Realiza a conversão de moeda com base na taxa fornecida."""
    return valor * taxa

taxas = {
    'dolar_real': 5.77,
    'dolar_euro': 0.92,
    'dolar_iene': 150.06,
    'real_dolar': 1/5.77,
    'real_euro': 1/6.24,
    'real_iene': 26,
    'euro_dolar': 1.08,
    'euro_real': 6.24,
    'euro_iene': 162.56,
    'iene_dolar': 0.0067,
    'iene_real': 0.038,
    'iene_euro': 0.0062
}

word = 'moedas'

print('=' * 20)
print(word.upper().center(20))
print('=' * 20)

while True:

    menu = """Selecione a opção:
    [1] Converter em Dólar
    [2] Converter em Real
    [3] Converter em Euro
    [4] Converter em Iene Japonês
    [5] Sair
    """ 
    opcao = input(menu) 
    print() 
    # Verificar se a opção é válida
    if opcao not in ('1', '2', '3', '4', '5'):
        print('Erro! Opção inválida. Tente novamente.')
        continue
    # Se o usuário escolher "Sair"
    if opcao == '5':
        print('Saindo...')
        exit()  
    # Pedir o valor da moeda correspondente
    moedas = {'1': 'Dólar', '2': 'Real', '3': 'Euro', '4': 'Iene'}
    moeda_origem = moedas[opcao]    
    try:
        valor = float(input(f'Digite o valor em {moeda_origem}: '))
        if valor < 0:
            raise ValueError # Impede o valor negativo
    except ValueError:
        print('Erro! Você deve digitar um número válido maior ou igual a zero.')
        exit()  
    if opcao == '1':
        print(f'O valor em Real, R$ {valor:.2f} para Dólar é USD {converter(valor, taxas["real_dolar"]):.2f}')
        print(f'O valor em Euro, EUR {valor:.2f} para Dólar é USD {converter(valor, taxas["euro_dolar"]):.2f}')
        print(f'O valor em Iene Japonês, JPY {valor:.2f} para Dólar é USD {converter(valor, taxas["iene_dolar"]):.2f}') 
    elif opcao == '2':
        print(f'O valor em Dólar, USD {valor:.2f} para Real é R$ {converter(valor, taxas["dolar_real"]):.2f}')
        print(f'O valor em Euro, EUR {valor:.2f} para Real é R$ {converter(valor, taxas["euro_real"]):.2f}')
        print(f'O valor em Iene Japonês, JPY {valor:.2f} para Real é R$ {converter(valor, taxas["iene_real"]):.2f}')    
    elif opcao == '3':
        print(f'O valor em Dólar, USD {valor:.2f} para Euro é EUR {converter(valor, taxas["dolar_euro"]):.2f}')
        print(f'O valor em Real, R$ {valor:.2f} para Euro é EUR {converter(valor, taxas["real_euro"]):.2f}')
        print(f'O valor em Iene Japonês, JPY {valor:.2f} para Euro é EUR {converter(valor, taxas["iene_euro"]):.2f}')   
    elif opcao == '4':
        print(f'O valor em Dólar, USD {valor:.2f} para Iene Japonês é JPY {converter(valor, taxas["dolar_iene"]):.2f}')
        print(f'O valor em Real, R$ {valor:.2f} para Real é JPY {converter(valor, taxas["real_iene"]):.2f}')
        print(f'O valor em Euro, EUR {valor:.2f} para Real é JPY {converter(valor, taxas["euro_iene"]):.2f}')
    print()