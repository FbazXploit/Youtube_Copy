const btnSearch = document.querySelector(".navbar .container .btn-search");
const divSearch = document.querySelector(".navbar .container .inputDiv");
const inputSearch = document.querySelector(".navbar .container .inputDiv .input-search");
const h3 = document.querySelector(".navbar .container .titleYt");
const btnDelete = document.querySelector(".navbar .container .inputDiv .delete");
const titleVideo = document.querySelector(".titleVideoSingle .title");
const detailVideo = document.querySelector(".titleVideoSingle .detail");
const showComments = document.querySelector(".mainVideoSingle .showComments");
const mainVideoSingle = document.querySelector(".mainVideoSingle")
const commentsList = document.querySelector(".comments-list")
const closeComments = document.querySelector(".comments-list .close .close-button")

btnSearch.onclick = () => {
  h3.classList.toggle("nonActive");
  divSearch.classList.toggle("active");
}

btnDelete.onclick = () => {
  inputSearch.value = "";
}

titleVideo.onclick = () => {
  detailVideo.classList.toggle("active");
}

showComments.onclick = () => {
  mainVideoSingle.classList.toggle("nonActive")
  commentsList.classList.toggle("active")
}

closeComments.onclick = () => {
  mainVideoSingle.classList.remove("nonActive")
  commentsList.classList.remove("active")
}