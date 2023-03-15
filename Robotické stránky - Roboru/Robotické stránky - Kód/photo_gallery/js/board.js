const prevBtn = document.querySelector(".prev-btn");
const nextBtn = document.querySelector(".next-btn");
const photo = document.querySelector(".photo");
const photoNumber = document.querySelector(".photo-number");

let currentPhotoIndex = 1;

const updatePhotoNumber = () => {
  photoNumber.textContent = `${currentPhotoIndex} / 9`;
};

const showPhoto = () => {
  photo.src = `../resized_top_images/Board/fotka${currentPhotoIndex}.jpg`;
  updatePhotoNumber();
};

prevBtn.addEventListener("click", () => {
  if (currentPhotoIndex > 1) {
    currentPhotoIndex--;
    showPhoto();
  }
});

nextBtn.addEventListener("click", () => {
  if (currentPhotoIndex < 9) {
    currentPhotoIndex++;
    showPhoto();
  }
});

updatePhotoNumber();

const photoContainer = document.querySelector(".photo-container");

const setGalleryHeight = () => {
  const photos = document.querySelectorAll(".photo");
  let maxHeight = 0;
  for (let i = 0; i < photos.length; i++) {
    const photoHeight = photos[i].clientHeight;
    if (photoHeight > maxHeight) {
      maxHeight = photoHeight;
    }
  }
  photoContainer.style.height = `${maxHeight}px`;
};

window.addEventListener("load", () => {
  setGalleryHeight();
});

window.addEventListener("resize", () => {
  setGalleryHeight();
});
