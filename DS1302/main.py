# ----- Codigo DS1306 ------
from machine import Pin
from ds1302_local import DS1302

# Initialize DS1302 RTC with specified pins (clk, dio, cs)
ds = DS1302(Pin(0),Pin(1),Pin(2))
print(ds)
print(dir(ds))

ds.date_time() # returns the current datetime.
ds.date_time([2018, 3, 9, 4, 23, 0, 1, 0]) # set datetime.

ds.hour() # returns hour.
ds.second(10) # set second to 10.