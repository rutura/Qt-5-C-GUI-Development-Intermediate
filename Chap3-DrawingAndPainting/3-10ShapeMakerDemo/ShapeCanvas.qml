import QtQuick
import QtQuick.Controls

Item {
    id: root
    implicitWidth: 400
    implicitHeight: 200
    
    // Exposed properties for drawing configuration
    property int shapeType: 0  // Polygon by default
    property int penWidth: 1
    property int penStyle: Qt.SolidLine
    property int penCap: Qt.FlatCap
    property int penJoin: Qt.MiterJoin
    property int brushStyle: 4  // Solid by default
    property bool antialiased: false
    property bool transformed: false
    
    // Enumeration for shape types
    readonly property var shapeTypes: {
        "Polygon": 0,
        "Rect": 1,
        "RoundedRect": 2,
        "Ellipse": 3,
        "Pie": 4,
        "Chord": 5,
        "Text": 6,
        "Pixmap": 7
    }
    
    // Enumeration for brush styles
    readonly property var brushStyles: {
        "LinearGradient": 0,
        "RadialGradient": 1,
        "ConicalGradient": 2,
        "Texture": 3,
        "Solid": 4,
        "Horizontal": 5,
        "Vertical": 6,
        "Cross": 7,
        "BDiag": 8,
        "FDiag": 9,
        "DiagCross": 10,
        "NoBrush": 11
    }
    
    // Helper function to apply pen style to canvas context
    function applyPenStyle(ctx) {
        // Set line width
        ctx.lineWidth = penWidth
        
        // Set line cap style
        switch (penCap) {
            case Qt.RoundCap:
                ctx.lineCap = "round"
                break
            case Qt.SquareCap:
                ctx.lineCap = "square"
                break
            default:
                ctx.lineCap = "butt"  // FlatCap
        }
        
        // Set line join style
        switch (penJoin) {
            case Qt.RoundJoin:
                ctx.lineJoin = "round"
                break
            case Qt.BevelJoin:
                ctx.lineJoin = "bevel"
                break
            default:
                ctx.lineJoin = "miter"  // MiterJoin
        }
        
        // Set line dash pattern based on pen style
        switch (penStyle) {
            case Qt.DashLine:
                ctx.setLineDash([4, 2])
                break
            case Qt.DotLine:
                ctx.setLineDash([1, 2])
                break
            case Qt.DashDotLine:
                ctx.setLineDash([4, 2, 1, 2])
                break
            case Qt.DashDotDotLine:
                ctx.setLineDash([4, 2, 1, 2, 1, 2])
                break
            case Qt.NoPen:
                ctx.strokeStyle = "transparent"
                break
            default:
                // Solid line
                ctx.setLineDash([])
        }
    }
    
    // Helper function to apply brush style to canvas context
    function applyBrushStyle(ctx, x, y, width, height) {
        switch (brushStyle) {
            case brushStyles.LinearGradient: {
                let gradient = ctx.createLinearGradient(x, y, x + width, y + height)
                gradient.addColorStop(0.0, "red")
                gradient.addColorStop(0.2, "green")
                gradient.addColorStop(1.0, "blue")
                ctx.fillStyle = gradient
                break
            }
            case brushStyles.RadialGradient: {
                let centerX = x + width/2
                let centerY = y + height/2
                let radius = Math.min(width, height)/2
                let gradient = ctx.createRadialGradient(
                    centerX, centerY, 0,
                    centerX + width/5, centerY + height/5, radius
                )
                gradient.addColorStop(0.0, "red")
                gradient.addColorStop(0.2, "green")
                gradient.addColorStop(1.0, "blue")
                ctx.fillStyle = gradient
                break
            }
            case brushStyles.ConicalGradient:
                // HTML Canvas doesn't directly support conical gradients
                // Using a radial gradient as a visual approximation
                let centerX = x + width/2
                let centerY = y + height/2
                let radius = Math.min(width, height)/2
                let gradient = ctx.createRadialGradient(
                    centerX, centerY, 0,
                    centerX, centerY, radius
                )
                gradient.addColorStop(0.0, "red")
                gradient.addColorStop(0.2, "green")
                gradient.addColorStop(1.0, "blue")
                ctx.fillStyle = gradient
                break
            case brushStyles.Texture:
                if (textureImg.status === Image.Ready) {
                    let pattern = ctx.createPattern(textureImg, "repeat")
                    ctx.fillStyle = pattern
                } else {
                    ctx.fillStyle = "darkCyan"
                }
                break
            case brushStyles.Solid:
                ctx.fillStyle = "blue"
                break
            case brushStyles.Horizontal:
                // Creating a pattern for horizontal lines
                let hPattern = ctx.createPattern(horizontalPattern, "repeat")
                ctx.fillStyle = hPattern
                break
            case brushStyles.Vertical:
                // Creating a pattern for vertical lines
                let vPattern = ctx.createPattern(verticalPattern, "repeat")
                ctx.fillStyle = vPattern
                break
            case brushStyles.Cross:
                // Creating a pattern for crossed lines
                let cPattern = ctx.createPattern(crossPattern, "repeat")
                ctx.fillStyle = cPattern
                break
            case brushStyles.BDiag:
                // Creating a pattern for backward diagonal lines
                let bdPattern = ctx.createPattern(bdiagPattern, "repeat")
                ctx.fillStyle = bdPattern
                break
            case brushStyles.FDiag:
                // Creating a pattern for forward diagonal lines
                let fdPattern = ctx.createPattern(fdiagPattern, "repeat")
                ctx.fillStyle = fdPattern
                break
            case brushStyles.DiagCross:
                // Creating a pattern for diagonal crossed lines
                let dcPattern = ctx.createPattern(diagCrossPattern, "repeat")
                ctx.fillStyle = dcPattern
                break
            case brushStyles.NoBrush:
                ctx.fillStyle = "transparent"
                break
            default:
                ctx.fillStyle = "blue"
        }
    }
    
    // Helper function to draw a shape
    function drawShape(ctx, shapeType, x, y, width, height) {
        // Apply transformation if enabled
        if (transformed) {
            ctx.save()
            ctx.translate(x + width/2, y + height/2)
            ctx.rotate(Math.PI/3)  // 60 degrees
            ctx.scale(0.6, 0.9)
            ctx.translate(-(x + width/2), -(y + height/2))
        }
        
        // Draw the selected shape
        switch (shapeType) {
            case shapeTypes.Polygon:
                // Define polygon points
                ctx.beginPath()
                ctx.moveTo(x + 10, y + 80)
                ctx.lineTo(x + 20, y + 10)
                ctx.lineTo(x + 80, y + 30)
                ctx.lineTo(x + 90, y + 70)
                ctx.closePath()
                ctx.fill()
                ctx.stroke()
                break
                
            case shapeTypes.Rect:
                ctx.fillRect(x, y, width, height)
                ctx.strokeRect(x, y, width, height)
                break
                
            case shapeTypes.RoundedRect:
                // Draw rounded rectangle
                const radius = Math.min(width, height) * 0.25
                ctx.beginPath()
                ctx.moveTo(x + radius, y)
                ctx.lineTo(x + width - radius, y)
                ctx.arcTo(x + width, y, x + width, y + radius, radius)
                ctx.lineTo(x + width, y + height - radius)
                ctx.arcTo(x + width, y + height, x + width - radius, y + height, radius)
                ctx.lineTo(x + radius, y + height)
                ctx.arcTo(x, y + height, x, y + height - radius, radius)
                ctx.lineTo(x, y + radius)
                ctx.arcTo(x, y, x + radius, y, radius)
                ctx.closePath()
                ctx.fill()
                ctx.stroke()
                break
                
            case shapeTypes.Ellipse:
                ctx.beginPath()
                ctx.ellipse(
                    x + width/2, y + height/2,
                    width/2, height/2,
                    0, 0, Math.PI * 2, false
                )
                ctx.fill()
                ctx.stroke()
                break
                
            case shapeTypes.Pie:
                // Draw pie (arc with lines to center)
                ctx.beginPath()
                ctx.moveTo(x + width/2, y + height/2)
                ctx.arc(
                    x + width/2, y + height/2,
                    Math.min(width, height)/2,
                    (20 * Math.PI)/180,
                    ((20 + 120) * Math.PI)/180,
                    false
                )
                ctx.closePath()
                ctx.fill()
                ctx.stroke()
                break
                
            case shapeTypes.Chord:
                // Draw chord (arc with line connecting the endpoints)
                ctx.beginPath()
                let startAngle = (20 * Math.PI)/180
                let endAngle = ((20 + 120) * Math.PI)/180
                let chordRadius = Math.min(width, height)/2
                let centerX = x + width/2
                let centerY = y + height/2
                
                let startX = centerX + chordRadius * Math.cos(startAngle)
                let startY = centerY + chordRadius * Math.sin(startAngle)
                let endX = centerX + chordRadius * Math.cos(endAngle)
                let endY = centerY + chordRadius * Math.sin(endAngle)
                
                ctx.moveTo(startX, startY)
                ctx.arc(centerX, centerY, chordRadius, startAngle, endAngle, false)
                ctx.lineTo(startX, startY)
                ctx.fill()
                ctx.stroke()
                break
                
            case shapeTypes.Text:
                ctx.font = "bold 8px Consolas"
                ctx.textAlign = "center"
                ctx.textBaseline = "middle"
                ctx.fillText("Qt GUI", x + width/2, y + height/2)
                ctx.strokeText("Qt GUI", x + width/2, y + height/2)
                break
                
            case shapeTypes.Pixmap:
                if (textureImg.status === Image.Ready) {
                    ctx.drawImage(textureImg, x + 10, y + 10)
                } else {
                    // Fallback
                    ctx.fillStyle = "darkCyan"
                    ctx.fillRect(x + 10, y + 10, 50, 50)
                }
                break
        }
        
        // Restore transformation if enabled
        if (transformed) {
            ctx.restore()
        }
    }
    
    // Create off-screen canvases for brush patterns
    Canvas {
        id: horizontalPattern
        width: 8; height: 8
        visible: false
        onPaint: {
            var ctx = getContext("2d")
            ctx.fillStyle = "transparent"
            ctx.fillRect(0, 0, width, height)
            ctx.strokeStyle = "blue"
            ctx.beginPath()
            ctx.moveTo(0, 4)
            ctx.lineTo(8, 4)
            ctx.stroke()
        }
        Component.onCompleted: requestPaint()
    }
    
    Canvas {
        id: verticalPattern
        width: 8; height: 8
        visible: false
        onPaint: {
            var ctx = getContext("2d")
            ctx.fillStyle = "transparent"
            ctx.fillRect(0, 0, width, height)
            ctx.strokeStyle = "blue"
            ctx.beginPath()
            ctx.moveTo(4, 0)
            ctx.lineTo(4, 8)
            ctx.stroke()
        }
        Component.onCompleted: requestPaint()
    }
    
    Canvas {
        id: crossPattern
        width: 8; height: 8
        visible: false
        onPaint: {
            var ctx = getContext("2d")
            ctx.fillStyle = "transparent"
            ctx.fillRect(0, 0, width, height)
            ctx.strokeStyle = "blue"
            ctx.beginPath()
            ctx.moveTo(0, 4)
            ctx.lineTo(8, 4)
            ctx.moveTo(4, 0)
            ctx.lineTo(4, 8)
            ctx.stroke()
        }
        Component.onCompleted: requestPaint()
    }
    
    Canvas {
        id: bdiagPattern
        width: 8; height: 8
        visible: false
        onPaint: {
            var ctx = getContext("2d")
            ctx.fillStyle = "transparent"
            ctx.fillRect(0, 0, width, height)
            ctx.strokeStyle = "blue"
            ctx.beginPath()
            ctx.moveTo(0, 8)
            ctx.lineTo(8, 0)
            ctx.stroke()
        }
        Component.onCompleted: requestPaint()
    }
    
    Canvas {
        id: fdiagPattern
        width: 8; height: 8
        visible: false
        onPaint: {
            var ctx = getContext("2d")
            ctx.fillStyle = "transparent"
            ctx.fillRect(0, 0, width, height)
            ctx.strokeStyle = "blue"
            ctx.beginPath()
            ctx.moveTo(0, 0)
            ctx.lineTo(8, 8)
            ctx.stroke()
        }
        Component.onCompleted: requestPaint()
    }
    
    Canvas {
        id: diagCrossPattern
        width: 8; height: 8
        visible: false
        onPaint: {
            var ctx = getContext("2d")
            ctx.fillStyle = "transparent"
            ctx.fillRect(0, 0, width, height)
            ctx.strokeStyle = "blue"
            ctx.beginPath()
            ctx.moveTo(0, 0)
            ctx.lineTo(8, 8)
            ctx.moveTo(0, 8)
            ctx.lineTo(8, 0)
            ctx.stroke()
        }
        Component.onCompleted: requestPaint()
    }
    
    // Image for texture and pixmap
    Image {
        id: textureImg
        source: controller.pixmapPath
        visible: false
        
        // Create fallback if image loading fails
        onStatusChanged: {
            if (status === Image.Error) {
                textureCanvas.requestPaint()
            }
        }
    }
    
    // Fallback canvas for textures
    Canvas {
        id: textureCanvas
        width: 50
        height: 50
        visible: false
        onPaint: {
            var ctx = getContext("2d")
            ctx.fillStyle = "darkCyan"
            ctx.fillRect(0, 0, width, height)
        }
    }
    
    // Main canvas for drawing shapes
    Canvas {
        id: canvas
        anchors.fill: parent
        
        // Request painting when component is loaded
        Component.onCompleted: requestPaint()
        
        // Handle painting event
        onPaint: {
            var ctx = getContext("2d")
            ctx.reset()
            
            // Apply antialiasing if enabled
            ctx.imageSmoothingEnabled = antialiased
            
            // Draw shapes in a grid pattern
            let gridSize = 100
            for (let x = 0; x < width; x += gridSize) {
                for (let y = 0; y < height; y += gridSize) {
                    ctx.save()
                    
                    // Set up pen properties
                    ctx.strokeStyle = "black"
                    applyPenStyle(ctx)
                    
                    // Set up brush properties (needs x, y, width, height for gradients)
                    let shapeRect = { x: x + 10, y: y + 20, width: 80, height: 60 }
                    applyBrushStyle(ctx, shapeRect.x, shapeRect.y, shapeRect.width, shapeRect.height)
                    
                    // Draw the shape
                    drawShape(ctx, shapeType, shapeRect.x, shapeRect.y, shapeRect.width, shapeRect.height)
                    
                    ctx.restore()
                }
            }
            
            // Draw a red border around the canvas
            ctx.strokeStyle = "red"
            ctx.lineWidth = 1
            ctx.setLineDash([])
            ctx.strokeRect(0, 0, width, height)
        }
    }
    
    // Make the canvas repaint when resized
    onWidthChanged: canvas.requestPaint()
    onHeightChanged: canvas.requestPaint()
    
    // Public method to request a repaint
    function requestPaint() {
        canvas.requestPaint()
    }
}