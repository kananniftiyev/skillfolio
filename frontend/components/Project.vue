<template>
  <a>
    <div
      class="border border-[#000] rounded-lg p-5 inline-block transition-transform transform-gpu hover:scale-105"
    >
      <div class="top-prj">
        <h2 class="font-semibold mb-1 text-2xl">{{ title }}</h2>
        <p class="text-xs font-semibold w-56 mb-2">{{ description }}</p>
      </div>
      <div class="line my-3"></div>
      <div class="mid-prj">
        <img :src="img_url" alt="" class="prj-img rounded-lg" />
        <div class="flex items-center mt-4">
          <div class="">
            <p class="font-semibold">{{ category }}</p>
            <p class="text-sm">{{ subCategory }}</p>
          </div>
        </div>
      </div>
      <div class="line my-3 mt-6 mb-4"></div>
      <div class="btm-prj">
        <div class="text-center grid grid-cols-3 gap-2">
          <span
            v-for="(tag, index) in tags"
            :key="index"
            class="overflow-hidden whitespace-nowrap overflow-ellipsis border border-[#000] font-thin bg-[#fff] px-2 py-1 rounded-full text-center text-xs"
            @mouseover="hoveredIndex = index"
            @mouseleave="hoveredIndex = null"
            :class="{ hovered: hoveredIndex === index }"
            >{{ tag }}</span
          >
        </div>
      </div>
    </div>
  </a>
</template>

<script setup>
import { ref } from "vue";

const hoveredIndex = ref(null);

const props = defineProps({
  title: String,
  description: String,
  category: String,
  subCategory: String,
  tags: Array,
  img_url: String,
  project_link: String,
});
</script>

<style>
.overflow-hidden {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  transition: transform 0.3s ease; /* Add transition for smooth scaling */
}

/* Style for hovered text */
.hovered {
  transform: scale(1.2); /* Scale up on hover */
  white-space: normal; /* Display full text on hover */
  overflow: visible;
  transition: transform 0.3s ease; /* Display overflowed content */
}
.prj-img {
  width: 278px;
  height: 180px;
}
.asd {
  flex-flow: wrap;
}
</style>
