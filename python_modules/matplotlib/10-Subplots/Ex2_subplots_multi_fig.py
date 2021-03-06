import pandas as pd
from matplotlib import pyplot as plt

# print(plt.style.available)
plt.style.use('seaborn')

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

data = pd.read_csv('data.csv')
ages_x = data['Age']
dev_y = data['All_Devs']
py_dev_y = data['Python']
js_dev_y = data['JavaScript']

ax1.plot(ages_x, py_dev_y, label='Python')

ax1.plot(ages_x, js_dev_y, label='Java Script')

ax2.plot(ages_x, dev_y, color = 'k', linestyle='--', label='All Devs')

ax1.set_title('Median Salary (USD) by Age')
ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')
ax1.legend()

ax2.set_title('Median Salary (USD) by Age')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')
ax2.legend()

plt.tight_layout()
fig1.savefig('png1.png')
fig2.savefig('png2.png')
plt.show()
