import QtQuick

Item {
    id: root
    
    property int rating: 0
    property int maxRating: 5
    property bool readOnly: false
    property color starColor: "black"
    property color hoverColor: "yellow"
    property color backgroundColor: "green"
    property color textColor: "white"  // Ensure text is visible on colored backgrounds
    
    // Custom signal for editing
    signal edited(int newRating)
    
    width: row.width
    height: row.height
    
    // Main row containing the stars
    Row {
        id: row
        spacing: 2
        
        // Create the stars
        Repeater {
            id: starRepeater
            model: root.maxRating
            
            // Star shape (using Canvas for customizability)
            Canvas {
                id: canvas
                width: 20
                height: 20
                property bool containsMouse: mouseArea.containsMouse
                property int starIndex: index
                
                onPaint: {
                    var ctx = getContext("2d");
                    ctx.clearRect(0, 0, width, height);
                    
                    // Fill background if in editor mode
                    if (!root.readOnly && canvas.containsMouse) {
                        ctx.fillStyle = root.backgroundColor;
                        ctx.fillRect(0, 0, width, height);
                    }
                    
                    // Set star color based on rating and mouse
                    if (index < root.rating) {
                        ctx.fillStyle = root.starColor;
                    } else if (!root.readOnly && canvas.containsMouse && index <= mouseArea.starRating) {
                        ctx.fillStyle = root.hoverColor;
                    } else {
                        ctx.fillStyle = "transparent";
                    }
                    
                    ctx.strokeStyle = root.starColor;
                    ctx.lineWidth = 1;
                    
                    // Create star path (5-point star)
                    ctx.beginPath();
                    
                    // Calculate star points
                    var centerX = width / 2;
                    var centerY = height / 2;
                    var outerRadius = width / 2;
                    var innerRadius = outerRadius * 0.4;
                    var startAngle = -Math.PI / 2; // Start at top
                    
                    for (var i = 0; i < 10; i++) {
                        var radius = i % 2 === 0 ? outerRadius : innerRadius;
                        var angle = startAngle + (i * Math.PI) / 5;
                        var x = centerX + radius * Math.cos(angle);
                        var y = centerY + radius * Math.sin(angle);
                        
                        if (i === 0) {
                            ctx.moveTo(x, y);
                        } else {
                            ctx.lineTo(x, y);
                        }
                    }
                    
                    ctx.closePath();
                    ctx.fill();
                    ctx.stroke();
                }
                
                // Handle mouse interaction
                MouseArea {
                    id: mouseArea
                    anchors.fill: parent
                    enabled: !root.readOnly
                    hoverEnabled: !root.readOnly
                    property int starRating: index
                    
                    onEntered: {
                        canvas.requestPaint();
                        updateStarPainting(index);
                    }
                    
                    onExited: {
                        canvas.requestPaint();
                        updateStarPainting(-1);
                    }
                    
                    onPositionChanged: {
                        updateStarPainting(index);
                    }
                    
                    onClicked: {
                        if (!root.readOnly) {
                            root.rating = index + 1;
                            root.edited(root.rating);
                        }
                    }
                }
            }
        }
    }
    
    // Function to update all star canvases
    function updateStarPainting(hoverIndex) {
        // Access canvases through the repeater items
        for (var i = 0; i < starRepeater.count; i++) {
            var item = starRepeater.itemAt(i);
            if (item) {
                item.requestPaint();
            }
        }
    }
}