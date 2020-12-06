var num = 0;

function cheak() {
    num = document.getElementById('numpass').value;
    num = Number(num);
}


function hide2jump() {
        if(num === 1027) {
            location.replace("hide2.html");
        }
        else {
            location.replace("hide.html");
        }
}

function indexjump() {
    location.replace("index.html");
}
