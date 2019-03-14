# Pie Pie Chart

`pie_pie_chart.py` is a pie pie chart for Pi Day powered by the Raspberry Pi.

A pie is pie chart that shows how much pie is left. To verify this, we have
created a real-time pie measurement and reporting device which continuously
weighs the amount of pie that is left. The viewing screen, juxtaposed with the
pie in question, provides immediate visual confirmation that the pie chart made
by the original pie is accurate.

![The Pie Pie Chart in action](pie-pie-chart.jpg)

Happy Pi Day!

## Materials needed

* [Load Cell - 5kg](https://www.sparkfun.com/products/14729?_ga=2.24515706.1936956039.1552598453-1561457067.1552166144&_gac=1.115816180.1552174572.Cj0KCQiA5Y3kBRDwARIsAEwloL46FxiD3YNyOx13p7sVzKgmAnDuFhzwXxAw4RRtC2iJ8tYv5psYXeoaAgeIEALw_wcB)
* [Load Cell Amplifier - HX711](https://learn.sparkfun.com/tutorials/load-cell-amplifier-hx711-breakout-hookup-guide/all)
* [Raspberry Pi 3 Model B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/)
* [10.1" LCD Screen](https://www.robotshop.com/en/1280x800-101-lcd-ips-screen-raspberry-pi.html?gclid=CjwKCAjw96fkBRA2EiwAKZjFTU8E2x6RaMLMpzV93_2UvaS4hqcBabY84NoMAyt84qUMzNkNBTGt7xoCQUUQAvD_BwE)
* 8GB Micro SD card
* tiny breadboard
* hookup wires
* Two 8" x 8" x 1/8" pieces of wood or plastic
* 7 tart apples, peeled and cored
* 1 cup white sugar
* 1 1/2 teaspoons ground cinnamon, or to taste
* 2 tablespoons all-purpose flour
* 1/2 teaspoon ground nutmeg
* salt to taste
* 2 recipes unbaked pie shells
* 1 tablespoon butter

## Tools needed

* Soldering iron
* Wire stripper
* Mixing bowl
* Two 9" deep dish pie pans
* Oven

## Setup and Installation

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

Preheat oven to 400 degrees F (200 degrees C).

Cut the apples into 1/4 inch slices.

In a mixing bowl, combine sugar, cinnamon, flour, nutmeg (or apple pie spice),
and salt; mix thoroughly. Pour the spice mix over the apples and stir until the
apples are coated.

Line one crust in a 9 inch deep dish pie pan. Place the apples in the pie
crust. Dot the apple filling evenly with butter. Fit the top crust over the
apples. Press the crust down gently and cut 3 or 4 slits in the top crust to
allow steam to escape while the pie bakes

Bake in the preheated oven 50 minutes, or until the crust is golden brown.
Check the pie after the first 30 minutes of cooking: if the crust is already
browned reduce the heat to 350 degrees F (175 degrees C) to allow the apples to
cook without the crust burning.

Run script and place pie on scale when prompted.
