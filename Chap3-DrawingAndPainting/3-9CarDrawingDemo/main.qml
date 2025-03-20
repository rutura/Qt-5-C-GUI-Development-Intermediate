import QtQuick
import QtQuick.Window

Window {
    id: mainWindow
    width: 976
    height: 691
    visible: true
    title: "Car Drawing"
    
    CarCanvas {
        anchors.fill: parent
    }
}