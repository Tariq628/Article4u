// let tagName = document.getElementsByTagName("section")[0];
function fixHtml(html) {
    var div = document.createElement('div');
    div.innerHTML = html
    return (div.innerHTML);
}
let tagName = document.getElementById("sec1");
let btn1 = document.querySelector(".btn1");
let visible = 5;
let node = document.createElement("div");
node.setAttribute("class", "container-inside");
tagName.appendChild(node);
var container = Array.from(document.querySelectorAll(".container-inside")).pop();
const handleArticles = () => {
    $.ajax({
        type: "GET",
        url: `${document.location.pathname}${visible}/`,
        success: function (response) {
            let posts = response.posts;
            posts.map((post) => {
                container.innerHTML += `
                    <article class="post">
                    <img src="/media/${post.image}" alt="">
                    <div>
                    <span><b style='font-size:14px;'>${post.created_by__username} </b><span style='font-size:12px;'>in </span><b style='font-size:14px;'>${post.category}</b></span>
                    </div>
                    <h6>${post.title}</h6>
                    <p>${fixHtml(post.content.slice(0, 600))}</p>
                    <p><a href="/template-view/${post.id}">Read more . </a><span>4 min read</span></p> 
                    </article>
                    `
            });
                        if (response.check) {
                btn1.innerHTML = "No more posts";
            }
        }
    })
};


handleArticles();
bt.addEventListener("click", () => {
    visible += 3;
    handleArticles();
    let c_inside = document.querySelectorAll(".container-inside");
    c_inside.forEach(element => {
        setTimeout(() => {
            if (element.children.length === 1) {
                element.children[0].classList.add("one");
            }
            else if (element.children.length === 2) {
                Array.from(element.children).forEach(item => {
                    item.classList.add("two");
                });
            }
        }, 100);
    });
})
