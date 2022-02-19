const miFrame = document.getElementsByTagName("iframe")[0];
if(miFrame != undefined){
    const miFrameOH = miFrame.outerHTML.split(' ');
    miFrameOH.splice(1, 0, 'allowfullscreen=""');
    miFrame.outerHTML = miFrameOH.join(' ');
}
