import time
import random
carteira = 1.00000000
voltar_ao_menu_inicial = 'voltar'
while voltar_ao_menu_inicial == 'voltar':
    time.sleep(1)
    print('\033[1;34;40m========================================\033[m')
    print('\033[1;34;40m============== BÓSONLÂNDIA =============\033[m')
    print('\033[1;34;40m========================================\033[m')
    print('      \033[4;31mVocê tem {:.9f} Bósons!\033[m'.format(carteira))
    print('')
    print('          \033[0;35m[1]- Ganhar Agora!\033[m')
    print('')
    print('          \033[0;35m[2]- Multiplicador\033[m')
    print('')
    print('          \033[0;35m[3]- Instruções\033[m')
    print('')
    print('=' *40)
    pergunta_do_menu_inicial = input('Digite aqui: ')
    print('=' *40)
    if pergunta_do_menu_inicial == '1':
        carteira = carteira + 0.00100000
        print('Você recebeu 0.00100000 Bósons!')
        time.sleep(2)
        print('=' *40)
        print('Tempo restante:')
        for c in range(10, 0, -1):
            print(c)
            time.sleep(1)
        print('Pronto para ganhar!')
        print('')
        voltar_ao_menu_inicial = 'voltar'
    elif pergunta_do_menu_inicial == '2':
        repeticao_do_multiplicador = '1'
        while repeticao_do_multiplicador == '1':
            # COLETANDO INFORMAÇÕES ===============
            print('\033[4;35;40m====== MULTIPLICADOR ======\033[m')
            time.sleep(1)
            print('\033[1;33m[1]- Multiplicar por 2X')
            print('[2]- Multiplicar por 3X')
            print('[3]- Multiplicar por 5X')
            print('[4]- Sair do Multiplicador\033[m')
            # MENU ACIMA ^
            time.sleep(1)
            valor_de_multiplicacao_ou_comando_de_voltar = str(input('\033[1;31mDigite aqui: \033[m'))
            print('')
            time.sleep(1)
            # COLETADO! =============================
            if valor_de_multiplicacao_ou_comando_de_voltar == '1':
                voltar_ao_multiplicador_2x = '1'
                while voltar_ao_multiplicador_2x:
                    print('\033[4;35;40m========= MULTIPLICADOR 2X =========\033[m')
                    print('')
                    print('\033[1;32mDe 0 a 1000, seu número da sorte é:')
                    print('')
                    print('[1]- <= MENOR OU IGUAL A 499')
                    print('[2]- >= MAIOR OU IGUAL A 500')
                    print('[3]- Voltar\033[m')
                    posicao_do_numero_da_sorte = str(input('Digite aqui: '))
                    time.sleep(1)
                    if posicao_do_numero_da_sorte == '1':
                        print('')
                        valor_a_multiplicar = float(input('\033[1;31mValor da aposta: \033[m'))
                        if valor_a_multiplicar > carteira:
                            print('')
                            print('SALDO INSUFICIENTE!')
                            print('')
                            valor_da_aposta_loop = 1
                        elif valor_a_multiplicar < carteira:
                            print('')
                            numero_sorteado = random.randint(0, 1000)
                            print('O número sorteado foi: {}!'.format(numero_sorteado))
                            print('')
                            time.sleep(1)
                            if numero_sorteado <= 499:
                                if posicao_do_numero_da_sorte == '1':
                                    time.sleep(1)
                                    print('Você ganhou!')
                                    print('')
                                    carteira = carteira + valor_a_multiplicar *2
                                    time.sleep(1)
                                    print('Saldo atual: {:.9f}'.format(carteira))
                                    print('')
                                    repeticao_do_multiplicador = '1'
                            elif numero_sorteado >= 500:
                                if posicao_do_numero_da_sorte == '1':
                                    time.sleep(1)
                                    print('Você perdeu!')
                                    print('')
                                    carteira = carteira - valor_a_multiplicar *2
                                    time.sleep(1)
                                    print('Saldo atual: {:.9f}'.format(carteira))
                                    print('')
                                    repeticao_do_multiplicador = '1'
                            elif numero_sorteado >= 500:
                                if posicao_do_numero_da_sorte == '2':
                                    time.sleep(1)
                                    print('Você ganhou!')
                                    print('')
                                    carteira = carteira + valor_a_multiplicar *2
                                    time.sleep(1)
                                    print('Saldo atual: {:.9f}'.format(carteira))
                                    print('')
                                    repeticao_do_multiplicador = '1'
                            elif numero_sorteado <= 499:
                                if posicao_do_numero_da_sorte == '1':
                                    time.sleep(1)
                                    print('Você perdeu!')
                                    print('')
                                    carteira = carteira - valor_a_multiplicar *2
                                    time.sleep(1)
                                    print('Saldo atual: {:.9f}'.format(carteira))
                                    print('')
                                    repeticao_do_multiplicador = '1'
                    elif posicao_do_numero_da_sorte == '2':
                        print('')
                        valor_a_multiplicar = float(input('\033[1;31mValor da aposta: \033[m'))
                        if valor_a_multiplicar > carteira:
                            print('')
                            print('SALDO INSUFICIENTE!')
                            print('')
                            valor_da_aposta_loop = 1
                        elif valor_a_multiplicar < carteira:
                            print('')
                            numero_sorteado = random.randint(0, 1000)
                            print('O número sorteado foi: {}!'.format(numero_sorteado))
                            print('')
                            time.sleep(1)
                            if numero_sorteado <= 499:
                                if posicao_do_numero_da_sorte == '1':
                                    time.sleep(1)
                                    print('Você ganhou!')
                                    print('')
                                    carteira = carteira + valor_a_multiplicar *2
                                    time.sleep(1)
                                    print('Saldo atual: {:.9f}'.format(carteira))
                                    print('')
                                    repeticao_do_multiplicador = '1'
                            elif numero_sorteado >= 500:
                                time.sleep(1)
                                print('Você ganhou!')
                                print('')
                                carteira = carteira + valor_a_multiplicar *2
                                time.sleep(1)
                                print('Saldo atual: {:.9f}'.format(carteira))
                                print('')
                                repeticao_do_multiplicador = '1'
                            elif numero_sorteado >= 500:
                                if posicao_do_numero_da_sorte == '2':
                                    time.sleep(1)
                                    print('Você perdeu!')
                                    print('')
                                    carteira = carteira - valor_a_multiplicar *2
                                    time.sleep(1)
                                    print('Saldo atual: {:.9f}'.format(carteira))
                                    print('')
                                    repeticao_do_multiplicador = '1'
                            elif numero_sorteado <= 499:
                                time.sleep(1)
                                print('Você ganhou!')
                                print('')
                                carteira = carteira + valor_a_multiplicar *2
                                time.sleep(1)
                                print('Saldo atual: {:.9f}'.format(carteira))
                                print('')
                                repeticao_do_multiplicador = '1'
                    elif posicao_do_numero_da_sorte == '3':
                            repeticao_do_multiplicador = '1'
                            break
                    else:
                        print('')
                        print('COMANDO NÃO IDENTIFICADO!')
                        print('')
                        voltar_ao_multiplicador_2x = '1'
            elif valor_de_multiplicacao_ou_comando_de_voltar == '2':
                print('\033[4;35;40m========= MULTIPLICADOR 3X =========\033[m')
                print('')
                print('\033[1;32mDe 0 a 1000, seu número da sorte é:')
                print('')
                print('[1]- <= MENOR OU IGUAL A 499')
                print('[2]- >= MAIOR OU IGUAL A 500')
                print('[3]- Voltar\033[m')
                posicao_do_numero_da_sorte = str(input('Digite aqui: '))
                time.sleep(1)
                if posicao_do_numero_da_sorte == '1':
                    print('')
                    valor_a_multiplicar = float(input('\033[1;31mValor da aposta: \033[m'))
                    if valor_a_multiplicar > carteira:
                        print('')
                        print('SALDO INSUFICIENTE!')
                        print('')
                        valor_da_aposta_loop = 1
                    elif valor_a_multiplicar < carteira:
                        print('')
                        numero_sorteado = random.randint(0, 1000)
                        print('O número sorteado foi: {}!'.format(numero_sorteado))
                        print('')
                        time.sleep(1)
                        if numero_sorteado <= 499:
                            if posicao_do_numero_da_sorte == '1':
                                time.sleep(1)
                                print('Você ganhou!')
                                print('')
                                carteira = carteira + valor_a_multiplicar *3
                                time.sleep(1)
                                print('Saldo atual: {:.9f}'.format(carteira))
                                print('')
                                repeticao_do_multiplicador = '1'
                        elif numero_sorteado >= 500:
                            time.sleep(1)
                            print('Você perdeu!')
                            print('')
                            carteira = carteira - valor_a_multiplicar *3
                            time.sleep(1)
                            print('Saldo atual: {:.9f}'.format(carteira))
                            print('')
                            repeticao_do_multiplicador = '1'
                        elif numero_sorteado >= 500:
                            if posicao_do_numero_da_sorte == '2':
                                time.sleep(1)
                                print('Você ganhou!')
                                print('')
                                carteira = carteira + valor_a_multiplicar *3
                                time.sleep(1)
                                print('Saldo atual: {:.9f}'.format(carteira))
                                print('')
                                repeticao_do_multiplicador = '1'
                        elif numero_sorteado <= 499:
                            time.sleep(1)
                            print('Você perdeu!')
                            print('')
                            carteira = carteira - valor_a_multiplicar *3
                            time.sleep(1)
                            print('Saldo atual: {:.9f}'.format(carteira))
                            print('')
                            repeticao_do_multiplicador = '1'
                elif posicao_do_numero_da_sorte == '2':
                    print('')
                    valor_a_multiplicar = float(input('\033[1;31mValor da aposta: \033[m'))
                    if valor_a_multiplicar > carteira:
                        print('')
                        print('SALDO INSUFICIENTE!')
                        print('')
                        valor_da_aposta_loop = 1
                    elif valor_a_multiplicar < carteira:
                        print('')
                        numero_sorteado = random.randint(0, 1000)
                        print('O número sorteado foi: {}!'.format(numero_sorteado))
                        print('')
                        time.sleep(1)
                        if numero_sorteado <= 499:
                            if posicao_do_numero_da_sorte == '1':
                                time.sleep(1)
                                print('Você ganhou!')
                                print('')
                                carteira = carteira + valor_a_multiplicar *3
                                time.sleep(1)
                                print('Saldo atual: {:.9f}'.format(carteira))
                                print('')
                                repeticao_do_multiplicador = '1'
                        elif numero_sorteado >= 500:
                            time.sleep(1)
                            print('Você ganhou!')
                            print('')
                            carteira = carteira + valor_a_multiplicar *3
                            time.sleep(1)
                            print('Saldo atual: {:.9f}'.format(carteira))
                            print('')
                            repeticao_do_multiplicador = '1'
                        elif numero_sorteado >= 500:
                            if posicao_do_numero_da_sorte == '2':
                                time.sleep(1)
                                print('Você perdeu!')
                                print('')
                                carteira = carteira - valor_a_multiplicar *3
                                time.sleep(1)
                                print('Saldo atual: {:.9f}'.format(carteira))
                                print('')
                                repeticao_do_multiplicador = '1'
                        elif numero_sorteado <= 499:
                            time.sleep(1)
                            print('Você ganhou!')
                            print('')
                            carteira = carteira + valor_a_multiplicar *3
                            time.sleep(1)
                            print('Saldo atual: {:.9f}'.format(carteira))
                            print('')
                            repeticao_do_multiplicador = '1'
                elif posicao_do_numero_da_sorte == '3':
                        repeticao_do_multiplicador = '1'
            elif valor_de_multiplicacao_ou_comando_de_voltar == '3':
                print('\033[4;35;40m========= MULTIPLICADOR 5X =========\033[m')
                print('')
                print('\033[1;32mDe 0 a 1000, seu número da sorte é:')
                print('')
                print('[1]- <= MENOR OU IGUAL A 499')
                print('[2]- >= MAIOR OU IGUAL A 500')
                print('[3]- Voltar\033[m')
                posicao_do_numero_da_sorte = str(input('Digite aqui: '))
                time.sleep(1)
                if posicao_do_numero_da_sorte == '1':
                    print('')
                    valor_a_multiplicar = float(input('\033[1;31mValor da aposta: \033[m'))
                    if valor_a_multiplicar > carteira:
                        print('')
                        print('SALDO INSUFICIENTE!')
                        print('')
                        valor_da_aposta_loop = 1
                    elif valor_a_multiplicar < carteira:
                        print('')
                        numero_sorteado = random.randint(0, 1000)
                        print('O número sorteado foi: {}!'.format(numero_sorteado))
                        print('')
                        time.sleep(1)
                        if numero_sorteado <= 499:
                            if posicao_do_numero_da_sorte == '1':
                                time.sleep(1)
                                print('Você ganhou!')
                                print('')
                                carteira = carteira + valor_a_multiplicar *5
                                time.sleep(1)
                                print('Saldo atual: {:.9f}'.format(carteira))
                                print('')
                                repeticao_do_multiplicador = '1'
                        elif numero_sorteado >= 500:
                            time.sleep(1)
                            print('Você perdeu!')
                            print('')
                            carteira = carteira - valor_a_multiplicar *5
                            time.sleep(1)
                            print('Saldo atual: {:.9f}'.format(carteira))
                            print('')
                            repeticao_do_multiplicador = '1'
                        elif numero_sorteado >= 500:
                            if posicao_do_numero_da_sorte == '2':
                                time.sleep(1)
                                print('Você ganhou!')
                                print('')
                                carteira = carteira + valor_a_multiplicar *5
                                time.sleep(1)
                                print('Saldo atual: {:.9f}'.format(carteira))
                                print('')
                                repeticao_do_multiplicador = '1'
                        elif numero_sorteado <= 499:
                            time.sleep(1)
                            print('Você perdeu!')
                            print('')
                            carteira = carteira - valor_a_multiplicar *5
                            time.sleep(1)
                            print('Saldo atual: {:.9f}'.format(carteira))
                            print('')
                            repeticao_do_multiplicador = '1'
                elif posicao_do_numero_da_sorte == '2':
                    print('')
                    valor_a_multiplicar = float(input('\033[1;31mValor da aposta: \033[m'))
                    if valor_a_multiplicar > carteira:
                        print('')
                        print('SALDO INSUFICIENTE!')
                        print('')
                        valor_da_aposta_loop = 1
                    elif valor_a_multiplicar < carteira:
                        print('')
                        numero_sorteado = random.randint(0, 1000)
                        print('O número sorteado foi: {}!'.format(numero_sorteado))
                        print('')
                        time.sleep(1)
                        if numero_sorteado <= 499:
                            if posicao_do_numero_da_sorte == '1':
                                time.sleep(1)
                                print('Você ganhou!')
                                print('')
                                carteira = carteira + valor_a_multiplicar *5
                                time.sleep(1)
                                print('Saldo atual: {:.9f}'.format(carteira))
                                print('')
                                repeticao_do_multiplicador = '1'
                        elif numero_sorteado >= 500:
                            time.sleep(1)
                            print('Você ganhou!')
                            print('')
                            carteira = carteira + valor_a_multiplicar *5
                            time.sleep(1)
                            print('Saldo atual: {:.9f}'.format(carteira))
                            print('')
                            repeticao_do_multiplicador = '1'
                        elif numero_sorteado >= 500:
                            if posicao_do_numero_da_sorte == '2':
                                time.sleep(1)
                                print('Você perdeu!')
                                print('')
                                carteira = carteira - valor_a_multiplicar *5
                                time.sleep(1)
                                print('Saldo atual: {:.9f}'.format(carteira))
                                print('')
                                repeticao_do_multiplicador = '1'
                        elif numero_sorteado <= 499:
                            time.sleep(1)
                            print('Você ganhou!')
                            print('')
                            carteira = carteira + valor_a_multiplicar *5
                            time.sleep(1)
                            print('Saldo atual: {:.9f}'.format(carteira))
                            print('')
                            repeticao_do_multiplicador = '1'
                elif posicao_do_numero_da_sorte == '3':
                        repeticao_do_multiplicador = '1'
            elif valor_de_multiplicacao_ou_comando_de_voltar == '4':
                voltar_ao_menu_inicial = 'voltar'
                break
            else:
                print('COMANDO NÃO IDENTIFICADO!')
                print('')
                repeticao_do_multiplicador = '1'
    elif pergunta_do_menu_inicial == '3':
        print('INSTRUÇÕES')
        print()
        print('1- Você deverá escolher uma das opções do menu')
        print('2- Em seguida basta seguir o que se pede!')
        print()
        print('Criador: Carlos Emanoel')
        voltar_ao_menu_inicial = 'voltar'
    else:
        print('COMANDO NÃO IDENTIFICADO!')
        voltar_ao_menu_inicial = 'voltar'
        