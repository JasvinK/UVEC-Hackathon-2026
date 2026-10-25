roots = []
class Node:
<<<<<<< HEAD

  def __init__(self, id, name, context = "", category = "", timeframe = "", todays_goal = False):
    self.children = []
    self.id = id 
    self.name = name
    self.context = context

  def __init__(self, id, name, context = "", category = "", timeframe = "", todays_goal = False):
=======
  next_id = 0
  def __init__(self, name, context = "", category = "", timeframe = "", todays_goal = False):
    self.id = Node.next_id
    Node.next_id += 1
>>>>>>> 4cb9248f3142eb97bc50b2c74f7c243791b3b412
    self.children = []
    self.parent=None
    self.name = name
    self.context = context
    self.category = category
    self.timeframe = timeframe
    self.todays_goal = todays_goal
    self.completed = False

<<<<<<< HEAD
  class Node:
    def __init__(
        self,
        id,
        name,
        context=None,
        category=None,
        timeframe=None,
        todays_goal=False
    ):
      self.children = []
      self.id = id 
      self.name = name
      self.context = context
      self.category = category
      self.timeframe = timeframe
      self.todays_goal = todays_goal
      self.completed = False

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

=======
  def add_child(self, name, context="", category="",timeframe="", todays_goal=False):
    new_node = Node(name=name, context=context, category=category, timeframe=timeframe, todays_goal=todays_goal)

    new_node.parent = self
    self.children.append(new_node)
    return new_node
>>>>>>> 4cb9248f3142eb97bc50b2c74f7c243791b3b412

  
  def find_node(self, node_id):
      if self.id == node_id:
          return self

      for child in self.children:
          result = child.find_node(node_id)
          if result is not None:
              return result
      return None



  def print_tree(self, level=0):
    print("   " * level + self.name + " " + f"{self.id}")
    for child in self.children:
      child.print_tree(level + 1)


COMMON_GOALS = [
    "Get on top of School",
    "Improve Fitness",
    "Get Organized",
    "Learn a New Hobby"]

def make_sample_goals():
  goal_dict = {}
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


# # Tree 1: School
# school = Node(0, "School")

# # Level 2
# assignment = Node(1, "Complete Assignment")
# midterm = Node(2, "Prepare for Midterm")
# school.add_child(assignment)
# school.add_child(midterm)

# # Level 3
# research = Node(3, "Research Topic")
# writing = Node(4, "Write Report")
# studying = Node(5, "Study Material")

# assignment.add_child(research)
# assignment.add_child(writing)
# midterm.add_child(studying)

# # Level 4
# sources = Node(6, "Find Sources")
# outline = Node(7, "Create Outline")
# notes = Node(8, "Review Notes")

# research.add_child(sources)
# writing.add_child(outline)
# studying.add_child(notes)

# # Level 5
# articles = Node(9, "Read Articles")
# citations = Node(10, "Record Citations")
# sections = Node(11, "Organize Sections")
# practice = Node(12, "Practice Questions")

# sources.add_child(articles)
# sources.add_child(citations)
# outline.add_child(sections)
# notes.add_child(practice)


# # Tree 2: Personal Goals
# personal = Node(13, "Personal Goals")

<<<<<<< HEAD

=======
>>>>>>> 4cb9248f3142eb97bc50b2c74f7c243791b3b412
# # Level 2
# fitness = Node(14, "Improve Fitness")
# organization = Node(15, "Get Organized")
# hobby = Node(16, "Learn a New Hobby")


# fitness.add_child()

# personal.add_child(fitness)
# personal.add_child(organization)
# personal.add_child(hobby)

# # Level 3
# exercise = Node(17, "Exercise Regularly")
# planning = Node(18, "Plan Weekly Tasks")
# learning = Node(19, "Learn Basics")

# fitness.add_child(exercise)
# organization.add_child(planning)
# hobby.add_child(learning)

# # Level 4
# routine = Node(20, "Create Exercise Routine")
# schedule = Node(21, "Create Schedule")
# tutorials = Node(22, "Follow Tutorials")

# exercise.add_child(routine)
# planning.add_child(schedule)
# learning.add_child(tutorials)

# # Level 5
# workouts = Node(23, "Choose Workouts")
# calendar = Node(24, "Add Tasks to Calendar")
# practice_hobby = Node(25, "Practice Skills")

# routine.add_child(workouts)
# schedule.add_child(calendar)
# tutorials.add_child(practice_hobby)

# print("Tree 1: School")
# school.PrintTree()

# print("Tree 2: Personal Goals")
# personal.PrintTree()
<<<<<<< HEAD

print("Tree 2: Personal Goals")
personal.PrintTree()

# Add all nodes in the tree to the nodes dict
def register_tree(node):
    nodes[node.id] = node

    for child in node.children:
        register_tree(child)

# add the roots to root list and each node to the dict of nodes
roots.append(school)
roots.append(personal)
register_tree(school)
register_tree(personal)

=======
>>>>>>> 4cb9248f3142eb97bc50b2c74f7c243791b3b412
