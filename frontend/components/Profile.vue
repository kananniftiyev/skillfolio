<template>
  <div class="profile-section flex items-center justify-center gap-12 mt-12">
    <div class="profile-section-image">
      <img
        class="rounded-lg profile-image border border-[#666]"
        src="https://s3.amazonaws.com/www-inside-design/uploads/2020/10/aspect-ratios-blogpost-1x1-1.png"
        alt=""
      />
    </div>
    <div class="profile-seciton-texts flex flex-col justify-between">
      <p class="mb-1 font-medium text-lg txt">
        Hello🌻 I am Ayush, a product designer.
      </p>
      <p class="leading-relaxed mb-5 font-medium text-base txt">
        Designing innovative solutions to complex problems with a focus on
        business needs, transforming challenges into user-friendly solutions. A
        curious human thinking by heart ❤️designing by brain 🧠
      </p>
      <a
        href=""
        class="text-center rounded-md border-solid border hover:bg-[#63b874] bg-[#B2E0BB] transition-all duration-300 text-[#2A6B37] border-[#666] px-6 text-base py-2 max-w-[25%]"
        >Open for work</a
      >
    </div>
  </div>
</template>

<style>
.profile-section-image {
  width: 169px !important; /* Fixed width */
  height: 169px !important; /* Fixed height */
}

.profile-image {
  width: auto;
  height: 100%; /* Set height equal to container height */
  max-width: none; /* Remove the maximum width restriction */
  object-fit: cover; /* Ensure the image covers the entire container */
  object-position: center; /* Center the image horizontally */ /* Let the height adjust based on aspect ratio */
}

.txt {
  font-weight: 600;
  font-size: 17px;
  width: 82%;
}
</style>
