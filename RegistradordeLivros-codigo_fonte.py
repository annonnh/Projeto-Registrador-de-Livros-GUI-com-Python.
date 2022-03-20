# coding=utf-8
import PySimpleGUI as ps

# Janelas que serão executadas e Layouts
def janela_cadastro():
    ps.theme('DarkBlue2')
    fontt=20
    layout = [
        [ps.Text('Nome do Livro:\n', size=(14,1)), ps.Input(key='nomelivro', size=(60,1))],
        [ps.Text('Autor:\n', size=(14,1)), ps.Input(key='autor')],
        [ps.Text('Tradutor:\n', size=(14,1)), ps.Input(key='tradutor')],
        [ps.Text('ISBN:\n', size=(14,1)), ps.Input(key='isbn')],
        [ps.Text('Editora:\n', size=(14,1)), ps.Input(key='editora')],
        [ps.Text('Edição(data):\n', size=(14,1)), ps.Input(key='edicao')],
        [ps.Text('Data de Entrada:\n', size=(14,1)), ps.Input(key='datadeentrada')],
        [ps.Text('Preço de capa:\n', size=(14,1)), ps.Input(key='preco')],
        [ps.Text('Sinopse:\n', size=(14,1)), ps.Multiline(size=(48,10), key='textosinopse')],
        [ps.Text('\n')],
        [ps.Text('-------- Qual é o estado de conservação do livro --------')],
        [ps.Checkbox('Novo', key='botaonovo'), ps.Checkbox('Usado', key='botaousado')],
        [ps.Text('\n')],
        [ps.Button('Concluir', size=(100,5), font=fontt)],
        [ps.Text('\n')],
        [ps.Text('Register(0.0.1)---> Feito por: Anonmixs Amaro Afonso')]
        ]
    return ps.Window('Registrador de Livros', layout, finalize=True, size=(400,600))


# Janela opcional(se o livro for usado)
def janela_livro_usado():
    ps.theme('DarkBlue2')
    layout = [
        [ps.Text('Escreva um breve resumo do estado de conservação do livro')],
        [ps.Multiline('Usado, descrição do estado: ', key='livrousado', size=(400,40))],
        [ps.Button('Enviar')]
        ]
    return ps.Window('Descrição da condição do livro', layout, finalize=True, size=(400,600))


# Janela opcinal do resumo
def janela_de_resumo():
    ps.theme('DarkBlue2')
    layout = [
        [ps.Text('############ Resumo ############')],
        [ps.Output(size=(400,40))],
        [ps.Button('Fechar o resumo')]
        ]
    return ps.Window('Resumo', layout, finalize=True, size=(400,600))


def janela_pergunta():
    ps.theme('DarkBlue2')
    layout = [
        [ps.Text('Deseja cadastrar outro livro? ')],
        [ps.Button('Editar Cadastro')],
        [ps.Button('Salvar Cadastro e Sair do Programa')],
        [ps.Button('Salvar Cadastro e Cadastrar outro Livro')],
        [ps.Button('Cadastrar Outro Sem Salvar o Atual')],
        [ps.Button('Finalizar Programa')]
        ]
    return ps.Window('Deseja continuar?', layout, finalize=True, size=(400,200))


# Perguta sobre mostrar resumo ou não
def janela_pergunta_resumo():
    ps.theme('DarkBlue2')
    layout = [
        [ps.Text('Gostaria de Ver o resumo do cadastro?')],
        [ps.Button('Sim'), ps.Button('Não')]
        ]
    return ps.Window('Mostrar resumo', layout, finalize=True, size=(400,200))


# Iniciando as janelas(chamando as funções)
janela1, janela2, janela3, janela4, janela5 = janela_cadastro(), None, None, None, None

