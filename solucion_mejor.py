import time


def guardar_coordenadas(coordenadas, nombre_archivo="coordenadas_out.txt"):
    with open(nombre_archivo, "w") as archivo:
        for x, y in coordenadas:
            archivo.write(f"{x} {y}\n")


def combinaciones(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)


def leer_campo(nombre_archivo="coordenadas.txt"):
    coordenadas = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            x, y = map(int, linea.split())
            coordenadas.append((x, y))
    return coordenadas


def producto_cruzado(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def envolvente_convexa(puntos):
    puntos = sorted(puntos)
    lower, upper = [], []
    for p in puntos:
        while len(lower) >= 2 and producto_cruzado(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(puntos):
        while len(upper) >= 2 and producto_cruzado(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def calcular_area(campo):
    area_max = 0
    a = b = c = None
    contador = 0
    puntos_envolvente = envolvente_convexa(campo)

    print(f"Puntos a evaluar sus combinaciones: {len(puntos_envolvente)}")

    for p1, p2, p3 in combinaciones(puntos_envolvente, 3):
        area = abs(
            p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) +
            p3[0] * (p1[1] - p2[1])
        ) / 2
        contador += 1
        if area > area_max:
            area_max = area
            a, b, c = p1, p2, p3
    print(f"Numero operaciones (combinaciones) realizadas: {contador}")
    return area_max, a, b, c


def main():
    inicio = time.time()
    campo = leer_campo()
    campo.pop()
    area_maxima, a, b, c = calcular_area(campo)
    print(f"Area Maxima: {area_maxima} \n XY1:{a} \n XY2:{b} \n XY3:{c}")

    fin = time.time()
    tiempo_ejecucion = fin - inicio
    print(f"Tiempo de ejecución: {tiempo_ejecucion:.4f} segundos")

    coor_out = [a, b, c]
    guardar_coordenadas(coor_out)


if __name__ == '__main__':
    main()
