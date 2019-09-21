/*
Debug utility JavaScript.

Written by Michael Wheeler.
 */

function printDebug(event) {
    let debugEl = document.getElementById("debug");
    debugEl.innerText = `Width: ${window.innerWidth}px; Height: ${window.innerHeight}px`;
}

printDebug();
window.onresize = printDebug;

