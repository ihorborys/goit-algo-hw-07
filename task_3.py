class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def sum_tree(root):
    # Якщо дерево порожнє, сума дорівнює 0
    if root is None:
        return 0

    # Рекурсивно обчислюємо суму для лівого і правого піддерев
    left_sum = sum_tree(root.left)
    right_sum = sum_tree(root.right)

    # Повертаємо суму значення поточного вузла і піддерев
    return root.key + left_sum + right_sum

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

# Обчислюємо суму всіх елементів
total_sum = sum_tree(root)
print("Сума всіх значень у дереві:", total_sum)