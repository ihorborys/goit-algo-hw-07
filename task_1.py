class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_max_value(root):
    # Перевірка на порожнє дерево
    if root is None:
        return None

    # Рухаємося по правому піддереву до кінця
    current_node = root
    while current_node.right is not None:
        current_node = current_node.right

    return current_node.key

# Створимо просте двійкове дерево пошуку:
#          20
#         /  \
#       10    30
#            /  \
#          25    40

root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.right.left = TreeNode(25)
root.right.right = TreeNode(40)

# Знаходимо найбільший елемент
max_value = find_max_value(root)
print("Найбільше значення в дереві:", max_value)