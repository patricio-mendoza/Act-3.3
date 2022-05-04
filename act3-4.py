def main():
    # Abrir Archivos
    htmlFile = open("index.html","w")
    exampleFile = open("ejemplo.txt","r")
    # Estructura Basica de HTML
    htmlFile.write("<!DOCTYPE html>\n")
    htmlFile.write("<html>\n")
    htmlFile.write("\t<head>\n")
    htmlFile.write("\t\t<meta charset=\"utf-8\"/>\n")
    htmlFile.write("\t\t<title>Resaltador de Sintaxix</title>\n")
    htmlFile.write("\t\t<link rel=\"stylesheet\" href=\"styles.css\">\n")
    htmlFile.write("\t</head>\n")
    htmlFile.write("\t<body bgcolor=#121212>\n")

    # LEYENDA
    htmlFile.write("\t\t<h2>" + "Leyenda:" + "</h2>\n")
    htmlFile.write("\t\t<span class=\"reservado\">" + "Palabra Reservada: int, float, for" + "</span>\n")
    htmlFile.write("\t\t<br>\n")
    htmlFile.write("\t\t<span class=\"operador\">" + "Operador: +, -, =, ;" + "</span>\n")
    htmlFile.write("\t\t<br>\n")
    htmlFile.write("\t\t<span class=\"literal\">" + "Literal: 4, 6.4, -31.1" + "</span>\n")
    htmlFile.write("\t\t<br>\n")
    htmlFile.write("\t\t<span class=\"variable\">" + "Variable: hola1, _f4ws, i" + "</span>\n")
    htmlFile.write("\t\t<br>\n")
    htmlFile.write("\t\t<span class=\"char\">" + "Char: 'a', '5', 'V'" + "</span>\n")
    htmlFile.write("\t\t<br>\n")
    htmlFile.write("\t\t<span class=\"string\">" + "String: \"Hola\",\"String\"" + "</span>\n")
    htmlFile.write("\t\t<br>\n")
    htmlFile.write("\t\t<span class=\"comentario\">" + "Comentario: // Esto es un comentario" + "</span>\n")
    htmlFile.write("\t\t<br>\n")
    htmlFile.write("\t\t<span class=\"error\">" + "1a2svb4v" + "</span>\n")
    htmlFile.write("\t\t<br>\n\n")

    # RESALTADOR DE SINTAXIS
    htmlFile.write("\t\t<h2>" + "Resaltador de Sintaxis:" + "</h2>\n")
    for line in exampleFile.readlines():
        line = line.rstrip()
        htmlFile.write("\t\t<span class=\"comentario\">" + line + "</span>\n")
        htmlFile.write("\t\t<br>\n")

    htmlFile.write("\t</body>\n")
    htmlFile.write("</html>")

    # Cerrar Archivos  
    exampleFile.close()

main()