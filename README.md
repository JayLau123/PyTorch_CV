# CNN-for-image-process

### Background

Deep learning techniques are commonly used for text data or image data. 

A japanese scientist Kunihiko, known for his artificial neural networks. He explained how our brains process images. After light enters the eyes, it will be converted into light signals and spread in the brain. In the biological visual system, there are multiple cortices, and each cortex processes signals differently, starting from pixels and then developing some rough features, such as directional edges (horizontal, vertical), and corners, as well as combining the features of the previous layer into an outline, and incorporating facial content such as a nose, an eye, and finally adding details to complete the final image. A French scientist Yann LeCun, who created the most famous algorithm in computer vision field: CNN.


The convolution operation is fundamental to understanding how convolutional neural networks (CNNs) work, especially in the context of image processing tasks like image classification, object detection, and more. 

Here’s a detailed explanation of the convolution operation in the context of neural networks:

### Basic Concept
A convolution involves sliding a **filter/kernel** over the **input image/input feature map** and computing the **element-wise multiplication (Note: different from matrix dot product)** of the filter and the local regions it covers. The result is a new feature map that highlights certain features from the input, such as edges, textures, or other patterns, depending on the filter's weights.

### Components of Convolution in CNNs

1. **Filters/Kernels**: These are small matrices of weights that are learned during training. Each filter is designed to detect specific features in the input data. For example, in image processing, filters might detect edges, color transitions, or textures.

2. **Stride**: Steplength. This refers to the number of pixels by which the filter moves across the input image. A stride of 1 moves the filter one pixel at a time, while a stride of 2 moves it two pixels. Increasing the stride reduces the size of the output feature map.

3. **Padding**: To handle the boundaries of the input image and to control the spatial dimensions of the output feature maps, padding is often applied. If no padding is used ('valid' padding), the output dimensions will be reduced based on the filter size. To maintain the same dimensions as the input, 'same' padding (adding zeros around the edges of the input) is used. See below input image is $5\times5$, while output image is also $5\times5$, with 'same' padding.

### How Convolution Works
- Place the filter at the top-left corner of the input image.
- Perform **element-wise multiplication**(Note: different from matrix dot product) between the filter and the corresponding portion of the input image it covers, then sum up all the products. This sum gives you a single pixel in the output feature map.
- Slide the filter over to the next position, determined by the stride(steplength), and repeat the operation.
- Continue this process across the entire input image. The resulting matrix from this operation is the **convolved feature** (also known as the feature map).

### Importance in Deep Learning

In deep learning, multiple filters are typically used in each convolutional layer, with each filter designed to detect different features. As the data progresses through successive convolutional layers, the network can recognize increasingly complex patterns. The network learns the optimal values for the filter weights during training, using backpropagation to minimize the difference between the predicted and actual outputs.

Convolution operations are not only fundamental to image processing tasks but have also been adapted for various other data types, including time series, audio signals, and more, wherever data can be represented in a grid-like structure.

### Example. See below

Consider a simple 3x3 filter and a 5x5 input image with a stride of 1 and 'same' padding(adding zeros around the edges of the input image). Here's a step-by-step of how the convolution would typically work:

1. Apply the filter to the top-left 3x3 region of the input image.
2. Calculate the elemetn-wise product (plus any bias, if applicable).
3. Write the result to the corresponding location in the output feature map.
4. Slide the filter one pixel to the right and repeat. Once the filter reaches the end of a row, it moves down to the next row and repeats the process.
5. If 'same' padding is used, pad the input image with zeros on all sides so that the output feature map has the same width and height($5\times5$) as the input image.


We can use mathematical method to extract some properties of a picture. Computer stores an image as a matirx(channel), and each element of the matrix is a number from 0-255, the number represents the pixel. The bigger the number, the darker the corlor. For any colorful images, we can use three matrixes or three channel to store it, the colors are red, green, blue, respectively(RGB). Therfore, this is a three-dimensional matrix. For demonstration, we just use an 1D matrix to store an image.


A convolutional neural network consists of an input layer, hidden layers and an output layer. We start with the input layer and performs a dot product of the convolution kernel with the input matrix.

Here, we use different convolution kernels, which is a 3 $\times$ 3 matrix, to do convolution operation, so as to extract corresponding properties and generate a feature map, this feature will contribute to the input of the next layer.

![Picture1](https://user-images.githubusercontent.com/98719524/220838575-63f49ec8-2b87-4bf1-9e98-87d982f0fb10.png)





### Pooling

![Picture1](https://user-images.githubusercontent.com/98719524/221042999-efb612fd-867a-45d6-a439-6eea09d32aea.png)

