#!/usr/bin/env python3

import RPi.GPIO as GPIO  # import GPIO
from hx711 import HX711  # import the class HX711
import matplotlib.pyplot as plt
 
def main():
    GPIO.setmode(GPIO.BCM)
    hx = HX711(dout_pin=5, pd_sck_pin=6)
    err = hx.zero()
    if err:
        raise ValueError('Tare is unsuccessful.')

    zero_reading = hx.get_raw_data_mean()
    if zero_reading:
        print('Data subtracted by offset: ', zero_reading)
    else:
        print('invalid data', zero_reading)

    input('Put known weight on the scale and then press Enter')
    known_reading = hx.get_data_mean()
    if known_reading:
        print('Mean value from HX711 subtracted by offset:', known_reading)
        known_weight_grams = input(
            'Write how many grams it was and press Enter: ')
        try:
            value = float(known_weight_grams)
            print(value, 'grams')
        except ValueError:
            print('Expected integer or float and I have got:',
                  known_weight_grams)

        ratio = known_reading / value
        hx.set_scale_ratio(ratio)
        print('Ratio is set.')
    else:
        raise ValueError('Cannot calculate mean value.')

    input('Put the pie tin on the scale for tear weight and press enter.')
    tear_weight = hx.get_weight_mean(20)
    print ("Tear weight is ", tear_weight, "g")

    input('Put the pie on the scale for a full weight and press enter.')
    full_weight = hx.get_weight_mean(20)
    print ("Full weight is ", full_weight, "g")

    plot_reading(hx, tear_weight, full_weight)

def plot_reading (hx, tear_weight, full_weight):
    while True:
        current_weight = hx.get_weight_mean(20)
        print ("Current weight is ", current_weight, "g")

        labels = ['Remaining', 'Eaten']
        sizes = [current_weight, max(0,full_weight - current_weight)]
        colors = ['gold', 'yellowgreen']
        explode = (0.1, 0)  # explode 1st slice
         
        # Plot
        h = plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=270)
        #hx.set(plt.findobj(h,'type','text'),'fontsize',18);
        plt.title("Pi Day Pie Pie Chart")
         
        plt.axis('equal')
        plt.plot()
        plt.draw()
        plt.pause(1)
        plt.clf()

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print('Bye :)')

    finally:
        GPIO.cleanup()
