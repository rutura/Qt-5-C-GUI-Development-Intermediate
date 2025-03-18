import QtQuick

Item {
    id: carCanvas
    
    Canvas {
        id: canvas
        anchors.fill: parent
        
        // Request a redraw when the component is loaded
        Component.onCompleted: requestPaint()
        
        onPaint: {
            var ctx = getContext("2d");
            ctx.reset();
            
            // Draw all cars using the drawCar function
            drawCar(ctx, Qt.rect(100, 400, 200, 200), "black");     // Bottom left
            drawCar(ctx, Qt.rect(500, 400, 200, 200), "red");       // Bottom right
            drawCar(ctx, Qt.rect(100, 100, 200, 200), "blue");      // Top left
            drawCar(ctx, Qt.rect(500, 100, 200, 200), "green");     // Top right
        }
        
        // Utility function to convert Qt's 1/16 degrees to radians
        function degToRad(qtDeg) {
            return (qtDeg * Math.PI) / (180 * 16);
        }
        
        function drawCar(ctx, rect, tireColor) {
            if (!rect) {
                rect = Qt.rect(100, 100, 200, 200);
            }
            if (!tireColor) {
                tireColor = "black";
            }
            
            ctx.lineWidth = 3;
            ctx.strokeStyle = "black";
            
            // Upper Section
            var startAngle = 15 * 16;
            var spanAngle = 150 * 16;
            var outRect = {
                x: rect.x, 
                y: rect.y, 
                width: rect.width, 
                height: rect.height
            };
            var inRect = {
                x: outRect.x + 10, 
                y: outRect.y + 10, 
                width: outRect.width - 20, 
                height: outRect.height - 20
            };
            
            // Draw the upper roofs
            // For the arc, we need to convert from Qt's angles to proper HTML5 Canvas angles
            ctx.beginPath();
            ctx.arc(
                outRect.x + outRect.width/2,
                outRect.y + outRect.height/2,
                outRect.width/2,
                Math.PI + degToRad(startAngle),
                Math.PI + degToRad(startAngle + spanAngle),
                false
            );
            ctx.stroke();
            
            ctx.beginPath();
            ctx.arc(
                inRect.x + inRect.width/2,
                inRect.y + inRect.height/2,
                inRect.width/2,
                Math.PI + degToRad(20 * 16),
                Math.PI + degToRad(20 * 16 + 65 * 16),
                false
            );
            ctx.stroke();
            
            ctx.beginPath();
            ctx.arc(
                inRect.x + inRect.width/2,
                inRect.y + inRect.height/2,
                inRect.width/2,
                Math.PI + degToRad(92 * 16),
                Math.PI + degToRad(92 * 16 + 68 * 16),
                false
            );
            ctx.stroke();
            
            // Draw upper vertical lines
            ctx.beginPath();
            ctx.moveTo(outRect.x + 97, outRect.y + 10);
            ctx.lineTo(outRect.x + 97, outRect.y + 70);
            ctx.stroke();
            
            ctx.beginPath();
            ctx.moveTo(outRect.x + 107, outRect.y + 10);
            ctx.lineTo(outRect.x + 107, outRect.y + 70);
            ctx.stroke();
            
            // Draw low horizontal line
            ctx.beginPath();
            ctx.moveTo(outRect.x + 20, outRect.y + 70);
            ctx.lineTo(outRect.x + 95, outRect.y + 70);
            ctx.stroke();
            
            ctx.beginPath();
            ctx.moveTo(outRect.x + 110, outRect.y + 70);
            ctx.lineTo(outRect.x + 185, outRect.y + 70);
            ctx.stroke();
            
            // Back Section
            ctx.beginPath();
            ctx.moveTo(outRect.x + 5, outRect.y + 74);
            ctx.lineTo(outRect.x - 50, outRect.y + 79);
            ctx.stroke();
            
            ctx.beginPath();
            ctx.moveTo(outRect.x - 50, outRect.y + 79);
            ctx.lineTo(outRect.x - 55, outRect.y + 135);
            ctx.stroke();
            
            // Front Section
            ctx.beginPath();
            ctx.moveTo(outRect.x + 200, outRect.y + 74);
            ctx.lineTo(outRect.x + 290, outRect.y + 75);
            ctx.stroke();
            
            ctx.beginPath();
            ctx.moveTo(outRect.x + 290, outRect.y + 75);
            ctx.lineTo(outRect.x + 300, outRect.y + 135);
            ctx.stroke();
            
            // Tires
            // Frames
            var backTireFrame = {
                x: outRect.x - 10, 
                y: outRect.y + 100, 
                width: 80, 
                height: 80
            };
            var frontTireFrame = {
                x: outRect.x + 170, 
                y: outRect.y + 100, 
                width: 80, 
                height: 80
            };
            
            ctx.beginPath();
            ctx.arc(
                backTireFrame.x + backTireFrame.width/2,
                backTireFrame.y + backTireFrame.height/2,
                backTireFrame.width/2,
                Math.PI,
                Math.PI + degToRad(170 * 16),
                false
            );
            ctx.stroke();
            
            ctx.beginPath();
            ctx.arc(
                frontTireFrame.x + frontTireFrame.width/2,
                frontTireFrame.y + frontTireFrame.height/2,
                frontTireFrame.width/2,
                Math.PI + degToRad(10 * 16),
                Math.PI + degToRad(10 * 16 + 170 * 16),
                false
            );
            ctx.stroke();
            
            // Lower connectors
            ctx.beginPath();
            ctx.moveTo(outRect.x - 55, outRect.y + 135);
            ctx.lineTo(outRect.x - 7, outRect.y + 132);
            ctx.stroke();
            
            ctx.beginPath();
            ctx.moveTo(outRect.x + 70, outRect.y + 140);
            ctx.lineTo(outRect.x + 170, outRect.y + 140);
            ctx.stroke();
            
            ctx.beginPath();
            ctx.moveTo(outRect.x + 250, outRect.y + 135);
            ctx.lineTo(outRect.x + 300, outRect.y + 135);
            ctx.stroke();
            
            // Back Tire
            var backTire = {
                x: outRect.x, 
                y: outRect.y + 110, 
                width: 60, 
                height: 60
            };
            ctx.beginPath();
            ctx.arc(
                backTire.x + backTire.width/2,
                backTire.y + backTire.height/2,
                backTire.width/2,
                0,
                2 * Math.PI
            );
            ctx.stroke();
            
            var backTireInner = {
                x: outRect.x + 10, 
                y: outRect.y + 120, 
                width: 40, 
                height: 40
            };
            ctx.beginPath();
            ctx.arc(
                backTireInner.x + backTireInner.width/2,
                backTireInner.y + backTireInner.height/2,
                backTireInner.width/2,
                0,
                2 * Math.PI
            );
            ctx.fillStyle = tireColor;
            ctx.fill();
            ctx.stroke();
            
            // Front Tire
            var frontTire = {
                x: outRect.x + 180, 
                y: outRect.y + 110, 
                width: 60, 
                height: 60
            };
            ctx.beginPath();
            ctx.arc(
                frontTire.x + frontTire.width/2,
                frontTire.y + frontTire.height/2,
                frontTire.width/2,
                0,
                2 * Math.PI
            );
            ctx.stroke();
            
            var frontTireInner = {
                x: outRect.x + 190, 
                y: outRect.y + 120, 
                width: 40, 
                height: 40
            };
            ctx.beginPath();
            ctx.arc(
                frontTireInner.x + frontTireInner.width/2,
                frontTireInner.y + frontTireInner.height/2,
                frontTireInner.width/2,
                0,
                2 * Math.PI
            );
            ctx.fillStyle = tireColor;
            ctx.fill();
            ctx.stroke();
        }
    }
}