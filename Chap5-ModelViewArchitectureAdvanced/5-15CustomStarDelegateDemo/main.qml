import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    visible: true
    width: 600
    height: 400
    title: "Star Rating Demo (Qt Quick)"
    
    // Main content
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10
        spacing: 10
        
        // Header with column titles
        Rectangle {
            Layout.fillWidth: true
            height: 30
            color: "#f0f0f0"
            
            RowLayout {
                anchors.fill: parent
                spacing: 0
                
                Label {
                    text: "Course Title"
                    font.bold: true
                    Layout.preferredWidth: parent.width * 0.5
                    Layout.leftMargin: 5
                    color: "black"
                }
                
                Label {
                    text: "Category"
                    font.bold: true
                    Layout.preferredWidth: parent.width * 0.25
                    color: "black"
                }
                
                Label {
                    text: "Rating"
                    font.bold: true
                    Layout.preferredWidth: parent.width * 0.25
                    color: "black"
                }
            }
        }
        
        // Table of courses
        ListView {
            id: courseListView
            Layout.fillWidth: true
            Layout.fillHeight: true
            clip: true
            model: courseModel
            
            // Row delegate
            delegate: Rectangle {
                width: courseListView.width
                height: 50
                color: index % 2 === 0 ? "#ffffff" : "#f8f8f8"
                
                // Row content
                RowLayout {
                    anchors.fill: parent
                    spacing: 0
                    
                    // Course title column
                    Text {
                        text: title
                        color: "black"
                        Layout.preferredWidth: parent.width * 0.5
                        Layout.fillHeight: true
                        verticalAlignment: Text.AlignVCenter
                        elide: Text.ElideRight
                        Layout.leftMargin: 5
                    }
                    
                    // Category column
                    Text {
                        text: category
                        color: "black"
                        Layout.preferredWidth: parent.width * 0.25
                        Layout.fillHeight: true
                        verticalAlignment: Text.AlignVCenter
                        elide: Text.ElideRight
                    }
                    
                    // Rating column with imported StarRating component
                    Item {
                        Layout.preferredWidth: parent.width * 0.25
                        Layout.fillHeight: true
                        
                        Loader {
                            id: starRatingLoader
                            anchors.verticalCenter: parent.verticalCenter
                            anchors.left: parent.left
                            anchors.leftMargin: 5
                            source: "StarRating.qml"
                            
                            onLoaded: {
                                item.rating = model.rating;
                                item.starColor = "black";
                                item.hoverColor = "yellow";
                                item.backgroundColor = "green";
                                item.textColor = "white";
                            }
                            
                            Connections {
                                target: starRatingLoader.item
                                function onEdited(newRating) {
                                    courseController.updateRating(index, newRating);
                                }
                            }
                        }
                    }
                }
            }
            
            ScrollBar.vertical: ScrollBar {}
        }
    }
}