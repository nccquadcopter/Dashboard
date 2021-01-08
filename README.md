# Dashboard

Using Python Dash library to help building the dashboard web application.


*Install the needed libraries:
```
$ pip install dash
```
```
$ pip install plotly
```
```
$ pip install pandas
```

*Replace your file
Make sure to put your CSV file in the same directory of the program
On line 19, replace "mag_data.csv" with your file (should be CSV file)

On line 22, 31, and 40, they are the codes to graph the lines,
To change the x-axis, replace "sensor_time" with whatever name of the column in the CSV file that you want to represent the x-axis. Likewise for y-axis.

If you only want to test with one sensor, comment out from line 30 to line 46, and from line 79 to line 88. Remember to delete the comma ',' on line 77.



*To run the program
Copy this and put it in the command line:
```
$ python3 test2.py
```
