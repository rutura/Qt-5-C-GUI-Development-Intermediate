import QtQuick
import QtQuick.Window
import QtQuick.Layouts
import QtQuick.Controls

Window {
    id: mainWindow
    width: 400
    height: 300
    visible: true
    title: "Pixmap Demo"
    
    // Main layout to match the original widget layout
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 11
        spacing: 6
        
        // Canvas component to replace QPixmap painting
        Canvas {
            id: pixmapCanvas
            Layout.fillWidth: true
            Layout.fillHeight: true
            
            // Track the current size to handle resizing
            property int canvasWidth: width - 10
            property int canvasHeight: height - 10
            
            // Redraw when size changes
            onWidthChanged: requestPaint()
            onHeightChanged: requestPaint()
            
            // Main drawing function
            onPaint: {
                var ctx = getContext("2d");
                ctx.reset();
                
                // Create the equivalent of our pixmap with a gray background
                ctx.fillStyle = "gray";
                ctx.fillRect(0, 0, canvasWidth, canvasHeight);
                
                // Set up pen and brush equivalent
                ctx.lineWidth = 5;
                ctx.strokeStyle = "white";
                ctx.fillStyle = "green";
                
                // Set up font equivalent
                ctx.font = "bold 20px Consolas";
                
                // Draw a rectangle around the border (like pixmap.rect())
                ctx.strokeRect(0, 0, canvasWidth, canvasHeight);
                
                // Change brush color and draw another rectangle
                ctx.fillStyle = "blue";
                ctx.fillRect(50, 50, 100, 100);
                
                // Draw text
                ctx.fillStyle = "white";
                ctx.fillText("I'm loving Qt", 30, 120);
                
                // Log coordinate system info (like the original print statements)
                console.log("Canvas logical coordinates: 0, 0, " + canvasWidth + ", " + canvasHeight);
                console.log("Canvas physical coordinates: 0, 0, " + width + ", " + height);
            }
        }
    }
}