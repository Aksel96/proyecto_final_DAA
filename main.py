import time


def guardar_coordenadas(coordenadas, nombre_archivo="coordenadas_out.txt"):
    with open(nombre_archivo, "w") as archivo:
        for x, y in coordenadas:
            archivo.write(f"{x} {y}\n")


def leer_campo(nombre_archivo="coordenadas.txt"):
    coordenadas = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            x, y = map(int, linea.split())
            coordenadas.append((x, y))
    return coordenadas


def calcular_area(campo):
    area_max = 0
    campo.pop()
    rango = len(campo)
    contador = 0
    a, b, c = None, None, None
    print(f"Puntos a evaluar sus combinaciones: {len(campo)}")
    for i in range(rango):
        for j in range(rango):
            for k in range(rango):
                area = abs(
                    campo[i][0] * (campo[j][1] - campo[k][1]) + campo[j][0] * (campo[k][1] - campo[i][1]) +
                    campo[k][0] * (campo[i][1] - campo[j][1])) / 2
                contador += 1
                if area >= area_max:
                    a = campo[i]
                    b = campo[j]
                    c = campo[k]
                    area_max = area

    print(f"Numero operaciones (combinaciones) realizadas: {contador}")
    return area_max, a, b, c


def main():
    inicio = time.time()
    campo = leer_campo()
    area_maxima, a, b, c = calcular_area(campo)
    print(f"Area Maxima: {area_maxima} \n XY1:{a} \n XY2:{b} \n XY3:{c}")
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    print(f"Tiempo de ejecución: {tiempo_ejecucion:.4f} segundos")

    coor_out = [a, b, c]
    guardar_coordenadas(coor_out)


if __name__ == '__main__':
    main()
