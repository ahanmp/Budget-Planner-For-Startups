from pprint import pprint

def generate_insights(forecast_df):
    # Extracting the last 6 rows of the forecast data for each department
    latest = forecast_df.tail(6)

    # Initialize a dictionary to store the average predicted expense for each department
    average_expenses = {}

    # Looping through each department and calculating the average predicted expense
    departments = ['Data Science', 'Marketing', 'Salaries', 'Operations']

    for department in departments:
        avg_expense = latest[department].mean()
        average_expenses[department] = round(avg_expense, 2)

    # Generate recommendations based on the average expenses for each department
    recommendations = []

    for department, avg_expense in average_expenses.items():
        if avg_expense > 180000:
            recommendations.append(f"🔺 {department} expenses are high (Avg: ₹{avg_expense}). Consider reviewing budget allocations.")
        else:
            recommendations.append(f"✅ {department} expenses are under control (Avg: ₹{avg_expense}). Maintain current strategy.")

    # Pretty formatted output
    print("\n📊 Average Predicted Expenses:")
    for dept, expense in average_expenses.items():
        print(f"   • {dept}: ₹{expense}")

    print("\n📝 Recommendations:")
    for rec in recommendations:
        print(f"   - {rec}")

    # Returning the data in case further processing is needed
    return {
        "average_predicted_expenses": average_expenses,
        "recommendations": recommendations
    }

# Sample DataFrame
import pandas as pd

data = {
    'Data Science': [190000, 195000, 200000, 180000, 185000, 192000],
    'Marketing': [150000, 145000, 155000, 140000, 152000, 148000],
    'Salaries': [200000, 210000, 190000, 180000, 195000, 205000],
    'Operations': [170000, 175000, 160000, 165000, 155000, 160000]
}

forecast_df = pd.DataFrame(data)

# Generate and display insights
generate_insights(forecast_df)
