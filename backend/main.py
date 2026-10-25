nodes = {}
roots = []

class Node:
<<<<<<< HEAD
  def __init__(self, id, name, context = "", category = "", timeframe = "", todays_goal = False):
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
=======
    def __init__(self, id, name, context="", category="Personal", timeframe="Short Term", todays_goal=False, percent_completed=0):
      self.id = id 
      self.name = name
      self.children = []
      self.parent = None
      self.context = context
      self.category = category
      self.timeframe = timeframe
      self.todays_goal = todays_goal
      self.percent_completed = percent_completed

    def add_child(self, child):
        self.children.append(child)
        child.parent = self
>>>>>>> 11a895e0be722d480dffd5871654b2f66fe0abd2

  def PrintTree(self, level=0):
    print("   " * level + self.name + " " + f"{self.id}")
    for child in self.children:
      child.PrintTree(level + 1)

def add_task(name, parent_id=None, context="", category="", timeframe="", todays_goal=False):
  new_id = max(nodes.keys(), default=-1) + 1
  new_node = Node(id=new_id, name=name, context=context, category="", timeframe=timeframe, todays_goal=todays_goal)
  if parent_id is None:
    roots.append(new_node)
  else:
    if parent_id not in nodes:
      raise ValueError("Error, parent does not exist")
    parent = nodes[parent_id]
    parent.add_child(new_node)
  nodes[new_id] = new_node
  return new_node


COMMON_GOALS = [
    "Get on top of School",
    "Improve Fitness",
    "Get Organized",
    "Learn a New Hobby"]

def make_sample_goals():
  goal_dict = {}
  school_goal = Node(0, "School")
  fitness_goal = Node(1, "Fitness")
  organization_goal = Node(2, "Organized")
  personal_hobby_goal = Node(3, "Hobby")

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
=======
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
>>>>>>> 11a895e0be722d480dffd5871654b2f66fe0abd2
