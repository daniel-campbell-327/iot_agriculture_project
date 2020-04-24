# IoT Agriculture Project

![](https://specials-images.forbesimg.com/imageserve/5ea0bf898c2caa0006e718e2/960x0.jpg?fit=scale)

## Introduction
This project is a prototype for an agriculture environment data sensing system.
The prototype has an ETL pipeline that reads data from the sensor and loads this into an initial data file using Python. We then apply Data Modelling through the use of the pandas library to create a predictive model as to anticipate the temperature state in an hour.
We also create a data visualisation using the matplotlib library to create a line chart of the temperature of the previous 24 hours.
Both of the above are sent via an email, using the smtplib library, depending on the runtime of the system.
