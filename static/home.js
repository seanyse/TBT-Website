function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

const counter = document.getElementById("counter-hours");
let count = 0;
const max = 170;

const intervalId = setInterval(() => {
  count++;
  counter.innerHTML = '<i class="fa-regular fa-clock"></i> Hours Tutored: ' + count + "+";

  if (count === max) {
    clearInterval(intervalId);
  }
}, 20);


const counter2 = document.getElementById("counter-tutors");
let count2 = 0;
const max2 = 20;

const intervalId2 = setInterval(() => {
  count2++;
  counter2.innerHTML = '<i class="fa-solid fa-chalkboard-user"></i> Availble Tutors: ' + count2 + "+";

  if (count2 === max2) {
    clearInterval(intervalId2);
  }
}, 100);


const counter1 = document.getElementById("counter-money");
let count1 = 3400;
const max1 = 4000;

const intervalId1 = setInterval(() => {
  count1++;
  counter1.innerHTML = '<i class="fa-solid fa-money-bill"></i></i> Money Raised: $' + count1 + "+";

  if (count1 === max1) {
    clearInterval(intervalId1);
  }
}, );

// collapsible

var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}

// scrolling

function reveal() {
  var reveals = document.querySelectorAll(".reveal");
  for (var i = 0; i < reveals.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = reveals[i].getBoundingClientRect().top;
    var elementVisible = 150;
    if (elementTop < windowHeight - elementVisible + 225) {
      reveals[i].classList.add("active");
    } else {
      reveals[i].classList.remove("active");
    }
  }
}
window.addEventListener("scroll", reveal);
