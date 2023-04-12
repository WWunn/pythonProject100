import numpy as np
# tablice
# a = np.array([0, 2, 7, 4])
# print(a)
# b = np.arange(2, 5, 0.1)
# print(b)
# # wypisywanie typu zmiennej
# print(type(a), " x ", type(b))
# # sprawdzanie typu danych w tablicy
# print(a.dtype)
# # tablica z konkretnym typem danych
# c = np.arange(2, dtype='int64')
# print(c.dtype)
# # zapisywanie kopii tablicy jako tablica z innym typem danych
# d = a.astype('float')
# print(d)
# print(d.dtype)
# rozmiar tablicy
# print(a.shape)
# m = np.array([np.arange(2), np.arange(2)])
# print(m.shape)
# # ilosc wymiarow tablicy
# print(a.ndim)
# # macierz pusta i macierz jedynek
# zera = np.zeros((5, 5), dtype='int64')
# jedynki = np.ones((4, 4), dtype='int64')
# print(zera)
# print(jedynki)
# print(zera.dtype)
# print(jedynki.dtype)
# # pusta macierz o wymiarach 2x2
# pusta = np.empty((2, 2))
# print(pusta)
# # maciesz
# macierz = np.array([[12, 11], [2, 1]])
# print(macierz)
# # odwolywanie do elementow macierzy
# poz_1 = macierz[1, 1]
# poz_2 = macierz[0][1]
# print(poz_1)
# print(poz_2)
# # linspace
# liczbylin = np.linspace(1, 2, 5, endpoint=False)
# dwie macierze?
# z = np.indices((5, 3))
# print(z)
# print(z[1][1][2])  # pierwszy indeks wybiera macierz, drugi wiersz, trzeci kolumne
# # macierz diagonalna
# mat_diag = np.diag([a for a in range(1, 14, 4)])
# print(mat_diag)
# z = np.fromiter(range(5), dtype='int32')
# print(z)
# znaki = b'ogolna xd'
# z1 = np.frombuffer(znaki, dtype='S1')
# print(z1)
# z2 = np.frombuffer(znaki, dtype='S3')
# print(z2)
# # dla list
# z3 = np.array(list(znaki))
# z4 = np.array(list(znaki), dtype='S1')
# z5 = np.array(list(b'ogolna'))
# z6 = np.fromiter(znaki, dtype='S1')
# a = np.arange(10)
# s = slice(2, 7, 2)  # 2 start, 7 koniec 2 co ile brac
# print(a[s])
# # listy
# print(a[2:7:2])
# print(a[3:])
# print(a[2:5])
# # zmiana rozmiaru - ilosc wierszy x ilosc kolumn = ilosc elementow
mat = np.arange(25)
print(mat)
mat = mat.reshape((5, 5))
print(mat)
print(mat[1:])  # od drugiego wiersza
print(mat[:, 1:2])   # tylko kolumna nr 1
print(mat[:, -1])   # ostatnia kolumna
print(mat[2:5, 1:3])  # 2 i 3 kolumna dla 3,4,5 wierszy
print(mat[2, 4])  # 3 i 5 kolumna
print(' ')