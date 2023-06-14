let sun           = document.querySelector(".morning");
let moon          = document.querySelector(".night");
let body          = document.getElementsByTagName('body');
let section       = document.querySelector('.main')
let form          = document.querySelector('form')



sun.addEventListener('click', switchsun)
moon.addEventListener('click', switchmoon)

function switchsun(){
  body[0].style.backgroundColor = 'rgb(27, 90, 87)';
  form.style.backgroundColor    = 'rgb(191, 191, 43)';
  section.style.backgroundColor = 'rgb(18, 111, 53)';
  
  


};




function switchmoon(){
  body[0].style              = 'backgroundColor:rgb(19, 19, 33)';
  section.style              = 'background-color: rgb(25, 85, 135)';
  form.style.backgroundColor = 'rgb(23, 50, 75)';
  
  

  
  
};
