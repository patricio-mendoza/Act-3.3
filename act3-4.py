palabrasReservadas = [
    "double", 
    "else", 
    "false", 
    "float", 
    "for", 
    "if", 
    "int",
    "long", 
    "namespace",
    "new", 
    "#include",
    "private", 
    "protected", 
    "public", 
    "return",
    "const",
    "include",
    "struct",
    "switch", 
    "this", 
    "throw",
    "char",
    "true", 
    "void",
    "while",
    "cin",
    "cout",
    "bool",
    "endl",
    "auto"]

operadores = [
    "+",
    "-", 
    "/",
    "*",
    "(",
    ")",
    "[",
    "]",
    "{",
    "}",
    "<",
    ">",
    "!",
    "&",
    "||",
    ">>",
    "<<",
    "=",
    ",",
    ";",
    "?", 
    ":"]

def areAllOperators(palabra):
    for car in palabra:
        if(not(car in operadores)): return False
    return True

def isVariable(palabra):
    if not palabra[0].isalpha() : return False
    
    for i in range(1,len(palabra)):
        if not (palabra[i].isalpha() or palabra[i].isnumeric() or palabra[i] == "_"):
            return False
    return True

def isNumber(token):
    try:
        float(token)
        return True
    except ValueError:
        return False

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
        tipo = ""
        insideString = False

        for palabra in line.split():
            if(palabra[0] == "\"" and not(insideString)):
                insideString = not("\"" in palabra[1:])
                htmlFile.write("\t\t<span class=\"string\">" + palabra + "</span>\n")
                continue
            elif(palabra[-1] == "\""):
                htmlFile.write("\t\t<span class=\"string\">" + palabra + "</span>\n")
                insideString = False
                continue
            elif(insideString):
                htmlFile.write("\t\t<span class=\"string\">" + palabra + "</span>\n")
                continue
            elif(palabra in palabrasReservadas):
                tipo = "reservado"
            elif(len(palabra) >= 2 and palabra[0:2] == "//"):
                tipo = "comentario"
                htmlFile.write("\t\t<span class=\"comentario\">" + "//" + line.split("//")[1] + "</span>\n")
                break
            elif(palabra in operadores or all(map(areAllOperators,list(palabra)))):
                tipo = "operador"
            elif(len(palabra) == 3 and palabra[0] == "'" and palabra[2] == "'"):
                tipo = "char"
            elif(isVariable(palabra)):
                tipo = "variable"
            elif(isNumber(palabra)):
                tipo = "literal"
            else:
                tipo = "error"

            htmlFile.write("\t\t<span class=\"" + tipo + "\">" + palabra + "</span>\n")
        htmlFile.write("\t\t<br>\n")
        

    htmlFile.write("\t</body>\n")
    htmlFile.write("</html>")

    # Cerrar Archivos  
    exampleFile.close()

main()