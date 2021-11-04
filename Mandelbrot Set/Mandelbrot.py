import matplotlib.animation as animation
import matplotlib.pyplot as plt
import matplotlib.image
import numpy as np

import typing


def mandelbrot_point(c: complex, threshold: int = 4) -> int:
    """
    Returns the number of iterations needed to escape the mandelbrot set's bounding circle
    """
    z = complex(0, 0)
    for i in range(threshold):
        z = z ** 2 + c
        if abs(z) > 4:
            return i
    return threshold - 1


def mandelbrot(x, y, max_iteration=100) -> np.ndarray:
    """
    Returns a matrix of the mandelbrot set
    """
    z = np.zeros(x.shape)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            c = complex(x[i, j], y[i, j])
            z[i, j] = mandelbrot_point(c, max_iteration)

    return z


def animate(frame: int) -> typing.List[matplotlib.image.AxesImage]:

    ax.clear()
    ax.set_xticks([])
    ax.set_yticks([])

    threshold = round(1.15 ** (frame + 1))
    array = mandelbrot(X, Y, threshold)

    image = ax.imshow(array, interpolation="bicubic", cmap="magma")

    return [image]


def save_image(z: np.ndarray, title: str = "Mandelbrot Set") -> None:
    ax.imshow(z, cmap='hot')
    plt.savefig("Mandelbrot.png", bbox_inches="tight", transparent=True, pad_inches=0)
    plt.show(title=title)


FRAMES = 30  # reduce the number of frames for a faster output
INTERVAL = 100  # reduce the interval for a faster output

x_min, x_max = -2.1, 0.6
y_min, y_max = -1.5, 1.5
width, height = 1000, 1000

real = np.linspace(x_min, x_max, width)
im = np.linspace(y_min, y_max, height)

X, Y = np.meshgrid(real, im)
Z = mandelbrot(X, Y, 100)

fig = plt.figure(figsize=(50, 50))

plt.axis("off")
ax = plt.axes()
ax.axis("off")
ax.set_facecolor("tab:blue")

option = int(input("Choose an option:\n1:Save image\n2:Save gif\n3:Save image and gif\n"))

if option == 1:
    save_image(Z)
    print("Image Saved!")

elif option == 2:
    anim = animation.FuncAnimation(fig, animate, frames=FRAMES, interval=INTERVAL, blit=True)
    anim.save("Mandelbrot.gif")
    plt.show(title="Mandelbrot")
    print("Gif Saved!")

elif option == 3:
    save_image(Z)
    anim = animation.FuncAnimation(fig, animate, frames=FRAMES, interval=INTERVAL, blit=True)
    anim.save("Mandelbrot.gif")
    print("Image and Gif saved!")

else:
    print("Invalid option. Exiting..")
