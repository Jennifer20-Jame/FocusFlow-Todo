FocusFlow 

FocusFlow is a simple and intuitive task management app built with Django and Bootstrap. It helps users create, organize, and track tasks with ease, while providing a clean and responsive interface.

Features Overview

-User Authentication: Secure sign up, login, and logout.
-Task Management: Create, view, edit, and delete tasks.
-Task Categories: Organize tasks into categories (e.g., Work, Personal, School).
-Task Status Tracking: View statistics for Total, Completed, and Pending tasks.
-Dashboard Overview: Get a quick snapshot of your productivity.
-Responsive UI: Works seamlessly on desktop and mobile.

⚙️ Local Setup Instructions

Follow these steps to run the project locally:

-Clone the repository:

git clone https://github.com/Jennifer20-Jame/FocusFlow-Todo.git

cd ToDo_Project


-Create and activate a virtual environment:

python -m venv ToDoenv

-Install dependencies:

pip install -r requirements.txt

-Apply migrations:

python manage.py migrate

-Create a superuser:

python manage.py createsuperuser

-Run the development server:

-python manage.py runserver

Open the app in your browser:

http://127.0.0.1:8000/

Known Issues / Future Improvements

-Notifications: Add reminders for upcoming tasks.
-Calendar Integration: Sync tasks with Google Calendar or Outlook.
-Improved User Dashboard: Show charts/graphs for productivity stats.
-Focus Mode: Allow users to concentrate on one task at a time.
-Unit Tests: Add automated tests for better reliability.