Pie Pie Chart
=============

`pie_pie_chart.py` is a pie pie chart for Pi Day powered by the Raspberry Pi.

A pie is pie chart that shows how much pie is left. To verify this, we have
created a realtime pie measurement and reporting device which continuously
weighs the amount of pie that is left. The viewing screen, juxaposed with the
pie in question, provides immediate visual confirmation that the pie chart made
by the original pie is accurate.

![The Pie Pie Chart in action](pie-pie-chart.jpg)

Happy Pi Day!

# Setup and Installation

The project is running on a Raspberry Pi 3B+ with HX711 compatible 1kg load
cell. The OS is Raspbian version 2018-11-13-raspbian-stretch-full and Python3
is used to run the script.

Download and install Raspbian to and SD and boot your RaspberryPi following
[the instructions](https://www.raspberrypi.org/downloads/raspbian/) on their
website.

Connect the HX711 load cell to the RaspberryPi using [this tutorial](https://tutorials-raspberrypi.com/digital-raspberry-pi-scale-weight-sensor-hx711/)
and test to make sure you're getting a reading using their example script.

Download this repository, install dependencies, and run. There will be a brief
calibration sequence to follow before the pie chart displays.

    git clone https://github.com/mmachenry/pie-pie-chart.git
    cd pie-pie-chart/
    pip3 install -r requirements.txt
    python3 pie_pie_chart.py

