console.log('box generator script');

// hide hidden elements in boxform2
/*
let boxform2 = document.getElementById('boxform2');
for (const child of boxform2.children) {
    if (child.tagName == "LABEL") {
        child.style.display = 'none';
    }
    else if (child.tagName == "INPUT" && child.id != "boxcode" && child.value != "Add to Database") {

        child.style.display = 'none';
    }
}*/

function generateBox(thisForm) {
    var boxcode = document.getElementById("boxcode");
    var boxtxt = "; Box generator gcode";
    boxtxt += "\n;Name = "+thisForm.box_Name.value;
    boxtxt += "\n;Length = "+thisForm.box_Length.value;
    boxtxt += "\n;Width = "+thisForm.box_Width.value;
    boxtxt += "\n;Height = "+thisForm.box_Depth.value;
    //console.log(boxtxt);
    
    document.getElementById("id_boxcode_Length").value = thisForm.box_Length.value;
    document.getElementById("id_boxcode_Width").value = thisForm.box_Width.value;
    document.getElementById("id_boxcode_Depth").value = thisForm.box_Depth.value;
    document.getElementById("id_boxcode_Name").value = thisForm.box_Name.value;

    boxcode.innerHTML = boxtxt;
}