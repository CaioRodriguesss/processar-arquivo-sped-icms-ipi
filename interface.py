import PySimpleGUI as sg
import excecoes as exc
import funcoes as fun

##### INTERFACE GRÁFICA #####

# A interface é baseada em eventos dos componentes, como por exemplo, o clique de um botão, gera um evento que pode ser processado. O processamento dos dados é feito de forma procedural, com cada função do módulo manipular_funcoes executando uma parte do processo e servindo de suprimento para outras funções. 

# Estilização da interface gráfica
sg.set_options(
    text_element_background_color = "#E5E5E9",
    text_color="#656565",
    background_color="#E5E5E9",
    button_color=("#656565", "#BED133"),
    input_elements_background_color="#FFFFFF",
    input_text_color="#656565"
)

# Suprimento de dados advindo de funções para os componentes.
sup_tex_mes_ano = fun.texto_data_e_validade()
sup_tex_ult_uso = fun.busca_data_ultimo_uso()
autenticar = fun.programa_validado()

# Tempo definido para encerramento do programa.
tempo_encerramento = 60

# Layout dos campos de validação de dados
layout_validacao = [
    [
        sg.T("Mes/Ano de Uso - Autenticado", size=(25,1)), 
        sg.In(sup_tex_mes_ano, key="-TXT_VALID-", size=(20,1), readonly=True, justification="center"),
        sg.T("Último Uso", size=(14, 1)), 
        sg.In(sup_tex_ult_uso, key="-TXT_ULT_USO-", size=(20,1), readonly=True, justification="center")
    ],
    [
        sg.T("Código de Validação", size=(25,1)),
        sg.In("", key="-VALID_USO-", size=(20,1), readonly=autenticar, do_not_clear=False, tooltip="Informe o código de validação."), 
        sg.B("Validar", key="-BOTAO_VALID-", size=(15, 1), disabled=autenticar)
    ]
]

# Layout dos campos de seleção de arquivo para processamento.
layout_arquivo = [
    [
        sg.T('Selecione o tipo de arquivo SPED:', size=(30, 1), justification='left'), 
        sg.Radio("ICMS/IPI", "GRUPO_SPED", default=True, key="-ICMS_IPI-", background_color="#E5E5E9", circle_color="#FFFFFF"), sg.Radio("Contribuições", "GRUPO_SPED", default=False, key="-CONTRIB-", background_color="#E5E5E9", circle_color="#FFFFFF"),
        sg.Push(), sg.T("01:00", key="-TEMPO-")
    ],
    [
        sg.FileBrowse(button_text='Selecionar', key='-SELEC_ARQ-', size=(15, 1), target='-TXT_ARQ-', file_types=[("TXT files", "*.txt")]),
        sg.In('Nenhum arquivo selecionado.', key='-TXT_ARQ-', size=(70, 1), readonly=True)
    ],
    [
        sg.B(button_text='Processar arquivo', key='-BOTAO_PROCES-', size=(38, 1)),
        sg.B(button_text='Limpar Dados', key='-BOTAO_LIMP-', size=(38, 1))
    ],
    [sg.ProgressBar(max_value=1000, orientation="h", size=(58, 12), key="-PROG-", bar_color=("#BED133", "#FFFFFF"))]
]

# Layout da interface gráfica.
layout = [
    [sg.Frame("Validação De Dados", layout=layout_validacao, background_color="#E5E5E9", title_color="#1B1B1B")],
    [sg.Frame("Processamento De Arquivo", layout=layout_arquivo, background_color="#E5E5E9", title_color="#1B1B1B")]
    
]

window = sg.Window(title='Manipulador De Arquivo SPED ICMS/IPI', layout=layout, icon="5N_icone_padrao.ico")

# Exclusão de variáveis
del sup_tex_mes_ano, sup_tex_ult_uso, autenticar

