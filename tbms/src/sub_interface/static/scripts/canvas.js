function drawSemiCircle(canvasId) {
    document.write("Hellooooo");
    var canvas = document.getElementById(canvasId);
    var context = canvas.getContext('2d');
    var x = canvas.width / 2;
    var y = canvas.height / 2;
    var radius = 50;
    var startAngle = 0;
    var endAngle = 2 * Math.PI;
    var counterClockwise = false;

    context.beginPath();
    context.arc(x, y, radius, startAngle, endAngle, counterClockwise);
    context.lineWidth = 15;

    // line color
    context.strokeStyle = 'black';
    context.stroke();
}

function draw(){
    var canvas = document.getElementById('myCanvas');
    var ctx = canvas.getContext('2d');
    ctx.clearRect(0,0,WIDTH,HEIGHT);
    for (var i = 0; i < 100; i++) {
        ctx.beginPath();
        ctx.fillStyle = 'rgba(255,0,0,0.5)';
        ctx.arc(random(WIDTH), random(HEIGHT), random(50), 0, 2 * Math.PI);
        ctx.fill();
    }
}