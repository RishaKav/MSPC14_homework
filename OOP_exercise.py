class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product: {self.name}, Price: {self.price:.2f}")

class ShoppingCart:
    def __init__(self):
        self.items = {} 

    def add_product(self, product: Product, quantity: int):
        if product.name in self.items:
            self.items[product.name]["quantity"] += quantity
        else:
            self.items[product.name] = {"product": product, "quantity": quantity}
        print(f"Added {quantity} of {product.name} to the cart.")

    def remove_product(self, product: Product, quantity: int):
        if product.name in self.items:
            if self.items[product.name]["quantity"] > quantity:
                self.items[product.name]["quantity"] -= quantity
                print(f"Removed {quantity} of {product.name} from the cart.")
            else:
                del self.items[product.name]
                print(f"Removed {product.name} from the cart.")
        else:
            print(f"{product.name} is not in the cart.")

    def calculate_total(self) -> float:
        return sum(item["product"].price * item["quantity"] for item in self.items.values())

    def display_cart(self):
        if not self.items:
            print("Your shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for item in self.items.values():
                product, quantity = item["product"], item["quantity"]
                print(f"{product.name} - Quantity: {quantity}, Price: {product.price:.2f} each")
            print(f"Total Cost: ${self.calculate_total():.2f}")

# Example usage:
if __name__ == "__main__":
    apple = Product("Apple", 0.5)
    banana = Product("Banana", 0.3)
    
    cart = ShoppingCart()
    cart.add_product(apple, 3)
    cart.add_product(banana, 5)
    cart.display_cart()
    
    cart.remove_product(apple, 1)
    cart.display_cart()
    
    cart.remove_product(banana, 5)
    cart.display_cart()
