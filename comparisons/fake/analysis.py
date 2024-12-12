import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import numpy as np
from scipy.stats import shapiro, mannwhitneyu, spearmanr, f_oneway
from itertools import combinations

df = pd.read_csv("BuzzFeed_fake_news_grouped_temp_data_diff.csv")
orig_per_word = df["avg_sentiment_per_word"]
temp0_per_word = df["avg_gen_sentiment_per_word_temp0"]
temp05_per_word = df["avg_gen_sentiment_per_word_temp0.5"]
temp1_per_word = df["avg_gen_sentiment_per_word_temp1"]

def plot_histogram():
    plt.figure(figsize=(10, 6))
    #sns.histplot(orig_per_word, bins=30, kde=False, color='blue', label='Original Sentiment', alpha=0.6)
    sns.histplot(temp0_per_word, bins=30, kde=False, color='orange', label='Temp0 Sentiment', alpha=0.6)
    sns.histplot(temp05_per_word, bins=30, kde=False, color='green', label='Temp0.5 Sentiment', alpha=0.6)
    sns.histplot(temp1_per_word, bins=30, kde=False, color='red', label='Temp1 Sentiment', alpha=0.6)
    
    plt.title('Histogram of Sentiment per Word (Different Temperatures)', fontsize=16)
    plt.xlabel('Sentiment Value', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    
def plot_density():
    plt.figure(figsize=(10, 6))
    sns.kdeplot(orig_per_word, color='blue', label='Original Sentiment', linewidth=2)
    sns.kdeplot(temp0_per_word, color='orange', label='Temp0 Sentiment', linewidth=2)
    sns.kdeplot(temp05_per_word, color='green', label='Temp0.5 Sentiment', linewidth=2)
    sns.kdeplot(temp1_per_word, color='red', label='Temp1 Sentiment', linewidth=2)

    plt.title('Density Plot of Sentiment per Word for Fake News (Different Temperatures)', fontsize=16)
    plt.xlabel('Sentiment Value', fontsize=14)
    plt.ylabel('Density', fontsize=14)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def plot_boxplot():
    boxplot_data = pd.DataFrame({
        'Original': orig_per_word,
        'Temp0': temp0_per_word,
        'Temp0.5': temp05_per_word,
        'Temp1': temp1_per_word
    })
    boxplot_data_long = boxplot_data.melt(var_name='Temperature', value_name='Sentiment')

    plt.figure(figsize=(10, 6))
    sns.boxplot(data=boxplot_data_long, x='Temperature', y='Sentiment', palette='Set2')

    plt.title('Boxplot of Sentiment per Word for Fake News (Different Temperatures)', fontsize=16)
    plt.xlabel('Temperature', fontsize=14)
    plt.ylabel('Sentiment Value per Word', fontsize=14)
    plt.show()
    
#plot_histogram()
#plot_density()    
#plot_boxplot()

#Test Normality

def plot_QQ():
    data_list = [orig_per_word, temp0_per_word, temp05_per_word, temp1_per_word]
    labels = ["Original", "Temp0", "Temp0.5", "Temp1"]

    # Create subplots
    plt.figure(figsize=(10, 8))
    for i, (data, label) in enumerate(zip(data_list, labels), start=1):
        plt.subplot(2, 2, i)  # 2x2 grid of subplots
        stats.probplot(data, dist="norm", plot=plt)
        plt.title(f"Q-Q Plot for Fake News: {label}")
        plt.ylabel("Sentimental Score per Word")

    plt.tight_layout()  # Adjust spacing between plots
    plt.show()
    
def shapiro_wilk():
    # List of datasets and their labels
    data_list = [orig_per_word, temp0_per_word, temp05_per_word, temp1_per_word]
    labels = ["Original", "Temp0", "Temp0.5", "Temp1"]

    print("Shapiro-Wilk Test Results:")
    print("-" * 40)
    for label, data in zip(labels, data_list):
        stat, p = shapiro(data)
        print(f"{label} Sentiment:")
        print(f"  Test Statistic: {stat:.4f}, p-value: {p:.4e}")
        if p > 0.01:
            print(f"  Result: Data is likely normal (parametric).")
        else:
            print(f"  Result: Data is not normal (non-parametric).")
        print("-" * 40)

#plot_QQ()
#shapiro_wilk()

#According to the shapiro-wilk test, the datasets are normal with a level of significance of 0.01.

#Mann-Whitney Test, si tiene novalidad, ANOVA para comparar todas

def mann_whitney():
    # List of datasets and labels
    data_list = [orig_per_word, temp0_per_word, temp05_per_word, temp1_per_word]
    labels = ["Original", "Temp0", "Temp0.5", "Temp1"]
    
    print("Mann-Whitney U Test Results:")
    print("-" * 50)
    
    # Loop through all pairwise combinations
    for (data1, label1), (data2, label2) in combinations(zip(data_list, labels), 2):
        stat, p = mannwhitneyu(data1, data2, alternative='two-sided')
        print(f"{label1} vs {label2}")
        print(f"  U Statistic: {stat:.4f}, p-value: {p:.4e}")
        if p > 0.05:
            print("  Result: No significant difference between the distributions.")
        else:
            print("  Result: Significant difference between the distributions.")
        print("-" * 50)
        
#mann_whitney()

def anova():
    diff_temp0 = df['diff_sentiment_temp0']
    diff_temp05 = df['diff_sentiment_temp0.5']
    diff_temp1 = df['diff_sentiment_temp1']
    anova_result = f_oneway(diff_temp0, diff_temp05, diff_temp1)
    print("ANOVA Results:")
    print(f"F-Statistic: {anova_result.statistic:.4f}, p-value: {anova_result.pvalue:.4e}")

    # Interpret the results
    if anova_result.pvalue < 0.05:
        print("Result: Significant differences between group means (reject H0).")
    else:
        print("Result: No significant differences between group means (fail to reject H0).")
        
#anova()

#Spearman Correlation (If Original Article Sent Score higher, does that mean generated also higher?)
def spearman():
    comparisons = [
        ("Original vs Temp0", orig_per_word, temp0_per_word),
        ("Original vs Temp0.5", orig_per_word, temp05_per_word),
        ("Original vs Temp1", orig_per_word, temp1_per_word),
    ]
    
    print("Spearman's Rank Correlation Results:")
    print("-" * 50)
    
    for label, data1, data2 in comparisons:
        # Compute Spearman's correlation
        rho, p = spearmanr(data1, data2)
        
        # Display results
        print(f"{label}")
        print(f"  Spearman's Correlation (ρ): {rho:.4f}")
        print(f"  p-value: {p:.4e}")
        if p > 0.05:
            print("  Result: No significant monotonic relationship.")
        else:
            print("  Result: Significant monotonic relationship.")
        print("-" * 50)
spearman()

#Find outliers with IQR method, can do with valores z
def outliers():
    diff_columns = ['diff_sentiment_temp0', 'diff_sentiment_temp0.5', 'diff_sentiment_temp1']

    def detect_outliers(column):
        Q1 = df[column].quantile(0.25)  # First quartile
        Q3 = df[column].quantile(0.75)  # Third quartile
        IQR = Q3 - Q1                   # Interquartile range
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        return (df[column] < lower_bound) | (df[column] > upper_bound)

    outlier_info = pd.DataFrame()

    for col in diff_columns:
        outlier_info[col] = detect_outliers(col)
        
    df['is_outlier'] = outlier_info.any(axis=1)

    outliers = df[df['is_outlier']]
    outliers.to_csv("BuzzFeed_outliers_fake.csv", index=False)

    print(f"Total Outliers: {len(outliers)}")
    print(outliers[['text'] + diff_columns])
        
#outliers()

def outliers_z(threshold=3):
    diff_columns = ['diff_sentiment_temp0', 'diff_sentiment_temp0.5', 'diff_sentiment_temp1']
    z_outliers = pd.DataFrame()
    for col in diff_columns:
        mean = df[col].mean()
        std = df[col].std()
        z_scores = (df[col] - mean) / std
        z_outliers[col] = np.abs(z_scores) > threshold  # Mark True for outliers

    # Combine results to create a final column indicating any outliers across the columns
    df['is_outlier_zscore'] = z_outliers.any(axis=1)
    
    outliers_z = df[df['is_outlier_zscore']]
    outliers_z.to_csv("BuzzFeed_Zoutliers_fake.csv", index=False)
    
    print(f"Total Outliers: {len(outliers_z)}")
    print(outliers_z[['text'] + diff_columns])   
#outliers_z()

def main_menu():
    while True:
        print("\n--- Data Analysis: Main Menu ---")
        print("1. Show Histogram")
        print("2. Show Density Plot")
        print("3. Show Boxplot")
        print("4. Show Q-Q Plot (Normality Test)")
        print("5. Perform Shapiro-Wilk Test (Normality)")
        print("6. Perform Mann-Whitney U Test (Comparison)")
        print("7. Detect Outliers (IQR)")
        print("8. Exit")
        
        # Get user input
        choice = input("Select an option (1-8): ").strip()

        if choice == '1':
            print("\nGenerating Histogram...")
            plot_histogram()
        elif choice == '2':
            print("\nGenerating Density Plot...")
            plot_density()
        elif choice == '3':
            print("\nGenerating Boxplot...")
            plot_boxplot()
        elif choice == '4':
            print("\nGenerating Q-Q Plot...")
            plot_QQ()
        elif choice == '5':
            print("\nPerforming Shapiro-Wilk Test...")
            shapiro_wilk()
        elif choice == '6':
            print("\nPerforming Mann-Whitney U Test...")
            mann_whitney()
        elif choice == '7':
            print("\nDetecting Outliers...")
            #outliers()
        elif choice == '8':
            print("\nExiting the program. Goodbye!")
            break
        else:
            print("\nInvalid option. Please try again.")

#main_menu()