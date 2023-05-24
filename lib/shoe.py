#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size


class TestShoe:
    def test_has_brand_and_size(self):
        stan_smith = Shoe("Adidas", 9)
        assert stan_smith.brand == "Adidas"
        assert stan_smith.size == 9
