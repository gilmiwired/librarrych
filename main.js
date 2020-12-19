var bgm;
bgm = new Audio();
bgm.src = "music/っざけんなよおおおお！！！.wav"

function set2fig(num) {
   // 桁数が1桁だったら先頭に0を加えて2桁に調整する
   var ret;
   if( num < 10 ) { ret = "0" + num; }
   else { ret = num; }
   return ret;
}
function nowTime() { //日時の表示をリアルタイム化
   var now = new Date();
   var year = set2fig(now.getFullYear());
   var mon = set2fig(now.getMonth()+1);
   var day = set2fig(now.getDate());
   var hour = set2fig(now.getHours());
   var min = set2fig(now.getMinutes());
   var sec = set2fig(now.getSeconds());
   var msg = year + "年" + mon + "月" + day + "日" + hour + "時" + min + "分" + sec + "秒";
   document.getElementById("time").innerHTML = msg;
}
setInterval('nowTime()',100); //100ミリ秒ごとに時刻を更新。できれば1000ミリ秒ごとにしたい。

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
