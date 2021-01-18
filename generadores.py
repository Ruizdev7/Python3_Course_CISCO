def potenciasDe2(n):
    potencia = 1
    for i in range(n):
        yield potencia
        potencia *= 2

for v in potenciasDe2(8):
    print(v)

Los generadores también pueden usarse dentro de listas de comprensión, como aqui:
def potenciasDe2(n):
    potencia = 1
    for i in range(n):
        yield potencia
        potencia *= 2

t = [x for x in potenciasDe2(5)]

print(t)

La función list() puede transformar una serie de invocaciones de generador subsequentes en una lista real:
def potenciasDe2(n):
    potencia = 1
    for i in range(n):
        yield potencia
        potencia *= 2

t = list(potenciasDe2(3))

print(t)

Además, el contexto creado por el operador in también te permite usar un generador.

El ejemplo muestra cómo hacerlo:
def potenciasDe2(n):
    potencia= 1
    for i in range(n):
        yield potencia
        potencia*= 2

for i in range(20):
    if i in potenciasDe2(4):
        print(i)

Ahora veamos un Generador de números de la serie Fibonacci implementando lo anterior.

Aquí está:
def Fib(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(Fib(10))

print(fibs)

listaUno = []

for ex in range(6):
    listaUno.append(10 ** ex)


listaDos = [10 ** ex for ex in range(6)]

print(listaUno)
print(listaDos)


