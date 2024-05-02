class Cookie:
    def __init__(self, color) -> None:
        self.color = color

    def get_color(self) -> str:
        return self.color
    
    def set_color(self, color) -> None:
        self.color = color

    def __str__(self) -> str:
        color = self.get_color()
        return f"This cookie is {color} colored"

def main():
    cookie_one = Cookie('green')
    cookie_two = Cookie('blue')
    print(cookie_two)
    cookie_two.set_color('yellow')
    print(cookie_two)

    num1 = {'name': 'ebran'}
    num2 = num1
    print(id(num1))
    print(id(num2))
    num2['name'] = 'bright'
    print(id(num2))
    print(num1)
    
if __name__ == '__main__':
    main()