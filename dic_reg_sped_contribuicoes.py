# Dicionário de dados feito com base no Guia Prático EFD-Contribuições – Versão 1.35 Atualização: 18 de junho de 2021, obtido no seguinte link:
# http://sped.rfb.gov.br/pasta/show/1989.

dic_registro_contribuicoes = {
    # BLOCO 0 ============================================================== INICIO #
    "0000": {
        "nome_reg": "Abertura do Arquivo Digital e Identificação da Pessoa Jurídica",
        "colunas_reg": ["REG", "COD_VER", "TIPO_ESCRIT", "IND_SIT_ESP", "NUM_REC_ANTERIOR", "DT_INI", "DT_FIN", "NOME", "CNPJ", "UF", "COD_MUN", "SUFRAMA", "IND_NAT_PJ", "IND_ATIV"]
    },
    "0001": {
        "nome_reg": "Abertura do Bloco 0",
        "colunas_reg": ["REG", "IND_MOV"]
    },
    "0100": {
        "nome_reg": "Dados do Contabilista",
        "colunas_reg": ["REG", "NOME", "CPF", "CRC", "CNPJ", "CEP", "END", "NUM", "COMPL", "BAIRRO", "FONE", "FAX", "EMAIL", "COD_MUN"]
    },
    "0110": {
        "nome_reg": "Regimes de Apuração da Contribuição Social e de Apropriação de Crédito",
        "colunas_reg": ["REG", "COD_INC_TRIB", "IND_APRO_CRED", "COD_TIPO_CONT", "IND_REG_CUM"]
    },
    "0111": {
        "nome_reg": "Tabela de Receita Bruta Mensal Para Fins de Rateio de Créditos Comuns",
        "colunas_reg": ["REG", "REC_BRU_NCUM_TRIB_MI", "REC_BRU_NCUM_NT_MI", "REC_BRU_NCUM_EXP", "REC_BRU_CUM", "REC_BRU_TOTAL"]
    },
    "0140": {
        "nome_reg": "Tabela de Cadastro de Estabelecimentos",
        "colunas_reg": ["REG", "COD_EST", "NOME", "CNPJ", "UF", "IE", "COD_MUN", "IM", "SUFRAMA"]
    },
    "0150": {
        "nome_reg": "Tabela de Cadastro do Participante",
        "colunas_reg": ["REG", "COD_PART", "NOME", "COD_PAIS", "CNPJ", "CPF", "IE", "COD_MUN", "SUFRAMA", "END", "NUM", "COMPL", "BAIRRO"]
    },
    "0190": {
        "nome_reg": "Identificação das Unidades de Medida",
        "colunas_reg": ["REG", "UNID", "DESCR"]
    },
    "0200": {
        "nome_reg": "Tabela de Identificação do Item (Produtos e Serviços)",
        "colunas_reg": ["REG", "COD_ITEM", "DESCR_ITEM", "COD_BARRA", "COD_ANT_ITEM", "UNID_INV", "TIPO_ITEM", "COD_NCM", "EX_IPI", "COD_GEN", "COD_LST", "ALIQ_ICMS"]
    },
    "0205": {
        "nome_reg": "Alteração do Item",
        "colunas_reg": ["REG", "DESCR_ANT_ITEM", "DT_INI", "DT_FIM", "COD_ANT_ITEM"]
    },
    "0400": {
        "nome_reg": "Tabela de Natureza da Operação/Prestação",
        "colunas_reg": ["REG", "COD_NAT", "DESCR_NAT"]
    },
    "0450": {
        "nome_reg": "Tabela de Informação Complementar do Documento Fiscal",
        "colunas_reg": ["REG", "COD_INF", "TXT"]
    },
    "0500": {
        "nome_reg": "Plano de Contas Contábeis",
        "colunas_reg": ["REG", "DT_ALT", "COD_NAT_CC", "IND_CTA", "NIVEL", "COD_CTA", "NOME_CTA", "COD_CTA_REF", "CNPJ_EST"]
    },
    "0600": {
        "nome_reg": "Centro de Custos",
        "colunas_reg": ["REG", "DT_ALT", "COD_CCUS", "CCUS"]
    },
    "0990": {
        "nome_reg": "Encerramento do Bloco 0",
        "colunas_reg": ["REG", "QTD_LIN_0"]
    },
    # BLOCO 0 ============================================================== FIM # - INCOMPLETO

	# BLOCO A ============================================================== INICIO #
    "A001": {
        "nome_reg": "Abertura do Bloco A",
        "colunas_reg": ["REG", "IND_MOV"]
    },
    "A010": {
        "nome_reg": "Identificação do Estabelecimento",
        "colunas_reg": ["REG", "CNPJ"]
    },
    "A100": {
        "nome_reg": "Documento - Nota Fiscal de Serviço",
        "colunas_reg": ["REG", "IND_OPER", "IND_EMIT", "COD_PART", "COD_SIT", "SER", "SUB", "NUM_DOC", "CHV_NFSE", "DT_COD", "DT_EXE_SERV", "VL_DOC", "IND_PGTO", "VL_DESC", "VL_BC_PIS", "VL_PIS", "VL_BC_COFINS", "VL_COFINS", "VL_PIS_RET", "VL_COFINS_RET", "VL_ISS"]
    },
    "A110": {
        "nome_reg": "Complemento do Documento - Informação Complementar da NF",
        "colunas_reg": ["REG", "COD_INF", "TXT_COMPL"]
    },
    "A170": {
        "nome_reg": "Complemento do Documento - Itens do Documento",
        "colunas_reg": ["REG", "NUM_ITEM", "COD_ITEM", "DESCR_COMPL", "VL_ITEM", "VL_DESC", "NAT_BC_CRED", "IND_ORIG_CRED", "CST_PIS", "VL_BC_PIS", "ALIQ_PIS", "VL_PIS", "CST_COFINS", "VL_BC_COFINS", "ALIQ_COFINS", "VL_COFINS", "COD_CTA", "COD_CCUS"]
    },
    "A990": {
        "nome_reg": "Encerramento do Bloco A",
        "colunas_reg": ["REG", "QTD_LIN_A"]
    },
    # BLOCO A ============================================================== FIM # - INCOMPLETO

	# BLOCO C ============================================================== INICIO #
    "C001": {
        "nome_reg": "Abertura do Bloco C",
        "colunas_reg": ["REG", "IND_MOV"]
    },
    "C010": {
        "nome_reg": "Identificação do Estabelecimento",
        "colunas_reg": ["REG", "CNPJ", "IND_ESCRI"]
    },
    "C100": {
        "nome_reg": "Documento - Nota Fiscal (Código 01), Nota Fiscal Avulsa (Código 1B), Nota Fiscal de Produtor (Código 04), NF-e (Código 55) e NFC-e (Código 65).",
        "colunas_reg": ["REG", "IND_OPER", "IND_EMIT", "COD_PART", "COD_MOD", "COD_SIT", "SER", "NUM_DOC", "CHV_NFE", "DT_DOC", "DT_E_S", "VL_DOC", "IND_PGTO", "VL_DESC", "VL_ABAT_NT", "VL_MERC", "IND_FRT", "VL_FRT", "VL_SEG", "VL_OUT_DA", "VL_BC_ICMS", "VL_ICMS", "VL_BC_ICMS_ST", "VL_ICMS_ST", "VL_IPI", "VL_PIS", "VL_COFINS", "VL_PIS_ST", "VL_COFINS_ST"]
    },
    "C110": {
        "nome_reg": "Complemento do Documento - Informação Complementar da Nota Fiscal (Códigos 01, 1B, 04 e 55)",
        "colunas_reg": ["REG", "COD_INF", "TXT_COMPL"]
    },
    "C120": {
        "nome_reg": "Complemento do Documento - Operações de Importação (Código 01)",
        "colunas_reg": ["REG", "COD_DOC_IMP", "NUM_DOC_IMP", "VL_PIS_IMP", "VL_COFINS_IMP", "NUM_ACD_RAW"]
    },
    "C170": {
        "nome_reg": "Complemento do Documento - Itens do Documento (Códigos 01, 1B, 04 e 55)",
        "colunas_reg": ["REG", "NUM_ITEM", "COD_ITEM", "DESCR_COMPL", "QTD", "UNID", "VL_ITEM", "VL_DESC", "IND_MOV", "CST_ICMS", "CFOP", "COD_NAT", "VL_BC_ICMS", "ALIQ_ICMS", "VL_ICMS", "VL_BC_ICMS_ST", "ALIQ_ST", "VL_ICMS_ST", "IND_APUR", "CST_IPI", "COD_ENQ", "VL_BC_IPI", "ALIQ_IPI", "VL_IPI", "CST_PIS", "VL_BC_PIS", "ALIQ_PIS", "QUANT_BC_PIS", "ALIQ_PIS_QUANT", "VL_PIS", "CST_COFINS", "VL_BC_COFINS", "ALIQ_COFINS", "QUANT_BC_COFINS", "ALIQ_COFINS_QUANT", "VL_COFINS", "COD_CTA"]
    },
    "C190": {
        "nome_reg": "Encerramento do Bloco C",
        "colunas_reg": ["REG", "QTD_LIN_C"]
    },
    "C500": {
        "nome_reg": "Nota Fiscal/Conta de Energia Elétrica (Código 06), Nota Fiscal de Energia Elétrica Eletrônica - NF3e (Código 66), Nota Fiscal/Conta de fornecimento D'água Canalizada (Código 29), Nota Fiscal/Consumo Fornecimento de Gás (Código 28) e NF-e (Código 55) - Documentos de Entrada / Aquisição com Crédito",
        "colunas_reg": ["REG", "COD_PART", "COD_MOD", "COD_SIT", "SER", "SUB", "NUM_DOC", "DT_DOC", "DT_ENT", "VL_DOC", "VL_ICMS", "COD_INF", "VL_PIS", "VL_COFINS", "CFV_DOCe"]
    },
    "C501": {
        "nome_reg": "Complemento da Operação (Códigos 06, 28 e 29) - PIS/Pasep",
        "colunas_reg": ["REG", "CST_PIS", "VL_ITEM", "NAT_BC_CRED", "VL_BC_PIS", "ALIQ_PIS", "VL_PIS", "COD_CTA"]
    },
    "C505": {
        "nome_reg": "Complemento da Operação (Códigos 06, 28 e 29) - Cofins",
        "colunas_reg": ["REG", "CTS_COFINS", "VL_ITEM", "NAT_BC_CRED", "VL_BC_COFINS", "ALIQ_COFINS", "VL_COFINS", "COD_CTA"]
    },
    "C990": {
        "nome_reg": "Encerramento do Bloco C",
        "colunas_reg": ["REG", "QTD_LIN_C"]
    },
    # BLOCO C ============================================================== FIM # - INCOMPLETO

	# BLOCO D ============================================================== INICIO #
    "D001": {
        "nome_reg": "Abertura do Bloco D",
        "colunas_reg": ["REG", "IND_MOV"]
    },
    "D010": {
        "nome_reg": "Identificação do Estabelecimento",
        "colunas_reg": ["REG", "CNPJ"]
    },
    "D100": {
        "nome_reg": "Aquisição de Serviços de Transporte - Nota Fiscal de Serviço de Transporte (Código 07), Conhecimento de Transporte Rodoviário de Cargas (Código 08), Conhecimento de Transporte de Cargas Avulso (Código 8B), Conhecimento de Transporte Aquaviário de Cargas (Código 09), Conhecimento de Transporte Aéreo (Código 10), Conhecimento de Transporte Ferroviário de Cargas (Código 11), Conhecimento de Transporte Multimodal de Cargas (Código 26), Nota Fiscal de Transporte Ferroviário de Carga (Código 27), Conhecimento de Transporte Eletrônico - CT-E (Código 57), Bilhete de Passagem Eletrônico - BP-e (Código 63) e Conhecimento de Transporte Eletrônico para Outros Serviços - CT-e OS, modelo 67",
        "colunas_reg": ["REG", "IND_OPER", "IND_EMIT", "COD_PART", "COD_MOD", "COD_SIT", "SER", "SUB", "NUM_DOC", "CHV_CTE", "DT_DOC", "DT_A_P", "TP_CT-e", "CHV_CTE_REF", "VL_DOC", "VL_DESC", "IND_FRT", "VL_SERV", "VL_BC_ICMS", "VL_ICMS", "VL_NT", "COD_INF", "COD_CTA"]
    },
    "D101": {
        "nome_reg": "Complemento do Documento de Transporte (Códigos 07, 08, 8B, 09, 10, 11, 26, 27, 57, 63 e 67) - PIS/Pasep",
        "colunas_reg": ["REG", "IND_NAT_FRT", "VL_ITEM", "CST_PIS", "NAT_BC_CRED", "VL_BC_PIS", "ALIQ_PIS", "VL_PIS", "COD_CTA"]
    },
    "D105": {
        "nome_reg": "Complemento do Documento de Transporte (Códigos 07, 08, 8B, 09, 10, 11, 26, 27, 57, 63 e 67) - Cofins",
        "colunas_reg": ["REG", "IND_NAT_FRT", "VL_ITEM", "CST_COFINS", "NAT_BC_CRED", "VL_BC_COFINS", "ALIQ_COFINS", "VL_COFINS", "COD_CTA"]
    },
    "D990": {
        "nome_reg": "Encerramento do Bloco D",
        "colunas_reg": ["REG", "QTD_LIN_D"]
    },
    # BLOCO D ============================================================== FIM # - INCOMPLETO

	# BLOCO F ============================================================== INICIO #
    "F001": {
        "nome_reg": "Abertura do Bloco F",
        "colunas_reg": ["REG", "IND_MOV"]
    },
    "F010": {
        "nome_reg": "Identificação do Estabelecimento",
        "colunas_reg": ["REG", "CNPJ"]
    },
    "F100": {
        "nome_reg": "Demais Documentos e Operações Geradoras de Contribuição e Créditos",
        "colunas_reg": ["REG", "IND_OPER", "COD_PART", "COD_ITEM", "DT_OPER", "VL_OPER", "CST_PIS", "VL_BC_PIS", "ALIQ_PIS", "VL_PIS", "CST_COFINS", "VL_BC_COFINS", "ALIQ_COFINS", "VL_COFINS", "NAT_BC_CRED", "IND_ORIG_CRED", "COD_CTA", "COD_CCUS", "DESC_DOC_OPER"]
    },
    "F600": {
        "nome_reg": "Contribuição Retida na Fonte",
        "colunas_reg": ["REG", "IND_NAT_RET", "DT_RET", "VL_BC_RET", "VL_RET", "COD_REC", "IND_NAT_REC", "CNPJ", "VL_RET_PIS", "VL_RET_COFINS", "IND_DEC"]
    },
    "F990": {
        "nome_reg": "Encerramento do Bloco F",
        "colunas_reg": ["REG", "QTD_LIN_F"]
    },
    # BLOCO F ============================================================== FIM # - INCOMPLETO

	# BLOCO I ============================================================== INICIO #
    "I001": {
        "nome_reg": "Abertura do Bloco I",
        "colunas_reg": ["REG", "IND_MOV"]
    },
    "I990": {
        "nome_reg": "Encerramento do Bloco I",
        "colunas_reg": ["REG", "QTD_LIN_I"]
    },
    # BLOCO I ============================================================== FIM # - INCOMPLETO

	# BLOCO M ============================================================== INICIO #
    "M001": {
        "nome_reg": "Abertura do Bloco M",
        "colunas_reg": ["REG", "IND_MOV"]
    },
    "M100": {
        "nome_reg": "Crédito de PIS/Pasep Relativo ao Período",
        "colunas_reg": ["REG", "COD_CRED", "IND_CRED_ORI", "VL_BC_PIS", "ALIQ_PIS", "QUANT_BC_PIS", "ALIQ_PIS_QUANT", "VL_CRED", "VL_AJUS_ACRES", "VL_AJUS_REDUC", "VL_CRED_DIF", "VL_CRED_DISP", "IND_DESC_CRED", "VL_CRED_DESC", "SLD_CRED"]
    },
    "M105": {
        "nome_reg": "Detalhamento da Base de Calculo do Crédito Apurado no Período - PISPasep",
        "colunas_reg": ["REG", "NAT_BC_CRED", "CST_PIS", "VL_BC_PIS_TOT", "VL_BC_PIS_CUM", "VL_BC_PIS_NC", "VL_BC_PIS", "QUANT_BC_PIS_TOT", "QUANT_BC_PIS", "DESC_CRED", ""]
    },
    "M200": {
        "nome_reg": "Consolidação da Contribuição para o PIS/Pasep do Período",
        "colunas_reg": ["REG", "VL_TOT_CONT_NC_PER", "VL_TOT_CRED_DESC", "VL_TOT_CRED_DESC_ANT", "VL_TOT_CONT_NC_DEV", "VL_RET_NC", "VL_OUT_DED_NC", "VL_CONT_NC_REC", "VL_TOT_CONT_CUM_PER", "VL_RET_CUM", "VL_OUT_DED_CUM", "VL_CONT_CUM_REC", "VL_TOT_CONT_REC"]
    },
    "M205": {
        "nome_reg": "Contribuição para o PIS/Pasep a Recolher - Detalhamento por Código de Receita",
        "colunas_reg": ["REG", "NUM_CAMPO", "COD_REC", "VL_DEBITO"]
    },
    "M210": {
        "nome_reg": "Detalhamento da Contribuição para o PIS/Pasep do Período",
        "colunas_reg": ["REG", "COD_CONT", "VL_REC_BRT", "VL_BC_CONT", "ALIQ_PIS", "QUANT_BC_PIS", "ALIQ_PIS_QUANT", "VL_CONT_APUR", "VL_AJUST_ACRES", "VL_AJUS_REDUC", "VL_CONT_DIFER", "VL_CONT_DIFER_ANT", "VL_CONT_PER"]
    },
    "M400": {
        "nome_reg": "Receitas Isentas, não Alcançadas pela Incidência da Contribuição, Sujeitas a Alíquota Zero ou de Vendas com Suspensão - PIS/Pasep",
        "colunas_reg": ["REG", "CST_PIS", "VL_TOT_REC", "COD_CTA", "DESC_COMPL"]
    },
    "M410": {
        "nome_reg": "Detalhamento das Receitas Isentas, não Alcançadas pela Incidência da Contribuição, Sujeitas a Alíquota Zero ou de Vendas com Suspensão - Cofins",
        "colunas_reg": ["REG", "NAT_REC", "VL_REC", "COD_CTA", "DESC_COMPL"]
    },
    "M500": {
        "nome_reg": "Crédito de Cofins Relativo Ao Período",
        "colunas_reg": ["REG", "COD_CRED", "IND_CRED_ORI", "VL_BC_COFINS", "ALIQ_COFINS", "QUANT_BC_COFINS", "ALIQ_COFINS_QUANT", "VL_CRED", "VL_AJUS_ACRES", "VL_AJUS_REDUC", "VL_CRED_DIFER", "VL_CRED_DISP", "IND_DESC_CRED", "VL_CRED_DESC", "SLD_CRED"]
    },
    "M505": {
        "nome_reg": "Detalhamento da Base de Calculo do Crédito Apurado no Período - Cofins",
        "colunas_reg": ["REG", "NAT_BC_CRED", "CST_COFINS", "VL_BC_COFINS_TOT", "VL_BC_COFINS_CUM", "VL_BC_COFINS_NC", "VL_BC_COFINS", "QUANT_BC_COFINS_TOT", "QUANT_BC_COFINS", "DESC_CRED"]
    },
    "M600": {
        "nome_reg": "Consolidação da Contribuição para a Seguridade Social - Cofins do Período",
        "colunas_reg": ["REG", "VL_TOT_CONT_NC_PER", "VL_TOT_CRED_DESC", "VL_TOT_CRED_DESC_ANT", "VL_TOT_CONT_NC_DEV", "VL_RET_NC", "VL_OUT_DED_NC", "VL_CONT_NC_REC", "VL_TOT_CONT_CUM_PER", "VL_RET_CUM", "VL_OUT_DED_CUM", "VL_CONT_CUM_REC", "VL_TOT_CONT_REC"]
    },
    "M605": {
        "nome_reg": "Cofins a Recolher - Detalhamento por Código de Receita",
        "colunas_reg": ["REG", "NUM_CAMPO", "COD_REC", "VL_DEBITO"]
    },
    "M610": {
        "nome_reg": "Detalhamento da Contribuição para a Seguridade Social - Cofins do Período",
        "colunas_reg": ["REG", "COD_CONT", "VL_REC_BRT", "VL_BC_CONT", "ALIQ_COFINS", "QUANT_BC_COFINS", "ALIQ_COFINS_QUANT", "VL_CONT_APUR", "VL_AJUS_ACRES", "VL_AJUS_REDUC", "VL_CONT_DIFER", "VL_CONT_DIFER_ANT", "VL_CONT_PER"]
    },
    "M800": {
        "nome_reg": "Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, Sujeitas a Alíquota Zero ou de Vendas Com Suspensão - Cofins",
        "colunas_reg": ["REG", "CST_COFINS", "VL_TOT_REC", "COD_CTA", "DESC_COMPL"]
    },
    "M810": {
        "nome_reg": "Detalhamento das Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, Sujeitas a Alíquota Zero ou de Vendas com Suspensão - Cofins",
        "colunas_reg": ["REG", "NAT_REC", "VL_REC", "COD_CTA", "DESC_COMPL"]
    },
    "M990": {
        "nome_reg": "Encerramento do Bloco M",
        "colunas_reg": ["REG", "QTD_LIN_M"]
    },
    # BLOCO M ============================================================== FIM # - INCOMPLETO

	# BLOCO P ============================================================== INICIO #
    "P001": {
        "nome_reg": "Abertura do Bloco P",
        "colunas_reg": ["REG", "IND_MOV"]
    },
    "P990": {
        "nome_reg": "Encerramento do Bloco P",
        "colunas_reg": ["REG", "QTD_LIN_P"]
    },
    # BLOCO P ============================================================== FIM # - INCOMPLETO

	# BLOCO 1 ============================================================== INICIO #
    "1001": {
        "nome_reg": "Abertura do Bloco 1",
        "colunas_reg": ["REG", "IND_MOV"]
    },
    "1100": {
        "nome_reg": "Controle de Créditos Fiscais - PIS/Pasep",
        "colunas_reg": ["REG", "PER_APU_CRED", "ORIG_CRED", "CNPJ_SUC", "COD_CRED", "VL_CRED_APU", "VL_CRED_EXT_APU", "VL_TOT_CRED_APU", "VL_CRED_DESC_PA_ANT", "VL_CRED_PER_PA_ANT", "VL_CRED_DCO_MP_PA_ANT", "SD_CRED_DISP_EFD", "VL_CRED_DESC_EFD", "VL_CRED_PER_EFD", "VL_CRED_DCO_MP_EFD", "VL_CRED_TRANS", "VL_CRED_OUT", "SLD_CRED_FIM"]
    },
    "1300": {
        "nome_reg": "Controle dos Valores Retidos na Fonte - PIS/Pasep",
        "colunas_reg": ["REG", "IND_NAT_RET", "PR_REC_RET", "VL_RET_APU", "VL_RET_DED", "VL_RET_PER", "VL_RET_DCOMP", "SLD_RET"]
    },
    "1500": {
        "nome_reg": "Controle de Créditos Fiscais - Cofins",
        "colunas_reg": ["REG", "PER_APU_CRED", "ORIG_CRED", "CNPJ_SUC", "COD_CRED", "VL_CRED_APU", "VL_CRED_EXT_APU", "VL_TOT_CRED_AP", "VL_CRED_DESC_PA_ANT", "VL_CRED_PER_PA_ANT", "VL_CRED_DCOMP_PA_ANT", "SD_CRED_DISP_EFD", "VL_CRED_DESC_EFD", "VL_CRED_PER_EFD", "VL_CRED_DCOMP_EFD", "VL_CRED_TRANS", "VL_CRED_OUT", "SLD_CRED_FIM"]
    },
    "1700": {
        "nome_reg": "Controle dos Valores Retidos na Fonte - Cofins",
        "colunas_reg": ["REG", "IND_NAT_RET", "PR_REC_RET", "VL_RET_APU", "VL_RET_DED", "VL_RET_PER", "VL_RET_DCOMP", "SLD_RET"]
    },
    "1990": {
        "nome_reg": "Encerramento do Bloco 1",
        "colunas_reg": ["REG", "QTD_LIN_1"]
    },
    # BLOCO 1 ============================================================== FIM # - INCOMPLETO

	# BLOCO 9 ============================================================== INICIO #
    "9001": {
        "nome_reg": "Abertura do Bloco 9",
        "colunas_reg": ["REG", "IND_MOV"]
    },
    "9900": {
        "nome_reg": "Registros do Arquivo",
        "colunas_reg": ["REG", "REG_BLC", "QTD_REG_BLC"]
    },
    "9990": {
        "nome_reg": "Encerramento do Bloco 9",
        "colunas_reg": ["REG", "QTD_LIN_9"]
    },
    "9999": {
        "nome_reg": "Encerramento do Arquivo Digital",
        "colunas_reg": ["REG", "QTD_LIN"]
    }
    # BLOCO 9 ============================================================== FIM #
}
