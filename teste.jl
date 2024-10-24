using PyCall

# Adiciona o diretório atual ao sys.path para permitir a importação do script
pushfirst!(PyVector(pyimport("sys")."path"), ".")

# Importa o módulo
py_imported = pyimport("teste")

# Chama a função Python definida no script "teste.py"
resultado = py_imported.soma(3, 5)  # Assumindo que a função 'soma' está definida no script
println(resultado)  # Saída será 8 (se a função soma retornar a soma dos números)
