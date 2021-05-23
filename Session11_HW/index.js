function getRandomHexaColor() {
    const hexa = '0123456789abcdef';
    var color = "#" ;
    for ( i =0; i<6; i++ ) {
        color += hexa[Math.floor(Math.random() * 16)];
    }
    return color;
};


setInterval( () => {
    document.querySelector('body').style.backgroundColor =  getRandomHexaColor();
},100);



// -----시계 들어갈 자리------


function getCurrentTime() {
    const date = new Date();
    // console.log(date);
    var year = date.getFullYear();
    var month = date.getMonth();
    var day = date.getDate();
    var hour = date.getHours();
    var minute = date.getMinutes();
    var second = date.getSeconds();

    month += 1 
    // 아니 이게 왜 안맞는지는 모르겠는데; 출력은 MAY인데 왜 값은 4로 나오는지... 
    // 어쩔수 없이 보정합니다.
    if (month < 10){
        month = '0' + month
    }

    if (day < 10){
        day = '0' + day
    }

    if (hour < 10){
        hour = '0' + hour
    }

    if (minute < 10){
        minute = '0' + minute
    }

    if (second < 10){
        second = '0' + second
    }


    result=`${year}년 ${month}월 ${day}일 ${hour}시 ${minute}분 ${second}초`;
    return result;
};




setInterval( () => {
    document.querySelector('.now').innerHTML =  getCurrentTime();
},100);
