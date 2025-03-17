import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

Window {
    id: mainWindow
    width: 400
    height: 350  // Added extra height for coordinate display
    visible: true
    title: "Coordinate Systems Demo"
    
    // Property to store coordinate information
    property string logicalCoords: ""
    property string physicalCoords: ""
    
    // Text area to display coordinate information
    Rectangle {
        id: infoArea
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        height: 50
        color: "lightgray"
        
        Label {
            anchors.fill: parent
            anchors.margins: 5
            text: "Logical coordinates: " + logicalCoords + "\n" +
                  "Physical coordinates: " + physicalCoords
            font.family: "Monospace"
        }
    }
    
    // Canvas for drawing
    Canvas {
        id: drawingCanvas
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: infoArea.top
        
        // Draw equivalent of QPainter demonstration
        onPaint: {
            var ctx = getContext("2d");
            
            // Get the current canvas dimensions for display
            mainWindow.logicalCoords = "0, 0, " + width + ", " + height;
            mainWindow.physicalCoords = "0, 0, " + width + ", " + height;
            
            // Clear canvas
            ctx.clearRect(0, 0, width, height);
            
            // Draw a red rectangle using default coordinates (equivalent to first rect)
            ctx.lineWidth = 3;
            ctx.strokeStyle = "red";
            ctx.strokeRect(50, 50, 100, 100);
            
            // Save the current state
            ctx.save();
            
            // Change the logical coordinates (equivalent to setWindow)
            // Scale the context to simulate a logical window of 300x200
            var scaleX = width / 300;
            var scaleY = height / 200;
            ctx.scale(scaleX, scaleY);
            
            // Draw a green rectangle with modified logical coordinates
            ctx.lineWidth = 3 / scaleX;  // Adjust line width for scaling
            ctx.strokeStyle = "green";
            ctx.strokeRect(50, 50, 100, 100);
            
            // Restore to default state
            ctx.restore();
            
            // Save the current state again
            ctx.save();
            
            // Change physical coordinates (equivalent to setViewport)
            // Translate and scale to simulate a viewport of 300x200
            var vpScaleX = 300 / width;
            var vpScaleY = 200 / height;
            ctx.scale(vpScaleX, vpScaleY);
            
            // Draw a blue rectangle with modified physical coordinates
            ctx.lineWidth = 3 / vpScaleX;  // Adjust line width for scaling
            ctx.strokeStyle = "blue";
            ctx.strokeRect(50, 50, 100, 100);
            
            // Restore to default state
            ctx.restore();
            
            // Add text labels for each rectangle
            ctx.font = "12px sans-serif";
            ctx.fillStyle = "black";
            ctx.fillText("Default coordinates (red)", 60, 170);
            ctx.fillText("Modified logical coordinates (green)", 180, 90);
            ctx.fillText("Modified physical coordinates (blue)", 200, 220);
        }
    }
    
    // Button to redraw and show updated coordinates
    Button {
        anchors.right: parent.right
        anchors.bottom: infoArea.top
        anchors.margins: 5
        text: "Refresh"
        onClicked: drawingCanvas.requestPaint()
    }
}