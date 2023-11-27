num1 = 54;
num2 = 0;
async function logJSONData() {
    const response = await fetch("https://api.openweathermap.org/data/2.5/onecall?lat=37.5582018&lon=126.9979742&appid=4ada87268facd87550e6a5126401fda4&units=metric");
    const jsonData = await response.json();
    const hourly = jsonData.hourly;
    let weather_time = document.querySelector('#weather_time'); //id가 weather_time인 html 요소 지정
    for (let hour of hourly) { //array로 되어있는 배열 for of를 이용하여 반복문 돌리기
        let container = document.createElement('li');
        let weather_desc = hour.weather[0].main
        container.className = 'hour'
        container.id = hour.dt * 1000;
        let date = new Date(hour.dt * 1000); // 1000을 곱해야 timestamp를 javascript Date 객체에 연동 가능!
        container.style.textAlign = 'center'
        num2 = date.getHours();
        if(num1 ==54){
            num1 = date.getHours();
            console.log(num1);
        }else if(num2==num1){
            break;
        }
        container.innerHTML = `${date.getHours()}시의 기온은 ${hour.temp}°C 날씨는 ${weather_desc}`;
        weather_time.appendChild(container); //ul의 자손으로 li 붙이기
    }
}