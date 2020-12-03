#Sortowanie rosnące metodą bąbelkową

# niech l będzie listą wejściową (nieposortowaną)
# pętla for po wszystkich indeksach l, gdzie zmienną iterującą będzie i:
# pętla for po wszystkich indeksach l, gdzie zmienną iterującą będzie j:
# jeżeli l[i] < l[j], to zamień te wartości miejscami w liście

#wybieranie

# niech l będzie listą wejściową (nieposortowaną)
# pętla for po wszystkich indeksach l, gdzie zmienną iterującą będzie i:
#   min_index = i
#   pętla for w zakresie od i + 1 do długości l - 1:
#       jeżeli l[j] < l[min_index] to ustaw min_index = j
#   zamień miejscami wartości w liście na pozycjach i oraz min_index     <=== nie j tylko i :)

#wstawianie

# niech l będzie listą wejściową (nieposortowaną)
# niech n będzie liczbą elementów w l
# pętla for ze zmienną iterującą i w zakresie od 1 do n - 1:
# key = l[i]
# j = i - 1
# while j >= 0 and l[j] > key:
# l[j + 1] = l[j]
# j = j - 1 l[j + 1] = key

from typing import List

class Sorting:
    def booble(self,l:List):
        for i in range(0,len(l)):
            for j in range(0,len(l)):
                if l[i]<l[j]:
                    temp= l[i]
                    l[i]=l[j]
                    l[j]=temp

    def select(self,l):
        for i in range(0,len(l)):
            min_index=i
            for j in range(i+1,len(l)):
                if l[j]<l[min_index]:
                    min_index=j
            temp= l[i]
            l[i]=l[min_index]
            l[min_index]=temp

    def insert(self,l):
        n=len(l)
        for i in range(1,n):
            key=l[i]
            j=i-1
            while ((j>=0)&(l[j]>key)):
                l[j+1]=l[j]
                j=j-1
                l[j+1]=key

    def booble_reverse(self, l):
        for i in range(0,len(l)):
            for j in range(0,len(l)):
                if l[i]>l[j]:
                    temp= l[i]
                    l[i]=l[j]
                    l[j]=temp

    def select_reverse(self,l):
        for i in range(0,len(l)):
            min_index=i
            for j in range(i+1,len(l)):
                if l[j]>l[min_index]:
                    min_index=j
            temp= l[i]
            l[i]=l[min_index]
            l[min_index]=temp

    def insert_reverse(self,l):
        n=len(l)
        for i in range(1,n):
            key=l[i]
            j=i-1
            while ((j>=0)&(l[j]<key)):
                l[j+1]=l[j]
                j=j-1
                l[j+1]=key



sortowanko =Sorting()
li= [0,5,2,8,3,8,2]
print(li)
#sortowanko.booble(li)
#sortowanko.select(li)
#sortowanko.insert(li)
#sortowanko.booble_reverse(li)
#sortowanko.select_reverse(li)
#sortowanko.insert_reverse(li)
print(li)