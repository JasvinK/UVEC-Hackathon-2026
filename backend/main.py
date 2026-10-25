

class Node:
    def __init__(self, id, name, context, category, timeframe, todays_goal):
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

    def PrintTree(self, level=0):
      print("   " * level + self.name + " " + f"{self.id}")
      for child in self.children:
        child.PrintTree(level + 1)


# Tree 1: School
school = Node(0, "School")

# Level 2
assignment = Node(1, "Complete Assignment")
midterm = Node(2, "Prepare for Midterm")
school.add_child(assignment)
school.add_child(midterm)

# Level 3
research = Node(3, "Research Topic")
writing = Node(4, "Write Report")
studying = Node(5, "Study Material")

assignment.add_child(research)
assignment.add_child(writing)
midterm.add_child(studying)

# Level 4
sources = Node(6, "Find Sources")
outline = Node(7, "Create Outline")
notes = Node(8, "Review Notes")

research.add_child(sources)
writing.add_child(outline)
studying.add_child(notes)

# Level 5
articles = Node(9, "Read Articles")
citations = Node(10, "Record Citations")
sections = Node(11, "Organize Sections")
practice = Node(12, "Practice Questions")

sources.add_child(articles)
sources.add_child(citations)
outline.add_child(sections)
notes.add_child(practice)


# Tree 2: Personal Goals
personal = Node(13, "Personal Goals")

# Level 2
fitness = Node(14, "Improve Fitness")
organization = Node(15, "Get Organized")
hobby = Node(16, "Learn a New Hobby")

personal.add_child(fitness)
personal.add_child(organization)
personal.add_child(hobby)

# Level 3
exercise = Node(17, "Exercise Regularly")
planning = Node(18, "Plan Weekly Tasks")
learning = Node(19, "Learn Basics")

fitness.add_child(exercise)
organization.add_child(planning)
hobby.add_child(learning)

# Level 4
routine = Node(20, "Create Exercise Routine")
schedule = Node(21, "Create Schedule")
tutorials = Node(22, "Follow Tutorials")

exercise.add_child(routine)
planning.add_child(schedule)
learning.add_child(tutorials)

# Level 5
workouts = Node(23, "Choose Workouts")
calendar = Node(24, "Add Tasks to Calendar")
practice_hobby = Node(25, "Practice Skills")

routine.add_child(workouts)
schedule.add_child(calendar)
tutorials.add_child(practice_hobby)

print("Tree 1: School")
school.PrintTree()

print("Tree 2: Personal Goals")
personal.PrintTree()
