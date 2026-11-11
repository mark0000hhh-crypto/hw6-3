class SearchEngine:
    def __init__(self, data):
        self.data = data

    def linear_search(self, target: int) -> int:
        for i in range(len(self.data)):
            if self.data[i] == target:
                return i
        return -1

    def binary_search(self, target: int) -> int:
        left = 0
        right = len(self.data) - 1

        while left <= right:
            middle = (left + right) // 2
            if self.data[middle] == target:
                return middle
            elif self.data[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
                
        return -1


prices = [
    100, 120, 135, 150, 175, 190, 200, 215,
    230, 250, 275, 290, 300, 320, 340, 350,
    370, 390, 400, 420, 440, 450, 470, 490,
    500, 520, 540, 560, 580, 600, 620, 650,
    670, 690, 700, 720, 740, 760, 780, 800,
    820, 850, 870, 890, 900, 920, 950, 980,
    1000, 1050, 1100, 1150, 1200, 1250, 1300, 1400,
    1500, 1600, 1750, 1800, 2000, 2200, 2500, 3000
]


search = SearchEngine(prices)


index_300 = search.linear_search(300)
index_450 = search.binary_search(450)
index_500_linear = search.linear_search(500)
index_500_binary = search.binary_search(500)

print(f"Индекс цены 300 (линейный поиск): {index_300}")
print(f"Индекс цены 450 (бинарный поиск): {index_450}")
print(f"Индекс цены 500 (линейным поиском): {index_500_linear}")
print(f"Индекс цены 500 (бинарным поиском): {index_500_binary}")