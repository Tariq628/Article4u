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
  // closeBtn.innerHTML = "<i class='fas fa-times'></i>";
});
// closeBtn.addEventListener("click", () => {
//   searchContainer.classList.remove("active");
//   searchBtn.classList.add("fa-search");
//   inputBtn.classList.remove("active");
//   inputBtn.setAttribute("placeholder", "");
//   submit.innerHTML = "";
//   closeBtn.innerHTML = "";
// });
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