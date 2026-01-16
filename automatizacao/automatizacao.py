import pandas as pd

enderecos_df = pd.read_excel(
    "18 - DO_FUNCIONARIOENDERECOS.xlsx",
    sheet_name=1
)

dados_1013_df = pd.read_csv(
    "1013- Complementar.csv",
    sep=";",
    encoding="latin1"
)

enderecos_df.columns = enderecos_df.columns.str.strip().str.upper()
dados_1013_df.columns = dados_1013_df.columns.str.strip().str.upper()

enderecos_df["FUNCIONARIO"] = (
    dados_1013_df["NUMCAD"]
    .astype(str)
    .str.lstrip("0")
)

enderecos_df["TIPOENDERECO"] = 115
enderecos_df["LOGRADOUROEXIBICAO"] = dados_1013_df["ENDRUA"]
enderecos_df["NUMEROEXIBICAO"] = dados_1013_df["ENDNUM"]
enderecos_df["PAIS"] = 1
enderecos_df["ESTADO"] = dados_1013_df["ESTCID"]
enderecos_df["MUNICIPIO"] = dados_1013_df["CODCID"]
enderecos_df["CEP"] = dados_1013_df["ENDCEP"]

enderecos_df.to_excel(
    "18 - DO_FUNCIONARIOENDERECOS_ATUALIZADO.xlsx",
    index=False
)

arquivo_telefone = "19 - DO_FUNCIONARIOTELEFONES.xlsx"

telefone_df = pd.read_excel(
    arquivo_telefone,
    sheet_name=1
)

telefone_df.columns = telefone_df.columns.str.strip().str.upper()

telefone_df["FUNCIONARIO"] = (
    dados_1013_df["NUMCAD"]
    .astype(str)
    .str.replace(r"\D", "", regex=True)
    .str.lstrip("0")
    .replace("", pd.NA)
)

telefone_df["TELEFONE"] = dados_1013_df["NUMTEL"]
telefone_df["TIPOTELEFONE"] = 13
telefone_df["DDI"] = dados_1013_df["DDITEL"]
telefone_df["DDD"] = dados_1013_df["DDDTEL"]

with pd.ExcelWriter(
    "19 - DO_FUNCIONARIOTELEFONES_ATUALIZADO.xlsx",
    engine="openpyxl"
) as writer:

    pd.read_excel(
        arquivo_telefone,
        sheet_name=0
    ).to_excel(writer, sheet_name="Sheet1", index=False)

    telefone_df.to_excel(writer, sheet_name="Sheet2", index=False)

cargos_df = pd.read_excel(
    "12 - DO_FUNCIONARIOCARGOS.xlsx",
    sheet_name=1
)

dados_1015_df = pd.read_csv(
    "1015 Hist cargos.csv",
    sep=";",
    encoding="latin1"
)

cargos_df.columns = cargos_df.columns.str.strip().str.upper()
dados_1015_df.columns = dados_1015_df.columns.str.strip().str.upper()

cargos_df["FUNCIONARIO"] = (
    dados_1015_df["NUMCAD"]
    .astype(str)
    .str.lstrip("0")
)

cargos_df["INICIO"] = dados_1015_df["DATALT"]
cargos_df["CARGO"] = dados_1015_df["CODCAR"]
cargos_df["MOTIVO"] = dados_1015_df["CODMOT"]
cargos_df["FIM"] = [
    f'=SEERRO(MÍNIMOSES(B:B;A:A;A{i};B:B;">"&B{i})-1;"")'
    for i in range(2, len(cargos_df) + 2)
]

cargos_df.to_excel(
    "12 - DO_FUNCIONARIOCARGOS_ATUALIZADO.xlsx",
    index=False
)

hierarquias_df = pd.read_excel(
    "11 - DO_FUNCIONARIOHIERARQUIAS.xlsx",
    sheet_name=1
)

dados_1012_df = pd.read_csv(
    "1012 - Colaborador.csv",
    sep=";",
    encoding="latin1"
)

hierarquias_df.columns = hierarquias_df.columns.str.strip().str.upper()
dados_1012_df.columns = dados_1012_df.columns.str.strip().str.upper()

hierarquias_df["FUNCIONARIO"] = (
    dados_1012_df["NUMCAD"]
    .astype(str)
    .str.lstrip("0")
)

