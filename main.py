"Controle de estoque"
import datetime

produtos_de_entrada_iphone = []
produtos_de_entrada_camera = []
produtos_de_entrada_computador = []

while True:
    opcao = int(input('Digite o numero da operação que deseja fazer:\n '
                      '{1} - Acrescentar produto\n'
                      '{2} - Ver saldo do estoque\n'
                      '{3} - Retirar produto\n'
                      '{4} - Sair do programa\n'))
    if opcao == 1:
        nome_do_produto = int(input('Informe o nome do seu produto: {1} Iphone \n'
                                '                               {2} Câmera \n'
                                '                               {3} Computador\n'))
        if nome_do_produto == 1:
            ano_entrada = int(input('Informe o ano de entrada do seu produto: '))
            dia_entrada = int(input('Informe o dia da entrada do seu produto: '))
            mes_entrada = int(input('Informe o mês da entrada do seu produto: '))
            data_entrada_iphone = datetime.date(ano_entrada, mes_entrada, dia_entrada)
            produtos_de_entrada_iphone.append(f"Iphone, {data_entrada_iphone}")
        elif nome_do_produto == 2:
            ano_entrada = int(input('Informe o ano de entrada do seu produto: '))
            dia_entrada = int(input('Informe o dia da entrada do seu produto: '))
            mes_entrada = int(input('Informe o mês da entrada do seu produto: '))
            data_entrada_camera = datetime.date(ano_entrada, mes_entrada, dia_entrada)
            produtos_de_entrada_camera.append(f"Câmera,{data_entrada_camera}")
        elif nome_do_produto == 3:
            ano_entrada = int(input('Informe o ano de entrada do seu produto: '))
            dia_entrada = int(input('Informe o dia da entrada do seu produto: '))
            mes_entrada = int(input('Informe o mês da entrada do seu produto: '))
            data_entrada_computador = datetime.date(ano_entrada,mes_entrada,dia_entrada)
            produtos_de_entrada_computador.append(f"Computador, {data_entrada_computador}")
    elif opcao == 2:
        print(f"Esse é o saldo de estoque da camera: {len(produtos_de_entrada_camera)}")
        print(f"Esse é o saldo de estoque de iphone: {len(produtos_de_entrada_iphone)}")
        print(f"Esse é o saldo de estoque do computador: {len(produtos_de_entrada_computador)}")
    elif opcao == 3:
        nome_do_produto = int(input('Informe o nome do seu produto vendido: {1} Iphone \n'
                                    '                               {2} Câmera \n'
                                    '                               {3} Computador\n'))
        if nome_do_produto == 1:
            produtos_de_entrada_iphone.pop()
        elif nome_do_produto == 2:
            produtos_de_entrada_camera.pop()
        elif nome_do_produto == 3:
            produtos_de_entrada_computador.pop()
    elif opcao == 4:
        break
print(produtos_de_entrada_iphone)
print(produtos_de_entrada_camera)