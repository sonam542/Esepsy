import matplotlib.pyplot as plt
import numpy as np

# Data
dates = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
minutes = [5, 15, 60, 25, 45, 5, 5]  # Sample weekly data (adjust as needed)

# Colors to mimic the Forest app
colors = ['#a8e6cf', '#81c784', '#66bb6a', '#a5d6a7', '#8bc34a', '#aed581', '#c8e6c9']

# Create figure
fig, ax = plt.subplots(figsize=(10, 6), facecolor='#16261f')
ax.set_facecolor('#16261f')

# Plot bars with glow-style effect
bars = ax.bar(dates, minutes, color=colors, width=0.6, zorder=3)

# Display total time
total_minutes = sum(minutes)
ax.text(0.5, -0.15, f'{total_minutes//60} day {total_minutes%60} hour 0 mins',
        transform=ax.transAxes, ha='center', fontsize=12, color='white', alpha=0.9)

# Display date range
ax.text(0.5, -0.22, '2025 Mar 10 - Mar 16', transform=ax.transAxes,
        ha='center', fontsize=10, color='lightgray', alpha=0.7)

# Remove spines and ticks
for spine in ax.spines.values():
    spine.set_visible(False)
ax.tick_params(left=False, bottom=False, labelcolor='white')

# Add grid
ax.yaxis.grid(True, linestyle=':', alpha=0.2)
ax.set_axisbelow(True)
ax.set_title('🌱 Focus Time This Week', color='white', pad=20)

# Set Y axis limit and labels
ax.set_ylim(0, max(minutes) + 10)
ax.set_ylabel('Minutes', color='white')

plt.tight_layout()
plt.show()
