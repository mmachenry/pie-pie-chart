from pie_pie_chart import plot_reading

# Display the pie chart with dummy data for debugging purposes. Avoids needing
# to load GPIO pins and go through the sensor calibration process.
def debug_plot ():
    class Proxy:
        def __init__(self):
            pass

        def get_weight_mean(self, n):
            return 18
    plot_reading(Proxy(), 1, 20)

if __name__ == "__main__":
    debug_plot()
