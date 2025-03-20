import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts
import Qt.labs.platform as Platform

Window {
    id: mainWindow
    width: 950
    height: 684
    visible: true
    title: "Paint Application"
    color: "white"
    
    // Tool type enum to match the Python version
    readonly property int toolPen: 0
    readonly property int toolRect: 1
    readonly property int toolEllipse: 2
    readonly property int toolEraser: 3
    
    // Wait for controller to be initialized
    Component.onCompleted: {
        // Set initial checked state for first tool
        if (controller) {
            penButton.checked = (controller.tool === toolPen)
        }
    }
    
    ColumnLayout {
        anchors.fill: parent
        spacing: 0
        
        // Toolbar
        Rectangle {
            id: toolBar
            Layout.fillWidth: true
            height: 40
            color: "#f0f0f0"
            border.color: "#d0d0d0"
            
            RowLayout {
                anchors.fill: parent
                anchors.margins: 5
                spacing: 10
                
                // Pen width
                Label { text: "Pen Width:" }
                SpinBox {
                    id: penWidthSpinBox
                    from: 1
                    to: 15
                    value: 3
                    onValueChanged: paintCanvas.penWidth = value
                }
                
                // Pen color
                Label { text: "Pen Color:" }
                Rectangle {
                    id: penColorButton
                    width: 24
                    height: 24
                    color: paintCanvas.penColor
                    border.color: "black"
                    
                    MouseArea {
                        anchors.fill: parent
                        onClicked: penColorDialog.open()
                    }
                }
                
                // Fill color
                Label { text: "Fill Color:" }
                Rectangle {
                    id: fillColorButton
                    width: 24
                    height: 24
                    color: paintCanvas.fillColor
                    border.color: "black"
                    
                    MouseArea {
                        anchors.fill: parent
                        onClicked: fillColorDialog.open()
                    }
                }
                
                // Fill checkbox
                CheckBox {
                    id: fillCheckBox
                    text: "Fill Shape"
                    onToggled: paintCanvas.fill = checked
                }
                
                Rectangle {
                    width: 1
                    height: parent.height
                    color: "#d0d0d0"
                }
                
                // Drawing tools
                ToolButton {
                    id: penButton
                    icon.source: controller ? controller.penIcon : ""
                    text: (controller && controller.penIcon == "") ? "Pen" : ""
                    checked: controller ? (controller.tool === toolPen) : false
                    onClicked: if (controller) controller.tool = toolPen
                }
                
                ToolButton {
                    id: rectButton
                    icon.source: controller ? controller.rectangleIcon : ""
                    text: (controller && controller.rectangleIcon == "") ? "Rect" : ""
                    checked: controller ? (controller.tool === toolRect) : false
                    onClicked: if (controller) controller.tool = toolRect
                }
                
                ToolButton {
                    id: ellipseButton
                    icon.source: controller ? controller.circleIcon : ""
                    text: (controller && controller.circleIcon == "") ? "Ellipse" : ""
                    checked: controller ? (controller.tool === toolEllipse) : false
                    onClicked: if (controller) controller.tool = toolEllipse
                }
                
                ToolButton {
                    id: eraserButton
                    icon.source: controller ? controller.eraserIcon : ""
                    text: (controller && controller.eraserIcon == "") ? "Eraser" : ""
                    checked: controller ? (controller.tool === toolEraser) : false
                    onClicked: if (controller) controller.tool = toolEraser
                }
                
                Item { Layout.fillWidth: true } // Spacer
            }
        }
        
        // Canvas area
        PaintCanvas {
            id: paintCanvas
            Layout.fillWidth: true
            Layout.fillHeight: true
            currentTool: controller ? controller.tool : 0
        }
        
        // Status bar
        Rectangle {
            id: statusBar
            Layout.fillWidth: true
            height: 26
            color: "#f0f0f0"
            border.color: "#d0d0d0"
            
            Label {
                anchors.fill: parent
                anchors.margins: 5
                text: controller ? controller.statusMessage : "Ready"
            }
        }
    }
    
    // Color dialogs
    Platform.ColorDialog {
        id: penColorDialog
        title: "Select Pen Color"
        color: paintCanvas.penColor
        onAccepted: {
            paintCanvas.penColor = color
            penColorButton.color = color
        }
    }
    
    Platform.ColorDialog {
        id: fillColorDialog
        title: "Select Fill Color"
        color: paintCanvas.fillColor
        onAccepted: {
            paintCanvas.fillColor = color
            fillColorButton.color = color
        }
    }
}