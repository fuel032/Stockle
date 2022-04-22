stocks = ["Tesla","Roblox","Apple","Twitter","NVIDIA","Meta","Target","CVS","Amazon","Cisco"]
currentStock = [1008.78,34.61,166.42,47.08,201.83,188.07,248.17,105.18,2965.92,52.78]

class chooseStock():
    def __new__(self,stock) -> float:
        
        i = 0

        while i < len(stocks):
            if stock != stocks[i]:
                i = i + 1
            else:
                return currentStock[i]