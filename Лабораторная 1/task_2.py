# TODO Найдите количество книг, которое можно разместить на дискете

disk = 1.44     # объем дискеты в Мб
disk_bites = (disk * 1024) * 1024

pages_num = 100 
strings = 50
symbols = 25 
one_symbol = 4 
one_book_vol = one_symbol * symbols * strings * pages_num

books_num = int(disk_bites // one_book_vol)

print("Количество книг, помещающихся на дискету:", books_num)
