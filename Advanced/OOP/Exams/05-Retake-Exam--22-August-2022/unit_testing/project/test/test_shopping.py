from project.shopping_cart import ShoppingCart
import unittest


class ShoppingCartTests(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart("Levche", 100)
    
    def test_init(self):
        self.assertEqual("Levche", self.cart.shop_name)
        self.assertEqual(100, self.cart.budget)
        self.assertEqual({}, self.cart.products)
    
    def test_invalid_shop_name(self):
        with self.assertRaises(ValueError) as ve:
            ShoppingCart("levche", 100)
        
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))
        
        with self.assertRaises(ValueError) as ve:
            ShoppingCart("Levche1", 100)
        
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_expensive_product(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("Bowl", 100)
            
        self.assertEqual({}, self.cart.products)
        self.assertEqual("Product Bowl cost too much!", str(ve.exception))
    
    def test_add_to_cart_valid_all_and_doubled(self):
        result = self.cart.add_to_cart("Bowl", 10)
        self.assertEqual({"Bowl": 10}, self.cart.products)
        self.assertEqual("Bowl product was successfully added to the cart!", result)
        
        result = self.cart.add_to_cart("Bowl", 50)
        self.assertEqual({"Bowl": 50}, self.cart.products)
        self.assertEqual("Bowl product was successfully added to the cart!", result)

    def test_add_to_cart_valid_all_and_different(self):
        result = self.cart.add_to_cart("Bowl", 10)
        self.assertEqual({"Bowl": 10}, self.cart.products)
        self.assertEqual("Bowl product was successfully added to the cart!", result)
        
        result = self.cart.add_to_cart("Plate", 50)
        self.assertEqual({"Bowl": 10, "Plate": 50}, self.cart.products)
        self.assertEqual("Plate product was successfully added to the cart!", result)
    
    def test_remove_from_cart_valid_all(self):
        self.cart.add_to_cart("Bowl", 10)        
        result = self.cart.remove_from_cart("Bowl")
        
        self.assertEqual({}, self.cart.products)
        self.assertEqual("Product Bowl was successfully removed from the cart!", result)

    def test_remove_from_cart_valid_all_multiple(self):
        self.cart.add_to_cart("Bowl", 10)
        self.cart.add_to_cart("Plate", 50)
        result = self.cart.remove_from_cart("Bowl")
        
        self.assertEqual({"Plate": 50}, self.cart.products)
        self.assertEqual("Product Bowl was successfully removed from the cart!", result)
    
    def test_remove_from_cart_invalid_product(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart("Bowl")
        
        self.assertEqual("No product with name Bowl in the cart!", str(ve.exception))
    
    def test_add_no_products(self):
        cart_two = ShoppingCart("LevcheDve", 100)
        new_cart = self.cart.__add__(cart_two)
        
        self.assertEqual("LevcheLevcheDve", new_cart.shop_name)
        self.assertEqual(200, new_cart.budget)
        self.assertEqual({}, new_cart.products)
    
    def test_add_with_products(self):
        cart_two = ShoppingCart("LevcheDve", 100)
        self.cart.add_to_cart("Bowl", 10)
        cart_two.add_to_cart("Plate", 10)
        new_cart = self.cart.__add__(cart_two)
        
        self.assertEqual("LevcheLevcheDve", new_cart.shop_name)
        self.assertEqual(200, new_cart.budget)
        self.assertEqual({"Bowl": 10, "Plate": 10}, new_cart.products)

    def test_buy_products_with_valid_data(self):
        shop = ShoppingCart('Test', 200)
        shop.add_to_cart('product_name1', 99)
        shop.add_to_cart('product_name2', 98)
        self.assertEqual('Products were successfully bought! Total cost: 197.00lv.', shop.buy_products())

    def test_buy_products_should_raise_error(self):
        shop = ShoppingCart('Test', 20)
        shop.add_to_cart('product_name1', 99)
        with self.assertRaises(ValueError) as er:
            shop.buy_products()
        expected = 'Not enough money to buy the products! Over budget with 79.00lv!'
        actual = str(er.exception)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
