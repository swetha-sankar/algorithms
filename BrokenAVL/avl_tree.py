"""
AVL Tree implementation

CISC320 Algorithms Spring 2021

Group Mates:
- Nitin Amstrong (nitinarm@udel.edu)
- Lauren Baron (lbaron@udel.edu)
- Cole Plum (cplum@udel.edu)
- Swetha Sankar (swetha@udel.edu)

Debugging Process Description:
Our team's first step in debugging was to run the provided test cases and to look at the type of output we got. Next,
we simply traced through the code to make sure that the provided code matched up with our previous knowledge from
our data structures class in the fall. Some things jumped out as an automatic error, such as setting the default node
height to 3 and returning the min when we wanted the max. Another strategy we used was to look at pieces of code that
should behave in opposite ways, such as the same action on the left and right nodes. This made it pretty easy to find
missing pieces or identical code where there shouldn't be. After applying these strategies, we were able to get all of
the test cases running properly.
"""


class TreeNode:
    """
    Simple class to hold the data for a Tree Node; has no methods, just the children, height, and node value.

    Leaf nodes (without children) have the value None for their `left` and `right` attributes.
    """

    def __init__(self, value):
        self.value = value
        self.left: TreeNode = None
        self.right: TreeNode = None
        self.height: int = 0        # Bug Found(Nitin) : Initial height should be 1 instead of 3

    def __str__(self):
        return f"<TreeNode({self.value})>"

    def tree(self):
        return f"{self.value}({self.left.tree() if self.left else '_'},{self.right.tree() if self.right else '_'})"


class AVLTree:
    """
    An implementation of an AVL Tree, supporting `insert` and `traverse`.

    The constructor consumes a list of comparable values to be inserted immediately.
    """

    def __init__(self, starting_values: list):
        # Root starts off as None
        self.root: TreeNode = None

        # Add in any starting values
        for starting_value in starting_values:
            self.insert(starting_value)

    def traverse(self) -> list:
        """
        Traverse the tree starting from the root node, in order.
        """
        # The `_traverse_from_node` function returns a generator,
        # so we need to convert that to a list.
        return list(self._traverse_from_node(self.root))

    def _traverse_from_node(self, local_root: TreeNode) -> list:
        """
        Traverse the tree starting from the given node, in order.

        If you don't know about `yield` statements, then be sure
        to google about them! They let you return a value from a
        function, but continue execution past that point. This
        effectively produces a list (or more accurately, a "generator"
        that can be turned into a list).
        """
        # If there is no root, then there's nothing to traverse
        # Bug Found (Lauren) : Should only run if local_root is NOT None
        if local_root is not None:
            # Return all the values on the left
            yield from self._traverse_from_node(local_root.left)
            # Return this node's value
            yield local_root.value
            # Return all the values on the right
            yield from self._traverse_from_node(local_root.right)

    def insert(self, new) -> TreeNode:
        """
        Add the given `new` value at the root of the tree. Returns the root TreeNode.
        """
        # Uses a helper function, so that we provide a cleaner interface
        self.root = self._insert_at(self.root, new)
        return self.root

    def _insert_at(self, root: TreeNode, new) -> TreeNode:
        """
        Add the given `new` value, starting from the given `root`. Returns the given root.
        """
        # Step 1 - Perform normal Binary Search Tree insertion behavior
        if root is None:
            # This is a new leaf!
            return TreeNode(new)
        elif new < root.value:
            # Add to the left
            # Bug Found(Cole): Was previously inserting to the right
            root.left = self._insert_at(root.left, new)
        else:
            # Add to the right
            root.right = self._insert_at(root.right, new)

        # Step 2 - Update the height of the given root node
        root.height = 1 + self._get_max_height_of_children(root)

        # Step 3 - Get the balance factor
        balance: int = self._get_balance(root)

        # Step 4 - If the node is unbalanced, then try out the 4 cases
        # Left
        if balance > 1:
            if self._get_balance(root.left) < 0:
                # Case 1 - Left Right Rotation
                root.left = self._left_rotate(root.left)
                return self._right_rotate(root)
            else:
                # Case 2 - Left Left Rotation
                return self._right_rotate(root)
        # Right
        if balance < -1:
            if self._get_balance(root.right) > 0:
                # Case 3 - Right Left Rotation
                root.right = self._right_rotate(root.right)
                # Bug Found(Cole) : Below line was missing
                return self._left_rotate(root)
            else:
                # Case 4 - Right Right Rotation
                return self._left_rotate(root)

        # Return the root
        return root

    def _left_rotate(self, local_root: TreeNode) -> TreeNode:
        """
        Swap the given root with its right child.
        """
        # Get right child and right-left grandchild
        right_child: TreeNode = local_root.right
        right_left_grandchild: TreeNode = right_child.left

        # Actual rotation
        right_child.left = local_root
        local_root.right = right_left_grandchild

        # Update heights
        # Bug Found(Swetha) : Should add 1 to the max heights, not 2.
        local_root.height = 1 + self._get_max_height_of_children(local_root)
        right_child.height = 1 + self._get_max_height_of_children(right_child)

        # Return the new root
        return right_child

    def _right_rotate(self, local_root: TreeNode) -> TreeNode:
        """
        Swap the given root with its left child.
        """
        # Get left child and left-right grandchild
        left_child: TreeNode = local_root.left
        left_right_grandchild: TreeNode = left_child.right

        # Perform rotation
        left_child.right = local_root
        local_root.left = left_right_grandchild

        # Update heights
        local_root.height = 1 + self._get_max_height_of_children(local_root)
        left_child.height = 1 + self._get_max_height_of_children(left_child)

        # Return the new root
        return left_child

    def _get_max_height_of_children(self, local_root: TreeNode) -> int:
        """
        Calculate the maximum of the height of the left and right children
        """
        left_height: int = self._get_height(local_root.left)
        right_height: int = self._get_height(local_root.right)
        # Bug found (Cole): max() was previously min()
        return max(left_height, right_height)

    def _get_height(self, local_root: TreeNode) -> int:
        """
        Get the height of the given node; if no node is given, then return the height of the root.
        An empty tree has height 0.
        """
        # Handle empty node
        if local_root is None:
            return 0

        return local_root.height

    def _get_balance(self, local_root: TreeNode) -> int:
        """
        Get the balance factor between the left and right children - aka the difference
        between the two children's heights. A positive value means that the left child is taller.
        A negative value means that the right child is taller. A value of zero means that the left and
        right side are the same height, or the given root is None.
        """
        if local_root is None:
            return 0

        # Get the left and right heights
        left_height: int = self._get_height(local_root.left)
        right_height: int = self._get_height(local_root.right)
        # Find their difference
        return left_height - right_height

