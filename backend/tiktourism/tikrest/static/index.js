let slideIndex;
if (sessionStorage.getItem("index") === null) {
  slideIndex = 1;
  sessionStorage.setItem("index", 1);
} else {
  slideIndex = parseInt(sessionStorage.getItem("index"));
}

let slideTime = (new Date()).getTime();
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  var form = document.getElementById(document.getElementsByClassName("mySlides")[slideIndex - 1].children[1].innerHTML.split(" ")[0]);
  let time = document.createElement('input')
  time.setAttribute('name', 'time')
  time.setAttribute('value', ((new Date()).getTime() - slideTime).toString())
  time.style.display = 'none'
  form.appendChild(time);
  form.submit();
  sessionStorage.setItem("index", slideIndex + n);
  showSlides(parseInt(sessionStorage.getItem("index")));
}

function showSlides(n) {
  slideTime = (new Date()).getTime();
  let i;
  let slides = document.getElementsByClassName("mySlides");
  if (n > slides.length) {
    slideIndex = 1
  }
  if (n < 1) {
    slideIndex = slides.length
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block";
}

function like() {
  var form = document.getElementById(document.getElementsByClassName("mySlides")[slideIndex - 1].children[3].innerHTML.split(" ")[1]);
  let liked = document.createElement('input')
  liked.setAttribute('name', 'liked')
  liked.setAttribute('value', 'pressed')
  liked.style.display = 'none'
  form.appendChild(liked);
  form.submit();
}