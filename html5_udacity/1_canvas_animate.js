/**
 * Assets are from www.udacity.com
 */

var canvas = null;
var context = null;
var assets = ['/media/js/standalone/libs/gamedev_assets/robowalk/robowalk00.png',
              '/media/js/standalone/libs/gamedev_assets/robowalk/robowalk01.png',
              '/media/js/standalone/libs/gamedev_assets/robowalk/robowalk02.png',
              '/media/js/standalone/libs/gamedev_assets/robowalk/robowalk03.png',
              '/media/js/standalone/libs/gamedev_assets/robowalk/robowalk04.png',
              '/media/js/standalone/libs/gamedev_assets/robowalk/robowalk05.png',
              '/media/js/standalone/libs/gamedev_assets/robowalk/robowalk06.png',
              '/media/js/standalone/libs/gamedev_assets/robowalk/robowalk07.png',
              '/media/js/standalone/libs/gamedev_assets/robowalk/robowalk08.png',
              '/media/js/standalone/libs/gamedev_assets/robowalk/robowalk09.png',
              '/media/js/standalone/libs/gamedev_assets/robowalk/robowalk10.png',
              '/media/js/standalone/libs/gamedev_assets/robowalk/robowalk11.png',
              '/media/js/standalone/libs/gamedev_assets/robowalk/robowalk12.png',
              '/media/js/standalone/libs/gamedev_assets/robowalk/robowalk13.png',
              '/media/js/standalone/libs/gamedev_assets/robowalk/robowalk14.png',
              '/media/js/standalone/libs/gamedev_assets/robowalk/robowalk15.png',
              '/media/js/standalone/libs/gamedev_assets/robowalk/robowalk16.png',
              '/media/js/standalone/libs/gamedev_assets/robowalk/robowalk17.png',
              '/media/js/standalone/libs/gamedev_assets/robowalk/robowalk18.png'
             ];
var frames = [];

var loadedCount = 0;
var onImageLoad = function(){
    loadedCount++;
    if (loadedCount == 19) {
        setInterval(animate, 33);
    }
};

var setup = function() {
    body = document.body;
    canvas = document.createElement('canvas');

    context = canvas.getContext('2d');
    
    canvas.width = 100;
    canvas.height = 100;

    body.appendChild(canvas);

    // Load each image URL from the assets array into the frames array 
    // in the correct order.
    // Afterwards, call setInterval to run at a framerate of 30 frames 
    // per second, calling the animate function each time.
    // YOUR CODE HERE
    
    var ixImage = 0;
    var loadedCount = 0;
    for (; ixImage < assets.length; ixImage++) {
        var img = new Image();
        img.src = assets[ixImage];
        img.onload = onImageLoad;
        frames.push(img);
    }
};

var ixFrame = 0;
var animate = function(){
    // Draw each frame in order, looping back around to the 
    // beginning of the animation once you reach the end.
    // Draw each frame at a position of (0,0) on the canvas.
  
    // Try your code with this call to clearRect commented out
    // and uncommented to see what happens!
    //
    context.clearRect(0,0,canvas.width, canvas.height);
    // YOUR CODE HERE
    context.drawImage(frames[ixFrame], 0, 0);
    if (++ixFrame > 18) {
        ixFrame = 0;
    }
};

setup();

