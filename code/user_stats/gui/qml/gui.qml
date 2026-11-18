import Qt.labs.platform
import QtQuick
import QtQuick.Controls
import QtQuick.Window

ApplicationWindow {
    width: 480
    height: 640
    visible: true
    title: qsTr("user statistics")

    JsonLoader {
        id: jsonLoader

        source: "data.json"
    }

    Text {
        // reference element by id
        y: 60
        x: 20
        color: 'white'
        horizontalAlignment: Text.AlignHCenter
        text: Qt.formatDate(new Date(), "ddd MMM d yyyy")
    }

    Grid {
        id: activityMatrix

        // anchors.fill: parent
        x: 4
        y: 100
        anchors.bottom: page.bottom
        anchors.bottomMargin: 4
        rows: 4
        columns: 7
        spacing: 4

        Repeater {
            model: 28

            Rectangle {
                // blue -> red

                property real value: index / 27

                width: 50
                height: 50
                color: Qt.hsla(0.67 - value * 0.67, 1, 0.5, 1)
            }

        }

    }

}
