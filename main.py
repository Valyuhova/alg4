class Node:
    def __init__(self, key, phone):
        self.key = key
        self.phone = phone
        self.left = None
        self.right = None
        self.parent = None


class BSTree:
    def __init__(self):
        self.root = None

    def search(self, x, k):
        if x is None or k == x.key:
            return x
        if k < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)

    def find(self, key):
        return self.search(self.root, key)

    def insert(self, key, phone):
        z = Node(key, phone)
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def _min_value_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def delete(self, key):
        z = self.find(key)
        if z is None:
            return False

        if z.left is None:
            self._transplant(z, z.right)
        elif z.right is None:
            self._transplant(z, z.left)
        else:
            y = self._min_value_node(z.right)
            if y.parent != z:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
        return True

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(f"{node.key}: {node.phone}")
            self.inorder(node.right)

    def show_all(self):
        if self.root is None:
            print("Довідник порожній.")
        else:
            print("Телефонний довідник:")
            self.inorder(self.root)


def main():
    tree = BSTree()

    start_contacts = [
        ("Гордієнко Анна", "099-311-42-53"),
        ("Денисенко Сергій", "066-842-10-94"),
        ("Іващенко Нікіта", "097-738-94-23"),
        ("Лихацький Денис", "093-434-05-76"),
        ("Лозовська Роксана", "067-035-65-27"),
    ]

    for name, phone in start_contacts:
        tree.insert(name, phone)

    print("Початкові записи додано до довідника.")
    tree.show_all()

    while True:
        print("\n=== МЕНЮ ТЕЛЕФОННОГО ДОВІДНИКА ===")
        print("1 - Додати запис")
        print("2 - Знайти запис")
        print("3 - Видалити запис")
        print("4 - Показати всі записи")
        print("5 - Вихід")
        choice = input("Ваш вибір: ")

        if choice == "1":
            name = input("Введіть прізвище та ім'я: ")
            phone = input("Введіть номер телефону: ")
            tree.insert(name, phone)
            print("Запис додано.")

        elif choice == "2":
            name = input("Введіть прізвище та ім'я для пошуку: ")
            node = tree.find(name)
            if node:
                print(f"Знайдено: {node.key} -> {node.phone}")
            else:
                print("Такий запис не знайдено.")

        elif choice == "3":
            name = input("Введіть прізвище та ім'я, яке потрібно видалити: ")
            if tree.delete(name):
                print("Запис видалено.")
            else:
                print("Запис з таким прізвищем та ім'ям не знайдено.")

        elif choice == "4":
            tree.show_all()

        elif choice == "5":
            print("Вихід з програми.")
            break

        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()