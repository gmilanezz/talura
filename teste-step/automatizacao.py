import pandas as pd

steps_df = pd.read_excel(
    "15 - DO_FUNCIONARIOSTEPS.xlsx",
    sheet_name=1
)

dados_1012_df = pd.read_csv(
    "1012 - Colaborador.csv",
    sep=";",
    encoding="latin1"
)

demissao = pd.read_csv(
    "1036 - Rescisão.csv",
    sep=";",
    encoding="latin1"
)

steps_df.columns = steps_df.columns.str.strip().str.upper()
dados_1012_df.columns = dados_1012_df.columns.str.strip().str.upper()

steps_df["FUNCIONARIO"] = (
    dados_1012_df["NUMCAD"]
    .astype(str)
    .str.lstrip("0")
)
steps_df["INICIO"] = dados_1012_df["DATADM"]
steps_df["MOTIVO"] = 1
demissao_map = (
    demissao.assign(NUMCAD=demissao["NUMCAD"].astype(str).str.lstrip("0"))
    .sort_values("DATDEM")
    .drop_duplicates(subset="NUMCAD", keep="last")
    .set_index("NUMCAD")["DATDEM"]
)

steps_df["FUNCIONARIO"] = steps_df["FUNCIONARIO"].astype(str).str.lstrip("0")

steps_df["FIM"] = steps_df["FUNCIONARIO"].map(demissao_map).fillna(0)

steps_df.to_excel(
    "15 - DO_FUNCIONARIOSTEPS_ATUALIZADO.xlsx",
    index=False
)
