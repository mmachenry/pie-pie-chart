# Pie pie Chart

`pie_pie_chart.py` is a pie pie chart for Pi Day powered by the Raspberry Pi.

A pie is pie chart that shows how much pie is left. To verify this, we have
created a realtime pie measurement and reporting device which continuously
weighs the amount of pie that is left. The viewing screen, juxaposed with the
pie in question, provides immediate visual confirmation that the pie chart made
by the original pie is accurate.

# Setup and Installation

The project is running on a Raspberry Pi 3B+ with HX711 compatible 1kg load
cell. The OS is Raspbian version 2018-11-13-raspbian-stretch-full and Python3
is used to run the script.

    pip3 install -r requirements.txt
    python3 pie_pie_chart.py

