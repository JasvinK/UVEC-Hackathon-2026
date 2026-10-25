roots = []


class Node:
    # Automatically gives each new node a unique ID
    next_id = 0

    def __init__(
        self,
        name,
        context="",
        category="",
        timeframe="",
        todays_goal=False
    ):
        # Automatically assign an ID
        self.id = Node.next_id
        Node.next_id += 1

        # Node information
        self.children = []
        self.parent = None
        self.name = name
        self.context = context
        self.category = category
        self.timeframe = timeframe
        self.todays_goal = todays_goal
        self.completed = False

    # Creates a child node and adds it to this node
    def add_child(
        self,
        name,
        context="",
        category="",
        timeframe="",
        todays_goal=False
    ):
        new_node = Node(
            name=name,
            context=context,
            category=category,
            timeframe=timeframe,
            todays_goal=todays_goal
        )

        new_node.parent = self
        self.children.append(new_node)

        return new_node

    # Searches the tree for a node with a specific ID
    def find_node(self, node_id):
        if self.id == node_id:
            return self

        for child in self.children:
            result = child.find_node(node_id)

            if result is not None:
                return result

        return None

    # Prints the tree structure in the terminal
    def print_tree(self, level=0):
        print("   " * level + self.name + " " + f"{self.id}")

        for child in self.children:
            child.print_tree(level + 1)


# Common goals that can be shown in the frontend
COMMON_GOALS = [
    "Get on top of School",
    "Improve Fitness",
    "Get Organized",
    "Learn a New Hobby"
]


# Creates sample goal nodes for the common goals
def make_sample_goals():

    school_goal = Node("School")
    fitness_goal = Node("Fitness")
    organization_goal = Node("Organized")
    personal_hobby_goal = Node("Hobby")

    goal_dict = {
        "Get on top of School": school_goal,
        "Improve Fitness": fitness_goal,
        "Get Organized": organization_goal,
        "Learn a New Hobby": personal_hobby_goal,
    }

    return goal_dict