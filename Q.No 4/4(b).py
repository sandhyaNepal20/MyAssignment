
# b)
# You are provided with balanced binary tree with the target value k. return x number of values that are closest to the
# given target k. provide solution in O(n)
# Note: You have only one set of unique values x in binary search tree that are closest to the target.
# Input:
# K=3.8
# x=2
# Output: 4,5





class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_closest_values(root, k, x):
    result = []

    # Helper function to perform inorder traversal and update the result list
    def inorder(node):
        if not node:
            return

        inorder(node.left)
        if len(result) < x:
            result.append(node.val)
        elif abs(node.val - k) < abs(result[0] - k):
            result.pop(0)
            result.append(node.val)
        else:
            return
        inorder(node.right)

    inorder(root)
    return result


# Example usage:
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)


k = 3.8
x = 2
print(find_closest_values(root, k, x))