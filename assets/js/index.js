let node = document.createElement("div");
node.setAttribute("class", "container-inside");
// let tagName = document.getElementsByTagName("section")[0];
let tagName = document.getElementById("sec1");
let btn1 = document.querySelector(".btn1");
let visible = 5;
const handleArticles =()=>{
    let node = document.createElement("div");
    node.setAttribute("class", "container-inside");
    tagName.appendChild(node);
    var container = Array.from(document.querySelectorAll(".container-inside")).pop();
    console.log(container);
    $.ajax({
        type:"GET",
        url: `/blog/randomfacts/${visible}/`,
        success: function(response){
            let data = response.data;
            data.map((post)=>{
            container.innerHTML += `
<article class="post">
<img src="/media/${post.image}" alt="">
<div>
<span><b style='font-size:14px;'>Tariq Ahmed </b><span style='font-size:12px;'>in </span><b style='font-size:14px;'>${post.category}</b></span>
</div>
<h6>${post.title}</h6>
<p>${post.content.slice(0,500)}</p>
<p><a href="/blog/technologyview/${post.postId}">Read more . </a><span>4 min read</span></p> 
</article>
`
            });
            console.log(response.check);

            if(response.check){
                console.log(btn1)
                btn1.innerHTML = "No more posts";
            }
        }
    })
};
handleArticles();
bt.addEventListener("click", ()=>{
    visible += 3;
    handleArticles();
})