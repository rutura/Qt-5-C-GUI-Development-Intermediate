import QtQuick
import QtQuick.Window
import QtQuick.Controls

Window {
    id: mainWindow
    width: 973
    height: 530
    visible: true
    title: "Shape Drawing Demo"
    
    // Main Canvas for drawing all shapes
    Canvas {
        id: drawingCanvas
        anchors.fill: parent
        
        // Create placeholder image for Qt logo
        property var placeholderImage: null
        
        // Load or create placeholder image
        Component.onCompleted: {
            createPlaceholderImage();
        }
        
        // Create a placeholder cyan image with text
        function createPlaceholderImage() {
            var offscreenCanvas = document.createElement('canvas');
            offscreenCanvas.width = 200;
            offscreenCanvas.height = 200;
            var ctx = offscreenCanvas.getContext('2d');
            
            // Fill with cyan color
            ctx.fillStyle = '#008B8B'; // dark cyan
            ctx.fillRect(0, 0, 200, 200);
            
            // Add text
            ctx.fillStyle = 'white';
            ctx.font = '20px Arial';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText('Qt Logo', 100, 100);
            
            // Create image from canvas
            var img = new Image();
            img.src = offscreenCanvas.toDataURL();
            img.onload = function() {
                placeholderImage = img;
                drawingCanvas.requestPaint();
            };
        }
        
        onPaint: {
            var ctx = getContext("2d");
            ctx.clearRect(0, 0, width, height);
            
            // Set pen properties
            ctx.lineWidth = 5;
            ctx.strokeStyle = "black";
            
            // Draw rectangle
            ctx.fillStyle = "red";
            ctx.beginPath();
            ctx.rect(10, 10, 100, 100);
            ctx.fill();
            ctx.stroke();
            
            // Draw ellipse
            ctx.fillStyle = "green";
            ctx.beginPath();
            drawEllipse(ctx, 120, 10, 200, 100);
            ctx.fill();
            ctx.stroke();
            
            // Draw rounded rectangle
            ctx.fillStyle = "gray";
            ctx.beginPath();
            drawRoundedRect(ctx, 330, 10, 200, 100, 20, 20);
            ctx.fill();
            ctx.stroke();
            
            // Draw individual lines
            ctx.beginPath();
            ctx.moveTo(550, 30);
            ctx.lineTo(650, 30);
            ctx.moveTo(550, 50);
            ctx.lineTo(650, 50);
            ctx.moveTo(550, 70);
            ctx.lineTo(650, 70);
            ctx.moveTo(550, 90);
            ctx.lineTo(650, 90);
            ctx.stroke();
            
            // Draw lines using points (similar to vector of points)
            ctx.strokeStyle = "red";
            ctx.beginPath();
            ctx.moveTo(660, 30);
            ctx.lineTo(760, 30);
            ctx.moveTo(660, 50);
            ctx.lineTo(760, 50);
            ctx.moveTo(660, 70);
            ctx.lineTo(760, 70);
            ctx.moveTo(660, 90);
            ctx.lineTo(760, 90);
            ctx.stroke();
            
            // Draw polygon
            ctx.strokeStyle = "black";
            ctx.beginPath();
            ctx.moveTo(240.0, 150.0);
            ctx.lineTo(10.0, 150.0);
            ctx.lineTo(60.0, 200.0);
            ctx.lineTo(30.0, 250.0);
            ctx.lineTo(120.0, 250.0);
            ctx.closePath();
            ctx.fill();
            ctx.stroke();
            
            // Draw arc (30° to 270°)
            ctx.beginPath();
            ctx.arc(250.0 + 75.0, 150.0 + 75.0, 75.0, 30 * Math.PI/180, 270 * Math.PI/180);
            ctx.stroke();
            
            // Draw chord (30° to 270°)
            ctx.beginPath();
            ctx.arc(450.0 + 75.0, 150.0 + 75.0, 75.0, 30 * Math.PI/180, 270 * Math.PI/180);
            ctx.closePath();
            ctx.fill();
            ctx.stroke();
            
            // Draw pie (30° to 270°)
            ctx.beginPath();
            ctx.moveTo(650.0 + 75.0, 150.0 + 75.0);
            ctx.arc(650.0 + 75.0, 150.0 + 75.0, 75.0, 30 * Math.PI/180, 270 * Math.PI/180);
            ctx.closePath();
            ctx.fill();
            ctx.stroke();
            
            // Draw text
            ctx.fillStyle = "blue";
            ctx.strokeStyle = "blue";
            ctx.font = "bold 40px Times";
            ctx.fillText("I'm loving Qt", 50.0, 400.0);
            
            // Draw image if available
            if (placeholderImage) {
                ctx.drawImage(placeholderImage, 520.0, 350.0, 200.0, 200.0);
            }
        }
        
        // Helper function to draw an ellipse
        function drawEllipse(ctx, x, y, w, h) {
            var kappa = 0.5522848,
                ox = (w / 2) * kappa, // control point offset horizontal
                oy = (h / 2) * kappa, // control point offset vertical
                xe = x + w,           // x-end
                ye = y + h,           // y-end
                xm = x + w / 2,       // x-middle
                ym = y + h / 2;       // y-middle
            
            ctx.beginPath();
            ctx.moveTo(x, ym);
            ctx.bezierCurveTo(x, ym - oy, xm - ox, y, xm, y);
            ctx.bezierCurveTo(xm + ox, y, xe, ym - oy, xe, ym);
            ctx.bezierCurveTo(xe, ym + oy, xm + ox, ye, xm, ye);
            ctx.bezierCurveTo(xm - ox, ye, x, ym + oy, x, ym);
            ctx.closePath();
        }
        
        // Helper function to draw a rounded rectangle
        function drawRoundedRect(ctx, x, y, width, height, radiusX, radiusY) {
            if (radiusX === undefined) { radiusX = 5; }
            if (radiusY === undefined) { radiusY = 5; }
            
            ctx.beginPath();
            ctx.moveTo(x + radiusX, y);
            ctx.lineTo(x + width - radiusX, y);
            ctx.quadraticCurveTo(x + width, y, x + width, y + radiusY);
            ctx.lineTo(x + width, y + height - radiusY);
            ctx.quadraticCurveTo(x + width, y + height, x + width - radiusX, y + height);
            ctx.lineTo(x + radiusX, y + height);
            ctx.quadraticCurveTo(x, y + height, x, y + height - radiusY);
            ctx.lineTo(x, y + radiusY);
            ctx.quadraticCurveTo(x, y, x + radiusX, y);
            ctx.closePath();
        }
    }
}