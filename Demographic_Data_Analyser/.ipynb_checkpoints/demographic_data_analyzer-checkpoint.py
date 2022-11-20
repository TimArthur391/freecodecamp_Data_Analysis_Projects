import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    races = list(df['race'].unique())
    no_in_race = []
    for race in races:
      no_in_race.append(df['race'].value_counts()[race])
    race_count = pd.Series(data=no_in_race, index=races)

    # What is the average age of men?
    average_age_men = ((df['age'][df['sex'] == 'Male']).mean()).round(decimals=1)

    # What is the percentage of people who have a Bachelor's degree?
    no_of_bachelors = df['education'][df['education'] == 'Bachelors'].size
    percentage_bachelors = round((100*no_of_bachelors/df['education'].size),1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K? 
    indexs_of_higher_education = (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')
    indexs_of_lower_education = ~indexs_of_higher_education
  
    no_of_higher_education_people = df['education'][indexs_of_higher_education].size
    no_of_lower_education_people = df['education'][indexs_of_lower_education].size

    no_of_higher_education_people_above_50k = df['education'][(indexs_of_higher_education) & (df['salary']=='>50K')].size
    no_of_lower_education_people_above_50k = df['education'][(indexs_of_lower_education) & (df['salary']=='>50K')].size
    
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    lower_education = None

    # percentage with salary >50K
    higher_education_rich = round((100*no_of_higher_education_people_above_50k/no_of_higher_education_people),1)
    lower_education_rich = round((100*no_of_lower_education_people_above_50k/no_of_lower_education_people),1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df['hours-per-week'].value_counts()[1]
    num_min_worker_above_50k = df['salary'][(df['salary']=='>50K') & (df['hours-per-week'] == 1)].size
    rich_percentage = round((100*num_min_worker_above_50k/num_min_workers),1)

    # What country has the highest percentage of people that earn >50K?
    countries = list(df['native-country'].unique())
    highest_earning_country = None
    highest_earning_country_percentage = 0
    for country in countries:
      country_population = df['native-country'].value_counts()[country]
      rich_population_in_country = df['salary'][(df['native-country'] == country) & (df['salary']=='>50K')].size
      country_earning_percentage = (100*rich_population_in_country/country_population)
      if country_earning_percentage > highest_earning_country_percentage:
        highest_earning_country = country
        highest_earning_country_percentage = round(country_earning_percentage,1)
    

    # Identify the most popular occupation for those who earn >50K in India.
    index_for_rich_indians = (df['native-country'] == 'India') & (df['salary']=='>50K')
    top_IN_occupation = df['occupation'][index_for_rich_indians].mode().values[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
