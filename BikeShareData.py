import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
VALID_MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'All']
VALID_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'All']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter City name:\n').lower()
    while city not in CITY_DATA:
        print('Please enter a valid city name!')
        city = input('Enter City name:\n').lower()
        if city in CITY_DATA:
            break
        else:
            continue

    # get user input for month (all, january, february, ... , june)
    print('\n\nValid months include months from January to June or all')
    month = input('Enter Month:\n').lower().title()
    while month not in VALID_MONTHS:
        print('Please enter a valid month name!')
        month = input('Enter Month:\n').lower().title()
        if month in VALID_MONTHS:
            break
        else:
            continue

    # get user input for day of week (all, monday, tuesday, ... sunday)
    print('Valid days of week include days from Monday to Sunday or all')
    day = input('Enter Day:\n').lower().title()
    while day not in VALID_DAYS:
        print('Please enter a valid day name!')
        day = input('Enter Day:\n').lower().title()
        if day in VALID_DAYS:
            break
        else:
            continue

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load csv file into DataFrame
    df = pd.read_csv(CITY_DATA[city])

    #convert start time column to date time using the pandas to_datetime() function
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #create columns for month and day by using the 'dt method'
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_of_week
    df['hour'] = df['Start Time'].dt.hour

    #to filter by month and day we do the following:

    if month != 'All' and month in VALID_MONTHS:
        month = VALID_MONTHS.index(month) + 1
        df = df[df['month'] == month]

    if day != 'All':
        day = VALID_DAYS.index(day)
        df = df[df['day'] == day]

    #Replacing  NaN values in the already filtered data using '.fillna method'
    if df.isnull().sum().sum() > 0:
        df = df.fillna(method='ffill', axis=0, inplace=True)
    else:
        print('No NaN values present')

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode().iloc[0, 0]
    print('The most common month is: {}'.format(most_common_month))

    # display the most common day of week
    most_common_day_of_week = df['day'].mode().iloc[0, 0]
    print('The most common day of the week is: {}'.format(most_common_day_of_week))

    # display the most common start hour
    most_common_start_hour = df['hour'].mode().iloc[0, 0]
    print('The most common start hour is: {}'.format(str(most_common_start_hour)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode().iloc[0, 0]
    print('The most common start station is: {}'.format(most_common_start_station))

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode().iloc[0, 0]
    print('The most common end station: {}'.format(most_common_end_station))

    # display most frequent combination of start station and end station trip
    print('The most frequent combinations of start and end stations are {} and {} respectively'.format(
        most_common_start_station, most_common_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time_travel = df['Trip Duration'].sum()
    print('The total time travelled is : {}'.format(str(total_time_travel)))

    # display mean travel time
    mean_time_travel = bdf['Trip Duration'].mean()
    print('The mean time travel is: {}'.format(mean_time_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print('Counts of User Types: \n')
    print(user_type_count)

    # Display counts of gender
    gender_type_count = df['Gender'].value_counts()
    print('Counts of Gender: \n')
    print(gender_type_count)

    # Display earliest, most recent, and most common year of birth
    earliest_year = df['Birth Year'].min()
    latest_year = df['Birth Year'].max()
    most_common_year = df['Birth Year'].mode().iloc[0, 0]

    print('The earliest year is: {}'.format(str(earliest_year)))
    print('The latest year is: {}'.format(str(latest_year)))
    print('The most common year is: {}'.format(str(most_common_year)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    print('Would like to view the first 5 rows of this data?\n')
    view_data = input('Please enter "yes or no": \n').lower()

    if view_data == 'yes':
        df.head()
        print('Would you like to view the next 5 rows?')
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
