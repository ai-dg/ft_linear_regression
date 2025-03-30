import matplotlib
matplotlib.use('TkAgg')  # Utiliser TkAgg pour Fedora
import matplotlib.pyplot as plt

def plot_example():
    plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Test Graph')
    plt.show()

plot_example()
