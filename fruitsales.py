# add your code here
import pandas as pd
import matplotlib.pyplot as plt

fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'],
                index=['2017 Sales', '2018 Sales'])

print(fruit_sales)

fruit_sales.to_csv('fruit.csv')

# Wanted to try some different featurees
fruit_sales.plot(kind='bar')
plt.ylabel('Quantity')
plt.title('Fruit Sales')
plt.show()