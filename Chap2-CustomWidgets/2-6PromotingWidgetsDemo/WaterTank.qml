import QtQuick

// Water tank component with water level monitoring
Item {
    id: waterTank
    implicitWidth: 400
    implicitHeight: 400
    
    // Water level property
    property int waterHeight: 50
    
    // Define signals
    signal normal()   // Green - normal water level
    signal warning()  // Yellow - warning water level
    signal danger()   // Red - danger water level
    
    // Function to update water level and emit appropriate signals
    function updateWaterLevel() {
        waterHeight += 15;
        canvas.requestPaint();
        
        // Emit signals based on water level
        if (waterHeight <= 210) {
            normal();
        } else if (waterHeight <= 239) {
            warning();
        } else {
            danger();
        }
    }
    
    // Timer for automatic water level increase
    Timer {
        interval: 1000
        running: true
        repeat: true
        onTriggered: updateWaterLevel()
    }
    
    // Canvas for custom drawing
    Canvas {
        id: canvas
        anchors.fill: parent
        
        onPaint: {
            var ctx = getContext("2d");
            
            // Clear canvas
            ctx.clearRect(0, 0, width, height);
            
            // Draw tank walls
            ctx.lineWidth = 3;
            ctx.strokeStyle = "black";
            
            // Draw the tank walls
            ctx.beginPath();
            ctx.moveTo(10, 10);
            ctx.lineTo(10, 300);    // Left
            ctx.lineTo(300, 300);   // Bottom
            ctx.lineTo(300, 10);    // Right
            ctx.stroke();
            
            // Draw the water
            ctx.fillStyle = "blue";
            ctx.beginPath();
            ctx.rect(10, 300 - waterHeight, 290, waterHeight);
            ctx.fill();
        }
    }
    
    // Handle mouse wheel events to decrease water level
    MouseArea {
        anchors.fill: parent
        onWheel: function(wheel) {
            if (wheel.angleDelta.y < 0 && waterHeight > 10) {
                waterHeight -= 10;
                canvas.requestPaint();
                
                // Emit signals based on updated water level
                if (waterHeight <= 210) {
                    normal();
                } else if (waterHeight <= 239) {
                    warning();
                } else {
                    danger();
                }
            }
        }
    }
}