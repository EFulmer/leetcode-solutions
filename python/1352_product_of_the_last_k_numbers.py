class ProductOfNumbers:

    def __init__(self):
        # We need to start with one for the multiplicative identity.
        # (ps for products)
        self._ps = [1]

    @property
    def product_length(self):
        # - 1 since we start with a 1 to preserve the multiplicative
        # identity.
        return len(self._ps) - 1

    def add(self, num: int) -> None:
        # if num == 0, reset the list
        if num == 0:
            self._ps = [1]
        else:
            new_product = self._ps[-1] * num
            self._ps.append(new_product)

    def getProduct(self, k: int) -> int:
        if k < 1:
            raise ValueError(f"cannot get the product last of {k} numbers")
        elif k > self.product_length:
            return 0
        return self._ps[self.product_length] // self._ps[self.product_length - k]



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
