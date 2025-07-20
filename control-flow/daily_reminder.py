# This code snippet is simple diary reminder program that uses a loop, is statements ans Match-case statements to remind the user about their daily tasks.
# It takes user input for the task and provides appropriate reminders based on the task type.
# it asks the user to tell is the task is time sensitive or not.
# and its priority level

print("Daily Reminder Program")
task = input("Enter your task for today: ").strip()
time_bound = input("Is this task time-sensitive? (yes/no): ").strip().lower()
priority = input("Enter the priority level of the task (high/medium/low): ").strip().lower()
        
        
while True:
    another_task = input("Do you have another task to add? (yes/no): ").strip().lower()
    if another_task == "yes":
        task = input("Enter your task for today: ").strip()
        time_bound = input("Is this task time-sensitive? (yes/no): ").strip().lower()
        priority = input("Enter the priority level of the task (high/medium/low): ").strip().lower()
                
        if time_bound == "yes":
            print(f"Reminder: You have a time-sensitive task: {task}. Please complete it as soon as possible.")
        else:
            print(f"Reminder: You have a non-time-sensitive task: {task}. You can complete it at your convenience.")
                
        match priority:
            case "high":
                 print("This task has high priority. Please address it immediately.")
            case "medium":
                print("This task has medium priority. Please address it soon.")
            case "low":
                print("This task has low priority. You can address it later.")
            case _:
                print("Invalid priority level. Please enter high, medium, or low.")
    elif another_task == "no":
                    print("No more tasks to add. Have a productive day!")
    else:
        print("No more tasks to add. Have a productive day!")
        break

    # commit messages
    # feat: Implemented a daily reminder program with task management
    # refactor: Simplified task input and reminder logic