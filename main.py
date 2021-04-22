import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(2)

position1 = pt.locateOnScreen("whatsaap/sorriso_clip1.png", confidence=.6)
x = position1[0]
y = position1[1]

food = ''
recheio = ''
qtd = 0
pagto = ''
resumo = {'Cliente':'cliente', 'Lanche':'food', 'Recheio': 'recheio', 'Qtd': 'qtd', 'Pagto':'pagto'}

#Gets message
def get_principal():
    global x, y, food, recheio, qtd, pagto, resumo

    position = pt.locateOnScreen('sorriso_clip.png', confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.5)
    pt.moveTo(x + 50, y - 40, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12, 15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print('Mensagem recebida: ' + whatsapp_message)

    return whatsapp_message

def post_response(message):
    global x, y

    position = pt.locateOnScreen('sorriso_clip.png', confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    pt.typewrite('\n', interval=.01)

# Processes message
def process_response(message):
    random_no = random.randrange(3)
    
    if 'pedido' in str(message).lower():
        return '''E ai, tudo blz. Sou o Don, vou agilizar seu pedido aqui, me diz aí o que vai querer.
        Cardapio: 
        Pastel - ...R$ 5,00
        Coxinha -...R$ 6,00
        Croquete - .R$ 5,00
        Risole - ...R$ 4,00
         '''
    elif 'pastel' in str(message).lower():
        food = message
        resumo['Lanche'] = str(food)
        return f'{food}, perfeito. Agora me diz o recheio: Carne, Frango, Calabresa ou Camarao'
    elif 'coxinha' in str(message).lower():
        food = message
        resumo['Lanche'] = str(food)
        return f'{food}, perfeito. Agora me diz o recheio: Carne, Frango, Calabresa ou Camarao'
    elif 'croquete' in str(message).lower():
        food = message
        resumo['Lanche'] = str(food)
        return f'{food}, perfeito. Agora me diz o recheio: Carne, Frango, Calabresa ou Camarao'
    elif 'risole' in str(message).lower():
        food = message
        resumo['Lanche'] = str(food)
        return f'{food}, perfeito. Agora me diz o recheio: Carne, Frango, Calabresa ou Camarao'
    elif 'carne' in str(message).lower():
        recheio = message
        resumo['Recheio'] = str(recheio)
        return f'{recheio}, excelente escolha. Com queijo ou sem queijo: '
    elif 'frango' in str(message).lower():
        recheio = message
        resumo['Recheio'] = str(recheio)
        return f'{recheio}, excelente escolha. Com queijo ou sem queijo: '
    elif 'calabresa' in str(message).lower():
        recheio = message
        resumo['Recheio'] = str(recheio)
        return f'{recheio}, excelente escolha. Com queijo ou sem queijo: '
    elif 'camar' in str(message).lower():
        recheio = message
        resumo['Recheio'] = str(recheio)
        return f'{recheio}, excelente escolha. Com queijo ou sem queijo: '
    elif 'com' in str(message).lower():
        return 'Agora me diz a quantidade.'
    elif 'sem' in str(message).lower():
        return 'Agora me diz a quantidade.'
    elif '1' in str(message).lower():
        qtd = message
        resumo['Qtd'] = str(qtd)
        return f'Quantidade do pedido: {qtd}. Esta correto?'
    elif '2' in str(message).lower():
        qtd = message
        resumo['Qtd'] = str(qtd)
        return f'Quantidade do pedido: {qtd}. Esta correto?'
    elif '3' in str(message).lower():
        qtd = message
        resumo['Qtd'] = str(qtd)
        return f'Quantidade do pedido: {qtd}. Esta correto?'
    elif '4' in str(message).lower():
        qtd = message
        resumo['Qtd'] = str(qtd)
        return f'Quantidade do pedido: {qtd}. Esta correto?'
    elif '5' in str(message).lower():
        qtd = message
        resumo['Qtd'] = str(qtd)
        return f'Quantidade do pedido: {qtd}. Esta correto?'
    elif '6' in str(message).lower():
        qtd = message
        resumo['Qtd'] = str(qtd)
        return f'Quantidade do pedido: {qtd}. Esta correto?'
    elif '7' in str(message).lower():
        qtd = message
        resumo['Qtd'] = str(qtd)
        return f'Quantidade do pedido: {qtd}. Esta correto?'
    elif '8' in str(message).lower():
        qtd = message
        resumo['Qtd'] = str(qtd)
        return f'Quantidade do pedido: {qtd}. Esta correto?'
    elif '9' in str(message).lower():
        qtd = message
        resumo['Qtd'] = str(qtd)
        return f'Quantidade do pedido: {qtd}. Esta correto?'
    elif 'um' in str(message).lower():
        qtd = 1
        return f'Quantidade do pedido: {qtd}. Esta correto?'
    elif 'dois' in str(message).lower():
        qtd = 2
        return f'Quantidade do pedido: {qtd}. Esta correto?'
    elif 'tres' in str(message).lower():
        qtd = 3
        return f'Quantidade do pedido: {qtd}. Esta correto?'
    elif 'quatro' in str(message).lower():
        qtd = 4
        return f'Quantidade do pedido: {qtd}. Esta correto?'
    elif 'cinco' in str(message).lower():
        qtd = 5
        return f'Quantidade do pedido: {qtd}. Esta correto?'
    elif 'seis' in str(message).lower():
        qtd = 6
        return f'Quantidade do pedido: {qtd}. Esta correto?'
    elif 'sete' in str(message).lower():
        qtd = 7
        return f'Quantidade do pedido: {qtd}. Esta correto?'
    elif 'oito' in str(message).lower():
        qtd = 8
        return f'Quantidade do pedido: {qtd}. Esta correto?'
    elif 'nove' in str(message).lower():
        qtd = 9
        return f'Quantidade do pedido: {qtd}. Esta correto?'
    elif message.lower() == 'sim':
        return 'E como pretende pagar?'
    elif message.lower() == 'nao':
        return 'Reinicie seu pedido!'
    elif 'dito' in str(message).lower():
        pagto = 'Cartao Credito'
        resumo['Pagto'] = str(pagto)
        get_name()
        contact_info()
        send_resumo()
        return f'Resumo do pedido: {resumo}. \nAgradecemos pela escolha! Volte Sempre!'
    elif 'bito' in str(message).lower():
        pagto = 'Cartao Debito'
        resumo['Pagto'] = str(pagto)
        get_name()
        contact_info()
        send_resumo()
        return f'Resumo do pedido: {resumo}. \nAgradecemos pela escolha! Volte Sempre!'
    elif 'dinheiro' in str(message).lower():
        pagto = 'Dinheiro'
        resumo['Pagto'] = str(pagto)
        get_name()
        contact_info()
        send_resumo()
        return f'Resumo do pedido: {resumo}. \nAgradecemos pela escolha! Volte Sempre!'
    else:
        food = ''
        recheio = ''
        qtd = ''
        pagto = ''
        return 'Seja bem vindo! A qualquer momento escreva "Pedido" para iniciar.'


# Check for new message
def check_new_message():
    pt.moveTo(x + 70, y - 40, duration=.5)

    while True:
        try:
            position = pt.locateOnScreen('green_circle.png', confidence=.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(.5)
        except(Exception):
            print('Sem novas mensagens')

        try:
            if pt.pixelMatchesColor(int(x + 70), int(y - 40), (255, 255, 255), tolerance=10):
                print('branco')
                processed_message = process_response(get_principal())
                post_response(processed_message)
            else:
                print('Sem novas mensagens no momento.')
            sleep(5)
        except(Exception):
            print('Erro 1')

def process_resume(message):
    return f'Resumo do pedido: {resumo}. Obrigado por nos escolher!'

#Gets Name
def get_name():
    global x, y, food, recheio, qtd, pagto, resumo

    position = pt.locateOnScreen('pesquisa.png', confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.5)
    pt.moveTo(x - 400, y + 20, duration=.5)
    pt.click()
    pt.moveTo(x + 100, y + 40, duration=.5)

def contact_info():
    global x, y, food, recheio, qtd, pagto, resumo

    position = pt.locateOnScreen('contact_info.png', confidence=.7)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.5)
    pt.moveTo(x + 40, y + 315, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12, 15)
    pt.click()
    contact_message = pyperclip.paste()
    pt.click()
    print('Nome do Cliente: ' + contact_message)

    resumo['Cliente'] = str(contact_message)
    return contact_message

def send_resumo():
    global x, y, food, recheio, qtd, pagto, resumo

    position = pt.locateOnScreen('contact_info.png', confidence=.7)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.5)
    pt.moveTo(x + 10, y + 10, duration=.5)
    pt.click()
    pt.moveTo(x + 100, y + 580, duration=.5)
    pt.click()


resumo['Lanche'] = str(food)
resumo['Recheio'] = str(recheio)
resumo['Qtd'] = str(qtd)
resumo['Pagto'] = str(pagto)

check_new_message()

