class Flower:

    def __init__(self, name, color, length, price):
        self.name = name
        self.color = color
        self.length = length
        self.price = price


class Bouquet:

    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def add_flowers(self, flowers):
        self.flowers += flowers

    def calculate_cost(self):
        total_cost = sum(flower.price for flower in self.flowers)
        return total_cost
    
    def is_good_bouquet(self):
        colors = set(flower.color for flower in self.flowers)
        return len(colors) == 1 or len(self.flowers) <= 3

    
initial_flowers = [
    Flower("Ромашка", "белая", "средняя", 50),
    Flower("Ромашка", "белая", "средняя", 50),
    Flower("Ромашка", "белая", "средняя", 50),
    
    Flower("Ромашка", "белая", "длинная", 70),
    Flower("Ромашка", "белая", "длинная", 70),
    Flower("Ромашка", "белая", "длинная", 70),
    Flower("Ромашка", "белая", "длинная", 70),
    
    Flower("Ромашка", "зелёная", "средняя", 50),
    Flower("Ромашка", "зелёная", "средняя", 50),
    Flower("Ромашка", "зелёная", "средняя", 50),
    Flower("Ромашка", "зелёная", "средняя", 50),
    Flower("Ромашка", "зелёная", "средняя", 50),
    Flower("Ромашка", "зелёная", "средняя", 50),
    
    Flower("Ромашка", "жёлтая", "маленькая", 100),
    Flower("Ромашка", "жёлтая", "маленькая", 100),
    Flower("Ромашка", "жёлтая", "маленькая", 100),
    Flower("Ромашка", "жёлтая", "маленькая", 100),
    Flower("Ромашка", "жёлтая", "маленькая", 100),
    Flower("Ромашка", "жёлтая", "маленькая", 100),
    
    Flower("Ромашка", "жёлтая", "средняя", 150),
    
    Flower("Ромашка", "жёлтая", "длинная", 250),
    Flower("Ромашка", "жёлтая", "длинная", 250),
    
    Flower("Роза", "белая", "средняя", 50),
    Flower("Роза", "белая", "средняя", 50),
    Flower("Роза", "белая", "средняя", 50),
    Flower("Роза", "белая", "средняя", 50),
    Flower("Роза", "белая", "средняя", 50),

    Flower("Роза", "белая", "длинная", 70),
    Flower("Роза", "белая", "длинная", 70),
    Flower("Роза", "белая", "длинная", 70),
    Flower("Роза", "белая", "длинная", 70),
    Flower("Роза", "белая", "длинная", 70),

    Flower("Роза", "зелёная", "средняя", 50),
    Flower("Роза", "зелёная", "средняя", 50),
    Flower("Роза", "зелёная", "средняя", 50),
    Flower("Роза", "зелёная", "средняя", 50),
    Flower("Роза", "зелёная", "средняя", 50),

    Flower("Роза", "жёлтая", "маленькая", 100),
    Flower("Роза", "жёлтая", "маленькая", 100),
    Flower("Роза", "жёлтая", "маленькая", 100),
    Flower("Роза", "жёлтая", "маленькая", 100),
    Flower("Роза", "жёлтая", "маленькая", 100),

    Flower("Роза", "жёлтая", "средняя", 150),
    Flower("Роза", "жёлтая", "средняя", 150),
    Flower("Роза", "жёлтая", "средняя", 150),
    Flower("Роза", "жёлтая", "средняя", 150),
    Flower("Роза", "жёлтая", "средняя", 150),

    Flower("Роза", "жёлтая", "длинная", 250),
    Flower("Роза", "жёлтая", "длинная", 250),
    Flower("Роза", "жёлтая", "длинная", 250),
    Flower("Роза", "жёлтая", "длинная", 250),
    Flower("Роза", "жёлтая", "длинная", 250),

    Flower("Роза", "красная", "маленькая", 50),
    Flower("Роза", "красная", "маленькая", 50),
    Flower("Роза", "красная", "маленькая", 50),
    Flower("Роза", "красная", "маленькая", 50),
    Flower("Роза", "красная", "маленькая", 50),

    Flower("Роза", "красная", "средняя", 70),
    Flower("Роза", "красная", "средняя", 70),
    Flower("Роза", "красная", "средняя", 70),
    Flower("Роза", "красная", "средняя", 70),
    Flower("Роза", "красная", "средняя", 70),

    Flower("Роза", "розовая", "длинная", 50),
    Flower("Роза", "розовая", "длинная", 50),
    Flower("Роза", "розовая", "длинная", 50),
    Flower("Роза", "розовая", "длинная", 50),
    Flower("Роза", "розовая", "длинная", 50),

    Flower("Роза", "розовая", "маленькая", 100),
    Flower("Роза", "розовая", "маленькая", 100),
    Flower("Роза", "розовая", "маленькая", 100),
    Flower("Роза", "розовая", "маленькая", 100),
    Flower("Роза", "розовая", "маленькая", 100),

    Flower("Роза", "бордовая", "средняя", 150),
    Flower("Роза", "бордовая", "средняя", 150),
    Flower("Роза", "бордовая", "средняя", 150),
    Flower("Роза", "бордовая", "средняя", 150),
    Flower("Роза", "бордовая", "средняя", 150),

    Flower("Роза", "бордовая", "длинная", 250),
    Flower("Роза", "бордовая", "длинная", 250),
    Flower("Роза", "бордовая", "длинная", 250),
    Flower("Роза", "бордовая", "длинная", 250),
    Flower("Роза", "бордовая", "длинная", 250)
]

bouquet = Bouquet()
num_flowers = int(input("Введите количество цветов в букете: "))
i = 0

while i != num_flowers:
    name = input("Введите название цветка: ")
    color = input("Введите цвет цветка: ")
    length = input("Введите длину цветка: ")
    price = int(input("Введите стоимость цветка: "))
    flower = Flower(name, color, length, price)
    flag = True
    for initial_flower in initial_flowers:
        if name == initial_flower.name and color == initial_flower.color and length == initial_flower.length and price == initial_flower.price:
            if bouquet.flowers:
                if bouquet.flowers[0].length != length:
                    print("Цветы в букете должны быть одной длины!")
                    break
                else:
                    bouquet.add_flower(initial_flowers.pop(initial_flowers.index(initial_flower)))
                    i += 1
                    break
            else:
                    bouquet.add_flower(initial_flowers.pop(initial_flowers.index(initial_flower)))
                    i += 1
                    break
        else:
            print("Такого цветка нет в ассортименте.")

if num_flowers != 0:
    cost = bouquet.calculate_cost()
    
    if bouquet.is_good_bouquet():
        print(f"Стоимость букета: {cost} руб. (Хороший букет)")
    else:
        print(f"Стоимость букета: {cost} руб. (Плохой букет)")
else:
    print("Вы не составили букет.")