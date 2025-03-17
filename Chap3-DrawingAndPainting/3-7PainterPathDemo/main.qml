import QtQuick
import QtQuick.Window
import QtQuick.Controls

Window {
    id: mainWindow
    width: 902
    height: 620
    visible: true
    title: "Painter Path Demo"
    
    Canvas {
        id: drawingCanvas
        anchors.fill: parent
        
        onPaint: {
            var ctx = getContext("2d");
            ctx.clearRect(0, 0, width, height);
            
            // Set line settings for all paths
            ctx.lineWidth = 2;
            ctx.strokeStyle = "black";
            
            // First path: rectangle with line and arc
            ctx.beginPath();
            
            // Add a rectangle to the path
            ctx.rect(100, 100, 100, 100);
            
            // Move to the center of the rectangle
            ctx.moveTo(150, 150);
            
            // Draw a line upward
            ctx.lineTo(150, 50);
            
            // Draw an arc (x, y, radius, startAngle, endAngle, anticlockwise)
            // Converting from Qt angles (1/16th degrees) to radians
            // Qt: arcTo(50, 50, 200, 200, 90, 90) - draws arc from 90° to 180°
            // Canvas: arc(centerX, centerY, radius, startAngle, endAngle, anticlockwise)
            ctx.arc(150, 150, 100, Math.PI/2, Math.PI, false);
            
            // Complete the shape by going back to center
            ctx.lineTo(150, 150);
            
            // Fill the path with green color
            ctx.fillStyle = "green";
            ctx.fill();
            ctx.stroke();
            
            // Label for the first path
            ctx.fillStyle = "black";
            ctx.font = "14px Arial";
            ctx.fillText("Path 1: Rectangle with line and arc", 50, 30);
            
            // Second path: two circles connected by lines
            ctx.beginPath();
            
            // Add two circles to the path
            ctx.arc(150, 270, 50, 0, Math.PI * 2); // First circle
            ctx.moveTo(450, 270);
            ctx.arc(450, 270, 50, 0, Math.PI * 2); // Second circle
            
            // Draw the upper connecting line
            ctx.moveTo(150, 220);
            ctx.lineTo(450, 220);
            
            // Draw the lower connecting line
            ctx.moveTo(150, 320);
            ctx.lineTo(450, 320);
            
            // Draw the path (no fill)
            ctx.stroke();
            
            // Label for the second path
            ctx.fillStyle = "black";
            ctx.fillText("Path 2: Two circles connected by lines", 150, 200);
            
            // Draw a translated copy of the second path
            ctx.beginPath();
            
            // Translate by 150, 150
            var translateX = 150;
            var translateY = 150;
            
            // Add two circles to the path, translated
            ctx.arc(150 + translateX, 270 + translateY, 50, 0, Math.PI * 2); // First circle
            ctx.moveTo(450 + translateX, 270 + translateY);
            ctx.arc(450 + translateX, 270 + translateY, 50, 0, Math.PI * 2); // Second circle
            
            // Draw the upper connecting line, translated
            ctx.moveTo(150 + translateX, 220 + translateY);
            ctx.lineTo(450 + translateX, 220 + translateY);
            
            // Draw the lower connecting line, translated
            ctx.moveTo(150 + translateX, 320 + translateY);
            ctx.lineTo(450 + translateX, 320 + translateY);
            
            // Draw the translated path (no fill)
            ctx.stroke();
            
            // Label for the translated path
            ctx.fillText("Path 2 (Translated by 150,150)", 300, 350);
        }
    }
}