from datetime import datetime
from meteostat import Point
from meteostat import Hourly



start=datetime(2023,12,19)
end=datetime(2023,12,19)
place=Point(52.520008,13.404954)
data=Hourly(place,start,end)
data=data.fetch()
print(data.head())
