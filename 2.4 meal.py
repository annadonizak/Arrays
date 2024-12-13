"""
prints the weekly meal plan along with the day name as in the example below.
"""
# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
    ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
    ["Pancakes", "Sandwich", "Steak"],
    ["Smoothie", "Chicken Wrap", "Salmon"],
    ["Eggs", "Pasta", "Soup"],
    ["Toast", "Burrito", "Pizza"],
    ["Cereal", "Salad", "Fish Tacos"],
    ["Bagel", "Rice and Beans", "Stir-fry"]
]


# Returns a week day name
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n - 1]


# Returns a string with day meal names
# separated by comma
def day_meal_plan(meal_plan, day_number):
    selected_plan = meal_plan[day_number - 1]
    return f'{weekday(day_number)}: {", ".join(selected_plan)}'


def main():
    print("""WEEKLY MEAL PLAN
(Breakfast, Lunch, Dinner)
==========================""")
    for i in range(1, 8):
        print(day_meal_plan(meal_plan, i))


if __name__ == '__main__':
    main()