import random

names = ["klon", "milk", "beer"]
domains = ["to", "ru", "pro"]


class CreateEmail:

    def __init__(self, domains, names):
        self.domains = domains
        self.names = names

    def create_point(self, min_limit, max_limit):
        point = random.randint(min_limit, max_limit)
        return point

    def create_str(self, min_limit, max_limit):
        len = self.create_point(min_limit, max_limit)
        str = ""
        index = 0
        while index < len:
            str += chr(self.create_point(97, 122))  # ascii table
            index += 1
        return str

    def create(self, min_num = 100 , max_num = 999, min_len = 5 , max_len = 7):
        result = names[self.create_point(0, len(names) - 1)] + "."
        result += str(self.create_point(min_num, max_num)) + "@"
        result += self.create_str(min_len, max_len) + "."
        result += domains[self.create_point(0, len(domains) - 1)]
        return result


email = CreateEmail(domains, names)
print(email.create())
