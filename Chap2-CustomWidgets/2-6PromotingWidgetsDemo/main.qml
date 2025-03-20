import QtQuick
import QtQuick.Window
import QtQuick.Layouts

Window {
    id: mainWindow
    width: 590
    height: 397
    visible: true
    title: "Water Tank Monitor"
    
    // Main layout is horizontal, matching the original widget
    RowLayout {
        anchors.fill: parent
        anchors.margins: 11
        spacing: 6
        
        // Water tank component
        WaterTank {
            id: waterTank
            Layout.fillHeight: true
            Layout.fillWidth: true
            
            // Connect signals from water tank to indicator functions
            onNormal: indicator.activateNormal()
            onWarning: indicator.activateWarning()
            onDanger: indicator.activateDanger()
        }
        
        // Traffic light indicator component
        Indicator {
            id: indicator
            Layout.fillHeight: true
        }
    }
}