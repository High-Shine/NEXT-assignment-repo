const input = document.querySelector("#city");
const button = document.querySelector("#submit");
const weatherBox = document.querySelector("#weatherBox");

const API_KEY = "2caba635ce4294a097405142dac92d25";

button.addEventListener("click", async () => {
  //input의 값을 가져와서 도시이름으로 url에 넣는다.
  const city = input.value;

  try {
    const res = await axios.get(
      `https://api.openweathermap.org/data/2.5/forecast?q=${city}&appid=${API_KEY}`
    );
    console.log(res);

    // 다시 검색 시 초기화
    weatherBox.innerHTML = ''

    //for문으로 데이터 가져오기
    for (let i = 2; i < 7; i++) {
    const { main, description, icon } = res.data.list[i].weather[0];
    const temp = Math.round(res.data.list[i].main.temp - 273.15);
    const feels_like = Math.round(res.data.list[i].main.feels_like - 273.15);
    const humidity = res.data.list[i].main.humidity;
    const name = res.data.city.name;


    //사용자에게 보여주기(div 추가)
    weatherBox.innerHTML += `
      <div class ="information">
        <div class="name">${name}</div>
        <img class="icon" src="http://openweathermap.org/img/w/${icon}.png">
        <div class="main">${main}</div>
        <div class="description">${description}</div>
        <div class="temp">Temp = ${temp}°C</div>
        <div class="feels_like">Feels like ${feels_like}°C</div>
        <div class='humidity'>Humid = ${humidity}%</div>
      </div>
    `;
    }
  } catch (error) {
    console.log(error);
  }
});
