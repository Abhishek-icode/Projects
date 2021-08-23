const cityname = document.getElementById("cityname")
const submitbtn = document.getElementById('submitbtn')
const cname = document.getElementById('cname')

const getinfo = (event) => {
    event.preventDefault();
    let cityval = cityname.value;
    if(cityval === ""){
        cname.innerHTML = `Please enter your Location befor search`;
    }else{
        try{
            let url = `https://api.openweathermap.org/data/2.5/weather?q=${cityval}&appid=3b5b770eb1c757c9294345a09164e446`
            const response = await fetch(url)
            console.log(response)
        }catch{
            cname.innerHTML = `Please enter your Location Properly`;
        }
    }
}
submitbtn.addEventListener("click", getinfo)