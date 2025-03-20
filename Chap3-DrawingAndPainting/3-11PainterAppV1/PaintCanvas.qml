import QtQuick

Item {
    id: root
    
    // Properties to match the Python version
    property int currentTool: 0  // Pen by default
    property bool fill: false
    property int penWidth: 3
    property color fillColor: "red"
    property color penColor: "green"
    
    property bool drawing: false
    property point lastPoint: Qt.point(0, 0)
    property rect lastRect: Qt.rect(0, 0, 0, 0)
    property rect lastEraserRect: Qt.rect(0, 0, 0, 0)
    
    // Tool type enum to match the Python version
    readonly property int toolPen: 0
    readonly property int toolRect: 1
    readonly property int toolEllipse: 2
    readonly property int toolEraser: 3
    
    // The main canvas for drawing
    Canvas {
        id: canvas
        anchors.fill: parent
        
        // The actual image data that we'll draw on
        property var imageData: null
        
        // Handle when canvas becomes available
        onAvailableChanged: {
            if (available) {
                initializeCanvas()
            }
        }
        
        // Initialize canvas when it becomes available
        function initializeCanvas() {
            var ctx = getContext("2d")
            if (ctx) {
                imageData = ctx.createImageData(width, height)
                clearCanvas()
                requestPaint()
            }
        }
        
        // When size changes, resize the canvas
        onWidthChanged: if (available) resizeCanvas()
        onHeightChanged: if (available) resizeCanvas()
        
        // Paint event handler
        onPaint: {
            var ctx = getContext("2d")
            if (ctx && imageData) {
                ctx.clearRect(0, 0, width, height)
                ctx.putImageData(imageData, 0, 0)
            }
        }
        
        // Draw a line from last point to current point
        function drawLineTo(endPoint) {
            if (!available) return
            
            var ctx = getContext("2d")
            if (!ctx) return
            
            ctx.save()
            ctx.putImageData(imageData, 0, 0)
            
            // Set up pen properties
            ctx.lineWidth = penWidth
            ctx.strokeStyle = penColor
            ctx.lineCap = "round"
            ctx.lineJoin = "round"
            
            // Draw the line
            ctx.beginPath()
            ctx.moveTo(lastPoint.x, lastPoint.y)
            ctx.lineTo(endPoint.x, endPoint.y)
            ctx.stroke()
            
            // Save the image data
            imageData = ctx.getImageData(0, 0, width, height)
            ctx.restore()
            
            // Force canvas to update
            requestPaint()
        }
        
        // Draw a rectangle/ellipse from last point to current point
        function drawRectTo(endPoint, isEllipse) {
            if (!available) return
            
            var ctx = getContext("2d")
            if (!ctx) return
            
            // Restore the original image (without temporary shapes)
            ctx.putImageData(imageData, 0, 0)
            
            // Set up pen and brush properties
            ctx.lineWidth = penWidth
            ctx.strokeStyle = penColor
            ctx.lineCap = "round"
            ctx.lineJoin = "round"
            ctx.fillStyle = fillColor
            
            // Calculate rectangle coordinates
            var x = Math.min(lastPoint.x, endPoint.x)
            var y = Math.min(lastPoint.y, endPoint.y)
            var w = Math.abs(endPoint.x - lastPoint.x)
            var h = Math.abs(endPoint.y - lastPoint.y)
            
            // Draw the shape
            ctx.beginPath()
            if (isEllipse) {
                // Draw ellipse
                var centerX = x + w / 2
                var centerY = y + h / 2
                var radiusX = w / 2
                var radiusY = h / 2
                
                ctx.ellipse(centerX, centerY, radiusX, radiusY, 0, 0, Math.PI * 2)
            } else {
                // Draw rectangle
                ctx.rect(x, y, w, h)
            }
            
            // Fill if needed
            if (fill) {
                ctx.fill()
            }
            ctx.stroke()
            
            // If the mouse is released, save the image
            if (!drawing) {
                imageData = ctx.getImageData(0, 0, width, height)
            }
            
            // Force canvas to update
            requestPaint()
        }
        
        // Erase content under a specific point
        function eraseUnder(point) {
            if (!available) return
            
            var ctx = getContext("2d")
            if (!ctx) return
            
            // Restore the original image
            ctx.putImageData(imageData, 0, 0)
            
            // Calculate eraser rectangle
            var size = 20
            var x = point.x - size / 2
            var y = point.y - size / 2
            
            // Erase by drawing a white rectangle
            ctx.fillStyle = "white"
            ctx.fillRect(x, y, size, size)
            
            // If the mouse is released, save the image
            if (!drawing) {
                imageData = ctx.getImageData(0, 0, width, height)
            }
            
            // Force canvas to update
            requestPaint()
        }
        
        // Resize canvas and preserve content
        function resizeCanvas() {
            if (!available) return
            
            var ctx = getContext("2d")
            if (!ctx || !imageData) return
            
            var oldImageData = imageData
            
            // Create a new buffer for the new size
            imageData = ctx.createImageData(width, height)
            
            // Fill with white
            var data = imageData.data
            for (var i = 0; i < data.length; i += 4) {
                data[i] = 255     // R
                data[i + 1] = 255 // G
                data[i + 2] = 255 // B
                data[i + 3] = 255 // A
            }
            
            // Draw old content to the new buffer
            ctx.putImageData(imageData, 0, 0)
            ctx.drawImage(canvas, 0, 0)
            
            // Save new image data
            imageData = ctx.getImageData(0, 0, width, height)
            
            // Request a paint update
            requestPaint()
        }
        
        // Clear the canvas
        function clearCanvas() {
            if (!available) return
            
            var ctx = getContext("2d")
            if (!ctx) return
            
            // Fill with white
            ctx.fillStyle = "white"
            ctx.fillRect(0, 0, width, height)
            
            // Save the blank state
            imageData = ctx.getImageData(0, 0, width, height)
            
            // Force canvas to update
            requestPaint()
        }
    }
    
    // Mouse area for handling input
    MouseArea {
        id: mouseArea
        anchors.fill: parent
        hoverEnabled: true
        
        onPressed: {
            lastPoint = Qt.point(mouseX, mouseY)
            drawing = true
            
            if (currentTool === toolRect || currentTool === toolEllipse) {
                // For shape tools, don't draw immediately on press
                lastRect = Qt.rect(mouseX, mouseY, 0, 0)
            } else if (currentTool === toolPen) {
                // For pen, start drawing immediately
                // No need to do anything here as the move handler will draw
            } else if (currentTool === toolEraser) {
                // For eraser, start erasing immediately
                canvas.eraseUnder(Qt.point(mouseX, mouseY))
            }
        }
        
        onPositionChanged: {
            if (!drawing) return
            
            if (currentTool === toolPen) {
                // Draw line for pen tool
                var currentPoint = Qt.point(mouseX, mouseY)
                canvas.drawLineTo(currentPoint)
                lastPoint = currentPoint
            } else if (currentTool === toolRect) {
                // Update rectangle preview
                canvas.drawRectTo(Qt.point(mouseX, mouseY), false)
            } else if (currentTool === toolEllipse) {
                // Update ellipse preview
                canvas.drawRectTo(Qt.point(mouseX, mouseY), true)
            } else if (currentTool === toolEraser) {
                // Erase content
                canvas.eraseUnder(Qt.point(mouseX, mouseY))
            }
        }
        
        onReleased: {
            if (!drawing) return
            
            // Final draw or erase
            if (currentTool === toolPen) {
                canvas.drawLineTo(Qt.point(mouseX, mouseY))
            } else if (currentTool === toolRect) {
                canvas.drawRectTo(Qt.point(mouseX, mouseY), false)
            } else if (currentTool === toolEllipse) {
                canvas.drawRectTo(Qt.point(mouseX, mouseY), true)
            } else if (currentTool === toolEraser) {
                canvas.eraseUnder(Qt.point(mouseX, mouseY))
            }
            
            // Reset drawing state
            drawing = false
            lastRect = Qt.rect(0, 0, 0, 0)
            lastEraserRect = Qt.rect(0, 0, 0, 0)
        }
    }
}