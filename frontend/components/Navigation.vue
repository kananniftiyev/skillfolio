<template>
  <nav class="flex justify-between items-center">
    <a href=""
      ><h1 class="nav_username text-3xl">{{ url }}</h1></a
    >
    <div class="flex justify-between items-center gap-6">
      <a
        href=""
        class="rounded-md border-solid border-2 hover:bg-[#B2E0BB] bg-[#fff] transition-all duration-300 hover:text-[#000] border-[#666] px-6 text-base py-1"
        >Linkedin</a
      >
      <a
        href=""
        class="rounded-md border-solid border-2 hover:bg-[#B2E0BB] bg-[#fff] transition-all duration-300 hover:text-[#000] border-[#666] px-6 text-base py-1"
        >Resume</a
      >
    </div>
  </nav>
</template>

<script setup>
const props = defineProps({
  url: String,
});
</script>

<style>
.nav_username {
  font-family: "Platypi", serif;
}
</style>
