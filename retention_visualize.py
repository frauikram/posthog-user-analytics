import pandas as pdtree
import seaborn as sns
import matplotlib.pyplot as plt


# Simulated cohort data
data = {
    'signup_week': ['2024-01-01', '2024-01-01', '2024-01-01', '2024-01-08', '2024-01-08'],
    'activity_week': ['2024-01-01', '2024-01-08', '2024-01-15', '2024-01-08', '2024-01-15'],
    'retained_users': [100, 60, 30, 80, 40]
}
df = pd.DataFrame(data)
df['signup_week'] = pd.to_datetime(df['signup_week'])
df['activity_week'] = pd.to_datetime(df['activity_week'])

# Calculate cohort index
df['cohort_week'] = ((df['activity_week'] - df['signup_week']) / pd.Timedelta(weeks=1)).astype(int)

# Pivot table for heatmap
cohort_pivot = df.pivot_table(
    index='signup_week',
    columns='cohort_week',
    values='retained_users',
    fill_value=0
)

# Plotting
plt.figure(figsize=(10, 6))
ax = sns.heatmap(cohort_pivot, annot=True, fmt='d', cmap='YlGnBu')

# Clean up timestamp labels on the Y-axis (signup_week)
ax.set_yticklabels([d.strftime('%Y-%m-%d') for d in cohort_pivot.index])

plt.title('User Retention Cohort Heatmap')
plt.xlabel('Weeks Since Signup')
plt.ylabel('Signup Week')
plt.tight_layout()

# Save
heatmap_path = 'outputs/retention_heatmap_cleaned.png'
plt.savefig(heatmap_path)
heatmap_path
