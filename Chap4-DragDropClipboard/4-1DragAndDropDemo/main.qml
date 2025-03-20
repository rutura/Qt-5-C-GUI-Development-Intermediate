import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

Window {
    id: mainWindow
    width: 400
    height: 300
    visible: true
    title: "Drag & Drop Example"
    
    Component.onCompleted: {
        // Set initial instructions
        textEdit.text = "Information about dropped content will appear here.\n\n" +
                      "Try dragging and dropping:\n" +
                      "• Text from another application\n" +
                      "• Files from your file manager\n" +
                      "• Images from a browser\n" +
                      "• HTML content";
    }
    
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 11
        spacing: 6
        
        // Drag and drop area
        DragDropLabel {
            id: dragDropLabel
            Layout.fillWidth: true
            Layout.preferredHeight: 150
            
            onMimeDataReceived: function(text, urls, html, hasImage) {
                controller.processMimeData(text, urls, html, hasImage)
            }
            
            onDragStarted: {
                // Processing started
            }
            
            onDragEnded: {
                // Processing ended
            }
        }
        
        // Text edit for displaying MIME data
        ScrollView {
            Layout.fillWidth: true
            Layout.fillHeight: true
            
            TextArea {
                id: textEdit
                readOnly: true
                wrapMode: TextEdit.WordWrap
                textFormat: TextEdit.PlainText
                
                // Update when mimeData changes
                Connections {
                    target: controller
                    function onMimeDataChanged() {
                        if (controller.mimeEntries.length === 0) {
                            textEdit.text = "Information about dropped content will appear here.\n\n" +
                                          "Try dragging and dropping:\n" +
                                          "• Text from another application\n" +
                                          "• Files from your file manager\n" +
                                          "• Images from a browser\n" +
                                          "• HTML content";
                            return;
                        }
                        
                        textEdit.clear()
                        
                        for (var i = 0; i < controller.mimeEntries.length; i++) {
                            var entry = controller.mimeEntries[i]
                            var format = entry.format
                            var data = entry.data
                            
                            var text = i + " | Format: " + format + 
                                      "\n    | Data: " + data + 
                                      "\n------------"
                            
                            textEdit.append(text)
                        }
                    }
                }
            }
        }
        
        // Clear button
        RowLayout {
            Layout.fillWidth: true
            
            Item { Layout.fillWidth: true } // Spacer
            
            Button {
                id: clearButton
                text: "Clear"
                icon.source: "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2'><line x1='18' y1='6' x2='6' y2='18'/><line x1='6' y1='6' x2='18' y2='18'/></svg>"
                onClicked: {
                    textEdit.clear()
                    dragDropLabel.clear()
                    controller.clearData()
                    
                    // Restore help text
                    textEdit.text = "Information about dropped content will appear here.\n\n" +
                                  "Try dragging and dropping:\n" +
                                  "• Text from another application\n" +
                                  "• Files from your file manager\n" +
                                  "• Images from a browser\n" +
                                  "• HTML content";
                }
            }
        }
    }
}