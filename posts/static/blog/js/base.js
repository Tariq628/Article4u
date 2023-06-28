const searchBtn = document.querySelector(".search-btn");
const inputBtn = document.querySelector(".input");
const submit = document.querySelector(".span-submit");
const closeBtn = document.querySelector(".close-btn");
const searchContainer = document.querySelector(".search-container");

searchBtn.addEventListener("click", () => {
  inputBtn.classList.add("active");
  searchContainer.classList.add("active");
  inputBtn.setAttribute("placeholder", "Type to search..");
  searchBtn.classList.remove("fa-search");
  submit.innerHTML = "<button class='submit-btn' type='submit'>Search</button>";
});


document.body.addEventListener("click", function () {
  searchContainer.classList.remove("active");
  searchBtn.classList.add("fa-search");
  inputBtn.classList.remove("active");
  inputBtn.setAttribute("placeholder", "");
  submit.innerHTML = "";
  closeBtn.innerHTML = "";
});
searchBtn.addEventListener("click", function (ev) {
  ev.stopPropagation(); //this is important! If removed, you'll get both alerts
});
submit.addEventListener("click", function (ev) {
  ev.stopPropagation(); //this is important! If removed, you'll get both alerts
});
inputBtn.addEventListener("click", function (ev) {
  ev.stopPropagation(); //this is important! If removed, you'll get both alerts
});



// for below line of a tags
// let navItems = document.querySelectorAll(".nav-item");
// let Handler = (e) => {
//   navItems.forEach((node) => {
//     console.log(node.classList.contains('border-btm'))
//     if (node.classList.contains('border-btm')){
//       node.classList.remove("border-btm");
//     }
//   });
//   e.currentTarget.classList.add("border-btm");
// };
// navItems.forEach((node) => {
//   node.addEventListener("click", Handler);
// });


// video add through summernote
const iFrame = document.getElementsByTagName("iframe")[0];
if (iFrame) {
  iFrame.height = "100%";
  iFrame.width = "100%";
}



// Making right-items in navbar responsive
rightCenter = document.getElementById("right-center");
searchSmallScreen = document.getElementById("search-small-screen");
accountSmallScreen = document.getElementById("account-small-screen");
postSmallScreen = document.getElementById("post-small-screen");
searchLargeScreen = document.getElementById("search-large-screen");
accountLargeScreen = document.getElementById("account-large-screen");
postLargeScreen = document.getElementById("post-large-screen");


// function will return true if mediaWidth less than 955px
const checkScreenSize = ()=>{
  return window.matchMedia("(max-width:955px)");
}


// first time by default
if(checkScreenSize().matches){
  rightCenter.style.display = 'none';
  searchSmallScreen.innerHTML = searchLargeScreen.outerHTML;
  accountSmallScreen.innerHTML = accountLargeScreen.outerHTML;
  postSmallScreen.innerHTML = postLargeScreen.outerHTML;
}

else{
  rightCenter.style.display = 'flex';
  searchSmallScreen.innerHTML = "";
  accountSmallScreen.innerHTML = "";
  postSmallScreen.innerHTML = "";
}


// if window resize call responsive function
$(window).resize(function(e) {
      if(checkScreenSize().matches){
        rightCenter.style.display = 'none';
        searchSmallScreen.innerHTML = searchLargeScreen.outerHTML;
        accountSmallScreen.innerHTML = accountLargeScreen.outerHTML;
        postSmallScreen.innerHTML = postLargeScreen.outerHTML;

      }
      
      else{
        rightCenter.style.display = 'flex';
        searchSmallScreen.innerHTML = "";
        accountSmallScreen.innerHTML = "";
        postSmallScreen.innerHTML = "";
      }
  });