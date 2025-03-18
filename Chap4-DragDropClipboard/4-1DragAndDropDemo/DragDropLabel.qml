import QtQuick
import QtQuick.Controls

Rectangle {
    id: root
    
    // Signal for Python backend
    signal mimeDataReceived(string text, var urls, string html, bool hasImage)
    signal dragStarted()
    signal dragEnded()
    
    // Properties
    width: 100
    height: 100
    color: dropArea.containsDrag ? palette.highlight : "#333333"
    border.color: dropArea.containsDrag ? palette.highlight : palette.dark
    border.width: 2
    radius: 6
    
    // Colors
    SystemPalette {
        id: palette
    }
    
    // Main label
    Column {
        anchors.centerIn: parent
        spacing: 8
        visible: !droppedImage.visible
        
        Label {
            id: dropLabel
            anchors.horizontalCenter: parent.horizontalCenter
            text: "DROP SPACE"
            font.bold: true
            font.pixelSize: 16
            color: palette.highlightedText
        }
        
        Label {
            id: instructionLabel
            anchors.horizontalCenter: parent.horizontalCenter
            text: "Drag files, text, or images here"
            font.pixelSize: 12
            color: palette.highlightedText
            width: parent.width - 20
            horizontalAlignment: Text.AlignHCenter
            wrapMode: Text.WordWrap
        }
        
        Image {
            anchors.horizontalCenter: parent.horizontalCenter
            source: "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2'><path d='M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4'/><polyline points='7 10 12 15 17 10'/><line x1='12' y1='15' x2='12' y2='3'/></svg>"
            width: 32
            height: 32
        }
    }
    
    // Container for dropped images
    Image {
        id: droppedImage
        anchors.fill: parent
        anchors.margins: 5
        fillMode: Image.PreserveAspectFit
        visible: false
    }
    
    // Drop area
    DropArea {
        id: dropArea
        anchors.fill: parent
        
        onEntered: {
            dropLabel.text = "DROP YOUR DATA HERE"
            instructionLabel.text = "Release to analyze content"
            dragStarted()
        }
        
        onExited: {
            root.clear()
        }
        
        onDropped: {
            droppedImage.visible = false
            
            if (drop.hasImage) {
                droppedImage.source = drop.image
                droppedImage.visible = true
            } else if (drop.hasText) {
                dropLabel.text = drop.text
            } else if (drop.hasUrls) {
                var text = ""
                for (var i = 0; i < drop.urls.length; i++) {
                    text += drop.urls[i] + "-----"
                }
                dropLabel.text = text
            } else if (drop.hasHtml) {
                dropLabel.text = "HTML content"
            } else {
                dropLabel.text = "Data cannot be displayed"
            }
            
            // Signal the data to Python
            var urlStrings = []
            if (drop.hasUrls) {
                for (var j = 0; j < drop.urls.length; j++) {
                    urlStrings.push(drop.urls[j].toString())
                }
            }
            
            mimeDataReceived(
                drop.hasText ? drop.text : "",
                urlStrings,
                drop.hasHtml ? drop.html : "",
                drop.hasImage
            )
        }
    }
    
    // Method to reset the label
    function clear() {
        dropLabel.text = "DROP SPACE"
        instructionLabel.text = "Drag files, text, or images here"
        droppedImage.visible = false
        dragEnded()
    }
}