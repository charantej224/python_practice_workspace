import pandas as pd
import matplotlib.pyplot as plt

input_data = 'regular_output'
df = pd.read_csv(input_data + '.txt')
ax = plt.subplot(111)
ax.bar(df['class_name'], df['mAP score'], width=0.5, color='b', align='center')

plt.show()
plt.savefig(input_data+'.png')
