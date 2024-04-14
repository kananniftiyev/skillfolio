<template>
  <div class="border border-[#000] rounded-lg px-10 py-5 mb-12">
    <div class="">
      <h2 class="text-lg font-bold mb-1">Lets Get in Touch</h2>
      <p class="text-md max-w-[70%]">
        Hey there , I am available for full-time or freelance projects, whether
        they are remotely or on-site in India , I'd love to hear from you.
      </p>
    </div>
    <div class="flex items-center gap-3 mt-5">
      <a
        :href="gmailLink"
        class="transition-transform transform-gpu hover:scale-105"
      >
        <span
          class="border border-[#000] font-sm bg-[#fff] px-12 py-1 rounded-full text-center"
          >{{ gmail }}</span
        >
      </a>
      <a
        :href="linkedin"
        class="transition-transform transform-gpu hover:scale-105"
        ><span
          class="border border-[#000] font-sm bg-[#fff] px-12 py-1 rounded-full text-center"
          >Linkedin</span
        ></a
      >
      <a
        :href="resume"
        class="transition-transform transform-gpu hover:scale-105"
        ><span
          class="border border-[#000] font-sm bg-[#fff] px-12 py-1 rounded-full text-center"
          >Resume</span
        ></a
      >
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  gmail: String,
  linkedin: String,
  resume: String,
});

const gmailLink = `mailto:${props.gmail}`;
</script>
