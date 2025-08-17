import matplotlib.pyplot as plt
import matplotlib as mpl
import json
import math
from datetime import datetime

plt.rc('font', family='cmr10',size=12)
mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['mathtext.rm'] = 'serif'
plt.rcParams["axes.formatter.use_mathtext"] = True


gr = (1 + math.sqrt(5)) / 2

# Read Jekyll data file
with open('_data/cycle/temperature-data.json', 'r') as f:
    data = json.load(f)

# Extract and sort data
dates = []
temps = []
for date_str, values in sorted(data.items()):
    dates.append(datetime.strptime(date_str, '%Y-%m-%d'))
    temps.append(values['temperature'])

# Create chart
plt.figure(figsize=(6, 6/gr))
plt.plot(dates, temps, 'o-', color='tab:red', linewidth=2, markersize=6)
#plt.title('Temperature Tracking')
plt.ylabel(r"T ($^{\circ} $C)")
plt.grid(True, alpha=0.3)
plt.xticks(dates, rotation=45)
plt.tight_layout()

# Save to Jekyll assets
plt.savefig('assets/images/cycle/temperature-chart.png', dpi=900, bbox_inches='tight')
plt.close()

print("Chart generated successfully!")