import QtQuick
import QtQuick.Controls

ParentLineEdit {
    id: childLineEdit
    
    // Override key press events
    Keys.onPressed: function(event) {
        eventLogger.log(`ChildLineEdit Accepted: ${event.accepted}`)
        
        // Simulate event.ignore() by setting accepted to false
        event.accepted = false
        
        if (event.key === Qt.Key_Delete) {
            eventLogger.log("Pressed the Delete Key")
            childLineEdit.clear()
            // Prevent further processing
            event.accepted = true
        } else {
            // Call parent handler via ParentLineEdit's Keys.onPressed
            // In QML we can't directly call super() like in Python
            // So we implement the same behavior here
            eventLogger.log("ParentLineEdit keyPressEvent")
            eventLogger.log(`ParentLineEdit Accepted: ${event.accepted}`)
            
            // Let the default TextField handling occur if we didn't handle it
            if (!event.accepted) {
                // The default behavior will be applied by the TextField itself
                // since we set event.accepted = false
            }
        }
    }
}