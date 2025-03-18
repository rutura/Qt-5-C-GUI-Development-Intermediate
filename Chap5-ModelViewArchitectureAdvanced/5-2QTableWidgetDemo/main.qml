import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    id: window
    visible: true
    width: 800
    height: 600
    title: "QtQuick MVC Demo"
    
    Rectangle {
        anchors.fill: parent
        color: "#f0f0f0"
        
        ColumnLayout {
            anchors.fill: parent
            anchors.margins: 10
            
            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: "white"
                border.color: "#cccccc"
                
                ListView {
                    id: tableView
                    anchors.fill: parent
                    anchors.margins: 1
                    clip: true
                    
                    model: personListModel.people
                    
                    header: Rectangle {
                        width: tableView.width
                        height: 40
                        color: "#e0e0e0"
                        
                        Row {
                            anchors.fill: parent
                            
                            Repeater {
                                model: ["First Name", "Last Name", "Age", "Profession", "Status", "Country", "City", "Score"]
                                
                                Rectangle {
                                    width: tableView.width / 8
                                    height: 40
                                    color: "transparent"
                                    border.width: 1
                                    border.color: "#cccccc"
                                    
                                    Text {
                                        anchors.centerIn: parent
                                        text: modelData
                                        font.bold: true
                                    }
                                }
                            }
                        }
                    }
                    
                    delegate: Rectangle {
                        width: tableView.width
                        height: 30
                        color: index % 2 == 0 ? "#ffffff" : "#f7f7f7"
                        
                        Row {
                            anchors.fill: parent
                            
                            Rectangle {
                                width: tableView.width / 8
                                height: 30
                                color: "transparent"
                                border.width: 1
                                border.color: "#e0e0e0"
                                
                                Text {
                                    anchors.right: parent.right
                                    anchors.rightMargin: 10
                                    anchors.verticalCenter: parent.verticalCenter
                                    text: modelData.firstName
                                }
                            }
                            
                            Rectangle {
                                width: tableView.width / 8
                                height: 30
                                color: "transparent"
                                border.width: 1
                                border.color: "#e0e0e0"
                                
                                Text {
                                    anchors.right: parent.right
                                    anchors.rightMargin: 10
                                    anchors.verticalCenter: parent.verticalCenter
                                    text: modelData.lastName
                                }
                            }
                            
                            Rectangle {
                                width: tableView.width / 8
                                height: 30
                                color: "transparent"
                                border.width: 1
                                border.color: "#e0e0e0"
                                
                                Text {
                                    anchors.right: parent.right
                                    anchors.rightMargin: 10
                                    anchors.verticalCenter: parent.verticalCenter
                                    text: modelData.age
                                }
                            }
                            
                            Rectangle {
                                width: tableView.width / 8
                                height: 30
                                color: "transparent"
                                border.width: 1
                                border.color: "#e0e0e0"
                                
                                Text {
                                    anchors.right: parent.right
                                    anchors.rightMargin: 10
                                    anchors.verticalCenter: parent.verticalCenter
                                    text: modelData.profession
                                }
                            }
                            
                            Rectangle {
                                width: tableView.width / 8
                                height: 30
                                color: "transparent"
                                border.width: 1
                                border.color: "#e0e0e0"
                                
                                Text {
                                    anchors.right: parent.right
                                    anchors.rightMargin: 10
                                    anchors.verticalCenter: parent.verticalCenter
                                    text: modelData.maritalStatus
                                }
                            }
                            
                            Rectangle {
                                width: tableView.width / 8
                                height: 30
                                color: "transparent"
                                border.width: 1
                                border.color: "#e0e0e0"
                                
                                Text {
                                    anchors.right: parent.right
                                    anchors.rightMargin: 10
                                    anchors.verticalCenter: parent.verticalCenter
                                    text: modelData.country
                                }
                            }
                            
                            Rectangle {
                                width: tableView.width / 8
                                height: 30
                                color: "transparent"
                                border.width: 1
                                border.color: "#e0e0e0"
                                
                                Text {
                                    anchors.right: parent.right
                                    anchors.rightMargin: 10
                                    anchors.verticalCenter: parent.verticalCenter
                                    text: modelData.city
                                }
                            }
                            
                            Rectangle {
                                width: tableView.width / 8
                                height: 30
                                color: "transparent"
                                border.width: 1
                                border.color: "#e0e0e0"
                                
                                Text {
                                    anchors.right: parent.right
                                    anchors.rightMargin: 10
                                    anchors.verticalCenter: parent.verticalCenter
                                    text: modelData.socialScore
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}