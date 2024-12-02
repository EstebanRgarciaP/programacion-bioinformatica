from fasta import Record

# Crear un registro FASTA
record = Record(id='seq001', seq='ATGCATGCAT', desc='Example sequence')

# Imprimir el registro en formato FASTA con un límite de 5 caracteres por línea
print(record.format(wrap=5))

# Salida esperada:
# >seq001 Example sequence
# ATGCA
# TGCA
