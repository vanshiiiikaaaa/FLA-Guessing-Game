import json

class DecisionTree:
    class TreeNode:
        def __init__(self, data, yes_link=None, no_link=None):
            self.data = data
            self.yes_link = yes_link
            self.no_link = no_link

    def __init__(self, data_file):
        self.root = None
        self.nodes = {}
        self.title, self.help_info, self.root = self.build_binary_tree(data_file)

    def build_binary_tree(self, data_file):
        with open(data_file, "r") as file:
            data = json.load(file)

            self.title = data['title']
            self.help_info = data['help_info']
            self.root = self.build_tree_node(data['root'])

        return self.title, self.help_info, self.root

    def build_tree_node(self, node_data):
        if isinstance(node_data, str):
            return self.TreeNode(node_data)

        node = self.TreeNode(node_data['question'])
        self.nodes[node_data['node_num']] = node

        if node_data['l'] is not None:
            node.yes_link = self.build_tree_node(node_data['l'])

        if node_data['r'] is not None:
            node.no_link = self.build_tree_node(node_data['r'])

        return node

    def play_game(self):
        current_node = self.root
        while True:
            print(current_node.data)
            if current_node.yes_link is None and current_node.no_link is None:
                break
                print("The answer is found.")
            answer = input("Your choice (Y/N): ").strip().lower()
            while answer not in ["y", "yes", "n", "no"]:
                answer = input("Please enter a valid choice (Y/N): ").strip().lower()
            if answer in ["y", "yes"]:
                current_node = current_node.yes_link
            else:
                current_node = current_node.no_link

    def display_tree(self):
        while True:
            print("What order do you want to display?")
            print("1. Inorder")
            print("2. Preorder")
            print("3. Postorder")
            print("4. Return to main menu")
            choice = input("Your choice: ").strip()

            if choice == "1":
                print("Inorder Traversal:")
                self.inorder_traversal(self.root)
            elif choice == "2":
                print("Preorder Traversal:")
                self.preorder_traversal(self.root)
            elif choice == "3":
                print("Postorder Traversal:")
                self.postorder_traversal(self.root)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.yes_link)
            print(node.data)
            self.inorder_traversal(node.no_link)

    def preorder_traversal(self, node):
        if node is not None:
            print(node.data)
            self.preorder_traversal(node.yes_link)
            self.preorder_traversal(node.no_link)

    def postorder_traversal(self, node):
        if node is not None:
            self.postorder_traversal(node.yes_link)
            self.postorder_traversal(node.no_link)
            print(node.data)

if __name__ == "__main__":
    game_file = "game1.txt"
    decision_tree = DecisionTree(game_file)

    while True:
        print(decision_tree.title)
        print("P: Play the game")
        print("L: Load another game file")
        print("D: Display the binary tree")
        print("H: Help information")
        print("X: Exit the program")

        choice = input("Your choice: ").strip().lower()

        if choice == "p":
            decision_tree.play_game()
        elif choice == "l":
            new_game_file = input("Enter the name of the new game file: ")
            decision_tree = DecisionTree(new_game_file)
        elif choice == "d":
            decision_tree.display_tree()
        elif choice == "h":
            print(decision_tree.help_info)
        elif choice == "x":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
