# draw-mnist
## Overview
I trained a convolutional neural network (cnn) and used the saved model to be able to recognize numbers that you draw on a canvas.

The cnn is a Keras implementation of this [tensorflow tutorial](https://www.tensorflow.org/versions/r1.0/get_started/mnist/pros) to which I added an option to save the model, and an option to use tensorboard (see ```train.py```). The only difference between the models is the training time: I stopped training after 100 epochs and not 20k.

The ```model.json``` output after training is loaded by ```drawmnist.html``` through tensorflowjs (see ```guessing.js```) in order to do client-side inference. The canvas in which you draw is made with the canvas API (see ```board.js```).

## Use code locally
You have to open ```drawmnist.html``` in a local server and set the correct port in ```guessing.js```. For example, set 'port' to 8888 in ```guessing.js``` and use these commands:

```bash
cd path/to/cloned/repo
python -m http.server 8888 #python3
```
You can now go to localhost:8888/drawmnist.html from your browser.

## See model through tensorboard
Untar+unzip the file in logs/ and open it with tensorboard:

```bash
cd path/to/repo/logs/
tar -zxvf mnist-cnn-1535667182.tar.gz
tensorboard --logdir=mnist-cnn-1535667182
```

The training lasted 100 epochs, but I didn't put much thought into choosing this number. The 98.72% accuracy on the validation set was good enough for the app to work.
