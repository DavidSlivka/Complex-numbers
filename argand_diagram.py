import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111)

ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

ax.set_xlabel('Real', fontsize=10, loc='right')
ax.set_ylabel('Imaginary', fontsize=10, loc='top')


def argand(number: complex):
    imag_axis_x, imag_axis_y = [0, number.real], [number.imag, number.imag]
    real_axis_x, real_axis_y = [number.real, number.real], [0, number.imag]

    plt.plot(imag_axis_x, imag_axis_y, 'go--')  # Draw the projection on imaginary-axis
    plt.plot(real_axis_x, real_axis_y, 'ro--')  # Draw the projection on real-axis

    plt.plot(number.real, number.imag, 'bo')
    label = f"{number}"

    plt.annotate(label,  # this is the text
                 (number.real, number.imag),  # these are the coordinates to position the label
                 textcoords="offset points",  # how to position the text
                 xytext=(10, 5),  # distance from text to points (x,y)
                 ha='center')


a = np.array([-2. - 6.j, 2. + 8.j, 1. + 8.j, 7. + 9.j, 5. - 10.j, 4 - 3j])

for num in a:
    argand(num)

plt.show()

