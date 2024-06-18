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

Pooling is a fundamental operation in convolutional neural networks (CNNs) that reduces the spatial dimensions (i.e., width and height) of the input image for the next convolutional layer. It serves several purposes: 

- Reducing the computational load and memory usage
- Making the detection of features invariant to scale and orientation
- Helping to prevent overfitting by providing an abstracted form of the representation.

### Types of Pooling

There are several types of pooling, but the two most common are:

- **Max Pooling**: This is the most frequently used form of pooling in CNN architectures. Max pooling operates by sliding a filter (often 2x2 size) over the input and taking the maximum value from the region of the input covered by the filter. It essentially captures the most prominent feature that is, the highest value, within the region of interest.
- **Average Pooling**: Instead of taking the maximum value, average pooling calculates the average of the elements in the region of the filter. This method can be seen as smoothing the input features, which sometimes helps reduce noise.

### How Pooling Works

- **Filter/Kernel Size**: This defines the region over which the operation is performed. Common sizes include 2x2 or 3x3.
- **Stride**: This defines the step size the pooling operation moves the filter across the input. In many cases, the stride is equal to the filter size, which means that the pooling regions do not overlap.
- **Padding**: Similar to convolution, padding can be applied to the input of a pooling layer. However, in pooling, padding is less common since reducing dimensionality is often desired.

### Example of Max Pooling
Suppose we have the following 4x4 matrix as an input:

```
| 1  3  2  4 |
| 5  6  7  8 |
| 9  10 11 12 |
| 13 14 15 16 |
```

Using a 2x2 filter and a stride of 2 for max pooling, we would examine four regions:
- Top-left 2x2 corner: `[1, 3, 5, 6]` → Maximum value is `6`
- Top-right 2x2 corner: `[2, 4, 7, 8]` → Maximum value is `8`
- Bottom-left 2x2 corner: `[9, 10, 13, 14]` → Maximum value is `14`
- Bottom-right 2x2 corner: `[11, 12, 15, 16]` → Maximum value is `16`

The output after max pooling would be:
```
| 6  8 |
| 14 16 |
```

### Benefits of Pooling
- **Dimensionality Reduction**: Reduces the number of parameters and computation in the network.
- **Feature Invariance**: Helps to make the model invariant to small translations of the input.
- **Noise Suppression**: Can help in eliminating noise and capturing dominant features by summarizing the presence of features in patches of the feature map.

Pooling layers are typically placed between successive convolutional layers. Their role in reducing dimensionality and allowing deeper networks without increase in computational cost has made them an integral part of CNN architectures.
