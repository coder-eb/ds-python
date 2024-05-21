class HashTable:
    def __init__(self, size=7) -> None:
        # Python's way of creating an empty list
        self.data_map = [None] * size

    def __hash(self, key):
        generated_hash = 0
        RANDOM_PRIME_NUMBER = 23
        for letter in key:
            ascii_value = ord(letter)
            generated_hash = (generated_hash + ascii_value * RANDOM_PRIME_NUMBER) % len(self.data_map)
        return generated_hash

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key) -> list:
        index = self.__hash(key)
        if self.data_map[index] is None:
            return None
        
        for [data_key, value] in self.data_map[index]:
            if key == data_key:
                return value
        return None
    
    def keys(self) -> list:
        all_keys = []
        for items in self.data_map:
            if not items: continue

            for [key, value] in items:
                all_keys.append(key)
        return all_keys
    
    def __str__(self) -> str:
        formatted_string = ""
        for index, value in enumerate(self.data_map):
            formatted_string += f"{index} => {value}"
            formatted_string += "\n"
        return formatted_string
    
    def print_table(self) -> None:
        print(self.__str__())
