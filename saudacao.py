 hora = input('Por favor insira um horario de 0-23: ')
 nome = input('Qual o seu nome? ')
 if hora.isdigit():
     hora = int(hora)
     if hora < 0 or hora > 23:
         print('Por favor insira um valor entre 0 e 23!')
     else:
         if hora < 11:
             input(f'Bom dia {nome}!')
         elif hora < 18:
             print(f'Boa tarde {nome}!')
         else:
             print(f'Boa noite {nome}!')
 else:
     print('Por favor digite um valor numerico!')