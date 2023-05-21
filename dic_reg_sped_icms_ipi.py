# Dicionário de dados feito com base no Guia Prático EFD-ICMS/IPI – Versão 3.1.3 Atualização: 01 de março de 2023, obtido no seguinte link:
# http://sped.rfb.gov.br/pasta/show/1573.

dic_registro_sped = {
    # BLOCO 0 ============================================================== INICIO #
	"0000": {
		"nome_reg": "Abertura do Arquivo Digital e Identificação da entidade",
		"colunas_reg": ['REG', 'COD_VER', 'COD_FIN', 'DT_INI', 'DT_FIM', 'NOME', 'CNPJ', 'CPF', 'UF', 'IE', 'COD_MUN', 'IM', 'SUFRAMA', 'IND_PERFIL', 'IND_ATIV']
	},
	"0001": {
		"nome_reg": "Abertura do Bloco 0",
		"colunas_reg": ['REG', 'IND_MOV']
	},
	"0002": {
		"nome_reg": "Classificação do Estabelecimento Industrial ou Equiparado a Industrial",
		"colunas_reg": ['REG', 'CLAS_ESTAB_IND']
	},
	"0005":	{
		"nome_reg": "Dados Complementares da entidade",
		"colunas_reg": ['REG', 'FANTASIA', 'CEP', 'END', 'NUM', 'COMPL', 'BAIRRO', 'FONE', 'FAX', 'EMAIL']
	},
	"0015": {
		"nome_reg": "Dados do Contribuinte Substituto ou Responsável pelo ICMS Destino",
		"colunas_reg": ['REG', 'UF_ST', 'IE_ST']
	},
	"0100": {
		"nome_reg": "Dados do Contabilista",
		"colunas_reg": ['REG', 'NOME', 'CPF', 'CRC', 'CNPJ', 'CEP', 'END', 'NUM', 'COMPL', 'BAIRRO', 'FONE', 'FAX', 'EMAIL', 'COD_MUN']
	},
	"0150": {
		"nome_reg": "Tabela de Cadastro do Participante",
		"colunas_reg": ['REG', 'COD_PART', 'NOME', 'COD_PAIS', 'CNPJ', 'CPF', 'IE', 'COD_MUN', 'SUFRAMA', 'END', 'NUM', 'COMPL', 'BAIRRO']
	},
	"0175": {
		"nome_reg": "Alteração da Tabela de Cadastro de Participante",
		"colunas_reg": ['REG', 'DT_ALT', 'NR_CAMPO', 'CONT_ANT']
	},
	"0190": {
		"nome_reg": "Identificação das unidades de medida",
		"colunas_reg": ['REG', 'UNID', 'DESCR']
	},
	"0200": {
		"nome_reg": "Tabela de Identificação do Item (Produtos e Serviços)",
		"colunas_reg": ['REG', 'COD_ITEM', 'DESCR_ITEM', 'COD_BARRA', 'COD_ANT_ITEM', 'UNID_INV', 'TIPO_ITEM', 'COD_NCM', 'EX_IPI', 'COD_GEN', 'COD_LST', 'ALIQ_ICMS', 'CEST']
	},
	"0205": {
		"nome_reg": "Alteração do Item",
		"colunas_reg": ['REG', 'DESCR_ANT_ITEM', 'DT_INI', 'DT_FIM', 'COD_ANT_ITEM']
	},
	"0206": {
		"nome_reg": "Código de produto conforme Tabela ANP",
		"colunas_reg": ['REG', 'COD_COMB']
	},
	"0210": {
		"nome_reg": "Consumo Específico Padronizado",
		"colunas_reg": ['REG', 'COD_ITEM_COMP', 'QTD_COMP', 'PERDA']
	},
	"0220": {
		"nome_reg": "Fatores de Conversão de Unidades",
		"colunas_reg": ['REG', 'UNID_CONV', 'FAT_CONV', 'COD_BARRA']
	},
	"0221": {
		"nome_reg": "Correlação entre códigos de itens comercializados",
		"colunas_reg": ['REG', 'COD_ITEM_ATOMICO', 'QTD_CONTIDA']
	},
	"0300": {
		"nome_reg": "Cadastro de bens ou componentes do Ativo Imobilizado",
		"colunas_reg": ['REG', 'COD_IND_BEM', 'IDENT_MERC', 'DESCR_ITEM', 'COD_PRNC', 'COD_CTA', 'NR_PARC']
	},
	"0305": {
		"nome_reg": "Informação sobre a Utilização do Bem",
		"colunas_reg": ['REG', 'COD_CCUS', 'FUNC', 'VIDA_UTIL']
	},
	"0400": {
		"nome_reg": "Tabela de Natureza da Operação/ Prestação",
		"colunas_reg": ['REG', 'COD_NAT', 'DESCR_NAT']
	},
	"0450": {
		"nome_reg": "Tabela de Informação Complementar do documento fiscal",
		"colunas_reg": ['REG', 'COD_INF', 'TXT']
	},
	"0460": {
		"nome_reg": "Tabela de Observações do Lançamento Fiscal",
		"colunas_reg": ['REG', 'COD_OBS', 'TXT']
	},
	"0500": {
		"nome_reg": "Plano de contas contábeis",
		"colunas_reg": ['REG', 'DT_ALT', 'COD_NAT_CC', 'IND_CTA', 'NIVEL', 'COD_CTA', 'NOME_CTA']
	},
	"0600": {
		"nome_reg": "Centro de custos",
		"colunas_reg": ['REG', 'DT_ALT', 'COD_CCUS', 'CCUS']
	},
	"0990": {
		"nome_reg": "Encerramento do Bloco 0",
		"colunas_reg": ['REG', 'QTD_LIN_0']
	},
    # BLOCO 0 ============================================================== FIM #

	# BLOCO B ============================================================== INICIO #
	"B001": {
		"nome_reg": "Abertura do Bloco B",
		"colunas_reg": ['REG', 'IND_DAD']
	},
	"B020": {
		"nome_reg": "Nota Fiscal (código 01), Nota Fiscal de Serviços (código 03), Nota Fiscal de Serviços Avulsa (código 3B), \
                     Nota Fiscal de Produtor (código 04), Conhecimento de Transporte Rodoviário de Cargas (código 08), NF-e (código55) e NFC-e (código 65)",
		"colunas_reg": [
					       'REG', 'IND_OPER', 'IND_EMIT', 'COD_PART', 'COD_MOD', 'COD_SIT', 'SER', 'NUM_DOC', 'CHV_NFE', 'DT_DOC', 'COD_MUN_SERV', 'VL_CONT', 'VL_MAT_TERC', 'VL_SUB',
						   'VL_ISNT_ISS', 'VL_DED_BC', 'VL_BC_ISS', 'VL_BC_ISS_RET', 'VL_ISS_RT', 'VL_ISS', 'COD_INF_OBS'
					   ]
	},
	"B025": {
		"nome_reg": "Detalhamento por combinação de alíquota e item da lista de serviços da Lei Complementar nº 116/2003",
		"colunas_reg": ['REG', 'VL_CONT_P', 'VL_BC_ISS_P', 'ALIQ_ISS', 'VL_ISS_P', 'VL_ISNT_ISS_P', 'COD_SERV']
	},
	"B030": {
		"nome_reg": "Nota Fiscal de Serviços Simplificada (código 3A)",
		"colunas_reg": ['REG', 'COD_MOD', 'SER', 'NUM_DOC_INI', 'NUM_DOC_FIN', 'DT_DOC', 'QTD_CANC', 'VL_CONT', 'VL_ISNT_ISS', 'VL_BC_ISS', 'VL_ISS', 'COD_INF_OBS']
	},
	"B035": {
		"nome_reg": "Detalhamento por combinação de alíquota e item da lista de serviços da Lei Complementar nº 116/2003",
		"colunas_reg": ['REG', 'VL_CONT_P', 'VL_BC_ISS_P', 'ALIQ_ISS', 'VL_ISS_P', 'VL_ISNT_ISS_P', 'COD_SERV']
	},
	"B350": {
		"nome_reg": "Serviços prestados por instituições financeiras",
		"colunas_reg": ['REG', 'COD_CTD', 'CTA_ISS', 'CTA_COSIF', 'QTD_OCOR', 'COD_SERV', 'VL_CONT', 'VL_BC_ISS', 'ALIQ_ISS', 'VL_ISS', 'COD_INF_OBS']
	},
	"B420": {
		"nome_reg": "Totalização dos valores de serviços prestados por combinação de alíquota e item da lista de serviços da Lei Complementar nº 116/2003",
		"colunas_reg": ['REG', 'VL_CONT', 'VL_BC_ISS', 'ALIQ_ISS', 'VL_ISNT_ISS', 'VL_ISS', 'COD_SERV']
	},
	"B440": {
		"nome_reg": "Totalização dos valores retidos",
		"colunas_reg": ['REG', 'IND_OPER', 'COD_PART', 'VL_CONT_RT', 'VL_BC_ISS_RT', 'VL_ISS_RT']
	},
	"B460": {
		"nome_reg": "Deduções do ISS",
		"colunas_reg": ['REG', 'IND_DED', 'VL_DED', 'NUM_PROC', 'IND_PROC', 'PROC', 'COD_INF_OBS', 'IND_OBR']
	},
	"B470": {
		"nome_reg": "Apuração do ISS",
		"colunas_reg": [
		                   'REG', 'VL_CONT', 'VL_MAT_TERC', 'VL_MAT_PROP', 'VL_SUB', 'VL_ISNT', 'VL_DED_BC', 'VL_BC_ISS', 'VL_BC_ISS_RT', 'VL_ISS', 'VL_ISS_RET',
						   'VL_DED', 'VL_ISS_REC', 'VL_ISS_ST', 'VL_ISS_REC_UNI'
					   ]
	},
	"B500": {
		"nome_reg": "Apuração do ISS sociedade uniprofissional",
		"colunas_reg": ['REG', 'VL_REC', 'QTD_PROF', 'VL_OR']
	},
	"B510": {
		"nome_reg": "Uniprofissional – empregados e sócios ",
		"colunas_reg": ['REG', 'IND_PROF', 'IND_ESC', 'IND_SOC', 'CPF', 'NOME']
	},
	"B990": {
		"nome_reg": "Encerramento do Bloco B",
		"colunas_reg": ['REG', 'QTD_LIN_B']
	},
    # BLOCO B ============================================================== FIM #

	# BLOCO C ============================================================== INICIO #
	"C001": {
		"nome_reg": "Abertura do Bloco C",
		"colunas_reg": ['REG', 'IND_MOV']
	},
	"C100": {
		"nome_reg": "Documento - Nota Fiscal (código 01), Nota Fiscal Avulsa (código 1B), Nota Fiscal de Produtor (código 04), Nota Fiscal Eletrônica (código55) e Nota Fiscal Eletrônica para Consumidor Final (código 65)",
		"colunas_reg": [
                           'REG', 'IND_OPER', 'IND_EMIT', 'COD_PART', 'COD_MOD', 'COD_SIT', 'SER', 'NUM_DOC', 'CHV_NFE', 'DT_DOC', 'DT_E_S', 
                           'VL_DOC', 'IND_PGTO', 'VL_DESC', 'VL_ABAT_NT', 'VL_MERC', 'IND_FRT', 'VL_FRT', 'VL_SEG', 'VL_OUT_DA', 'VL_BC_ICMS',
                           'VL_ICMS', 'VL_BC_ICMS_ST', 'VL_ICMS_ST', 'VL_IPI', 'VL_PIS', 'VL_COFINS', 'VL_PIS_ST', 'VL_COFINS_ST'
                       ]
	},
	"C101": {
		"nome_reg": "Informação complementar dos documentos fiscais quando das operações interestaduais destinadas a consumidor final não contribuinte EC 87/15 (código 55)",
		"colunas_reg": ['REG', 'VL_FCP_UF_DEST', 'VL_ICMS_UF_DEST', 'VL_ICMS_UF_REM']
	},
	"C105": {
		"nome_reg": "Operações com ICMS ST recolhido para UF diversa do destinatário do documento fiscal (Código 55)",
		"colunas_reg": ['REG', 'OPER', 'UF']
	},
	"C110": {
		"nome_reg": "Complemento de Documento - Informação Complementar da Nota Fiscal (código 01, 1B, 55)",
		"colunas_reg": ['REG', 'COD_INF', 'TXT_COMPL']
	},
	"C111": {
		"nome_reg": "Complemento de Documento - Processo referenciado",
		"colunas_reg": ['REG', 'NUM_PROC', 'IND_PROC']
	},
	"C112": {
		"nome_reg": "Complemento de Documento - Documento de Arrecadação Referenciado",
		"colunas_reg": ['REG', 'COD_DA', 'UF', 'NUM_DA', 'COD_AUT', 'VL_DA', 'DT_VCTO', 'DT_PGTO']
	},
	"C113": {
		"nome_reg": "Complemento de Documento - Documento Fiscal Referenciado",
		"colunas_reg": ['REG', 'IND_OPER', 'IND_EMIT', 'COD_PART', 'COD_MOD', 'SER', 'SUB', 'NUM_DOC', 'DT_DOC', 'CHV_DOCe']
	},
	"C114": {
		"nome_reg": "Complemento de Documento - Cupom Fiscal Referenciado",
		"colunas_reg": ['REG', 'COD_MOD', 'ECF_FAB', 'ECF_CX', 'NUM_DOC', 'DT_DOC']
	},
	"C115": {
		"nome_reg": "Local de coleta e/ou entrega (CÓDIGOS 01, 1B e 04)",
		"colunas_reg": ['REG', 'IND_CARGA', 'CNPJ_COL', 'IE_COL', 'CPF_COL', 'COD_MUN_COL', 'CNPJ_ENTG', 'IE_ENTG', 'CPF_ENTG', 'COD_MUN_ENTG']
	},
	"C116": {
		"nome_reg": "Cupom Fiscal Eletrônico - CF-e referenciado",
		"colunas_reg": ['REG', 'COD_MOD', 'NR_SAT', 'CGV_CFE', 'NUM_CFE', 'DT_DOC']
	},
	"C120": {
		"nome_reg": "Complemento de Documento - Operações de Importação (código 01 e 55)",
		"colunas_reg": ['REG', 'COD_DOC_IMP', 'NUM_DOC_IMP', 'PIS_IMP', 'COFINS_IMP', 'NUM_ACDRAW']
	},
	"C130": {
		"nome_reg": "Complemento de Documento - ISSQN, IRRF e Previdência Social",
		"colunas_reg": ['REG', 'VL_SERV_NT', 'VL_BC_ISSQN', 'VL_ISSQN', 'VL_BC_IRRF', 'VL_IRRF', 'VL_BC_PREV', 'VL_PREV']
	},
	"C140": {
		"nome_reg": "Complemento de Documento - Fatura (código 01)",
		"colunas_reg": ['REG', 'IND_EMIT', 'IND_TIT', 'DESC_TIT', 'NUM_TIT', 'QTD_PARC', 'VL_TIT']
	},
	"C141": {
		"nome_reg": "Complemento de Documento - Vencimento da Fatura (código 01)",
		"colunas_reg": ['REG', 'NUM_PARC', 'DT_VCTO', 'VL_PARC']
	},
	"C160": {
		"nome_reg": "Complemento de Documento - Volumes Transportados (código 01 e 04) Exceto Combustíveis",
		"colunas_reg": ['REG', 'COD_PART', 'VEIC_ID', 'QTD_VOL', 'PESO_BRT', 'PESO_LIQ', 'UF_ID']
	},
	"C165": {
		"nome_reg": "Complemento de Documento - Operações com combustíveis (código 01)",
		"colunas_reg": [
                           'REG', 'COD_PART', 'VEIC_ID', 'COD_AUT', 'NR_PASSE', 'HORA', 'TEMPER', 'QTD_VOL', 'PESO_BRT',
                           'PESO_LIQ', 'NOM_MOT', 'CPF', 'UF_ID'
                       ]
	},
	"C170": {
		"nome_reg": "Complemento de Documento - Itens do Documento (código 01, 1B, 04 e 55)",
		"colunas_reg": [
                           'REG', 'NUM_ITEM', 'COD_ITEM', 'DESCR_COMPL', 'QTD', 'UNID', 'VL_ITEM', 'VL_DESC', 'IND_MOV',
                           'CST_ICMS', 'CFOP', 'COD_NAT', 'VL_BC_ICMS', 'ALIQ_ICMS', 'VL_ICMS', 'VL_BC_ICMS_ST', 'ALIQ_ST',
                           'VL_ICMS_ST', 'IND_APUR', 'CST_IPI', 'COD_ENQ', 'VL_BC_IPI', 'ALIQ_IPI', 'VL_IPI', 'CST_PIS',
                           'VL_BC_PIS', 'ALIQ_PIS', 'QUANT_BC_PIS', 'ALIQ_PIS', 'VL_PIS', 'CST_COFINS', 'VL_BC_COFINS', 'ALIQ_COFINS',
                           'QUANT_BC_COFINS', 'ALIQ_COFINS', 'VL_COFINS', 'COD_CTA', 'VL_ABAT_NT'
                       ]
	},
	"C171": {
		"nome_reg": "Complemento de Item - Armazenamento de Combustíveis (código 01,55)",
		"colunas_reg": ['REG', 'NUM_TANQUE', 'QTDE']
	},
	"C172": {
		"nome_reg": "Complemento de Item - Operações com ISSQN (código 01)",
		"colunas_reg": ['REG', 'VL_BC_ISSQN', 'ALIQ_ISSQN', 'VL_ISSQN']
	},
	"C173": {
		"nome_reg": "Complemento de Item - Operações com Medicamentos (código 01,55)",
		"colunas_reg": ['REG', 'LOTE_MED', 'QTD_ITEM', 'DT_FAB', 'DT_VAL', 'IND_MED', 'TP_PROD', 'VL_TAB_MAX']
	},
	"C174": {
		"nome_reg": "Complemento de Item - Operações com Armas de Fogo (código 01)",
		"colunas_reg": ['REG', 'IND_ARM', 'NUM_ARM', 'DESCR_COMPL']
	},
	"C175": {
		"nome_reg": "Complemento de Item - Operações com Veículos Novos (código 01,55)",
		"colunas_reg": ['REG', 'IND_VEIC_OPER', 'CNPJ', 'UF', 'CHASSI_VEIC']
	},
	"C176": {
		"nome_reg": "Complemento de Item -Ressarcimento de ICMS em operações com Substituição Tributária (código 01,55)",
		"colunas_reg": [
                            'REG', 'COD_MOD_ULT_E', 'NUM_DOC_ULT_E', 'SER_ULT_E', 'DT_ULT_E', 'COD_PART_ULT_E', 'QUANT_ULT_E',
                            'VL_UNIT_ULT_E', 'VL_UNIT_BC_ST', 'CHAVE_NFE_ULT_E', 'NUM_ITEM_ULT_E', 'VL_UNIT_BC_ICMS_ULT_E',
                            'ALIQ_ICMS_ULT_E', 'VL_UNIT_LIMITE_BC_ICMS_ULT_E', 'VL_UNIT_ICMS_ULT_E', 'ALIQ_ST_ULT_E', 'VL_UNIT_RES',
                            'COD_RESP_RET', 'COD_MOT_RES', 'CHAVE_NFE_RET', 'COD_PART_NFE_RET', 'SER_NFE_RET',
                            'NUM_NFE_RET', 'ITEM_NFE_RET', 'COD_DA', 'NUM_DA', 'VL_UNIT_RES_FCP_ST'
                       ]
	},
	"C177": {
		"nome_reg": "Complemento de Item – Outras informações (Cód. 01, 55) – (Válido a partir de 01/01/2019)",
		"colunas_reg": ['REG', 'COD_INF_ITEM']
	},
	"C178": {
		"nome_reg": "Complemento de Item - Operações com Produtos Sujeitos a Tributação de IPI por Unidade ou Quantidade de produto",
		"colunas_reg": ['REG', 'CL_ENQ', 'VL_UNID', 'QUANT_PAD']
	},
	"C179": {
		"nome_reg": "Complemento de Item - Informações Complementares ST (código 01) ",
		"colunas_reg": ['REG', 'BC_ST_ORIG_DEST', 'ICMS_ST_REP', 'ICMS_ST_COMPL', 'BC_RET', 'ICMS_RET']
	},
	"C180": {
		"nome_reg": "Informações complementares das operações de entrada de mercadorias sujeitas à substituição tributária (código 01, 1B, 04 e 55)",
		"colunas_reg": [
                           'REG', 'COD_RESP_RET', 'QUANT_CONV', 'UNID', 'VL_UNIT_CONV', 'VL_UNIT_ICMS_OP_CONV',
                           'VL_UNIT_BC_ICMS_ST_CONV', 'VL_UNIT_ICMS_ST_CONV', 'VL_UNIT_FCP_ST_CONV', 'COD_DA', 'NUM_DA'
                       ]
	},
	"C181": {
		"nome_reg": "Informações complementares das operações de devolução de saídas de mercadorias sujeitas à substituição tributária (código 01, 1B, 04 e 55).",
		"colunas_reg": [
                            'REG', 'COD_MOT_REST_COMPL', 'QUANT_CONV', 'UNID', 'COD_MOD_SAIDA', 'SERIE_SAIDA', 'ECF_FAB_SAIDA',
                            'NUM_DOC_SAIDA', 'CHV_DFE_SAIDA', 'DT_DOC_SAIDA', 'NUM_ITEM_SAIDA', 'VL_UNIT_CONV_SAIDA', 'VL_UNIT_ICMS_OP_ESTOQUE_CONV_SAIDA',
                            'VL_UNIT_ICMS_ST_ESTOQUE_CONV_SAIDA', 'VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV_SAIDA', 'VL_UNIT_ICMS_NA_OPERACAO_CONV_SAIDA',
                            'VL_UNIT_ICMS_OP_CONV_SAIDA', 'VL_UNIT_ICMS_ST_CONV_REST', 'VL_UNIT_FCP_ST_CONV_REST',
                            'VL_UNIT_ICMS_ST_CONV_COMPL', 'VL_UNIT_FCP_ST_CONV_COMPL'
                       ]
	},
	"C185": {
		"nome_reg": "Informações complementares das operações de saída de mercadorias sujeitas à substituição tributária (código 01, 1B, 04 e 55)",
		"colunas_reg": [
                            'REG', 'NUM_ITEM', 'COD_ITEM', 'CST_ITEM', 'CFOP', 'COD_MOT_REST_COMPL', 'QUANT_CONV', 'UNID', 'VL_UNIT_CONV',
                            'VL_UNIT_ICMS_NA_OPERACAO_CONV', 'VL_UNIT_ICMS_OP_CONV', 'VL_UNIT_ICMS_OP_ESTOQUE_CONV',
                            'VL_UNIT_ICMS_ST_ESTOQUE_CONV', 'VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV', 'VL_UNIT_ICMS_ST_CONV_REST',
                            'VL_UNIT_FCP_ST_CONV_REST', 'VL_UNIT_ICMS_ST_CONV_COMPL', 'VL_UNIT_FCP_ST_CONV_COMPL'
                       ]
	},
	"C186": {
		"nome_reg": "Informações complementares das operações de devolução de entradas de mercadorias sujeitas à substituição tributária (código 01, 1B, 04 e 55).",
		"colunas_reg": [
                            'REG', 'NUM_ITEM', 'COD_ITEM', 'CST_ICMS', 'CFOP', 'COD_MOT_REST_COMPL', 'QUANT_CONV', 'UNID', 'COD_MOD_ENTRADA',
                            'SERIE_ENTRADA', 'NUM_DOC_ENTRADA', 'CHV_DFE_ENTRADA', 'DT_DOC_ENTRADA', 'NUM_ITEM_ENTRADA', 'VL_UNIT_CONV_ENTRADA',
                            'VL_UNIT_ICMS_OP_CONV_ENTRADA', 'VL_UNIT_BC_ICMS_ST_CONV_ENTRADA', 'VL_UNIT_ICMS_ST_CONV_ENTRADA',
                            'VL_UNIT_FCP_ST_CONV_ENTRADA'
                       ]
	},
	"C190": {
		"nome_reg": "Registro Analítico do Documento (código 01, 1B, 04, 55 e 65)",
		"colunas_reg": [
                            'REG', 'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS', 'VL_BC_ICMS_ST',
                            'VL_ICMS_ST', 'VL_RED_BC', 'VL_IPI', 'COD_OBS'
                       ]
	},
	"C191": {
		"nome_reg": "Informações do Fundo de Combate à Pobreza – FCP – na NF-e (Código 55)",
		"colunas_reg": ['REG', 'VL_FCP_OP', 'VL_FCP_ST', 'VL_FCP_RET']
	},
	"C195": {
		"nome_reg": "Complemento do Registro Analítico - Observações do Lançamento Fiscal (código 01, 1B, 04 e 55)",
		"colunas_reg": ['REG', 'COD_OBS', 'TXT_COMPL']
	},
	"C197": {
		"nome_reg": "Outras Obrigações Tributárias, Ajustes e Informações provenientes de Documento Fiscal",
		"colunas_reg": ['REG', 'COD_AJ', 'DESCR_COMPL_AJ', 'COD_ITEM', 'VL_BC_ICMS', 'ALIQ_ICMS', 'VL_ICMS', 'VL_OUTROS']
	},
	"C300": {
		"nome_reg": "Documento - Resumo Diário das Notas Fiscais de Venda a Consumidor (código 02)",
		"colunas_reg": [
                            'REG', 'COD_MOD', 'SER', 'SUB', 'NUM_DOC_INI', 'NUM_DOC_FIN', 'DT_DOC', 'VL_DOC', 'VL_PIS',
                            'VL_COFINS', 'COD_CTA'
                       ]
	},
	"C310": {
		"nome_reg": "Documentos Cancelados de Nota Fiscal de Venda a Consumidor (código 02)",
		"colunas_reg": ['REG', 'NUM_DOC_CANC']
	},
	"C320": {
		"nome_reg": "Registro Analítico das Notas Fiscais de Venda a Consumidor (código 02)",
		"colunas_reg": [
                            'REG', 'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS', 'VL_RED_BC', 'COD_OBS'
                       ]
	},
	"C321": {
		"nome_reg": "Itens dos Resumos Diários dos Documentos (código 02)",
		"colunas_reg": [
                            'REG', 'COD_ITEM', 'QTD', 'UNID', 'VL_ITEM', 'VL_DESC', 'VL_BC_ICMS', 'VL_ICMS', 'VL_PIS', 'VL_COFINS'
                       ]
	},
	"C330": {
		"nome_reg": "Informações complementares das operações de saída de mercadorias sujeitas à substituição tributária (código 02)",
		"colunas_reg": [
                            'REG', 'COD_MOT_REST_COMPL', 'QUANT_CONV', 'UNID', 'VL_UNIT_CONV', 'VL_UNIT_ICMS_NA_OPERACAO_CONV',
                            'VL_UNIT_ICMS_OP_CONV', 'VL_UNIT_ICMS_OP_ESTOQUE_CONV', 'VL_UNIT_ICMS_ST_ESTOQUE_CONV',
                            'VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV', 'VL_UNIT_ICMS_ST_CONV_REST', 'VL_UNIT_FCP_ST_CONV_REST',
                            'VL_UNIT_ICMS_ST_CONV_COMPL', 'VL_UNIT_FCP_ST_CONV_COMPL'
                       ]
	},
	"C350": {
		"nome_reg": "Nota Fiscal de venda a consumidor (código 02)",
		"colunas_reg": [
                            'REG', 'SER', 'SUB_SER', 'NUM_DOC', 'DT_DOC', 'CNPJ_CPF', 'VL_MERC', 'VL_DOC', 'VL_DESC', 'VL_PIS',
                            'VL_COFINS', 'COD_CTA'
                       ]
	},
	"C370": {
		"nome_reg": "Itens do documento (código 02)",
		"colunas_reg": [
                            'REG', 'NUM_ITEM', 'COD_ITEM', 'QTD', 'UNID', 'VL_ITEM', 'VL_DESC'
                       ]
	},
	"C380": {
		"nome_reg": "Informações complementares das operações de saída de mercadorias sujeitas à substituição tributária (código 02)",
		"colunas_reg": [
                            'REG', 'COD_MOT_REST_COMPL', 'QUANT_CONV', 'UNID', 'VL_UNIT_CONV', 'VL_UNIT_ICMS_NA_OPERACAO_CONV',
                            'VL_UNIT_ICMS_OP_CONV', 'VL_UNIT_ICMS_OP_ESTOQUE_CONV', 'VL_UNIT_ICMS_ST_ESTOQUE_CONV', 'VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV',
                            'VL_UNIT_ICMS_ST_CONV_REST', 'VL_UNIT_FCP_ST_CONV_REST', 'VL_UNIT_ICMS_ST_CONV_COMPL', 'VL_UNIT_FCP_ST_CONV_COMPL',
                            'CST_ICMS', 'CFOP'
                       ]
	},
	"C390": {
		"nome_reg": "Registro Analítico das Notas Fiscais de Venda a Consumidor (código 02)",
		"colunas_reg": [
                            'REG', 'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS', 'VL_RED_BC', 'COD_OBS'
                       ]
	},
	"C400": {
		"nome_reg": "Equipamento ECF (código 02, 2D e 60)",
		"colunas_reg": ['REG', 'COD_MOD', 'ECF_MOD', 'ECF_FAB', 'ECF_CX']
	},
	"C405": {
		"nome_reg": "Redução Z (código 02, 2D e 60)",
		"colunas_reg": ['REG', 'DT_DOC', 'CRO', 'CRZ', 'NUM_COO_FIN', 'GT_FIN', 'VL_BRT']
	},
	"C410": {
		"nome_reg": "PIS e COFINS Totalizados no Dia (código 02 e 2D)",
		"colunas_reg": ['REG', 'VL_PIS', 'VL_COFINS']
	},
	"C420": {
		"nome_reg": "Registro dos Totalizadores Parciais da Redução Z (código 02, 2D e 60)",
		"colunas_reg": ['REG', 'COD_TOT_PAR', 'VLR_ACUM_TOT', 'NR_TOT', 'DESCR_NR_TOT']
	},
	"C425": {
		"nome_reg": "Resumo de itens do movimento diário (código 02 e 2D)",
		"colunas_reg": ['REG', 'COD_ITEM', 'QTD', 'UNID', 'VL_ITEM', 'VL_PIS', 'VL_COFINS']
	},
	"C430": {
		"nome_reg": "Informações complementares das operações de saída de mercadorias sujeitas à substituição tributária (código 02, 2D e 60)",
		"colunas_reg": ['REG', 'COD_MOT_REST_COMPL', 'QUANT_CONV', 'UNID', 'VL_UNIT_CONV', 'VL_UNIT_ICMS_NA_OPERACAO_CONV', 'VL_UNIT_ICMS_OP_CONV', 'VL_UNIT_ICMS_OP_ESTOQUE_CONV', 'VL_UNIT_ICMS_ST_ESTOQUE_CONV', 'VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV', 'VL_UNIT_ICMS_ST_CONV_REST', 'VL_UNIT_FCP_ST_CONV_REST', 'VL_UNIT_ICMS_ST_CONV_COMPL', 'VL_UNIT_FCP_ST_CONV_COMPL', 'CST_ICMS', 'CFOP']
	},
	"C460": {
		"nome_reg": "Documento Fiscal Emitido por ECF (código 02, 2D e 60)",
		"colunas_reg": ['REG', 'COD_MOD', 'COD_SIT', 'NUM_DOC', 'DT_DOC', 'VL_DOC', 'VL_PIS', 'VL_COFINS', 'CPF_CNPJ', 'NOM_ADQ']
	},
	"C465": {
		"nome_reg": "Complemento do Cupom Fiscal Eletrônico Emitido por ECF - CF-e-ECF (código 60)",
		"colunas_reg": ['REG', 'CHV_CFE', 'NUM_CCF']
	},
	"C470": {
		"nome_reg": "Itens do Documento Fiscal Emitido por ECF (código 02 e 2D)",
		"colunas_reg": ['REG', 'COD_ITEM', 'QTD', 'QTD_CANC', 'UNID', 'VL_ITEM', 'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_PIS', 'VL_COFINS']
	},
	"C480": {
		"nome_reg": "Informações complementares das operações de saída de mercadorias sujeitas à substituição tributária (código 02, 2D e 60)",
		"colunas_reg": ['REG', 'COD_MOT_REST_COMPL', 'QUANT_CONV', 'UNID', 'VL_UNIT_CONV', 'VL_UNIT_ICMS_NA_OPERACAO_CONV', 'VL_UNIT_ICMS_OP_CONV', 'VL_UNIT_ICMS_OP_ESTOQUE_CONV', 'VL_UNIT_ICMS_ST_ESTOQUE_CONV', 'VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV', 'VL_UNIT_ICMS_ST_CONV_REST', 'VL_UNIT_FCP_ST_CONV_REST', 'VL_UNIT_ICMS_ST_CONV_COMPL', 'VL_UNIT_FCP_ST_CONV_COMPL', 'CST_ICMS', 'CFOP']
	},
	"C490": {
		"nome_reg": "Registro Analítico do movimento diário (código 02, 2D e 60)",
		"colunas_reg": ['REG', 'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS', 'COD_OBS']
	},
	"C495": {
		"nome_reg": "Resumo Mensal de Itens do ECF por Estabelecimento (código 02 e 2D e 2E)",
		"colunas_reg": ['REG', 'ALIQ_ICMS', 'COD_ITEM', 'QTD', 'QTD_CANC', 'UNID', 'VL_ITEM', 'VL_DESC', 'VL_CANC', 'VL_ACMO', 'VL_BC_ICMS', 'VL_ICMS', 'VL_ISEN', 'VL_NT', 'VL_ICMS_ST']
	},
	"C500": {
		"nome_reg": "Nota Fiscal/Conta de Energia Elétrica (código 06), Nota Fiscal de Energia Elétrica Eletrônica (código 66),\
                     Nota Fiscal/Conta de fornecimento dágua canalizada (código 29) e Nota Fiscal/Consumo Fornecimento de Gás (Código28)",
		"colunas_reg": ['REG', 'IND_OPER', 'IND_EMIT', 'COD_PART', 'COD_MOD', 'COD_SIT', 'SER', 'SUB', 'COD_CONS', 'NUM_DOC', 'DT_DOC', 'DT_E_S', 'VL_DOC', 'VL_DESC', 'VL_FORN', 'VL_SERV_NT', 'VL_TERC', 'VL_DA', 'VL_BC_ICMS', 'VL_ICMS', 'VL_BC_ICMS_ST', 'VL_ICMS_ST', 'COD_INF', 'VL_PIS', 'VL_COFINS', 'TP LIGACAO', 'COD_GRUPO_TENSAO', 'CHV_DOCe', 'FIN_DOCe', 'CHV_DOCe_REF', 'IND_DEST', 'COD_MUN_DEST', 'COD_CTA', 'COD_MOD_DOC_REF', 'HASH_DOC_REF', 'SER_DOC_REF', 'NUM_DOC_REF', 'MES_DOC_REF', 'ENER_INJET', 'OUTRAS_DED']
	},
	"C510": {
		"nome_reg": "Itens do Documento - Nota Fiscal/Conta de Energia Elétrica (código 06), Nota Fiscal/Conta de fornecimento\
                     d'água canalizada (código 29) e Nota Fiscal/Conta Fornecimento de Gás (Código 28)",
		"colunas_reg": ['REG', 'NUM_ITEM', 'COD_ITEM', 'COD_CLASS', 'QTD', 'UNID', 'VL_ITEM', 'VL_DES', 'CST_ICMS', 'CFOP', 'VL_BC_ICMS', 'ALIQ_ICMS', 'VL_ICMS', 'VL_BC_ICMS_ST', 'ALIQ_ST', 'VL_ICMS_ST', 'IND_REC', 'COD_PART', 'VL_PIS', 'VL_COFINS', 'COD_CTA']
	},
	"C590": {
		"nome_reg": "Registro Analítico do Documento - Nota Fiscal/Conta de Energia Elétrica (código 06), Nota Fiscal de Energia Elétrica\
                     Eletrônica (código 66), Nota Fiscal/Conta de fornecimento d'água canalizada (código 29) e Nota Fiscal/Conta Fornecimento de Gás (Código 28)",
		"colunas_reg": ['REG', 'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS', 'VL_BC_ICMS_ST', 'VL_ICMS_ST', 'VL_RED_BC', 'COD_OBS']
	},
	"C591": {
		"nome_reg": "Informações do Fundo de Combate à Pobreza – FCP na NF3e (código 66) ",
		"colunas_reg": ['REG', 'VL_FCP_OP', 'VL_FCP_ST']
	},
	"C595": {
		"nome_reg": "Observações do Lançamento Fiscal (códigos 06, 28, 29 e 66)",
		"colunas_reg": ['REG', 'COD_OBS', 'TXT_COMPL']
	},
	"C597": {
		"nome_reg": "Outras obrigações tributárias, ajustes e informações de valores provenientes de documento fiscal.",
		"colunas_reg": ['REG', 'COD_AJ', 'DESCR_COMPL_AJ', 'COD_ITEM', 'VL_BC_ICMS', 'ALIQ_ICMS', 'VL_ICMS', 'VL_OUTROS']
	},
	"C600": {
		"nome_reg": "Consolidação Diária de Notas Fiscais/Contas de Energia Elétrica (Código 06), Nota Fiscal/Conta de Fornecimento\
                     d´água (código 29) e Nota Fiscal/Conta de Fornecimento de Gás (Código 28) - (Empresas não obrigadas ao Convênio ICMS 115/03)",
		"colunas_reg": ['REG', 'COD_MOD', 'COD_MUN', 'SER', 'SUB', 'COD_CONS', 'QTD_CONS', 'QTD_CANC', 'DT_DOC', 'VL_DOC', 'VL_DESC', 'CONS', 'VL_FORN', 'VL_SERV_NT', 'VL_TERC', 'VL_DA', 'VL_BC_ICMS', 'VL_ICMS', 'VL_BC_ICMS_ST', 'VL_ICMS_ST', 'VL_PIS', 'VL_COFINS']
	},
    "C601": {
		"nome_reg": "Documentos cancelados - Consolidação diária de notas fiscais/conta de energia elétrica (Código 06), nota fiscal/conta de\
                     fornecimento de água (código 29) e nota fiscal/conta de fornecimento de gás (código 28)",
		"colunas_reg": ['REG', 'NUM_DOC_CANC']
	},
    "C610": {
		"nome_reg": "Itens do Documento Consolidado - Notas Fiscais/Contas de Energia Elétrica (Código 06), Nota Fiscal/Conta\
                     de Fornecimento d´água (código 29) e Nota Fiscal/Conta de Fornecimento de Gás (Código 28) -\
                     (Empresas não obrigadas ao Convênio ICMS 115/03)",
		"colunas_reg": ['REG', 'COD_CLASS', 'COD_ITEM', 'QTD', 'UNID', 'VL_ITEM', 'VL_DESC', 'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_BC_ICMS', 'VL_ICMS', 'VL_BC_ICMS_ST', 'VL_ICMS_ST', 'VL_PIS', 'VL_COFINS', 'COD_CTA']
	},
    "C690": {
		"nome_reg": "Registro Analítico dos Documentos - Notas Fiscais/Contas de Energia Elétrica (Código 06), Nota Fiscal/Conta de Fornecimento\
                     d´água (código 29) e Nota Fiscal/Conta de Fornecimento de Gás (Código 28)",
		"colunas_reg": ['REG', 'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS', 'VL_RED_BC', 'VL_BC_ICMS_ST', 'VL_ICMS_ST', 'COD_OBS']
	},
    "C700": {
		"nome_reg": "Consolidação dos Documentos Nota Fiscal/Conta Energia Elétrica (código 06) emitidas em via única -\
                     (Empresas obrigadas à entrega do arquivo previsto no Convênio ICMS 115/03), Nota Fiscal/Conta de Fornecimento de Gás Canalizado (Código 28) e Nota Fiscal de Energia Elétrica Eletrônica (código 66)",
		"colunas_reg": ['REG', 'COD_MOD', 'SER', 'NRO_ORD_INI', 'NRO_ORD_FIN', 'DT_DOC_INI', 'DT_DOC_FIN', 'NOM_MEST', 'CHV_COD_DIG']
	},
    "C790": {
		"nome_reg": "Registro Analítico dos Documentos (Códigos 06, 28 e 66)",
		"colunas_reg": ['REG', 'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS', 'VL_BC_ICMS_ST', 'VL_ICMS_ST', 'VL_RED_BC', 'COD_OBS']
	},
    "C791": {
		"nome_reg": "Registro de Informações de ICMS ST por UF (Código 06 e 66)",
		"colunas_reg": ['REG', 'UF', 'VL_BC_ICMS_ST', 'VL_ICMS_ST']
	},
    "C800": {
		"nome_reg": "Registro Cupom Fiscal Eletrônico - CF-e (Código 59)",
		"colunas_reg": ['REG', 'COD_MOD', 'COD_SIT', 'NUM_CFE', 'DT_DOC', 'VL_CFE', 'VL_PIS', 'VL_COFINS', 'CNPJ_CPF', 'NR_SAT', 'CHV_CFE', 'VL_DESC', 'VL_MERC', 'VL_OUT_DA', 'VL_ICMS', 'VL_PIS_ST', 'VL_COFINS_ST']
	},
    "C810": {
		"nome_reg": "Itens do documento do cupom fiscal eletrônico – SAT (CF-E-SAT) (código 59)",
		"colunas_reg": ['REG', 'NUM_ITEM', 'COD_ITEM', 'QTD', 'UNID', 'VL_ITEM', 'CST_ICMS', 'CFOP']
	},
    "C815": {
		"nome_reg": "Informações complementares das operações de saída de mercadorias sujeitas à substituição tributária (CF-E-SAT) (código 59)",
		"colunas_reg": ['REG', 'COD_MOT_REST_COMPL', 'QUANT_CONV', 'UNID', 'VL_UNIT_CONV', 'VL_UNIT_ICMS_NA_OPERACAO_CONV', 'VL_UNIT_ICMS_OP_CONV', 'VL_UNIT_ICMS_OP_ESTOQUE_CONV', 'VL_UNIT_ICMS_ST_ESTOQUE_CONV' 'VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV', 'VL_UNIT_ICMS_ST_CONV_REST', 'VL_UNIT_FCP_ST_CONV_REST', 'VL_UNIT_ICMS_ST_CONV_COMPL', 'VL_UNIT_FCP_ST_CONV_COMPL']
	},
    "C850": {
		"nome_reg": "Registro Analítico do CF-e (Código 59) ",
		"colunas_reg": ['REG', 'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS', 'COD_OBS']
	},
    "C855": {
		"nome_reg": "Observações do lançamento fiscal (Código 59)",
		"colunas_reg": ['REG', 'COD_OBS', 'TXT_COMPL']
	},
    "C857": {
		"nome_reg": "Outras obrigações tributárias, ajustes e informações de valores provenientes de documento fiscal.",
		"colunas_reg": ['REG', 'COD_AJ', 'DESCR_COMPL_AJ', 'COD_ITEM', 'VL_BC_ICMS', 'ALIQ_ICMS', 'VL_ICMS', 'VL_OUTROS']
	},
    "C860": {
		"nome_reg": "Identificação do equipamento SAT-CF-e (Código 59)",
		"colunas_reg": ['REG', 'COD_MOD', 'NR_SAT', 'DT_DOC', 'DT_INI', 'DT_FIN']
	},
    "C870": {
		"nome_reg": "Itens do documento do cupom fiscal eletrônico – SAT (CF-E-SAT) (código 59)",
		"colunas_reg": ['REG', 'COD_ITEM', 'QTD', 'UNID', 'CST_ICMS', 'CFOP']
	},
    "C880": {
		"nome_reg": "Informações complementares das operações de saída de mercadorias sujeitas à substituição tributária (CF-E-SAT) (código 59)",
		"colunas_reg": ['REG', 'COD_MOT_REST_COMPL', 'QUANT_CONV', 'UNID', 'VL_UNIT_CONV', 'VL_UNIT_ICMS_NA_OPERACAO_CONV', 'VL_UNIT_ICMS_OP_CONV', 'VL_UNIT_ICMS_OP_ESTOQUE_CONV', 'VL_UNIT_ICMS_ST_ESTOQUE_CONV', 'VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV', 'VL_UNIT_ICMS_ST_CONV_REST', 'VL_UNIT_FCP_ST_CONV_REST', 'VL_UNIT_ICMS_ST_CONV_COMPL', 'VL_UNIT_FCP_ST_CONV_COMPL']
	},
    "C890": {
		"nome_reg": "Resumo diário de CF-e (Código 59) por equipamento SAT-CF-e",
		"colunas_reg": ['REG', 'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS', 'COD_OBS']
	},
    "C895": {
		"nome_reg": "Observações do lançamento fiscal (Código 59)",
		"colunas_reg": ['REG', 'COD_OBS', 'TXT_COMPL']
	},
    "C897": {
		"nome_reg": "Outras obrigações tributárias, ajustes e informações de valores provenientes de documento fiscal.",
		"colunas_reg": ['REG', 'COD_AJ', 'DESCR_COMPL_AJ', 'COD_ITEM', 'VL_BC_ICMS', 'ALIQ_ICMS', 'VL_ICMS', 'VL_OUTROS']
	},
    "C990": {
		"nome_reg": "Encerramento do Bloco C",
		"colunas_reg": ['REG', 'QTD_LIN_C']
	},
    # BLOCO C ============================================================== FIM #

	# BLOCO D ============================================================== INICIO # - INCOMPLETO
    "D001": {
		"nome_reg": "Abertura do Bloco D",
		"colunas_reg": ['REG', 'IND_MOV']
	},
    "D100": {
		"nome_reg": "NOTA FISCAL DE SERVIÇO DE TRANSPORTE (CÓDIGO 07) E CONHECIMENTOS DE TRANSPORTE RODOVIÁRIO DE CARGAS (CÓDIGO 08), CONHECIMENTOS DE TRANSPORTE DE CARGAS AVULSO (CÓDIGO 8B), AQUAVIÁRIO DE CARGAS (CÓDIGO 09), AÉREO (CÓDIGO 10), FERROVIÁRIO DE CARGAS (CÓDIGO 11), MULTIMODAL DE CARGAS (CÓDIGO 26), NOTA FISCAL DE TRANSPORTE FERROVIÁRIO DE CARGA (CÓDIGO 27), CONHECIMENTO DE TRANSPORTE ELETRÔNICO - CT-e (CÓDIGO 57), CONHECIMENTO DE TRANSPORTE ELETRÔNICO PARA OUTROS SERVIÇOS - CT-e OS (CÓDIGO 67) E BILHETE DE PASSAGEM ELETRÔNICO - BP-e (CÓDIGO 63)",
		"colunas_reg": ["REG", "IND_OPER", "IND_EMIT", "COD_PART", "COD_MOD", "COD_SIT", "SER", "SUB", "NUM_DOC", "CHV_CTE", "DT_DOC", "DT_A_P", "TP_CTE-e", "CHV_CTE_REF", "VL_DOC", "VL_DESC", "IND_FRT", "VL_SERV", "VL_BC_ICMS", "VL_ICMS", "VL_NT", "COD_INF", "COD_CTA", "COD_MUN_ORIG", "COD_MUN_DEST"]
	},
    "D190": {
		"nome_reg": "REGISTRO ANALÍTICO DOS DOCUMENTOS (CÓDIGO 07, 08, 8B, 09, 10, 11, 26, 27, 57, 63 e 67)",
		"colunas_reg": ["REG", "CST_ICMS", "CFOP", "ALIQ_ICMS", "VL_OPR", "VL_BC_ICMS", "VL_ICMS", "VL_RED_BC", "COD_OBS"]
	},
    "D195": {
		"nome_reg": "OBSERVAÇÕES DO LANÇAMENTO FISCAL (CÓDIGO 07, 08, 8B, 09, 10, 11, 26, 27, 57, 63 e 67)",
		"colunas_reg": ["REG", "COD_OBS", "TXT_COMPL"]
	},
    "D990": {
		"nome_reg": "ENCERRAMENTO DO BLOCO D.",
		"colunas_reg": ["REG", "QTD_LIN_D"]
	},
    # BLOCO D ============================================================== FIM #

	# BLOCO E ============================================================== INICIO # - INCOMPLETO
    "E001": {
		"nome_reg": "ABERTURA DO BLOCO E",
		"colunas_reg": ["REG", "IND_MOV"]
	},
    "E100": {
		"nome_reg": "PERÍODO DE APURAÇÃO DO ICMS",
		"colunas_reg": ["REG", "DT_INI", "DT_FIN"]
	},
    "E110": {
		"nome_reg": "APURAÇÃO DO ICMS - OPERAÇÕES PRÓPRIAS",
		"colunas_reg": ["REG", "VL_TOT_DEBITOS", "VL_AJ_DEBITOS", "VL_TOT_AJ_DEBITOS", "VL_ESTORNOS_CRED", "VL_TOT_CREDITOS", "VL_AJ_CREDITOS", "VL_TOT_AJ_CREDITOS", "VL_ESTORNOS_DEB", "VL_SLD_CREDOR_ANT", "VL_SLD_APURADO", "VL_TOT_DED", "VL_ICMS_RECOLHER", "VL_SLD_CREDOR_TRANSPORTAR", "DEB_ESP"]
	},
    "E111": {
		"nome_reg": "AJUSTE/BENEFÍCIO/INCENTIVO DA APURAÇÃO DO ICMS",
		"colunas_reg": ["REG", "COD_AJ_APUR", "DESCR_COMPL_AJ", "VL_AJ_APUR"]
	},
    "E112": {
		"nome_reg": "INFORMAÇÕES ADICIONAIS DOS AJUSTES DA APURAÇÃO DO ICMS",
		"colunas_reg": ["REG", "NUM_DA", "NUM_PROC", "IND_PROC", "PROC", "TXT_COMPL"]
	},
    "E116": {
		"nome_reg": "OBRIGAÇÕES DO ICMS RECOLHIDO OU A RECOLHER - OPERAÇÕES PRÓPRIAS",
		"colunas_reg": ["REG", "COD_OR", "VL_OR", "DT_VCTO", "COD_REC", "NUM_PROC", "IND_PROC", "PROC", "TXT_COMPL", "MES_REF"]
	},
    "E500": {
		"nome_reg": "PERÍODO DE APURAÇÃO DO IPI",
		"colunas_reg": ["REG", "IND_APUR", "DT_INI", "DT_FIN"]
	},
    "E510": {
		"nome_reg": "CONSOLIDAÇÃO DOS VALORES DO IPI",
		"colunas_reg": ["REG", "CFOP", "CST_IPI", "VL_CONT_IPI", "VL_BC_IPI", "VL_IPI"]
	},
    "E520": {
		"nome_reg": "APURAÇÃO DO IPI",
		"colunas_reg": ["REG", "VL_SD_ANT_IPI", "VL_DEB_IPI", "VL_CRED_IPI", "VL_OD_IPI", "VL_OC_IPI", "VL_SC_IPI", "VL_SD_IPI"]
	},
    "E990": {
		"nome_reg": "ENCERRAMENTO DO BLOCO E",
		"colunas_reg": ["REG", "QTD_LIN_E"]
	},
    # BLOCO E ============================================================== FIM #

	# BLOCO G ============================================================== INICIO # - INCOMPLETO
    "G001": {
		"nome_reg": "ABERTURA DO BLOCO G",
		"colunas_reg": ["REG", "IND_MOV"]
	},
    "G110": {
		"nome_reg": "ICMS - ATIVO PERMANENTE - CIAP",
		"colunas_reg": ["REG", "DT_INI", "DT_FIN", "SALDO_IN_ICMS", "SOM_PARC", "VL_TRIB_EXP", "VL_TOTAL", "IND_PER_SAI", "ICMS_APROP", "SOM_ICMS_OC"]
	},
    "G125": {
		"nome_reg": "MOVIMENTAÇÃO DE BEM OU COMPONENTE DO ATIVO IMOBILIZADO",
		"colunas_reg": ["REG", "COD_IND_BEM", "DT_MOV", "TIPO_MOV", "VL_IMOB_ICMS_OP", "VL_IMOB_ICMS_ST", "VL_IMOB_ICMS_FRT", "VL_IMOB_ICMS_DIF", "NUM_PARC", "VL_PARC_PASS"]
	},
    "G130": {
		"nome_reg": "IDENTIFICAÇÃO DO DOCUMENTO FISCAL",
		"colunas_reg": ["REG", "IND_EMIT", "COD_PART", "COD_MOD", "SERIE", "NUM_DOC", "CHV_NFE_CTE", "DT_DOC", "NUM_DA"]
	},
    "G140": {
		"nome_reg": "IDENTIFICAÇÃO DO ITEM DO DOCUMENTO FISCAL",
		"colunas_reg": ["REG", "NUM_ITEM", "COD_ITEM", "QTDE", "UNID", "VL_ICMS_OP_APLICADO", "VL_ICMS_ST_APLICADO", "VL_ICMS_FRT_APLICADO", "VL_ICMS_DIF_APLICADO"]
	},
    "G990": {
		"nome_reg": "ENCERRAMENTO DO BLOCO G",
		"colunas_reg": ["REG", "QTD_LIN_G"]
	},
    # BLOCO G ============================================================== FIM #

	# BLOCO H ============================================================== INICIO # - INCOMPLETO
    "H001": {
		"nome_reg": "ABERTURA DO BLOCO H",
		"colunas_reg": ["REG", "IND_MOV"]
	},
    "H990": {
		"nome_reg": "ENCERRAMENTO DO BLOCO H",
		"colunas_reg": ["REG", "QTD_LIN_H"]
	},
    # BLOCO H ============================================================== FIM #

	# BLOCO K ============================================================== INICIO # - INCOMPLETO
    "K001": {
		"nome_reg": "ABERTURA DO BLOCO K",
		"colunas_reg": ["REG", "IND_MOV"]
	},
    "K010": {
		"nome_reg": "INFORMAÇÃO SOBRE O TIPO DE LEIAUTE (SIMPLIFICADO / COMPLETO)",
		"colunas_reg": ["REG", "IND_TP_LEIAUTE"]
	},
    "K100": {
		"nome_reg": "PERÍODO DE APURAÇÃO DO ICMS/IPI",
		"colunas_reg": ["REG", "DT_INI", "DT_FIN"]
	},
    "K200": {
		"nome_reg": "ESTOQUE ESCRITURADO",
		"colunas_reg": ["REG", "DT_EST", "COD_ITEM", "QTD", "IND_EST", "COD_PART"]
	},
    "K230": {
		"nome_reg": "ITENS PRODUZIDOS",
		"colunas_reg": ["REG", "DT_INI_OP", "DT_FIN_OP", "COD_DOC_OP", "COD_ITEM", "QTD_ENC"]
	},
	"K990": {
		"nome_reg": "ENCERRAMENTO DO BLOCO K",
		"colunas_reg": ["REG", "QTD_LIN_K"]
	},
    # BLOCO K ============================================================== FIM #

	# BLOCO 1 ============================================================== INICIO # - INCOMPLETO
	"1001": {
		"nome_reg": "ABERTURA DO BLOCO 1",
		"colunas_reg": ["REG", "IND_MOV"]
	},
	"1010": {
		"nome_reg": "OBRIGATORIEDADE DE REGISTROS DO BLOCO 1",
		"colunas_reg": ["REG", "IND_EXP", "IND_CCRF", "IND_COMB", "IND_USINA", "IND_VA", "IND_EE", "IND_CART", "IND_FORM", "IND_AER", "IND_GIAFI", "IND_GIAF3", "IND_GIAF4", "IND_REST_RESSARC_COMPL_ICMS"]
	},
	"1601": {
		"nome_reg": "OPERAÇÕES COM INSTRUMENTOS DE PAGAMENTOS ELETRÔNICOS (VÁLIDO A PARTIR DE 01/01/2022)",
		"colunas_reg": ["REG", "COD_PART_IP", "COD_PART_IT", "TOT_VS", "TOT_ISS", "TOT_OUTROS"]
	},
	"1990": {
		"nome_reg": "ENCERRAMENTO DO BLOCO 1",
		"colunas_reg": ["REG", "QTD_LIN_1"]
	},
    # BLOCO 1 ============================================================== FIM #

	# BLOCO 9 ============================================================== INICIO #
    "9001": {
		"nome_reg": "ABERTURA DO BLOCO 9",
		"colunas_reg": ["REG", "IND_MOV"]
	},
    "9900": {
		"nome_reg": "REGISTROS DO ARQUIVO",
		"colunas_reg": ["REG", "REG_BLC", "QTD_REG_BLC"]
	},
    "9990": {
		"nome_reg": "ENCERRAMENTO DO BLOCO 9",
		"colunas_reg": ["REG", "QTD_LIN_9"]
	},
    "9999": {
		"nome_reg": "ENCERRAMENTO DO ARQUIVO DIGITAL",
		"colunas_reg": ["REG", "QTD_LIN"]
	}
    # BLOCO 9 ============================================================== FIM #
}
