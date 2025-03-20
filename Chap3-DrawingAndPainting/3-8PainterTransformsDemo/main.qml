import QtQuick
import QtQuick.Window
import QtQuick.Controls

Window {
    id: mainWindow
    width: 871
    height: 780
    visible: true
    title: "Painter Transformations Demo"
    
    Canvas {
        id: drawingCanvas
        anchors.fill: parent
        
        onPaint: {
            var ctx = getContext("2d");
            ctx.clearRect(0, 0, width, height);
            
            // Set up pen equivalent
            ctx.lineWidth = 5;
            ctx.strokeStyle = "black";
            
            // Draw original rectangle (black)
            ctx.beginPath();
            ctx.rect(100, 100, 200, 200);
            ctx.stroke();
            
            // Add a label for the black rectangle
            ctx.fillStyle = "black";
            ctx.font = "14px Arial";
            ctx.fillText("Original Rectangle (Black)", 100, 80);
            
            // Rotate the coordinate system and draw rectangle (green)
            ctx.save(); // Save the current state
            
            // 1. Translate to the center of the rectangle
            ctx.translate(200, 200);
            // 2. Apply rotation (convert 45 degrees to radians)
            ctx.rotate(45 * Math.PI / 180);
            // 3. Translate back
            ctx.translate(-200, -200);
            
            ctx.strokeStyle = "green";
            ctx.beginPath();
            ctx.rect(100, 100, 200, 200);
            ctx.stroke();
            
            // Add a label for the green rectangle
            ctx.fillStyle = "green";
            ctx.fillText("Rotated Rectangle (Green)", 300, 320);
            
            // Scale the coordinate system and draw rectangle (blue)
            // 1. Translate to the center of the rectangle
            ctx.translate(200, 200);
            // 2. Undo the previous rotation
            ctx.rotate(-45 * Math.PI / 180);
            // 3. Apply scaling
            ctx.scale(0.6, 0.6);
            // 4. Translate back
            ctx.translate(-200, -200);
            
            ctx.strokeStyle = "blue";
            ctx.beginPath();
            ctx.rect(100, 100, 200, 200);
            ctx.stroke();
            
            // Add a label for the blue rectangle
            ctx.fillStyle = "blue";
            ctx.fillText("Scaled Rectangle (Blue)", 140, 170);
            
            ctx.restore(); // Restore to the original state
            
            // Reset all transformations and draw the original rectangle again (red)
            ctx.strokeStyle = "red";
            ctx.beginPath();
            ctx.rect(100, 100, 200, 200);
            ctx.stroke();
            
            // Add a label for the red rectangle
            ctx.fillStyle = "red";
            ctx.fillText("Reset Transformation (Red)", 110, 320);
            
            // Apply shearing transformation and draw rectangle (yellow)
            ctx.save(); // Save the current state
            
            // 1. Translate to the center of the rectangle
            ctx.translate(200, 200);
            // 2. Apply shearing (using transform matrix)
            // transform(a, b, c, d, e, f) is equivalent to:
            // | a c e |
            // | b d f |
            // | 0 0 1 |
            // For shear(0.6, 0.6) we need:
            // | 1 0.6 0 |
            // | 0.6 1 0 |
            // | 0   0 1 |
            ctx.transform(1, 0.6, 0.6, 1, 0, 0);
            // 3. Translate back
            ctx.translate(-200, -200);
            
            ctx.strokeStyle = "yellow";
            ctx.beginPath();
            ctx.rect(100, 100, 200, 200);
            ctx.stroke();
            
            // Add a label for the yellow rectangle
            ctx.fillStyle = "yellow";
            ctx.fillText("Sheared Rectangle (Yellow)", 270, 120);
            
            ctx.restore(); // Restore to the original state
            
            // Draw legend with explanations
            ctx.fillStyle = "black";
            ctx.font = "16px Arial";
            ctx.fillText("Transformation Examples:", 450, 120);
            ctx.font = "14px Arial";
            ctx.fillText("Black: Original rectangle", 450, 150);
            ctx.fillText("Green: Rotated 45°", 450, 180);
            ctx.fillText("Blue: Scaled to 60% after rotation", 450, 210);
            ctx.fillText("Red: Reset to original", 450, 240);
            ctx.fillText("Yellow: Sheared (0.6, 0.6)", 450, 270);
        }
    }
}