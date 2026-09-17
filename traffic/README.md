# Traffic

Classifies images of road signs into 43 categories using a convolutional neural network
built with TensorFlow, trained on the German Traffic Sign Recognition Benchmark (GTSRB).

## Usage

```
python traffic.py data_directory [model.h5]
```

`data_directory` contains one subdirectory per category, named `0` to `42`, each holding
that category's images. If a second argument is given, the trained model is saved to that
file.

Requires Python 3.12 (TensorFlow has no build for 3.14 yet):

```
pip install tensorflow opencv-python scikit-learn
```

```
$ python traffic.py gtsrb
Epoch 1/10
500/500 ━━━━━━━━━━━━━━━━━━━━ 3s 5ms/step - accuracy: 0.3170 - loss: 2.5655
...
Epoch 10/10
500/500 ━━━━━━━━━━━━━━━━━━━━ 2s 5ms/step - accuracy: 0.8292 - loss: 0.5080
333/333 - 1s - 2ms/step - accuracy: 0.9588 - loss: 0.1843
```

## How it works

Every image is loaded with OpenCV, resized to 30×30 pixels, and scaled so its pixel
values fall between 0 and 1. The labels are one-hot encoded, and 40% of the data is held
out for testing.

The network is `Conv2D` (32 filters, 3×3, ReLU) → `MaxPooling2D` (2×2) → `Flatten` →
`Dense` (128, ReLU) → `Dropout` (0.5) → `Dense` (43, softmax), trained for 10 epochs with
the Adam optimiser and categorical cross-entropy loss.

## Implementation notes

- `load_data` — walks each category folder with `os.path.join` so it works on any OS,
  returning the resized, normalised images and their integer labels.
- `get_model` — builds and compiles the CNN described above.

## Experimentation

At first I used a hidden layer of 8 nodes, this wasn't good enough and didnt seem to learn at all. Furthermore, without convolution the network couldn't pick out features like edges or shapes. Due to the output being 43 nodes, an 8 node hidden layer was no where near enough.

Therefore, I switched to: a convolution layer, pooling layer, flattening, 128 node hidden layer, dropouts and a 43 node output layer. To begin with this model didn't learn either (an accuracy score of 5.41%), but I came to realise that this was due to the pixel values ranging from 0 - 255, this resulted in the large values stopping the relu nodes from training properly. In order to fix this, I just divided the pixel values by 255 to scale them between 0 - 1.

My final network achieved an accuracy of 95.88%.