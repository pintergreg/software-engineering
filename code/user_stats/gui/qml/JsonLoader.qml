import QtQuick
import QtQuick.Controls

Item {
    property url source
    property string text
    property var jsonObject

    function load(url) {
        let xhr = new XMLHttpRequest();
        xhr.open("GET", url);
        xhr.onreadystatechange = function() {
            if (xhr.readyState !== XMLHttpRequest.DONE)
                return ;

            text = xhr.responseText;
            jsonObject = JSON.parse(xhr.responseText);
        };
        xhr.send();
    }

    onSourceChanged: load(source)
}
