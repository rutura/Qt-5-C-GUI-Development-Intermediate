import QtQuick

// Traffic light indicator that shows system status
Item {
    id: indicator
    implicitWidth: 120
    implicitHeight: 350
    
    // State properties
    property bool greenActive: false
    property bool redActive: false
    property bool yellowActive: false
    property bool lightsOn: true
    
    // Function to activate normal state (green light)
    function activateNormal() {
        greenActive = true;
        yellowActive = false;
        redActive = false;
        canvas.requestPaint();
    }
    
    // Function to activate warning state (yellow light)
    function activateWarning() {
        yellowActive = true;
        greenActive = false;
        redActive = false;
        canvas.requestPaint();
    }
    
    // Function to activate danger state (red light)
    function activateDanger() {
        redActive = true;
        greenActive = false;
        yellowActive = false;
        canvas.requestPaint();
    }
    
    // Timer for blinking effect
    Timer {
        interval: 300
        running: true
        repeat: true
        onTriggered: {
            lightsOn = !lightsOn;
            canvas.requestPaint();
        }
    }
    
    // Canvas for custom drawing
    Canvas {
        id: canvas
        anchors.fill: parent
        
        onPaint: {
            var ctx = getContext("2d");
            
            // Clear canvas
            ctx.clearRect(0, 0, width, height);
            
            // Draw traffic light box
            ctx.lineWidth = 3;
            ctx.strokeStyle = "black";
            ctx.fillStyle = "gray";
            ctx.beginPath();
            ctx.rect(0, 0, 120, 330);
            ctx.fill();
            ctx.stroke();
            
            // Draw lights based on state
            if (redActive) {
                // Red light active
                ctx.fillStyle = lightsOn ? "red" : "black";
                ctx.beginPath();
                ctx.ellipse(10, 10, 100, 100);
                ctx.fill();
                ctx.stroke();
                
                ctx.fillStyle = "black";
                ctx.beginPath();
                ctx.ellipse(10, 115, 100, 100);
                ctx.fill();
                ctx.stroke();
                
                ctx.fillStyle = "black";
                ctx.beginPath();
                ctx.ellipse(10, 220, 100, 100);
                ctx.fill();
                ctx.stroke();
            } 
            else if (greenActive) {
                // Green light active
                ctx.fillStyle = "black";
                ctx.beginPath();
                ctx.ellipse(10, 10, 100, 100);
                ctx.fill();
                ctx.stroke();
                
                ctx.fillStyle = lightsOn ? "green" : "black";
                ctx.beginPath();
                ctx.ellipse(10, 115, 100, 100);
                ctx.fill();
                ctx.stroke();
                
                ctx.fillStyle = "black";
                ctx.beginPath();
                ctx.ellipse(10, 220, 100, 100);
                ctx.fill();
                ctx.stroke();
            } 
            else if (yellowActive) {
                // Yellow light active
                ctx.fillStyle = "black";
                ctx.beginPath();
                ctx.ellipse(10, 10, 100, 100);
                ctx.fill();
                ctx.stroke();
                
                ctx.fillStyle = "black";
                ctx.beginPath();
                ctx.ellipse(10, 115, 100, 100);
                ctx.fill();
                ctx.stroke();
                
                ctx.fillStyle = lightsOn ? "yellow" : "black";
                ctx.beginPath();
                ctx.ellipse(10, 220, 100, 100);
                ctx.fill();
                ctx.stroke();
            }
        }
    }
    
    // Set initial state
    Component.onCompleted: activateNormal()
}