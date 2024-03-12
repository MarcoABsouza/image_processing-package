from image_processing.utils import io, plot
from image_processing.processing import combination, transformation

image1 = io.read_image(
    "C:/Users/mabds/Downloads/test1.png",
)
image2 = io.read_image(
    "C:/Users/mabds/Downloads/test2.jpeg",
)
plot.plot_image(image1)
plot.plot_image(image2)


result_image = combination.transfer_histogram(image1, image2)
plot.plot_result(image1, image2, result_image)
