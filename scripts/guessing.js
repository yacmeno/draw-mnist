(async function loadModel() {
    console.log('loading model...');
    let model = await tf.loadModel('http://localhost:port/saved_model/model.json');
    console.log('model loaded');

    const lastGuess = document.getElementById('lastGuess');
    const guessBtn = document.getElementById('guess');
    guessBtn.addEventListener('click', guessFunc);

    function guessFunc() {
        const canvas = document.getElementById('canvas');

        //load canvas as 1-channel image and reshape it
        let image = tf.fromPixels(canvas, 1).asType('float32');
        image = tf.image.resizeBilinear(image, [28, 28]);
        image = tf.reshape(image, [1, 1, 28, 28]);
        const prediction = tf.argMax(model.predict(image), 1).dataSync();
        lastGuess.textContent = prediction[0];
    }
})();