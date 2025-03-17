import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

// DateTimeWidget component that displays current date and time
Item {
    id: dateTimeWidget
    implicitWidth: 234
    implicitHeight: 100
    
    // Layout to arrange date and time vertically
    ColumnLayout {
        anchors.fill: parent
        spacing: 5
        
        // Date label
        Label {
            id: dateLabel
            text: new Date().toLocaleDateString(Qt.locale(), Locale.LongFormat)
            font.family: "Consolas"
            font.pixelSize: 20
            font.bold: true
            horizontalAlignment: Text.AlignHCenter
            Layout.fillWidth: true
        }
        
        // Time label
        Label {
            id: timeLabel
            text: new Date().toLocaleTimeString(Qt.locale(), Locale.LongFormat)
            font.family: "Consolas"
            font.pixelSize: 20
            font.bold: true
            horizontalAlignment: Text.AlignHCenter
            Layout.fillWidth: true
            
            // Style to match the original widget
            background: Rectangle {
                color: "#00eff9"
            }
            color: "#fffff1"
        }
    }
    
    // Timer to update time every second
    Timer {
        interval: 1000
        running: true
        repeat: true
        
        onTriggered: {
            // Update time display
            timeLabel.text = new Date().toLocaleTimeString(Qt.locale(), Locale.LongFormat)
            
            // Update date if needed (checking if day has changed)
            var currentDate = new Date().toLocaleDateString(Qt.locale(), Locale.LongFormat)
            if (dateLabel.text !== currentDate) {
                dateLabel.text = currentDate
            }
        }
    }
}