import uuid

class Receipt:
    def __init__(self, retailer, purchase_date, purchase_time, items, total):
        self.id = str(uuid.uuid4())
        self.retailer = retailer
        self.purchase_date = purchase_date
        self.purchase_time = purchase_time
        self.items = items
        self.total = total
        self.points = self.calculate_points()

    def calculate_points(self):
        points = 0
        points += len(self.retailer.strip())
        if float(self.total).is_integer():
            points += 50
        if float(self.total) % 0.25 == 0:
            points += 25
        points += sum(len(item['shortDescription'].strip()) for item in self.items)
        points += (len(self.items) // 2) * 5
        hour = int(self.purchase_time.split(':')[0])
        if 14 <= hour < 16:
            points += 10
        return points
