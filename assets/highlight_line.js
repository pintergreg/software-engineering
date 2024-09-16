function parse_lines(s){
    var lines = []
    for (let i of s.split(",")) {
        if (i.includes("-")){
            f = parseInt(i.split("-")[0])
            t = parseInt(i.split("-")[1])
            for (x = f; x <= t; x++){
                lines.push(x)
            }
        } else {
            lines.push(parseInt(i))
        }
    }
    return lines
}

function highlight_lines(){
    const collection = document.getElementsByClassName("sourceCode");

    for (let value of collection) {
    var line_numbers = value.getAttribute("data-line-numbers");
    const highlight_background = value.getAttribute("data-highlight-background");
    if (!!line_numbers) {
        for (let i of parse_lines(line_numbers)) {
            var line_id = value.id + "-" + i.toString();
            var line = document.getElementById(line_id);
            line.style.backgroundColor = highlight_background;
        }
    }
    }
}
