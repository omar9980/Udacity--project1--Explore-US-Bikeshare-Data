import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("^_^ this code will help you to explore US bike share data... let's start ^_^")
    print("choose between (chicago, new york city or washington) ")
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid
    # inputs

    city = input("Please input the city name: ").lower()
    while city not in CITY_DATA:
        city = input(":( sorry, no such country in our data \n choose chicago, new york city or washington  ").lower()

    filtering = input("DO you want data to be filtered by (month) , (day) or (both):").lower()
    while filtering not in ["day", "month", "both"]:
        print("wrong input.. ")
        filtering = input("DO you want data to be filtered by month , day or both:").lower()

    if filtering == "month":
        # TO DO: get user input for month (all, january, february, ... , june)
        print("choose month (january , february ,.....june or 'all')")
        month = input("Please input month name: ").title()
        while month not in ['All', 'January', 'February', 'March', 'April', 'May', 'June']:
            month = input(":/ something wrong , make sure to type the month name correctly").title()
        day = "All"

    elif filtering == "day":
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        print("choose(saturday, sunday, ...., friday)")
        day = input("Please input day of week: ").title()
        while day not in ['All', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
            day = input(":/ please type the day correctly").title()
        month = "All"

    elif filtering == "both":
        # TO DO: get user input for month (all, january, february, ... , june)
        print("choose month (january , february ,.....june or 'all')")
        month = input("Please input month name: ").title()
        while month not in ['All', 'January', 'February', 'March', 'April', 'May', 'June']:
            month = input(":/ something wrong , make sure to type the month name correctly").title()

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        print("choose(saturday, sunday, ...., friday)")
        day = input("Please input day of week: ").title()
        while day not in ['All', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
            day = input(":/ please type the day correctly").title()
    print("displaying data for:\n city: {} \n month:{} \n day:  {}".format(city, month, day))
    print('-' * 40)
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
    df = pd.read_csv("{}.csv".format(city.replace(" ", "_")))

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_name'] = df['Start Time'].dt.day_name()
    df['start_hour'] = df['Start Time'].dt.hour

    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'All':
        df = df[df['day_name'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_num = int(df["month"].mode()[0])

    def month_name(month_number):
        if month_number == 1:
            return "January"
        elif month_number == 2:
            return "February"
        elif month_number == 3:
            return "March"
        elif month_number == 4:
            return "April"
        elif month_number == 5:
            return "May"
        elif month_number == 6:
            return "June"

    print("the most common month is: [{}]".format(month_name(month_num)))

    # TO DO: display the most common day of week
    print("the most common day is: [{}]".format(df["day_name"].mode()[0]))

    # TO DO: display the most common start hour
    print("the most common start hour: [{}]".format(df["start_hour"].mode()[0]))

    print("\nThis took >>>>%s<<<< seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    print("The Most Commonly Used Start Station is: ({})".format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print("The Most Commonly Used End Station is: ({})".format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + "---" + df['End Station']
    print("The Most Frequent Combination Of Start And End Station is: ({})".format(df["combination"].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("\nThe Total Travel Time is: [{}]".format(total_time) + " seconds")

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("The Mean Travel Time is: [{}]".format(mean_time) + " seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("\nType Of Users:...")
    print(df["User Type"].value_counts())

    if "Gender" in df:
        # TO DO: Display counts of gender
        print("\nGender of Users...")
        print(df["Gender"].value_counts())
    elif "Gender" not in df:
        print("\n:/ No Gender Data To Be Analysed For This City")

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        earliest_birth_year = df["Birth Year"].min()
        resent_birth_year = df["Birth Year"].max()
        common_birth_year = df["Birth Year"].mode()[0]
        print("\nThe Earliest Birth Year is: [{}]".format(earliest_birth_year))
        print("The Most Recent Birth Year is: [{}]".format(resent_birth_year))
        print("The Most Common Birth Year is: [{}]".format(common_birth_year))
    elif "Birth Year" not in df:
        print("\n:/ No Birth Year Data To Be Analysed For This City")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_function(df):
    start_row = 0
    end_row = 5

    asking_for_display = input("Do You Want To See 5 Lines of raw data").title()
    while asking_for_display == "Yes":
        print(df[start_row:end_row])
        start_row = start_row + 5
        end_row = end_row + 5
        stopping = input("Do You Want To Display More 5 lines Of Raw Data").title()
        while stopping not in ["Yes", "No"]:
            stopping = input("please Type yes or no:").title()
            if stopping == "No":
                break
        if stopping == "No":
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_function(df)

        restart = input('\nWould You Like To Restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
