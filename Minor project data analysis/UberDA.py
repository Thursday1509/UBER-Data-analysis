import calendar
import matplotlib
import matplotlib.pyplot as plt
import pandas as pdd
import seaborn as sns

matplotlib.style.use('ggplot')

data = pdd.read_csv("My_Uber_Drives.csv")
print(data.head())
print(data.tail())

data = data[:-1]
print(data.isnull().sum())

sns.heatmap(data.isnull(), yticklabels=False, cmap="viridis")
plt.title('Heatmap of Null values of data')
plt.show()
data = data.dropna()
sns.heatmap(data.isnull(), yticklabels=False, cmap="viridis")
plt.title('Heatmap of removed Null values from data')
plt.show()

data['START_DATE*'] = pdd.to_datetime(data['START_DATE*'])
data['END_DATE*'] = pdd.to_datetime(data['END_DATE*'])

hour = []
day = []
dayofweek = []
month = []
weekday = []
for x in data['START_DATE*']:
    hour.append(x.hour)
    day.append(x.day)
    dayofweek.append(x.dayofweek)
    month.append(x.month)
    weekday.append(calendar.day_name[dayofweek[-1]])
data['HOUR'] = hour
data['DAY'] = day
data['DAY_OF_WEEK'] = dayofweek
data['MONTH'] = month
data['WEEKDAY'] = weekday

time = []
data['TRAVELLING_TIME'] = data['END_DATE*'] - data['START_DATE*']
for i in data['TRAVELLING_TIME']:
    time.append(i.seconds / 60)
data['TRAVELLING_TIME'] = time
print(data.head())

sns.countplot(x='CATEGORY*', data=data)
plt.title('Main purpose of most people for taking UBER')
plt.show()

data['MILES*'].plot.hist()
plt.legend(labels=('X=Distance in miles', 'Y=People'),
           loc='upper right')
plt.title('How much distance is travelled by most people')
plt.show()

data['PURPOSE*'].value_counts().plot(kind='pie', figsize=(10, 10))
plt.legend(labels=('Meeting', 'Meal/Entertain', 'supplies', 'Customer visit', 'Temporary site', 'Between offices', 'Moving', 'Airport/Travel', 'Charity', 'Commute'),
           loc='upper right')
plt.title('Diff. purpose of people for travelling')
plt.show()

data['HOUR'].value_counts().plot(kind='bar', figsize=(10, 5), color='green')
plt.legend(labels=('X=Hours',),
           loc='upper right')
plt.title('Hourly data of UBER trips per day')
plt.show()
data['WEEKDAY'].value_counts().plot(kind='bar', color='yellow')
plt.title('''Day wise data of UBER trip's''')
plt.show()
data['DAY'].value_counts().plot(kind='bar', figsize=(15, 5), color='red')
plt.legend(labels=('X=Date of month',),
           loc='upper right')
plt.title('Date wise data of UBER trips per month')
plt.show()
data['MONTH'].value_counts().plot(kind='bar', figsize=(10, 5), color='blue')
plt.legend(labels=('X=Month of year',),
           loc='upper right')
plt.title('Month wise data of UBER trips')
plt.show()
data['START_DESTINATION*'].value_counts().plot(kind='bar', figsize=(45, 5), color='green')
plt.tick_params(axis='x', which='major', labelsize=8)
plt.legend(labels=('X=Diff. City Names',),
           loc='upper right')
plt.title('From which city most people are taking UBER for travelling')
plt.show()
data.groupby('PURPOSE*').mean().plot(kind='bar', figsize=(15, 5))
plt.title('Comparing all the purpose with miles, hour, day of the month, day of the week, month, Travelling time')
plt.show()
