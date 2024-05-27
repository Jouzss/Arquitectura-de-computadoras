# Primer intento bota error, porque no se puede sumar un int a un str
# if __name__ == '__main__':
#     a = 1
#     b = '2'

#     c = a + b

#     print(f"el resultado de a + b es {c}")

if __name__ == '__main__':
    a = 1
    b = '2'

    try:
        c = a + b
    except TypeError:
        print("Ocurrió un error de tipo")
        if not isinstance(a, int):
            a = int(a)

        if not isinstance(b, int):
            b = int(b)

        c = a + b
    finally:
        print(f"el resultado de a + b es {c}")