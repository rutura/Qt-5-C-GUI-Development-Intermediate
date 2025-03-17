import QtQuick
import QtQuick.Window
import QtQuick.Controls

Window {
    id: mainWindow
    width: 963
    height: 589
    visible: true
    title: "Brush Styles Demo"
    
    Canvas {
        id: drawingCanvas
        anchors.fill: parent
        
        // Draw patterns directly on the canvas
        onPaint: {
            var ctx = getContext("2d");
            ctx.clearRect(0, 0, width, height);
            
            // First Row of Brush Patterns
            
            // Solid Pattern
            ctx.fillStyle = "red";
            ctx.fillRect(20, 20, 100, 100);
            ctx.strokeRect(20, 20, 100, 100);
            
            // Dense1Pattern - 12.5% density dots
            drawDensePattern(ctx, 130, 20, 100, 100, 1, "blue");
            
            // Dense2Pattern - 25% density dots
            drawDensePattern(ctx, 240, 20, 100, 100, 2, "red");
            
            // Dense3Pattern - 37.5% density dots
            drawDensePattern(ctx, 350, 20, 100, 100, 3, "black");
            
            // Dense4Pattern - 50% density dots
            drawDensePattern(ctx, 460, 20, 100, 100, 4, "blue");
            
            // Dense5Pattern - 62.5% density dots
            drawDensePattern(ctx, 570, 20, 100, 100, 5, "blue");
            
            // Dense6Pattern - 75% density dots
            drawDensePattern(ctx, 680, 20, 100, 100, 6, "blue");
            
            // Dense7Pattern - 87.5% density dots
            drawDensePattern(ctx, 790, 20, 100, 100, 7, "blue");
            
            // Second Row of Brush Patterns
            
            // HorPattern - Horizontal lines
            drawLinePattern(ctx, 20, 130, 100, 100, "hor", "blue");
            
            // VerPattern - Vertical lines
            drawLinePattern(ctx, 130, 130, 100, 100, "ver", "blue");
            
            // CrossPattern - Crossing horizontal and vertical lines
            drawLinePattern(ctx, 240, 130, 100, 100, "cross", "blue");
            
            // BDiagPattern - Backward diagonal lines
            drawLinePattern(ctx, 350, 130, 100, 100, "bdiag", "blue");
            
            // FDiagPattern - Forward diagonal lines
            drawLinePattern(ctx, 460, 130, 100, 100, "fdiag", "blue");
            
            // DiagCrossPattern - Crossing diagonal lines
            drawLinePattern(ctx, 570, 130, 100, 100, "diagcross", "blue");
            
            // TexturePattern - Custom pattern
            drawTexturePattern(ctx, 680, 130, 210, 100);
            
            // Add labels
            ctx.fillStyle = "black";
            ctx.font = "12px Arial";
            
            // First row labels
            ctx.fillText("SolidPattern", 25, 135);
            ctx.fillText("Dense1Pattern", 130, 135);
            ctx.fillText("Dense2Pattern", 240, 135);
            ctx.fillText("Dense3Pattern", 350, 135);
            ctx.fillText("Dense4Pattern", 460, 135);
            ctx.fillText("Dense5Pattern", 570, 135);
            ctx.fillText("Dense6Pattern", 680, 135);
            ctx.fillText("Dense7Pattern", 790, 135);
            
            // Second row labels
            ctx.fillText("HorPattern", 30, 245);
            ctx.fillText("VerPattern", 140, 245);
            ctx.fillText("CrossPattern", 245, 245);
            ctx.fillText("BDiagPattern", 350, 245);
            ctx.fillText("FDiagPattern", 460, 245);
            ctx.fillText("DiagCrossPattern", 565, 245);
            ctx.fillText("TexturePattern", 730, 245);
        }
        
        // Draw dense pattern with specified density level
        function drawDensePattern(ctx, x, y, width, height, level, color) {
            var dotSize = 2;
            var dotSpacing = 4;
            
            // First draw a border around the rectangle
            ctx.strokeRect(x, y, width, height);
            
            // Clip to the rectangle area for the pattern
            ctx.save();
            ctx.beginPath();
            ctx.rect(x, y, width, height);
            ctx.clip();
            
            if (level === 1) {
                // Dense1Pattern - 12.5% density
                for (var i = x; i < x + width; i += dotSpacing * 2) {
                    for (var j = y; j < y + height; j += dotSpacing * 2) {
                        drawDot(ctx, i, j, dotSize, color);
                    }
                }
            } else if (level === 2) {
                // Dense2Pattern - 25% density
                for (var i = x; i < x + width; i += dotSpacing * 2) {
                    for (var j = y; j < y + height; j += dotSpacing * 2) {
                        drawDot(ctx, i, j, dotSize, color);
                        drawDot(ctx, i + dotSpacing, j + dotSpacing, dotSize, color);
                    }
                }
            } else if (level === 3) {
                // Dense3Pattern - 37.5% density
                for (var i = x; i < x + width; i += dotSpacing) {
                    for (var j = y; j < y + height; j += dotSpacing) {
                        if ((Math.floor(i / dotSpacing) + Math.floor(j / dotSpacing)) % 2 === 0) {
                            drawDot(ctx, i, j, dotSize, color);
                        }
                    }
                }
            } else if (level === 4) {
                // Dense4Pattern - 50% density (checkerboard)
                for (var i = x; i < x + width; i += dotSpacing) {
                    for (var j = y; j < y + height; j += dotSpacing) {
                        if ((Math.floor(i / dotSpacing) % 2 === 0 && Math.floor(j / dotSpacing) % 2 === 0) || 
                            (Math.floor(i / dotSpacing) % 2 === 1 && Math.floor(j / dotSpacing) % 2 === 1)) {
                            drawDot(ctx, i, j, dotSize, color);
                        }
                    }
                }
            } else if (level === 5) {
                // Dense5Pattern - 62.5% density (inverse of level 3)
                for (var i = x; i < x + width; i += dotSpacing) {
                    for (var j = y; j < y + height; j += dotSpacing) {
                        if ((Math.floor(i / dotSpacing) + Math.floor(j / dotSpacing)) % 2 === 1) {
                            drawDot(ctx, i, j, dotSize, color);
                        }
                    }
                }
                // Add more dots in the remaining spaces
                for (var i = x; i < x + width; i += dotSpacing * 2) {
                    for (var j = y; j < y + height; j += dotSpacing * 2) {
                        drawDot(ctx, i, j, dotSize, color);
                    }
                }
            } else if (level === 6) {
                // Dense6Pattern - 75% density (inverse of level 2)
                ctx.fillStyle = color;
                ctx.fillRect(x, y, width, height);
                
                ctx.fillStyle = "white";
                for (var i = x; i < x + width; i += dotSpacing * 2) {
                    for (var j = y; j < y + height; j += dotSpacing * 2) {
                        ctx.fillRect(i, j, dotSize, dotSize);
                    }
                }
            } else if (level === 7) {
                // Dense7Pattern - 87.5% density (inverse of level 1)
                ctx.fillStyle = color;
                ctx.fillRect(x, y, width, height);
                
                ctx.fillStyle = "white";
                for (var i = x; i < x + width; i += dotSpacing * 2) {
                    for (var j = y; j < y + height; j += dotSpacing * 2) {
                        ctx.fillRect(i, j, 1, 1);
                    }
                }
            }
            
            ctx.restore();
        }
        
        // Helper to draw a dot
        function drawDot(ctx, x, y, size, color) {
            ctx.fillStyle = color;
            ctx.fillRect(x, y, size, size);
        }
        
        // Draw line patterns
        function drawLinePattern(ctx, x, y, width, height, type, color) {
            // First draw a border around the rectangle
            ctx.strokeRect(x, y, width, height);
            
            // Clip to the rectangle area for the pattern
            ctx.save();
            ctx.beginPath();
            ctx.rect(x, y, width, height);
            ctx.clip();
            
            ctx.strokeStyle = color;
            ctx.lineWidth = 1;
            
            if (type === "hor") {
                // Horizontal lines
                for (var j = y; j <= y + height; j += 4) {
                    ctx.beginPath();
                    ctx.moveTo(x, j);
                    ctx.lineTo(x + width, j);
                    ctx.stroke();
                }
            } else if (type === "ver") {
                // Vertical lines
                for (var i = x; i <= x + width; i += 4) {
                    ctx.beginPath();
                    ctx.moveTo(i, y);
                    ctx.lineTo(i, y + height);
                    ctx.stroke();
                }
            } else if (type === "cross") {
                // Cross pattern (horizontal + vertical)
                for (var j = y; j <= y + height; j += 4) {
                    ctx.beginPath();
                    ctx.moveTo(x, j);
                    ctx.lineTo(x + width, j);
                    ctx.stroke();
                }
                for (var i = x; i <= x + width; i += 4) {
                    ctx.beginPath();
                    ctx.moveTo(i, y);
                    ctx.lineTo(i, y + height);
                    ctx.stroke();
                }
            } else if (type === "bdiag") {
                // Backward diagonal lines
                var step = 8;
                for (var n = -height; n < width; n += step) {
                    ctx.beginPath();
                    ctx.moveTo(x + n, y);
                    ctx.lineTo(x + n + height, y + height);
                    ctx.stroke();
                }
            } else if (type === "fdiag") {
                // Forward diagonal lines
                var step = 8;
                for (var n = 0; n < width + height; n += step) {
                    ctx.beginPath();
                    ctx.moveTo(x + n, y);
                    ctx.lineTo(x + n - height, y + height);
                    ctx.stroke();
                }
            } else if (type === "diagcross") {
                // Diagonal cross lines
                var step = 8;
                // Backward diagonals
                for (var n = -height; n < width; n += step) {
                    ctx.beginPath();
                    ctx.moveTo(x + n, y);
                    ctx.lineTo(x + n + height, y + height);
                    ctx.stroke();
                }
                // Forward diagonals
                for (var n = 0; n < width + height; n += step) {
                    ctx.beginPath();
                    ctx.moveTo(x + n, y);
                    ctx.lineTo(x + n - height, y + height);
                    ctx.stroke();
                }
            }
            
            ctx.restore();
        }
        
        // Draw texture pattern (checkerboard as a simple example)
        function drawTexturePattern(ctx, x, y, width, height) {
            // First draw a border around the rectangle
            ctx.strokeRect(x, y, width, height);
            
            // Fill with dark cyan
            ctx.fillStyle = "#008B8B";
            ctx.fillRect(x, y, width, height);
            
            // Draw white X pattern
            ctx.strokeStyle = "white";
            ctx.lineWidth = 2;
            
            // Draw X pattern repeating every 50 pixels
            for (var i = 0; i < width; i += 50) {
                for (var j = 0; j < height; j += 50) {
                    ctx.beginPath();
                    ctx.moveTo(x + i, y + j);
                    ctx.lineTo(x + i + 50, y + j + 50);
                    ctx.moveTo(x + i, y + j + 50);
                    ctx.lineTo(x + i + 50, y + j);
                    ctx.stroke();
                }
            }
        }
    }
}