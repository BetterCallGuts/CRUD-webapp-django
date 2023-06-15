let sun           = document.querySelector(".morning");
let moon          = document.querySelector(".night");
let body          = document.getElementsByTagName('body');
let main          = document.querySelector(".main")
let headerRow     = document.querySelectorAll('.header-row');
let header        = document.querySelector('.header');
let bodyProject   = document.querySelector('.body');
let bodyRow       = document.querySelectorAll('.body-row');
let tables        = document.querySelectorAll('nav h2')
let arrowUp       = document.querySelector('.up')
let arrowDown     = document.querySelector('.down')
let arrowLeft     = document.querySelector('.left')
let arrowRight    = document.querySelector('.right')
let y             = 0
let x             = 0


sun.addEventListener('click', switchsun );
moon.addEventListener('click',switchmoon );
// click
arrowDown.addEventListener('click', arrowdown)
arrowUp.addEventListener('click', arrowup)
arrowLeft.addEventListener('click', arrowleft)
arrowRight.addEventListener('click', arrowright)
// mousedown
arrowDown.addEventListener('mousedown', arrowdown)
arrowUp.addEventListener('mousedown', arrowup)
arrowLeft.addEventListener('mousedown', arrowleft)
arrowRight.addEventListener('mousedown', arrowright)

document.addEventListener('keydown', recordKey);
// console.log(header.scrollWidth)

function  recordKey(event) {
  
  if (event.key =='ArrowUp' ){
    arrowup()
  }
  if( event.key == 'ArrowDown' ){
    arrowdown()
  }
  if( event.key == 'ArrowLeft'){
    arrowleft()
  }
  if( event.key == 'ArrowRight'){
    arrowright()
  }
  
}

function arrowleft(){
  if (x < 0){
    x = 50
  }
  
  x -= 50
  main.scroll(0,y)
  header.scroll(x,0)
  bodyProject.scroll(x,0)
}
function arrowright(){
  if (x > header.scrollWidth - header.offsetWidth){
    x = header.scrollWidth - header.offsetWidth
  }
  x += 50
  bodyProject.scroll(x,0)
  header.scroll(x,0)
  main.scroll(x,y)
}
function arrowdown(){
  y += 50
  if (y > bodyProject.scrollHeight - 450){
    y = bodyProject.scrollHeight - 450
  }
  bodyProject.scroll(x,0)
  main.scroll(0,y);
}
function arrowup(){
  if (y < 0){
    y = 50
  }
  y -= 50
  bodyProject.scroll(x,0)
  main.scroll(0,y);
}
// console.log()
function switchsun(){
  body[0].style.backgroundColor = 'rgb(27, 90, 87)';
  for (let i = 0; i < headerRow.length; i++){
    headerRow[i].style.backgroundColor = 'rgb(30, 129, 139)';
    
  };
  header.style.backgroundColor = 'rgb(94, 190, 76)';
  bodyProject.style.backgroundColor = 'rgb(155, 116, 11)';
  
  for( let i = 0; i < bodyRow.length; i++){
    bodyRow[i].style.backgroundColor = 'rgb(27, 163, 79)';
    bodyRow[i].style.color = 'black';
  }
  for( let i = 0; i < tables.length; i++){
    if (tables[i].classList.contains('selected')){
      tables[i].style.backgroundColor = 'rgb(152, 64, 30)'
    }else{

      tables[i].style.backgroundColor = 'rgb(203, 112, 22)';
    }
    
  }
  // for (let i =0; i< arrow.length; i++){
  //   arrow[i].style.backgroundColor = 'gray';
  // }
};


function switchmoon(){
  body[0].style = 'backgroundColor:rgb(19, 19, 33);';
  for (let i = 0; i < headerRow.length; i++){
    headerRow[i].style.backgroundColor = 'rgb(107, 102, 25)';
  };
  header.style.backgroundColor = 'rgb(25, 78, 19)';
  bodyProject.style.backgroundColor = 'rgb(82, 33, 33)';
  for( let i = 0; i < bodyRow.length; i++){
    bodyRow[i].style.backgroundColor = 'rgb(11, 9, 44)';
    bodyRow[i].style.color = 'white';
  }
  

  for( let i = 0; i < tables.length; i++){
    if (tables[i].classList.contains('selected')){
        tables[i].style.backgroundColor = 'rgb(46, 2, 87)';
    }else{

      tables[i].style.backgroundColor = 'rgb(3, 89, 73)';
    }
    
  }

  // for (let i =0; i< arrow.length; i++){
  //     arrow[i].style.backgroundColor = 'rgb(39, 44, 69)';
  // }
};

//rgb(19, 19, 33)