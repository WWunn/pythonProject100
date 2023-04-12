import numpy as np
# tablice
a = np.array([0, 2, 7, 4])
print(a)
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
print(a.shape)
m = np.array([np.arange(2), np.arange(2)])
print(m.shape)
# ilosc wymiarow tablicy
print(a.ndim)
# macierz pusta i macierz jedynek
zera = np.zeros((5, 5), dtype='int64')
jedynki = np.ones((4, 4), dtype='int64')
print(zera)
print(jedynki)
print(zera.dtype)
print(jedynki.dtype)
# pusta macierz o wymiarach 2x2
pusta = np.empty((2, 2))
print(pusta)
