class product:
    def __init__(self, name, min_price, max_price, price, ratio=0.05):
        self.name = name
        self.min_price = min_price
        self.max_price = max_price
        self.price = price
        self.X = self.inverse_price_equation()
        self.ratio = ratio

    def __repr__(self):
        return self.name

    def normalize_price(self, price):
        return (price - self.min_price)/(self.max_price - self.min_price)

    def denormalize_price(self, price):
        self.min_price + price*(self.max_price-self.min_price)

    def price_equation(self):
        '''
        Returns normalized (from 0 to 1) price
        '''
        return 0.5*(1-self.X**3)

    def inverse_price_equation(self):
        '''
        Returns X-value (-1 to 1) from current price
        '''
        return (1-2*self.normalize_price(self.price))**(1/3)

    def increase_price(self):
        '''
        Increases prices due to a new sold item
        '''
        self.X -= self.ratio
        if self.X < -1: self.X = -1
        self.update_price()

    def decrease_price(self):
        '''
        Decreases prices due to lack of purchases
        '''
        self.X += self.ratio
        if self.X > 1: self.X = 1
        self.update_price()

    def update_price(self):
        normalized_price = self.price_equation()
        self.price = self.denormalize_price(normalized_price)