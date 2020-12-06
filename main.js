document.getElementById("view_time").innerHTML = getNow();
var bgm;
bgm = new Audio();
bgm.src = "music/bgm.mp3"

function getNow(){//現在時刻の取得
    var now = new Date();
    var year = now.getFullYear();
    var mon = now.getMonth()+1;
    var day = now.getDate();
    var hour = now.getHours();
    var min = now.getMinutes();
    var sec = now.getSeconds();
    var s = year + "年" + mon + "月" + day + "日" + hour + "時" + min + "分" + sec + "秒";
    return s;
}
function koshin(){
	location.reload();
}

function koshin(){//サイト更新ボタン
    bgm.play(); //音楽再生
    var result=confirm('更新するよ！')
    if(result){ //サイト更新の確認
        location.reload();
    }
}

function open(){//ページを開いたときの処理。ここにカメラの更新と画像表示を記述
    //alert("ページが読み込まれました！");
}
window.onload = open();