hierarquias_df["INICIO"] = dados_1012_df["DATADM"]
hierarquias_df["FIM"] = [
    f'=SEERRO(MÍNIMOSES(B:B;A:A;A{i};B:B;">"&B{i})-1;"")'
    for i in range(2, len(hierarquias_df) + 2)
]

hierarquias_df.to_excel(
    "11 - DO_FUNCIONARIOHIERARQUIAS_ATUALIZADO.xlsx",
    index=False
)

afastamentos_df = pd.read_excel(
    "13 - DO_FUNCIONARIOAFASTAMENTOS.xlsx",
    sheet_name=1
)

dados_1014_df = pd.read_csv(
    "1014_O - Afastamentos.csv",
    sep=";",
    encoding="latin1"
)

afastamentos_df.columns = afastamentos_df.columns.str.strip().str.upper()
dados_1014_df.columns = dados_1014_df.columns.str.strip().str.upper()

afastamentos_df["FUNCIONARIO"] = (
    dados_1014_df["NUMCAD"]
    .astype(str)
    .str.lstrip("0")
)

dados_1014_df["DATAFA"] = pd.to_datetime(
    dados_1014_df["DATAFA"],
    dayfirst=True,
    errors="coerce"
)

dados_1014_df["DATTER"] = pd.to_datetime(
    dados_1014_df["DATTER"],
    dayfirst=True,
    errors="coerce"
)

afastamentos_df["ORIGINALT"] = 1
afastamentos_df["TPPROCV020500F"] = 1
afastamentos_df["AFASTAMENTO"] = dados_1014_df["DATAFA"]
afastamentos_df["PREVISAORETORNO"] = dados_1014_df["DATTER"]
afastamentos_df["DIASATESTADO"] = (
    dados_1014_df["DATTER"] - dados_1014_df["DATAFA"]
).dt.days + 1
afastamentos_df["SALDODEV13SALLICSEMVENC"] = 0
afastamentos_df["INICIOAFASTAMENTOEMPRESA"] = dados_1014_df["DATAFA"]
afastamentos_df["FIMAFASTAMENTOEMPRESA"] = (
    dados_1014_df["DATAFA"] + pd.Timedelta(days=14)
)
afastamentos_df["DIASPAGOS"] = 0
afastamentos_df["DIASTOTAL"] = 0
afastamentos_df["DIASINSS"] = 0
afastamentos_df["NAODESCONTA"] = "S"
afastamentos_df["PRORROGADO"] = "N"
afastamentos_df["DIASPRORROGADOS"] = 0
afastamentos_df["TAREFAGERADA"] = "S"

afastamentos_df.to_excel(
    "13 - DO_FUNCIONARIOAFASTAMENTOS_ATUALIZADO.xlsx",
    index=False
)

salarios_df = pd.read_excel(
    "14 - DO_FUNCIONARIOSALARIOS.xlsx",
    sheet_name=1
)

dados_1030_df = pd.read_csv(
    "1030 - hist Salario.csv",
    sep=";",
    encoding="latin1"
)

salarios_df.columns = salarios_df.columns.str.strip().str.upper()
dados_1030_df.columns = dados_1030_df.columns.str.strip().str.upper()

salarios_df["FUNCIONARIO"] = (
    dados_1030_df["NUMCAD"]
    .astype(str)
    .str.lstrip("0")
)

salarios_df["INICIO"] = dados_1030_df["DATALT"]
salarios_df["REAJUSTE"] = dados_1030_df["SEQALT"]
salarios_df["MOTIVO"] = dados_1030_df["CODMOT"]
salarios_df["SALARIO"] = dados_1030_df["VALSAL"]
salarios_df["TIPOSALARIO"] = dados_1030_df["TIPSAL"]
salarios_df["PERCENTUALAUMENTO"] = dados_1030_df["PERREA"]
salarios_df["FIM"] = [
    f'=SEERRO(MÍNIMOSES(B:B;A:A;A{i};B:B;">"&B{i})-1;"")'
    for i in range(2, len(salarios_df) + 2)
]

salarios_df.to_excel(
    "14 - DO_FUNCIONARIOSALARIOS_ATUALIZADO.xlsx",
    index=False
)