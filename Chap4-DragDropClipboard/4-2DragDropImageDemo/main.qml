import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import Qt.labs.platform as Platform

Window {
    id: mainWindow
    width: 600
    height: 400
    visible: true
    title: "Image Viewer"
    color: "#f5f5f5"
    
    // Container for the image display
    Rectangle {
        id: imageContainer
        anchors.fill: parent
        color: "#ffffff"
        border.color: "#cccccc"
        border.width: 1
        
        // Placeholder text when no image is loaded
        Column {
            anchors.centerIn: parent
            spacing: 10
            visible: !imageViewer.source.toString()
            
            Image {
                anchors.horizontalCenter: parent.horizontalCenter
                source: "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' width='64' height='64' viewBox='0 0 24 24' fill='none' stroke='%23999999' stroke-width='2'><rect x='3' y='3' width='18' height='18' rx='2' ry='2'/><circle cx='8.5' cy='8.5' r='1.5'/><polyline points='21 15 16 10 5 21'/></svg>"
                width: 64
                height: 64
            }
            
            Text {
                anchors.horizontalCenter: parent.horizontalCenter
                text: "Drag and drop an image here"
                font.pixelSize: 16
                color: "#666666"
            }
            
            Text {
                anchors.horizontalCenter: parent.horizontalCenter
                text: "Supported formats: PNG, JPG, JPEG"
                font.pixelSize: 12
                color: "#999999"
            }
        }
        
        // Image display with aspect ratio preserved
        Image {
            id: imageViewer
            anchors.fill: parent
            anchors.margins: 10
            fillMode: Image.PreserveAspectFit
            asynchronous: true
            cache: true
            smooth: true
            mipmap: true
        }
        
        // Drop area for handling drag and drop
        DropArea {
            id: dropArea
            anchors.fill: parent
            
            onEntered: {
                // Highlight the drop area
                imageContainer.border.color = "#4a90e2"
                imageContainer.border.width = 2
            }
            
            onExited: {
                // Reset the highlight
                imageContainer.border.color = "#cccccc"
                imageContainer.border.width = 1
            }
            
            onDropped: {
                // Reset the highlight
                imageContainer.border.color = "#cccccc"
                imageContainer.border.width = 1
                
                // Process dropped files
                if (drop.hasUrls) {
                    for (var i = 0; i < drop.urls.length; i++) {
                        var url = drop.urls[i].toString()
                        
                        // Remove the "file:///" prefix on Windows or "file://" on Unix
                        var path = url.replace(/^file:\/\/\//, "").replace(/^file:\/\//, "")
                        
                        // Handle URL decoding for special characters
                        path = decodeURIComponent(path)
                        
                        // Check if it's an image
                        if (controller.isImage(path)) {
                            imageViewer.source = drop.urls[i]
                            break
                        }
                    }
                }
            }
        }
    }
}