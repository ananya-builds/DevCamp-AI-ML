import pandas as pd
def load_data(filename):
    data_frame = pd.read_csv(filename, parse_dates=['date'])
    return data_frame
def calculate_averages(df):
    daily_avg=df.mean(numeric_only=True)
    return daily_avg
def best_and_worst_days(df):
    best = df.loc[df['steps'].idxmax()]
    worst = df.loc[df['steps'].idxmin()]
    return best, worst
def identify_trend(df):
    if len(df) >= 14:
        if df['steps'].iloc[-7:].mean() > df['steps'].iloc[:7].mean():
            return "You are walking more than before. Great!"
        else:
            return "Your steps have decreased. Try to stay active."
    else:
        return "Not enough data to check trend."
def generate_report(avg, best, worst, trend):
    report = f"""
===== Personal Fitness Data Analysis =====

Average Steps: {avg['steps']:.0f}
Average Distance (Km): {avg['distance_km']:.2f}
Average Sleep Hours: {avg['sleep_hours']:.1f}

Best Day: {best['date'].date()} with {best['steps']} steps
Worst Day: {worst['date'].date()} with {worst['steps']} steps

Trend: {trend}
"""
    return report

filename = "Dataset.csv"
df = load_data(filename)
daily_avg = calculate_averages(df)
best, worst = best_and_worst_days(df)
trend = identify_trend(df)
report = generate_report(daily_avg, best, worst, trend)
print(report)
#Saving report to a text file.
with open("fitness_report.txt", "w") as f:
    f.write(report)
print("Report saved as fitness_report.txt")