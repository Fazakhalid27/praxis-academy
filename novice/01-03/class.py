class MenuItem():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ': $' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        if count >= 3:
            total_price *= 0.9
        return(round(total_price))

menu_item1 = MenuItem('Roti Lapis', 5)
menu_item2 = MenuItem('Kue Coklat', 4)
menu_item3 = MenuItem('Kopi', 3)
menu_item4 = MenuItem('Jus Jeruk', 2)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]
index = 0

for menu_item in menu_items:
    print(str(index) + '.' + menu_item.info())
    index += 1

print('-'*40)

order = int(input('Masukkan nomor menu: '))

selected_menu = menu_items[order]

count = int(input('Jumlah pesanan (diskon 10% untuk 3 atau lebih): '))

result = selected_menu.get_total_price(count)

print('Total harga adalah $ ' + str(result))