# Loop para ler as janelas, eventos e valores(manter a interface em funcionamento)
while True:
    janela, evento, valor = ps.read_all_windows()
    
    # Se a janela for fechada
    ########################################################
    if janela == janela1 and evento == ps.WIN_CLOSED:
        break
    if janela == janela2 and evento == ps.WIN_CLOSED:   
        janela2.close()
        break
    if janela == janela3 and evento == ps.WIN_CLOSED:
        break
    ########################################################
    
    # Se a opção Usado for selecionada(novo/usado)
    ########################################################
    if janela == janela1 and evento == 'Concluir':
        NomeLivro = valor['nomelivro']
        Autor = valor['autor']
        Tradutor = valor['tradutor']
        ISBN = valor['isbn']
        Editora = valor['editora']
        Edicao = valor['edicao']
        Data = valor['datadeentrada']
        Preco = valor['preco']
        Sinopse = valor['textosinopse']
        
    if janela == janela1 and valor['botaousado'] == True and valor['botaonovo'] == True:
        ps.popup('Selecione apenas uma opção(novo ou usado)')
        continue
    if janela == janela1 and valor['botaousado'] == False and valor['botaonovo'] == False and evento == 'Concluir':
        ps.popup('Selecione o estado de conservação do livro(novo ou usado)')
        continue
    if janela == janela1 and valor['botaousado'] == True and evento == 'Concluir':
        janela2 = janela_livro_usado()
        janela1.hide()
    elif janela == janela1 and valor['botaonovo'] == True and evento == 'Concluir':
        janela1.hide()
        janela5 = janela_pergunta_resumo()
        estado = 'Novo'
    elif janela == janela2 and evento == 'Enviar':
        estado = valor['livrousado']
        janela5 = janela_pergunta_resumo()
        janela2.close()
    ########################################################
    
    # Finalizando(se a opção não mostrar resumo for selecionada)
    ########################################################
    if janela == janela5 and evento == 'Não':
        janela5.close()
        janela1.hide()
        janela4 = janela_pergunta()
        

    ########################################################
    if janela == janela3 or janela == janela1 and evento == 'Fechar o Resumo':
        janela3.close()
        janela4 = janela_pergunta()
    
    # Escrevendo no arquivo.txt
    ########################################################
    
    # Mostranto todos os valores escritos no cadastro se a opção resumo for selecionada
    if janela == janela5 and evento == 'Sim':
        janela3 = janela_de_resumo()
        janela5.close()
        print(f'Nome do Livro: {NomeLivro}\n')
        print(f'Autor: {Autor}\n')
        print(f'Tradutor: {Tradutor}\n') 
        print(f'ISBN: {ISBN}\n') 
        print(f'Editora: {Editora}\n') 
        print(f'Edição: {Edicao}\n') 
        print(f'Data: {Data}\n') 
        print(f'Preço: {Preco}\n') 
        print(f'Sinopse: {Sinopse}\n')
        print(f'Estado: {estado}\n')
        
    # Quando a janela 5 aparecer
    ########################################################
    if janela == janela4 and evento == 'Cadastrar Outro Sem Salvar o Atual':
        janela1.close()
        janela4.close()
        janela1 = janela_cadastro()
    if janela == janela4 and evento == 'Editar Cadastro':
        janela4.close()
        janela1.un_hide()
    if janela == janela4 and evento == 'Salvar Cadastro e Sair do Programa':
        # Gerando o arquivo .txt
        ######################################
        arquivo = open('Cadastro_dos_livros.txt', 'a')
        arquivo.write('\n')
        arquivo.write('*'*60)
        arquivo.write('\n')
        arquivo.write(f'Nome do Livro: {NomeLivro}\n')
        arquivo.write(f'Autor: {Autor}\n')
        arquivo.write(f'Tradutor: {Tradutor}\n')
        arquivo.write(f'ISBN: {ISBN}\n')
        arquivo.write(f'Editora: {Editora}\n')
        arquivo.write(f'Edição: {Edicao}\n')
        arquivo.write(f'Data: {Data}\n')
        arquivo.write(f'Preço: {Preco}\n')
        arquivo.write(f'Sinopse: {Sinopse}\n')
        arquivo.write(f'Estado: {estado}\n')
        arquivo.write('*'*60)
        arquivo.write('\n')
        arquivo.close()
        break
        ######################################
    if janela == janela4 and evento == 'Salvar Cadastro e Cadastrar outro Livro':
        # Gerando o arquivo .txt
        ######################################
        arquivo = open('Cadastro_dos_livros.txt', 'a')
        arquivo.write('\n')
        arquivo.write('*'*60)
        arquivo.write('\n')
        arquivo.write(f'Nome do Livro: {NomeLivro}\n')
        arquivo.write(f'Autor: {Autor}\n')
        arquivo.write(f'Tradutor: {Tradutor}\n')
        arquivo.write(f'ISBN: {ISBN}\n')
        arquivo.write(f'Editora: {Editora}\n')
        arquivo.write(f'Edição: {Edicao}\n')
        arquivo.write(f'Data: {Data}\n')
        arquivo.write(f'Preço: {Preco}\n')
        arquivo.write(f'Sinopse: {Sinopse}\n')
        arquivo.write(f'Estado: {estado}\n')
        arquivo.write('*'*60)
        arquivo.write('\n')
        arquivo.close()
        janela1.close()
        janela4.close()
        janela1 = janela_cadastro()
        ######################################
    
    if janela == janela4 and evento == 'Finalizar Programa':
        break

##################################################################################
# FIM DO PROGRAMA GRÁFICO
##################################################################################

