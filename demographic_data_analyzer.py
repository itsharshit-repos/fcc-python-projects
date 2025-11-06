import pandas as pd

def cal_dem_data(print_data=True):

    df = pd.read_csv("adult.data.csv", header=None)
    df.columns = [
        'age','workclass',"fnlwgt","education","education-num","marital-status","occupation","relationship","race","sex","capital-gain","capital-loss","hours-per-week","native-country","salary"
    ]

    # Race representation
    race_count = df['race'].value_counts()

    # Average age of men
    df['sex'] = df['sex'].str.strip()
    men_df = df[df['sex']=='Male']
    avg_age = round(men_df['age'].mean(), 1)

    # Percentage of people having Bachelors degree
    df['education'] = df['education'].str.strip()
    batch_df = len(df[df['education']=='Bachelors'])
    percen_num = round((batch_df/len(df['education']))*100, 1)

    # Percentage of people having Advanced education making >50K
    df['education'] = df['education'].str.strip()
    advanced_filter = (df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate')
    total_count = len(df[advanced_filter])
    df['salary'] = df['salary'].str.strip()
    rich_post = (df['salary']=='>50K')
    adv_earn_count = len(df[advanced_filter & rich_post])
    percent_count = round((adv_earn_count/total_count)*100, 1)

    # Percentage of people with advanced education making >50K 
    non_adv_filter = ~advanced_filter
    total_non_count = len(df[non_adv_filter])
    non_adv_earner = len(df[(non_adv_filter) & (df['salary']=='>50K')])
    non_percent_count = round((non_adv_earner/total_non_count)*100, 1)

    # Minimum number of hours a person works per week
    min_hr = df['hours-per-week'].min()

    # Percentage of people who work the minimum hours AND earn >50K
    total_min_hr_worker = len(df[df['hours-per-week']==min_hr])
    min_hr_earner = len(df[(df['hours-per-week']==min_hr) & (df['salary']=='>50K')])
    percen_min = round((min_hr_earner/total_min_hr_worker)*100, 1)

    # Country has the highest percentage of people that earn >50K and Percentage
    df['native-country'] = df['native-country'].str.strip()
    high_earn_percoun = df[df['salary']=='>50K']['native-country'].value_counts()
    total_cont_count = df['native-country'].value_counts()
    percen_each_country = (high_earn_percoun/total_cont_count)*100
    high_country = percen_each_country.idxmax()
    highest_percentage = round(percen_each_country.max(), 1)

    # Popular occupation for those who earn >50K in India
    df['occupation'] = df['occupation'].str.strip()
    filter_grp = df[(df['native-country']=='India') & (df['salary']=='>50K')]
    top_occupation = filter_grp['occupation'].value_counts().idxmax()

    if print_data:
        print("Data Load successfully")
        print(f"Race Count:\n{race_count}\n")
        print(f"Average age of men: {avg_age}\n")
        print(f"Percentage of people with Bachelors degree: {percen_num}%\n")
        print(f"Percentage of people with advanced education make more than 50K: {percent_count}%\n")
        print(f"Percentage of people without advanced education make more then 50K: {non_percent_count}%\n")
        print(f"The minimum number of hours a person works per week: {min_hr}\n")
        print(f"Percentage of people who work the minimum hours AND earn >50K: {percen_min}%\n")
        print(f"Country has the highest percentage of people that earn >50K and Percentage: {high_country} with {highest_percentage}%\n")
        print(f"The most popular occupation for those who earn >50K in India: {top_occupation}")

    return {
        'race_count': race_count,
        'avg_age': avg_age,
        'percen_num': percen_num,
        'percent_count': percent_count,
        'non_percent_count': non_percent_count,
        'min_hr': min_hr,
        'percen_min': percen_min,
        'high_country': high_country,
        'highest_percentage': highest_percentage,
        'top_occupation': top_occupation
    }

if __name__ == "__main__":
    cal_dem_data()