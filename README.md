# Redimensionamiento

### Tamaño del tipo de dato, bloque por defecto, cabezera del bloque, cabezera de la columna y el tamaño que necesita MySQL para almacenar una columna

KB = 1024
MB = math.pow(1024, 2)
GB = math.pow(1024, 3)

BLOCK_HEADER = 100
BLOCK_SIZE = KB # 10 bytes
TINYTEXT = 256 # 256 bytes
TEXT = 64 * KB # 64 kilobytes
MEDIUMTEXT = 16 * MB # 16 Megabytes
LONGTEXT = 4 * GB # 4 Gigabytes
TINYBLOB = 256
BLOB = 64 * KB
MEDIUMBLOB = 16 * MB
LONGBLOB = 4 * GB
TINYINT = 1
SMALLINT = 2
MEDIUMINT = 3
INT = 4
BIGINT = 8
FLOAT = 4
DOUBLE = 8
REAL = 8
HEADER = 1
CHAR = 1
VARCHAR = 1
HEADER = 1
MYSQL_SIZE = 3
