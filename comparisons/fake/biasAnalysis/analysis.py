import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from scipy.stats import f_oneway
from itertools import combinations

dfleft = pd.read_csv("leftWingFake.csv", encoding="ISO-8859-1")
orig_per_word_left = dfleft["avg_sentiment_per_word"]
temp0_per_word_left = dfleft["avg_gen_sentiment_per_word_temp0"]
temp05_per_word_left = dfleft["avg_gen_sentiment_per_word_temp0.5"]
temp1_per_word_left = dfleft["avg_gen_sentiment_per_word_temp1"]

dfright = pd.read_csv("rightWingFake.csv", encoding="ISO-8859-1")
orig_per_word_right = dfright["avg_sentiment_per_word"]
temp0_per_word_right = dfright["avg_gen_sentiment_per_word_temp0"]
temp05_per_word_right = dfright["avg_gen_sentiment_per_word_temp0.5"]
temp1_per_word_right = dfright["avg_gen_sentiment_per_word_temp1"]

def plot_histogram_left():  
    plt.figure(figsize=(10, 6))
    sns.histplot(orig_per_word_left, bins=30, kde=False, color='blue', label='Original Sentiment', alpha=0.6)
    sns.histplot(temp0_per_word_left, bins=30, kde=False, color='orange', label='Temp0 Sentiment', alpha=0.6)
    sns.histplot(temp05_per_word_left, bins=30, kde=False, color='green', label='Temp0.5 Sentiment', alpha=0.6)
    sns.histplot(temp1_per_word_left, bins=30, kde=False, color='red', label='Temp1 Sentiment', alpha=0.6)
    
    plt.title('Histogram of Sentiment per Word (Different Temperatures)', fontsize=16)
    plt.xlabel('Sentiment Value', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    
def plot_histogram_right():  
    plt.figure(figsize=(10, 6))
    sns.histplot(orig_per_word_right, bins=30, kde=False, color='blue', label='Original Sentiment', alpha=0.6)
    sns.histplot(temp0_per_word_right, bins=30, kde=False, color='orange', label='Temp0 Sentiment', alpha=0.6)
    sns.histplot(temp05_per_word_right, bins=30, kde=False, color='green', label='Temp0.5 Sentiment', alpha=0.6)
    sns.histplot(temp1_per_word_right, bins=30, kde=False, color='red', label='Temp1 Sentiment', alpha=0.6)
    
    plt.title('Histogram of Sentiment per Word (Different Temperatures)', fontsize=16)
    plt.xlabel('Sentiment Value', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    
def plot_density_left():
    plt.figure(figsize=(10, 6))
    sns.kdeplot(orig_per_word_left, color='blue', label='Original Sentiment', linewidth=2)
    sns.kdeplot(temp0_per_word_left, color='orange', label='Temp0 Sentiment', linewidth=2)
    sns.kdeplot(temp05_per_word_left, color='green', label='Temp0.5 Sentiment', linewidth=2)
    sns.kdeplot(temp1_per_word_left, color='red', label='Temp1 Sentiment', linewidth=2)

    plt.title('Density Plot of Sentiment per Word (Different Temperatures)', fontsize=16)
    plt.xlabel('Sentiment Value', fontsize=14)
    plt.ylabel('Density', fontsize=14)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    
def plot_density_right():
    plt.figure(figsize=(10, 6))
    sns.kdeplot(orig_per_word_right, color='blue', label='Original Sentiment', linewidth=2)
    sns.kdeplot(temp0_per_word_right, color='orange', label='Temp0 Sentiment', linewidth=2)
    sns.kdeplot(temp05_per_word_right, color='green', label='Temp0.5 Sentiment', linewidth=2)
    sns.kdeplot(temp1_per_word_right, color='red', label='Temp1 Sentiment', linewidth=2)

    plt.title('Density Plot of Sentiment per Word (Different Temperatures)', fontsize=16)
    plt.xlabel('Sentiment Value', fontsize=14)
    plt.ylabel('Density', fontsize=14)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def plot_boxplot_left():
    boxplot_data = pd.DataFrame({
        'Original': orig_per_word_left,
        'Temp0': temp0_per_word_left,
        'Temp0.5': temp05_per_word_left,
        'Temp1': temp1_per_word_left
    })
    boxplot_data_long = boxplot_data.melt(var_name='Temperature', value_name='Sentiment')

    plt.figure(figsize=(10, 6))
    sns.boxplot(data=boxplot_data_long, x='Temperature', y='Sentiment', palette='Set2')

    plt.title('Boxplot of Sentiment per Word (Different Temperatures)', fontsize=16)
    plt.xlabel('Temperature', fontsize=14)
    plt.ylabel('Sentiment Value', fontsize=14)
    plt.show()
    
def plot_boxplot_right():
    boxplot_data = pd.DataFrame({
        'Original': orig_per_word_right,
        'Temp0': temp0_per_word_right,
        'Temp0.5': temp05_per_word_right,
        'Temp1': temp1_per_word_right
    })
    boxplot_data_long = boxplot_data.melt(var_name='Temperature', value_name='Sentiment')

    plt.figure(figsize=(10, 6))
    sns.boxplot(data=boxplot_data_long, x='Temperature', y='Sentiment', palette='Set2')

    plt.title('Boxplot of Sentiment per Word (Different Temperatures)', fontsize=16)
    plt.xlabel('Temperature', fontsize=14)
    plt.ylabel('Sentiment Value', fontsize=14)
    plt.show()
    
#plot_histogram_left()
#plot_density_left()    
#plot_boxplot_left()

#plot_histogram_right()
#plot_density_right()    
#plot_boxplot_right()

#Test Normality

def plot_QQ_left():
    data_list = [orig_per_word_left, temp0_per_word_left, temp05_per_word_left, temp1_per_word_left]
    labels = ["Original", "Temp0", "Temp0.5", "Temp1"]

    # Create subplots
    plt.figure(figsize=(12, 10))
    for i, (data, label) in enumerate(zip(data_list, labels), start=1):
        plt.subplot(2, 2, i)  # 2x2 grid of subplots
        stats.probplot(data, dist="norm", plot=plt)
        plt.title(f"Q-Q Plot: {label}")

    plt.tight_layout()  # Adjust spacing between plots
    plt.show()

def plot_QQ_right():
    data_list = [orig_per_word_right, temp0_per_word_right, temp05_per_word_right, temp1_per_word_right]
    labels = ["Original", "Temp0", "Temp0.5", "Temp1"]

    # Create subplots
    plt.figure(figsize=(12, 10))
    for i, (data, label) in enumerate(zip(data_list, labels), start=1):
        plt.subplot(2, 2, i)  # 2x2 grid of subplots
        stats.probplot(data, dist="norm", plot=plt)
        plt.title(f"Q-Q Plot: {label}")

    plt.tight_layout()  # Adjust spacing between plots
    plt.show()
    

#plot_QQ_left()
#plot_QQ_right()

def anova():
    diff_temp0_left = dfleft['diff_sentiment_temp0'].dropna()
    diff_temp05_left = dfleft['diff_sentiment_temp0.5'].dropna()
    diff_temp1_left = dfleft['diff_sentiment_temp1'].dropna()
    
    diff_temp0_right = dfright['diff_sentiment_temp0'].dropna()
    diff_temp05_right = dfright['diff_sentiment_temp0.5'].dropna()
    diff_temp1_right = dfright['diff_sentiment_temp1'].dropna()

    left_data = [diff_temp0_left, diff_temp05_left, diff_temp1_left]
    right_data = [diff_temp0_right, diff_temp05_right, diff_temp1_right]
    
    all_data = []
    labels = []
    
    for i, (left, right) in enumerate(zip(left_data, right_data)):
        # Combine left and right data for each time point
        all_data.append(left)
        all_data.append(right)
        
        # Create corresponding labels for left and right groups
        labels.append(f"Left_temp{i}")
        labels.append(f"Right_temp{i}")
    
    # Run a one-way ANOVA across all groups combined (left vs right comparison)
    anova_result = f_oneway(*all_data)
    
    print("ANOVA Results (Left vs Right Comparison):")
    print(f"F-Statistic: {anova_result.statistic:.4f}, p-value: {anova_result.pvalue:.4e}")

    # Interpret the results
    if anova_result.pvalue < 0.05:
        print("Result: Significant differences between group means (reject H0).")
    else:
        print("Result: No significant differences between group means (fail to reject H0).")
        
anova()



