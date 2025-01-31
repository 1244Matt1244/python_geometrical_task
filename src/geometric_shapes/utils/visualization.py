# src/shapes/utils/visualization.py
import matplotlib.pyplot as plt

class ShapeVisualizer:
    @staticmethod
    def plot_circle(circle: Circle):
        fig, ax = plt.subplots()
        ax.add_patch(plt.Circle((0, 0), circle.radius, fill=False))
        plt.axis('equal')
        return fig
