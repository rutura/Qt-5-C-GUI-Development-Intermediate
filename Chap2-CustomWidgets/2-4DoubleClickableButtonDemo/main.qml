import QtQuick
import QtQuick.Window
import QtQuick.Controls

Window {
    id: mainWindow
    width: 400
    height: 300
    visible: true
    title: "Widget"
    
    // Create and position our double-clickable button
    DoubleClickableButton {
        id: button
        text: "Double Clickable Button"
        x: 100
        y: 100
        width: 200
        height: 50
        
        // Connect to the double-clicked signal
        onDoubleClicked: {
            // Call the Python function when double-clicked
            console.log("Button double clicked")
        }
    }
}