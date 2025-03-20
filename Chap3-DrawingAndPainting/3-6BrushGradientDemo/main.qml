import QtQuick
import QtQuick.Window
import QtQuick.Controls

Window {
    id: mainWindow
    width: 770
    height: 340
    visible: true
    title: "Gradient Brushes Demo"
    
    Canvas {
        id: drawingCanvas
        anchors.fill: parent
        
        onPaint: {
            var ctx = getContext("2d");
            ctx.clearRect(0, 0, width, height);
            
            // Linear Gradient
            // Define the gradient vector (same points as in the original)
            var linearGradient = ctx.createLinearGradient(70, 20, 70, 170);
            linearGradient.addColorStop(0, "red");
            linearGradient.addColorStop(0.5, "gray");
            linearGradient.addColorStop(1, "yellow");
            
            // Draw the rectangle with linear gradient
            ctx.fillStyle = linearGradient;
            ctx.fillRect(20, 20, 100, 300);
            
            // Draw the linear gradient vector as a line
            ctx.beginPath();
            ctx.moveTo(70, 20);
            ctx.lineTo(70, 170);
            ctx.strokeStyle = "black";
            ctx.lineWidth = 2;
            ctx.stroke();
            
            // Draw the gradient again to simulate QGradient.ReflectSpread
            // Since HTML5 Canvas doesn't have a direct equivalent to Qt's spread methods,
            // we need to manually draw the reflection pattern
            var reflectedGradient = ctx.createLinearGradient(70, 170, 70, 320);
            reflectedGradient.addColorStop(0, "yellow");
            reflectedGradient.addColorStop(0.5, "gray");
            reflectedGradient.addColorStop(1, "red");
            
            ctx.fillStyle = reflectedGradient;
            ctx.fillRect(20, 170, 100, 150);
            
            // Radial Gradient
            // Define the gradient with center and radius (same as in the original)
            var radialGradient = ctx.createRadialGradient(280, 170, 0, 280, 170, 75);
            radialGradient.addColorStop(0, "blue");
            radialGradient.addColorStop(1, "yellow");
            
            // To simulate Qt's RepeatSpread, we need to draw concentric circles with alternating gradients
            // First draw the inner gradient
            ctx.fillStyle = radialGradient;
            ctx.fillRect(130, 20, 300, 300);
            
            // Draw additional rings to simulate RepeatSpread
            // Since HTML5 Canvas doesn't have RepeatSpread directly, we'll manually create rings
            for (var i = 1; i <= 2; i++) {
                var repeatRadius = 75 * i;
                var repeatGradient = ctx.createRadialGradient(280, 170, repeatRadius, 280, 170, repeatRadius + 75);
                
                // Alternate the colors for the repeat effect
                if (i % 2 === 1) {
                    repeatGradient.addColorStop(0, "yellow");
                    repeatGradient.addColorStop(1, "blue");
                } else {
                    repeatGradient.addColorStop(0, "blue");
                    repeatGradient.addColorStop(1, "yellow");
                }
                
                ctx.fillStyle = repeatGradient;
                
                // Use clip to create ring shapes
                ctx.save();
                ctx.beginPath();
                ctx.arc(280, 170, repeatRadius + 75, 0, Math.PI * 2);
                ctx.clip();
                ctx.fillRect(130, 20, 300, 300);
                ctx.restore();
            }
            
            // Draw border around the radial gradient rectangle
            ctx.strokeStyle = "black";
            ctx.lineWidth = 1;
            ctx.strokeRect(130, 20, 300, 300);
            
            // Conical Gradient
            // HTML5 Canvas doesn't have conical gradients directly
            // We'll simulate it by drawing pie segments
            var centerX = 600;
            var centerY = 170;
            var radius = 150;
            
            // Draw many small pie segments to approximate a conical gradient
            var segments = 180;
            var angleStep = (Math.PI * 2) / segments;
            var startAngle = Math.PI / 2; // 90 degrees, same as original
            
            for (var i = 0; i < segments; i++) {
                var ratio = i / segments;
                
                // Interpolate between blue and yellow based on angle
                var r = Math.round(0 + (255 * ratio));
                var g = Math.round(0 + (255 * ratio));
                var b = Math.round(255 - (255 * ratio));
                
                var color = "rgb(" + r + "," + g + "," + b + ")";
                
                ctx.beginPath();
                ctx.moveTo(centerX, centerY);
                ctx.arc(centerX, centerY, radius, startAngle + (i * angleStep), 
                       startAngle + ((i + 1) * angleStep));
                ctx.closePath();
                
                ctx.fillStyle = color;
                ctx.fill();
            }
            
            // Labels
            ctx.fillStyle = "black";
            ctx.font = "14px Arial";
            ctx.fillText("Linear Gradient", 25, 40);
            ctx.fillText("ReflectSpread", 25, 60);
            
            ctx.fillText("Radial Gradient", 160, 40);
            ctx.fillText("RepeatSpread", 160, 60);
            
            ctx.fillText("Conical Gradient", 530, 40);
            ctx.fillText("Start Angle: 90°", 530, 60);
        }
    }
}