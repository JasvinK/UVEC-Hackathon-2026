# Task Treck

Idea of the Hackathon:
- Mental crisis prevention 

What specific mental health:
- Organization: as is it a root cause of many other downstream effects such as stress, anxiety and the feeling of being overwhelmed.

Who specifically are we targeting:
- Students, this could also work for a general audiences
- Those who struggle with self organization

How to run for yourself:
- git clone {repo}
- pip install streamlit 
- python3 -m streamlit run frontend/src/Dashboard.py

How we set about accomplishing this:

Current Features:
- Create custom goals or choose from a list of common goals.
- Categorize goals into School or Personal.
- Track progress for each goal.
- View active goals and progress from the Dashboard.
- View profile information and achievements.
- Light and dark mode support.

- A gamified Goals App that will award points to users for completing tasks they have set out to do.
- Frontend development: Fully streamlit (python library) front end which handles and calls web UI and task management
- Backend development: 
  - The Plan was to have a very in depth tree representation for the goals but unfortunately we ran out of time and used a json file instead for a quick development. you can see the unused code for the tree still in backend/main.py 
  - The goals page saves user goals to a JSON file, and the Dashboard reads from the same file so that newly created goals and progress updates are reflected across the application.

Project Structure:
- frontend/src/Dashboard.py : Main dashboard and activity overview
- frontend/src/pages/1_Goals.py : Goal creation and goal management
- frontend/src/pages/2_Profile.py : Account/profile and achievements
- frontend/src/theme.py : Light and dark theme styling
- backend/main.py : Original Node/tree implementation
- goals.json : Stores goal information used by the frontend

AI Usage
- Some AI was used to help with the styling and format of the front end pages, align column/text, debugging errors, and make website look nice. 
- Overall we tried to use AI as little as possible during our coding, using it to learn rather than implement
- AI was also used to help us understand Streamlit features and Git/GitHub errors during development.


Further implementation if we had more time:
- The points system isn't very robust. It would have been nicer to make it more dynamic and add more "gamified" elements like streaks and highs cores. Some ideas like leaderboards were considered briefly in the design planning phase.
- We thought we could leverage some AI API use to break much larger tasks into smaller, accomplishable goals for users in the design. This would also be good for people who would be Overwhelmed with even starting on how to use the app
- Fully implement the original tree structure so that large goals can be broken into connected subtasks and displayed visually.
- Add the ability to temporarily pause or hide lower-priority goals and remind the user when they want the goal to become active again.
- Improve the profile and achievements system so users can better see their progress over time.
