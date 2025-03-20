import QtQuick
import QtQuick.Window
import QtQuick.Controls

Window {
    id: mainWindow
    width: 899
    height: 558
    visible: true
    title: "Pen Styles Demo"
    
    Canvas {
        id: drawingCanvas
        anchors.fill: parent
        
        onPaint: {
            var ctx = getContext("2d");
            ctx.clearRect(0, 0, width, height);
            
            // ----------------
            // Pen Style
            // ----------------
            
            // Default: Qt::SolidLine
            ctx.lineWidth = 5;
            ctx.strokeStyle = "black";
            ctx.fillStyle = "red";
            ctx.setLineDash([]); // Solid line (empty array = no dashes)
            ctx.beginPath();
            ctx.rect(10, 10, 100, 100);
            ctx.fill();
            ctx.stroke();
            
            // Qt::NoPen equivalent
            ctx.strokeStyle = "transparent"; // Set stroke to transparent
            ctx.beginPath();
            ctx.rect(120, 10, 100, 100);
            ctx.fill();
            // Don't call stroke() for NoPen effect
            
            // Qt::DashLine
            ctx.strokeStyle = "black";
            ctx.setLineDash([15, 5]); // Dash, space pattern
            ctx.beginPath();
            ctx.rect(230, 10, 100, 100);
            ctx.fill();
            ctx.stroke();
            
            // Qt::DotLine
            ctx.setLineDash([3, 5]); // Dot, space pattern
            ctx.beginPath();
            ctx.rect(340, 10, 100, 100);
            ctx.fill();
            ctx.stroke();
            
            // Qt::DashDotLine
            ctx.setLineDash([15, 5, 3, 5]); // Dash, space, dot, space
            ctx.beginPath();
            ctx.rect(450, 10, 100, 100);
            ctx.fill();
            ctx.stroke();
            
            // Qt::DashDotDotLine
            ctx.setLineDash([15, 5, 3, 5, 3, 5]); // Dash, space, dot, space, dot, space
            ctx.beginPath();
            ctx.rect(560, 10, 100, 100);
            ctx.fill();
            ctx.stroke();
            
            // CustomDash Line
            ctx.setLineDash([1, 4, 3, 4, 9, 4, 27, 4, 9, 4]); // Custom pattern
            ctx.beginPath();
            ctx.rect(670, 10, 100, 100);
            ctx.fill();
            ctx.stroke();
            
            // ----------------
            // Cap Style
            // ----------------
            
            ctx.lineWidth = 20;
            ctx.setLineDash([]); // Back to solid line
            
            // Qt::FlatCap
            ctx.lineCap = "butt"; // Equivalent to Qt::FlatCap
            ctx.beginPath();
            ctx.moveTo(100, 150);
            ctx.lineTo(500, 150);
            ctx.stroke();
            
            // Qt::SquareCap
            ctx.lineCap = "square"; // Equivalent to Qt::SquareCap
            ctx.beginPath();
            ctx.moveTo(100, 200);
            ctx.lineTo(500, 200);
            ctx.stroke();
            
            // Qt::RoundCap
            ctx.lineCap = "round"; // Equivalent to Qt::RoundCap
            ctx.beginPath();
            ctx.moveTo(100, 250);
            ctx.lineTo(500, 250);
            ctx.stroke();
            
            // ----------------
            // Join Style
            // ----------------
            
            ctx.lineWidth = 10;
            
            // Define points for polygons
            var points1 = [
                { x: 10.0, y: 380.0 },
                { x: 50.0, y: 310.0 },
                { x: 320.0, y: 330.0 },
                { x: 250.0, y: 370.0 }
            ];
            
            // Qt::MiterJoin
            ctx.lineJoin = "miter"; // Equivalent to Qt::MiterJoin
            ctx.fillStyle = "transparent"; // No fill
            ctx.beginPath();
            ctx.moveTo(points1[0].x, points1[0].y);
            for (var i = 1; i < points1.length; i++) {
                ctx.lineTo(points1[i].x, points1[i].y);
            }
            ctx.closePath();
            ctx.stroke();
            
            // Qt::BevelJoin
            // Move the points down
            var points2 = points1.map(function(p) {
                return { x: p.x, y: p.y + 100.0 };
            });
            
            ctx.lineJoin = "bevel"; // Equivalent to Qt::BevelJoin
            ctx.fillStyle = "blue";
            ctx.beginPath();
            ctx.moveTo(points2[0].x, points2[0].y);
            for (var i = 1; i < points2.length; i++) {
                ctx.lineTo(points2[i].x, points2[i].y);
            }
            ctx.closePath();
            ctx.fill();
            ctx.stroke();
            
            // Qt::RoundJoin
            // Move the points right
            var points3 = points2.map(function(p) {
                return { x: p.x + 300.0, y: p.y };
            });
            
            ctx.lineJoin = "round"; // Equivalent to Qt::RoundJoin
            ctx.fillStyle = "yellow";
            ctx.beginPath();
            ctx.moveTo(points3[0].x, points3[0].y);
            for (var i = 1; i < points3.length; i++) {
                ctx.lineTo(points3[i].x, points3[i].y);
            }
            ctx.closePath();
            ctx.fill();
            ctx.stroke();
            
            // Add labels for clarity
            ctx.fillStyle = "black";
            ctx.font = "14px Arial";
            
            // Pen style labels
            ctx.fillText("SolidLine", 25, 130);
            ctx.fillText("NoPen", 145, 130);
            ctx.fillText("DashLine", 245, 130);
            ctx.fillText("DotLine", 360, 130);
            ctx.fillText("DashDotLine", 452, 130);
            ctx.fillText("DashDotDotLine", 555, 130);
            ctx.fillText("CustomDash", 675, 130);
            
            // Cap style labels
            ctx.fillText("FlatCap", 50, 150);
            ctx.fillText("SquareCap", 50, 200);
            ctx.fillText("RoundCap", 50, 250);
            
            // Join style labels
            ctx.fillText("MiterJoin", 150, 340);
            ctx.fillText("BevelJoin", 150, 440);
            ctx.fillText("RoundJoin", 450, 440);
        }
    }
}