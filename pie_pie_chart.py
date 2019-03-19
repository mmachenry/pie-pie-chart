import RPi.GPIO as GPIO
import hx711
import matplotlib.pyplot as plt
 
# Read initial calibration and tare weight data then display the plot.
def main():
    GPIO.setmode(GPIO.BCM)
    hx = hx711.HX711(dout_pin=5, pd_sck_pin=6)
    zero_the_scale(hx)
    calibrate_scale(hx)
    (tare_weight, total_weight) = get_tare_and_full_weight(hx)
    plot_reading(hx, tare_weight, total_weight - tare_weight)

# Set scale position to zero. The scale should be empty when this is run.
def zero_the_scale(hx):
    err = hx.zero()
    if err:
        raise ValueError('Tare is unsuccessful.')

    zero_reading = hx.get_raw_data_mean()
    if zero_reading:
        print('Data subtracted by offset: ', zero_reading)
    else:
        raise ValueError('Invalide zero reading')

# Calibrate the scale with prompts to the user.
def calibrate_scale (hx):
    input('Put known weight on the scale and then press Enter')
    reading = hx.get_data_mean()
    if reading:
        print('Mean value from HX711 subtracted by offset:', reading)
        user_input = input('Write how many grams it was and press Enter: ')
        try:
            weight = float(user_input)
            print(weight, 'grams')
        except ValueError:
            print('Expected integer or float and I have got:', user_input)

        ratio = reading / weight
        hx.set_scale_ratio(ratio)
        print('Ratio is set.')
    else:
        raise ValueError('Cannot calculate mean value.')

# Prompt user and get readings for the tare weight and full pie.
def get_tare_and_full_weight (hx):
    input('Put the pie tin on the scale for tare weight and press enter.')
    tare_weight = hx.get_weight_mean(20)
    print ("Tare weight is ", tare_weight, "g")

    input('Put the pie on the scale for a full weight and press enter.')
    total_weight = hx.get_weight_mean(20)
    print ("Full weight is ", total_weight, "g")

    return (tare_weight, total_weight)

# Continually read data from the sensor, update the pie chart, and display.
def plot_reading (hx, tare_weight, full_weight):
    while True:
        current_weight = hx.get_weight_mean(20)
        remaining_weight = max(0,current_weight - tare_weight)
        #print ("Current weight is ", current_weight, "g")

        labels = ['Remaining', 'Eaten']
        sizes = [remaining_weight, max(0,full_weight - remaining_weight)]
        colors = ['sandybrown', 'lightgrey']
        explode = (0, 0.1)
         
        title_font = { 'color':  'blue', 'weight': 'bold', 'size': 30 }
        label_font = { 'color':  'black', 'weight': 'normal', 'size': 20 }

        h = plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=180,
            textprops=label_font)

        plt.title("Pi Day Pie Pie Chart", title_font)

        plt.plot()
        plt.draw()
        plt.pause(1)
        plt.clf()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print('Happy Pi Day!')

    finally:
        GPIO.cleanup()
