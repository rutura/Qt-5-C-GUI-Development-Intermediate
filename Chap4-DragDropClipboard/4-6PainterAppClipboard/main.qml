import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Dialogs
import PaintApp 1.0

Window {
    id: mainWindow
    width: 950
    height: 684
    visible: true
    title: "Paint with Clipboard Support"
    color: "#f5f5f5"
    
    // Create global shortcut handlers
    Shortcut {
        sequences: [StandardKey.Copy]
        onActivated: {
            console.log("Copy shortcut activated")
            canvas.copy()
        }
    }
    
    Shortcut {
        sequences: [StandardKey.Paste]
        onActivated: {
            console.log("Paste shortcut activated")
            canvas.paste()
        }
    }
    
    // Main layout
    ColumnLayout {
        anchors.fill: parent
        spacing: 0
        
        // Toolbar component
        ToolBar {
            id: toolbar
            Layout.fillWidth: true
            Layout.preferredHeight: 50
            
            background: Rectangle {
                color: "#f0f0f0"
                border.color: "#d0d0d0"
                border.width: 1
            }
            
            RowLayout {
                anchors.fill: parent
                anchors.margins: 5
                spacing: 10
                
                // Pen width controls
                Label { 
                    text: "Pen Width"
                    Layout.alignment: Qt.AlignVCenter
                }
                
                SpinBox {
                    id: penWidthSpinBox
                    from: 1
                    to: 15
                    value: canvas.penWidth
                    onValueChanged: canvas.penWidth = value
                    Layout.alignment: Qt.AlignVCenter
                }
                
                // Pen color controls
                Label { 
                    text: "Pen Color"
                    Layout.alignment: Qt.AlignVCenter
                }
                
                Rectangle {
                    id: penColorButton
                    width: 30
                    height: 30
                    color: canvas.penColor
                    border.color: "black"
                    border.width: 1
                    Layout.alignment: Qt.AlignVCenter
                    
                    MouseArea {
                        anchors.fill: parent
                        onClicked: penColorDialog.open()
                    }
                }
                
                // Fill color controls
                Label { 
                    text: "Fill Color"
                    Layout.alignment: Qt.AlignVCenter
                }
                
                Rectangle {
                    id: fillColorButton
                    width: 30
                    height: 30
                    color: canvas.fillColor
                    border.color: "black"
                    border.width: 1
                    Layout.alignment: Qt.AlignVCenter
                    
                    MouseArea {
                        anchors.fill: parent
                        onClicked: fillColorDialog.open()
                    }
                }
                
                // Fill checkbox
                CheckBox {
                    id: fillCheckBox
                    text: "Fill Shape"
                    checked: canvas.fill
                    onCheckedChanged: canvas.fill = checked
                    Layout.alignment: Qt.AlignVCenter
                }
                
                // Spacer
                Item {
                    Layout.fillWidth: true
                }
                
                // Tool buttons
                ToolButton {
                    id: penButton
                    icon.source: paintController.penIconPath
                    checked: canvas.tool === 0
                    onClicked: {
                        canvas.tool = 0;
                        paintController.setTool(0);
                    }
                    ToolTip.visible: hovered
                    ToolTip.text: "Pen Tool"
                }
                
                ToolButton {
                    id: rectButton
                    icon.source: paintController.rectIconPath
                    checked: canvas.tool === 1
                    onClicked: {
                        canvas.tool = 1;
                        paintController.setTool(1);
                    }
                    ToolTip.visible: hovered
                    ToolTip.text: "Rectangle Tool"
                }
                
                ToolButton {
                    id: ellipseButton
                    icon.source: paintController.ellipseIconPath
                    checked: canvas.tool === 2
                    onClicked: {
                        canvas.tool = 2;
                        paintController.setTool(2);
                    }
                    ToolTip.visible: hovered
                    ToolTip.text: "Ellipse Tool"
                }
                
                ToolButton {
                    id: eraserButton
                    icon.source: paintController.eraserIconPath
                    checked: canvas.tool === 3
                    onClicked: {
                        canvas.tool = 3;
                        paintController.setTool(3);
                    }
                    ToolTip.visible: hovered
                    ToolTip.text: "Eraser Tool"
                }
            }
        }
        
        // Canvas area
        PaintCanvas {
            id: canvas
            Layout.fillWidth: true
            Layout.fillHeight: true
            
            // Connect mouse events to canvas methods
            MouseArea {
                id: canvasMouseArea
                anchors.fill: parent
                hoverEnabled: true
                
                onPressed: function(mouse) {
                    canvas.handleMousePress(Qt.point(mouse.x, mouse.y))
                }
                
                onPositionChanged: function(mouse) {
                    if (pressed) {
                        canvas.handleMouseMove(Qt.point(mouse.x, mouse.y))
                    }
                }
                
                onReleased: function(mouse) {
                    canvas.handleMouseRelease(Qt.point(mouse.x, mouse.y))
                }
            }
        }
        
        // Status bar
        Rectangle {
            id: statusBar
            Layout.fillWidth: true
            Layout.preferredHeight: 30
            color: "#f0f0f0"
            border.color: "#d0d0d0"
            border.width: 1
            
            Text {
                anchors.fill: parent
                anchors.margins: 5
                text: "Current tool: " + paintController.getToolName(paintController.currentTool) + 
                      " | Press Ctrl+C to copy and Ctrl+V to paste images"
                verticalAlignment: Text.AlignVCenter
            }
        }
    }
    
    // Color dialogs
    ColorDialog {
        id: penColorDialog
        title: "Select Pen Color"
        selectedColor: canvas.penColor
        onAccepted: canvas.penColor = selectedColor
    }
    
    ColorDialog {
        id: fillColorDialog
        title: "Select Fill Color"
        selectedColor: canvas.fillColor
        onAccepted: canvas.fillColor = selectedColor
    }
    
    // Resize the canvas image when window size changes
    onWidthChanged: canvas.resizeImage(width, height)
    onHeightChanged: canvas.resizeImage(width, height)
    
    Component.onCompleted: {
        // Initial resize of the canvas
        canvas.resizeImage(width, height)
    }
}