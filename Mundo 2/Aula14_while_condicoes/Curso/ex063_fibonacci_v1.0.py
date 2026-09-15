print("-" * 30)
print("\033[35mSEQUENCIA DE FIBONACCI\033[m")
print("-" * 30)
n = int(input("Quantos números deseja mostrar? "))
t1 = 0
t2 = 1
print(f"{t1} -> {t2}", end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f" -> {t3}", end='')
    cont += 1
    t1 = t2
    t2 = t3
print(" -> \033[1;32mConcluído\033[m")
