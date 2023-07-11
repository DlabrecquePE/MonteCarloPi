# libraries
import matplotlib.pyplot as plt
import numpy as np

# initialize
actual = 3.141592653589793238462643383279
batch_size, inside, outside, plot_sample = 250, 0, 0, 0

plt.ion()
plt.figure(figsize=(8, 8))
plt.axis([-1.1, 1.1, -1.1, 1.1])
plt.title("Pi by Monte Carlo Method")

while True:
    # generate data
    sample = np.array([np.random.uniform(-1, 1, size=batch_size), np.random.uniform(-1, 1, size=batch_size)])
    inner_x, inner_y, outer_x, outer_y = ([] for _ in range(4))

    # calculate and plot
    for point in range(batch_size):
        if np.sqrt(sample[0, point] ** 2 + sample[1, point] ** 2) > 1:
            outside += 1
            outer_x.append(sample[0, point])
            outer_y.append(sample[1, point])
        else:
            inside += 1
            inner_x.append(sample[0, point])
            inner_y.append(sample[1, point])
    pi_approx = 4 * inside / (inside + outside)
    pi_error = np.abs(pi_approx - actual)
    plt.scatter(outer_x, outer_y, color='blue')
    plt.scatter(inner_x, inner_y, color='red')

    # manage output
    plot_sample += batch_size
    output_string1 = 'Pi is approximately ' + str(pi_approx)
    output_string2 = 'Error: ' + str(pi_error * 100) + '%'
    output_string3 = 'Sample # ' + str(plot_sample)
    out1 = plt.text(-0.6, -1.25, output_string1)
    out2 = plt.text(-0.6, -1.30, output_string2)
    out3 = plt.text(-0.6, -1.35, output_string3)
    plt.pause(.001)
    out1.remove()
    out2.remove()
    out3.remove()
