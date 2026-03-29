import uuid
import datetime
class Habit():

    def __init__(self, name, frequency, category):
        self.name = name
        self.frequency = frequency
        self.category = category

        self.generated_habit = []


    def generate_habit(self):
        habit_entry  = {
            'habit_id': f"HABIT{uuid.uuid4().hex[:6].upper()}",
            'habit_name': self.name,
            'habit_frequency': self.frequency,
            'habit_category': self.category,
            'habit_complete': False,
            'date': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        self.generated_habit.append(habit_entry)
        return habit_entry

    def mark_habit(self):
        for habit in self.generated_habit:
            if habit['habit_name'] == self.name:
                habit['habit_complete'] = True
                return habit

    def check_habit(self):
        for habit in self.generated_habit:
            if habit['habit_name'] == self.name:
                if habit['habit_complete']:
                    print("Habit completed")
                else:
                    print("Habit not completed")
                return habit

        print("Habit not found")
        return None

    def calculate_streak(self):
        completed_dates = []

        for habit in self.generated_habit:
            if habit['habit_complete']:
                completed_dates.append(
                    datetime.datetime.strptime((habit['date']), "%d/%m/%Y %H:%M:%S").date()
                )
        if not completed_dates:
            return 0

        completed_dates.sort(reverse=True)

        streak = 1
        today = datetime.date.today()

        if completed_dates[0] != today and completed_dates[0] != today - datetime.timedelta(days=1):
            return 0

        for i in range(len(completed_dates) -1):
            if completed_dates[i] != completed_dates[i+1] - datetime.timedelta(days=1):
                streak += 1
            else:
                break

        return streak

    def __str__(self):
        return f"Habit: {self.name} | Frequency: {self.frequency} | Category: {self.category} | Streak: {self.calculate_streak()} | Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"

    def __repr__(self):
        return f"Habit(name='{self.name}', frequency='{self.frequency}', category='{self.category}',Streak: {self.calculate_streak()}, date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')})"





habit = Habit("Workout", "Daily", "Health")

habit.generate_habit()
habit.mark_habit()

print("Streak:", habit.calculate_streak())
print(habit)        # uses __str__
print(repr(habit))  # u