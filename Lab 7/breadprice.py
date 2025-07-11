import pandas as pd    
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('breadprice.csv')
    df.columns = [col.strip().lower() for col in df.columns]

    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
              'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    
    df[months] = df[months].apply(pd.to_numeric, errors='coerce')

    df['average_price']= df[months].mean(axis=1)

    df = df.sort_values('year')

    plt.figure(figsize=(10,6))
    plt.plot(df['year'],df['average_price'], marker='o', linestyle='-', color='b')
    plt.title('Average Price of Bread by Year')
    plt.xlabel('Year')
    plt.ylabel('Average Price (USD)')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()