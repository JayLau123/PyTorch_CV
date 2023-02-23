# CNN-for-image-process

### Background

Deep learning techniques are commonly used for text data or image data. 

A japanese scientist Kunihiko, known for his artificial neural networks. He explained how our brains process images. After light enters the eyes, it will be converted into light signals and spread in the brain. In the biological visual system, there are multiple cortices, and each cortex processes signals differently, starting from pixels and then developing some rough features, such as directional edges (horizontal, vertical), and corners, as well as combining the features of the previous layer into an outline, and incorporating facial content such as a nose, an eye, and finally adding details to complete the final image.

We can use mathematical method to extract some properties of a picture. Computer stores an image as a matirx(channel), and each element of the matrix is a number from 0-255, the number represents the pixel. The bigger the number, the darker the corlor. For any colorful images, we can use three matrixes or three channel to store it, the colors are red, green, blue, respectively(RGB). Therfore, this is a three-dimensional matrix. For demonstration, we just use an 1D matrix to store an image.

A French scientist Yann LeCun, who created the most famous algorithm in computer vision field.

A convolutional neural network consists of an input layer, hidden layers and an output layer. We start with the input layer and performs a dot product of the convolution kernel with the input matrix.

Here, we use different convolution kernels, which is a 3 $\times$ 3 matrix, to do convolution operation, so as to extract corresponding properties and generate a feature map, this feature will contribute to the input of the next layer.

![Picture1](https://user-images.githubusercontent.com/98719524/220838575-63f49ec8-2b87-4bf1-9e98-87d982f0fb10.png)










### Example 1: CNN for simple image recognition

### Example 2: 

To be continued...
