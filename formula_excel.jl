using ExcelReaders

# Lê a primeira planilha de um arquivo Excel
data = readxlsheet("formulas.xlsx", "Plan1")

data
