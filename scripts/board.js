const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
//global canvas options
ctx.strokeStyle = 'white';
ctx.fillStyle = 'black';
ctx.fillRect(0, 0, canvas.width, canvas.height);
ctx.lineCap = 'round';
ctx.lineWidth = 10;

//function to clear canvas
let clearBtn = document.getElementById('clear');
clearBtn.addEventListener('click', clear);
function clear() {
    ctx.fillRect(0, 0, canvas.width, canvas.height);
}

//draw on canvas when lmb is pressed
let currX;
let currY;
let newX;
let newY;

canvas.addEventListener('mousedown', draw);

function draw(event) {
    currX = event.clientX - canvas.getBoundingClientRect().x;
    currY = event.clientY;
    
    canvas.addEventListener('mousemove', move);

    function move(event) {
        // console.log(event.clientX - canvas.getBoundingClientRect().x, event.clientY);        //for debugging
        newX = event.clientX - canvas.getBoundingClientRect().x;
        newY = event.clientY;
        ctx.beginPath();
        ctx.moveTo(currX, currY);
        ctx.lineTo(newX, newY);
        ctx.stroke();
        currX = newX;
        currY = newY;
    }

    canvas.addEventListener('mouseup', function() {
        canvas.removeEventListener('mousemove', move);
    });

    canvas.addEventListener('mouseout', function() {
        canvas.removeEventListener('mousemove', move);
    });
}