# Loop de funcionamento de interface gráfica, a saída é feita por meio do fechamento da janela.
while True:
    event, value = window.read(timeout=1000)
    if event == sg.WIN_CLOSED:
        break

    # Atualização a cada segundo do campo de texto que indicar o tempo de desligamento do programa.
    tempo_encerramento -= 1
    window["-TEMPO-"].update(value=f"00:{tempo_encerramento}" if tempo_encerramento >= 10 else f"00:0{tempo_encerramento}")

    # Atualização do campo de validação no processo de digitação. Precisa disso por conta da atualização constante a cada 1 segundo do timeout no window.read().
    window["-VALID_USO-"].update(value=value["-VALID_USO-"])

    # Encerra o programa após o fim do tempo definido.
    if tempo_encerramento < 0:
        break
    
    # Evento (botão) para validar o programa utilizando uma senha.
    if event == "-BOTAO_VALID-":
        try:
            fun.verificar_e_adicionar_senha(value["-VALID_USO-"])
            window["-TXT_VALID-"].update(value=fun.texto_data_e_validade())
            window["-VALID_USO-"].update(disabled=fun.programa_validado())
            sg.popup("Programa validado!", title="Concluído", icon="5N_icone_padrao.ico")

        except exc.SenhaDiferenteDoHash:
            sg.popup("A senha informada não coincide com a senha para o mês atual.", title="Erro", icon="5N_icone_erro.ico")
        except exc.SenhaEmBranco:
            sg.popup("Não é possível validar uma senha em branco.", title="Erro", icon="5N_icone_erro.ico")

    # Evento que chama a função que irá processar o arquivo SPED ICMS/IPI. As excessões fornecidas pelo módulo "excessões.py" são lançadas e tratadas para alguns tipos de manuseio do usuário, como por exemplo, tentar processar um arquivo sem selecionar um arquivo previamente. O tratamento é feito com o levantamento de pop-ups com mensagens de erro e destaque do logo em vermelho.
    if event == "-BOTAO_PROCES-":
        if value["-ICMS_IPI-"] == True:
            try:
                caminho_arquivo = str(value["-TXT_ARQ-"]).strip()

                if value["-TXT_ARQ-"] == "Nenhum arquivo selecionado.":
                    raise exc.NenhumArquivoSelecionado("Selecione um arquivo antes de processar.")
                
                if fun.programa_validado() is False:
                    raise exc.ArquivoNaoAutenticado("O programa precisa ser autenticado com o código mensal antes de processar o arquivo.")
                
                if fun.confrontar_data_de_uso_com_data_atual() is False:
                    raise exc.MesOuAnoMenoresDoQueUltimoProcessamento("O mês do ano ano atual é menor do que o mês do último processamento de arquivo registrado pelo sistema. A data da máquina local pode ter sido modificada.")
                
                ok_cancel = sg.popup_ok_cancel("Deseja processar o arquivo selecionado?", title="Confirmação", icon="5N_icone_padrao.ico")
                if ok_cancel == "OK":
                    try:
                        for i in range(400):
                            window["-PROG-"].UpdateBar(i)

                        fun.manipular_e_processar_arq_sped_icms_ipi(caminho_arquivo)

                        for i in range(401, 1000):
                            window["-PROG-"].UpdateBar(i)

                        fun.adicionar_data_ultimo_uso()
                        sg.popup("Arquivo processado com sucesso!", title="Concluído", icon="5N_icone_padrao.ico")
                        window["-PROG-"].UpdateBar(0)

                    except exc.NaoEumArquivoSpedValido:
                        sg.popup("O arquivo selecionado não é um arquivo SPED válido.", title="Erro", icon="5N_icone_erro.ico")
                        window["-PROG-"].UpdateBar(0)

                if ok_cancel == "Cancel":
                    pass
            
            except exc.NenhumArquivoSelecionado:
                sg.popup("Selecione um arquivo antes de processar.", title="Erro", icon="5N_icone_erro.ico")
            except exc.ArquivoNaoAutenticado:
                sg.popup(
                    "O programa precisa ser autenticado com o código mensal antes de processar o arquivo.",
                    title="Erro",
                    icon="5N_icone_erro.ico"
                )
            except exc.MesOuAnoMenoresDoQueUltimoProcessamento:
                sg.popup("O mês do ano ano atual é menor do que o mês do último processamento de arquivo registrado pelo sistema. A data da máquina local pode ter sido modificada.",
                        title="Erro", 
                        icon="5N_icone_erro.ico"
                )
        if value["-CONTRIB-"] == True:
            try:
                caminho_arquivo = str(value["-TXT_ARQ-"]).strip()

                if value["-TXT_ARQ-"] == "Nenhum arquivo selecionado.":
                    raise exc.NenhumArquivoSelecionado("Selecione um arquivo antes de processar.")
                
                if fun.programa_validado() is False:
                    raise exc.ArquivoNaoAutenticado("O programa precisa ser autenticado com o código mensal antes de processar o arquivo.")
                
                if fun.confrontar_data_de_uso_com_data_atual() is False:
                    raise exc.MesOuAnoMenoresDoQueUltimoProcessamento("O mês do ano ano atual é menor do que o mês do último processamento de arquivo registrado pelo sistema. A data da máquina local pode ter sido modificada.")
                
                ok_cancel = sg.popup_ok_cancel("Deseja processar o arquivo selecionado?", title="Confirmação", icon="5N_icone_padrao.ico")
                if ok_cancel == "OK":
                    try:
                        for i in range(400):
                            window["-PROG-"].UpdateBar(i)

                        fun.manipular_e_processar_arq_sped_contribuicoes(caminho_arquivo)

                        for i in range(401, 1000):
                            window["-PROG-"].UpdateBar(i)

                        fun.adicionar_data_ultimo_uso()
                        sg.popup("Arquivo processado com sucesso!", title="Concluído", icon="5N_icone_padrao.ico")
                        window["-PROG-"].UpdateBar(0)

                    except exc.NaoEumArquivoSpedValido:
                        sg.popup("O arquivo selecionado não é um arquivo SPED válido.", title="Erro", icon="5N_icone_erro.ico")
                        window["-PROG-"].UpdateBar(0)

                if ok_cancel == "Cancel":
                    pass
            
            except exc.NenhumArquivoSelecionado:
                sg.popup("Selecione um arquivo antes de processar.", title="Erro", icon="5N_icone_erro.ico")
            except exc.ArquivoNaoAutenticado:
                sg.popup(
                    "O programa precisa ser autenticado com o código mensal antes de processar o arquivo.",
                    title="Erro",
                    icon="5N_icone_erro.ico"
                )
            except exc.MesOuAnoMenoresDoQueUltimoProcessamento:
                sg.popup("O mês do ano ano atual é menor do que o mês do último processamento de arquivo registrado pelo sistema. A data da máquina local pode ter sido modificada.",
                        title="Erro", 
                        icon="5N_icone_erro.ico"
                )

    # Evento para limpar o caminho de um arquivo selecionado.
    if event == "-BOTAO_LIMP-":
        window['-TXT_ARQ-'].update(value="Nenhum arquivo selecionado.")

window.close()
