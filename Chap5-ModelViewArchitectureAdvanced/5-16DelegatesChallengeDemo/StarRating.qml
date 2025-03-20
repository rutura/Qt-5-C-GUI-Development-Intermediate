import QtQuick
import QtQuick.Controls

Item {
    id: root
    
    property int rating: 0
    property int maxRating: 5
    property bool readOnly: false
    property color starColor: "black"
    property color hoverColor: "yellow"
    property color backgroundColor: "green"
    
    signal edited(int newRating)
    
    width: starRow.width
    height: starRow.height
    
    Rectangle {
        id: background
        anchors.fill: parent
        color: readOnly ? "transparent" : backgroundColor
        visible: !readOnly && mouseArea.containsMouse
    }
    
    // Mouse area for tracking entire component
    MouseArea {
        id: mouseArea
        anchors.fill: parent
        hoverEnabled: !readOnly
        enabled: !readOnly
        
        onClicked: {
            if (!readOnly) {
                // Calculate the star based on X position
                var star = Math.floor(mouseX / (starRow.width / maxRating)) + 1
                star = Math.max(1, Math.min(maxRating, star))
                rating = star
                edited(rating)
            }
        }
        
        onPositionChanged: {
            if (!readOnly) {
                // Update hover effect
                var position = Math.floor(mouseX / (starRow.width / maxRating))
                for (var i = 0; i < starRepeater.count; i++) {
                    var starItem = starRepeater.itemAt(i)
                    if (starItem) {
                        starItem.hovered = (i <= position)
                    }
                }
            }
        }
        
        onExited: {
            // Reset hover effects
            if (!readOnly) {
                for (var i = 0; i < starRepeater.count; i++) {
                    var starItem = starRepeater.itemAt(i)
                    if (starItem) {
                        starItem.hovered = false
                    }
                }
            }
        }
    }
    
    Row {
        id: starRow
        spacing: 2
        
        Repeater {
            id: starRepeater
            model: maxRating
            
            Item {
                id: starItem
                width: 20
                height: 20
                property bool hovered: false
                
                // Star shape using Canvas
                Canvas {
                    anchors.fill: parent
                    contextType: "2d"
                    
                    onPaint: {
                        var ctx = getContext("2d")
                        ctx.clearRect(0, 0, width, height)
                        
                        // Determine if star should be filled
                        var filled = index < rating || starItem.hovered
                        
                        // Set fill color
                        ctx.fillStyle = starItem.hovered ? hoverColor : starColor
                        ctx.strokeStyle = starColor
                        ctx.lineWidth = 1
                        
                        // Draw a star shape
                        var cx = width / 2
                        var cy = height / 2
                        var outerRadius = width / 2 - 1
                        var innerRadius = outerRadius * 0.4
                        var points = 5
                        
                        ctx.beginPath()
                        for (var i = 0; i < points * 2; i++) {
                            var radius = (i % 2 === 0) ? outerRadius : innerRadius
                            var angle = (Math.PI * 2 * i) / (points * 2) - Math.PI / 2
                            var x = cx + radius * Math.cos(angle)
                            var y = cy + radius * Math.sin(angle)
                            
                            if (i === 0) ctx.moveTo(x, y)
                            else ctx.lineTo(x, y)
                        }
                        ctx.closePath()
                        
                        // Fill if needed
                        if (filled) {
                            ctx.fill()
                        }
                        ctx.stroke()
                    }
                    
                    // Redraw when properties change
                    Component.onCompleted: requestPaint()
                    onWidthChanged: requestPaint()
                    onHeightChanged: requestPaint()
                }
                
                // Ensure redraw when star state changes
                onHoveredChanged: {
                    children[0].requestPaint()
                }
            }
        }
    }
    
    // Redraw stars when rating changes
    onRatingChanged: {
        for (var i = 0; i < starRepeater.count; i++) {
            var starItem = starRepeater.itemAt(i)
            if (starItem && starItem.children[0]) {
                starItem.children[0].requestPaint()
            }
        }
    }
}