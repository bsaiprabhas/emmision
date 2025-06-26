import pandas as pd
import os

# Corrected file path (pointing to Desktop)
df = pd.read_csv(r"C:\Users\bhava\OneDrive\Desktop\Shark_Tank_US_Dataset_Cleaned.csv")

print("------ First 5 Rows ------")
print(df.head())

print("\n------ Data Info ------")
print(df.info())

print("\n------ Missing Values ------")
print(df.isnull().sum())


# Grouping by INDUSTRY (uppercase column name in dataset)
industry_summary = df.groupby('INDUSTRY').agg(
    Total_Pitches=('STARTUP_NAME', 'count'),
    Total_Investment=('TOTAL_DEAL_AMOUNT', 'sum')
).reset_index()

# Sort by total investment
industry_summary = industry_summary.sort_values(by='Total_Investment', ascending=False)

# Display top industries
print("------ Industry-wise Summary ------")
print(industry_summary.head(10))

# Group by PITCHERS_GENDER and calculate deal conversion rate
gender_success = df.groupby('PITCHERS_GENDER').agg(
    Total_Pitches=('STARTUP_NAME', 'count'),
    Deals_Received=('GOT_DEAL', 'sum')
).reset_index()

# Add success rate column
gender_success['Success_Rate (%)'] = (gender_success['Deals_Received'] / gender_success['Total_Pitches']) * 100

# Show results
print("------ Success by Gender ------")
print(gender_success)


# Group by whether there are multiple entrepreneurs
team_success = df.groupby('MULTIPLE_ENTREPRENEURS').agg(
    Total_Pitches=('STARTUP_NAME', 'count'),
    Deals_Received=('GOT_DEAL', 'sum')
).reset_index()

# Add success rate column
team_success['Success_Rate (%)'] = (team_success['Deals_Received'] / team_success['Total_Pitches']) * 100

# Replace NaN or 0/1 with labels
team_success['MULTIPLE_ENTREPRENEURS'] = team_success['MULTIPLE_ENTREPRENEURS'].map({1.0: 'Team', 0.0: 'Solo'})

print("\n------ Success: Solo vs Team ------")
print(team_success)


# Export explicitly to your Desktop folder
df_path = r"C:\Users\bhava\OneDrive\Desktop"

industry_summary.to_csv(os.path.join(df_path, "industry_summary.csv"), index=False)
gender_success.to_csv(os.path.join(df_path, "gender_success.csv"), index=False)
team_success.to_csv(os.path.join(df_path, "team_success.csv"), index=False)

print("✅ Files saved to Desktop.")

