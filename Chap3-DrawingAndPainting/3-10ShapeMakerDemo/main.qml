import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

Window {
    id: mainWindow
    width: 722
    height: 514
    visible: true
    title: "Shape Drawing"
    
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 11
        spacing: 6
        
        // Shape canvas area
        ShapeCanvas {
            id: shapeCanvas
            Layout.fillWidth: true
            Layout.fillHeight: true
        }
        
        // Controls panel
        ColumnLayout {
            Layout.fillWidth: true
            spacing: 6
            
            // Shape selection
            RowLayout {
                Layout.fillWidth: true
                Label {
                    text: "Shape"
                }
                ComboBox {
                    id: shapeCombo
                    Layout.fillWidth: true
                    model: [
                        { text: "Polygon", value: 0 },
                        { text: "Rectangle", value: 1 },
                        { text: "Rounded Rectangle", value: 2 },
                        { text: "Ellipse", value: 3 },
                        { text: "Pie", value: 4 },
                        { text: "Chord", value: 5 },
                        { text: "Text", value: 6 },
                        { text: "Pixmap", value: 7 }
                    ]
                    textRole: "text"
                    valueRole: "value"
                    
                    onActivated: {
                        shapeCanvas.shapeType = currentValue
                        shapeCanvas.requestPaint()
                    }
                }
            }
            
            // Pen width
            RowLayout {
                Layout.fillWidth: true
                Label {
                    text: "Pen Width"
                }
                SpinBox {
                    id: penWidthSpinbox
                    Layout.fillWidth: true
                    from: 0
                    to: 20
                    value: 1
                    
                    onValueChanged: {
                        shapeCanvas.penWidth = value
                        shapeCanvas.requestPaint()
                    }
                }
            }
            
            // Pen style
            RowLayout {
                Layout.fillWidth: true
                Label {
                    text: "Pen Style"
                }
                ComboBox {
                    id: penStyleCombobox
                    Layout.fillWidth: true
                    model: [
                        { text: "Solid", value: Qt.SolidLine },
                        { text: "Dash", value: Qt.DashLine },
                        { text: "Dot", value: Qt.DotLine },
                        { text: "Dash Dot", value: Qt.DashDotLine },
                        { text: "Dash Dot Dot", value: Qt.DashDotDotLine },
                        { text: "None", value: Qt.NoPen }
                    ]
                    textRole: "text"
                    valueRole: "value"
                    
                    onActivated: {
                        shapeCanvas.penStyle = currentValue
                        shapeCanvas.requestPaint()
                    }
                }
            }
            
            // Pen cap
            RowLayout {
                Layout.fillWidth: true
                Label {
                    text: "Pen Cap"
                }
                ComboBox {
                    id: penCapCombobox
                    Layout.fillWidth: true
                    model: [
                        { text: "Flat", value: Qt.FlatCap },
                        { text: "Square", value: Qt.SquareCap },
                        { text: "Round", value: Qt.RoundCap }
                    ]
                    textRole: "text"
                    valueRole: "value"
                    
                    onActivated: {
                        shapeCanvas.penCap = currentValue
                        shapeCanvas.requestPaint()
                    }
                }
            }
            
            // Pen join
            RowLayout {
                Layout.fillWidth: true
                Label {
                    text: "Pen Join"
                }
                ComboBox {
                    id: penJoinComboBox
                    Layout.fillWidth: true
                    model: [
                        { text: "Miter", value: Qt.MiterJoin },
                        { text: "Bevel", value: Qt.BevelJoin },
                        { text: "Round", value: Qt.RoundJoin }
                    ]
                    textRole: "text"
                    valueRole: "value"
                    
                    onActivated: {
                        shapeCanvas.penJoin = currentValue
                        shapeCanvas.requestPaint()
                    }
                }
            }
            
            // Brush style
            RowLayout {
                Layout.fillWidth: true
                Label {
                    text: "Brush Style"
                }
                ComboBox {
                    id: brushStyleCombobox
                    Layout.fillWidth: true
                    model: [
                        { text: "Linear Gradient", value: 0 },
                        { text: "Radial Gradient", value: 1 },
                        { text: "Conical Gradient", value: 2 },
                        { text: "Texture", value: 3 },
                        { text: "Solid", value: 4 },
                        { text: "Horizontal", value: 5 },
                        { text: "Vertical", value: 6 },
                        { text: "Cross", value: 7 },
                        { text: "Backward Diagonal", value: 8 },
                        { text: "Forward Diagonal", value: 9 },
                        { text: "Diagonal Cross", value: 10 },
                        { text: "None", value: 11 }
                    ]
                    textRole: "text"
                    valueRole: "value"
                    
                    onActivated: {
                        shapeCanvas.brushStyle = currentValue
                        shapeCanvas.requestPaint()
                    }
                }
            }
            
            // Checkboxes
            RowLayout {
                Layout.fillWidth: true
                CheckBox {
                    id: antiAlisingCheckbox
                    text: "Antialising"
                    onToggled: {
                        shapeCanvas.antialiased = checked
                        shapeCanvas.requestPaint()
                    }
                }
                CheckBox {
                    id: transformsCheckbox
                    text: "Transforms"
                    onToggled: {
                        shapeCanvas.transformed = checked
                        shapeCanvas.requestPaint()
                    }
                }
            }
        }
    }
}