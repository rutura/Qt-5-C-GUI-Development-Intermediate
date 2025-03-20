import QtQuick
import QtQuick.Controls

TextField {
    id: parentLineEdit
    width: 200
    height: 40
    
    // Handle key press events
    Keys.onPressed: function(event) {
        eventLogger.log("ParentLineEdit keyPressEvent")
        eventLogger.log(`ParentLineEdit Accepted: ${event.accepted}`)
        // The default behavior is to allow the event to be processed by the TextField
    }
}