# Redimensionamiento

### Tamaño del tipo de dato, bloque por defecto, cabezera del bloque, cabezera de la columna y el tamaño que necesita MySQL para almacenar una columna

* KB = 1024 bytes
* MB = 1048576 bytes
* GB = 1073741824 bytes
* BLOCK_HEADER = 100 bytes
* BLOCK_SIZE = KB # 10 bytes
* TINYTEXT = 256 # 256 bytes
* TEXT = 64 * KB
* MEDIUMTEXT = 16 * MB
* LONGTEXT = 4 * GB
* TINYBLOB = 256 bytes
* BLOB = 64 * KB
* MEDIUMBLOB = 16 * MB
* LONGBLOB = 4 * GB
* TINYINT = 1 bytes
* SMALLINT = 2 bytes
* MEDIUMINT = 3 bytes
* INT = 4 bytes
* BIGINT = 8 bytes
* FLOAT = 4 bytes
* DOUBLE = 8 bytes
* REAL = 8 bytes
* HEADER = 1 bytes
* CHAR = 1 bytes
* VARCHAR = 1 bytes
* MYSQL_SIZE = 3 bytes