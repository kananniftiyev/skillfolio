<template>
  <div class="mx-auto container max-w-[980px] pt-8">
    <Navigation :url="formattedPortfolio" />
    <div class="line mt-5"></div>
    <Profile />
    <div class="projects mt-12 grid grid-cols-3 gap-4">
      <a
        v-for="(project, index) in projects"
        :key="index"
        :href="project.project_link"
      >
        <Project
          :title="project.title"
          :description="project.description"
          :category="project.category"
          :subCategory="project.subCategory"
          :tags="project.tags"
          :img_url="project.img_url"
          :project_link="project.project_link"
        />
      </a>
    </div>
    <ContactCard
      class="mt-6"
      :gmail="gmail"
      :linkedin="linkedin"
      :resume="resume"
    />
  </div>
</template>

<script setup>
import { useRoute } from "vue-router";
import Navigation from "~/components/Navigation.vue";
import Profile from "~/components/Profile.vue";
import Project from "~/components/Project.vue";
import ContactCard from "~/components/ContactCard.vue";

const route = useRoute();
const portfolio = route.params.portfolio;
const formattedPortfolio =
  portfolio.charAt(0).toUpperCase() + portfolio.slice(1);

/*

axios: GET api/portfolio/{portfolio}

*/

const projects = ref([
  {
    title: "Moonflower",
    description: "A new way of meaningful socializing platform",
    category: "Product/UX",
    subCategory: "App Design",
    tags: ["UX Research"],
    img_url:
      "https://static.wixstatic.com/media/06b579_af6d11aae87a485faea1f5855ac22429~mv2.png/v1/crop/x_6,y_0,w_1670,h_1080/fill/w_348,h_225,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/front%20chaiway.png",
    project_link: "https://www.google.com",
  },
  {
    title: "Sunshine",
    description: "A platform for outdoor enthusiasts",
    category: "Product/UX",
    subCategory: "Web Design",
    tags: ["UX Research", "asds"],
    img_url:
      "https://static.wixstatic.com/media/06b579_befe1d9ff217477f8fecfec5c7954e92~mv2.png/v1/fill/w_348,h_225,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/sosh%20png.png",
    project_link: "https://www.fb.com",
  },
  {
    title: "Stardust",
    description: "An astronomy education app",
    category: "Education/Tech",
    subCategory: "Mobile App",
    tags: ["UX Research"],
    img_url:
      "https://static.wixstatic.com/media/06b579_cecd248ab80b4660b7146e82f6066d26~mv2.png/v1/fill/w_348,h_225,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/1.png",
  },
  {
    title: "Galaxy",
    description: "A space exploration game",
    category: "Entertainment/Gaming",
    subCategory: "Game Design",
    tags: ["UX Research"],
    img_url:
      "https://static.wixstatic.com/media/06b579_3eb64fb572f14e0ba5c9fa0dd07b1112~mv2.png/v1/fill/w_348,h_225,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/806a15d4-eda7-46bf-ae2a-ec823f86ee68_1000x1000.png",
  },
]);

const gmail = "example@gmail.com";
const linkedin = "https://www.linkedin.com/in/example";
const resume = "https://www.yourwebsite.com/resume.pdf";
</script>

<style>
.line {
  width: 100%; /* Adjust the width as needed */
  height: 1px;
  background-color: black; /* Change the color as needed */
  /* Center the line horizontally with some margin */
  border-radius: 5px;
}
</style>
