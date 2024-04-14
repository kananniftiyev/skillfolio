<!-- signup.vue -->
<template>
  <div
    class="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8"
  >
    <div class="max-w-md w-full space-y-8">
      <div>
        <h1 class="logo text-center text-5xl mb-8">Skilfolio</h1>
        <h2 class="text-center text-3xl font-semibold text-gray-900">
          Create your account
        </h2>
      </div>
      <form class="mt-8 space-y-6" @submit.prevent="submitForm">
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="first_name" class="sr-only">First Name</label>
            <input
              v-model="formData.first_name"
              id="first_name"
              name="first_name"
              type="text"
              autocomplete="given-name"
              required
              class="appearance-none rounded-none relative block w-full px-3 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
              placeholder="First Name"
            />
          </div>
          <div>
            <label for="last_name" class="sr-only">Last Name</label>
            <input
              v-model="formData.last_name"
              id="last_name"
              name="last_name"
              type="text"
              autocomplete="family-name"
              required
              class="appearance-none rounded-none relative block w-full px-3 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
              placeholder="Last Name"
            />
          </div>
          <div>
            <label for="email" class="sr-only">Email address</label>
            <input
              v-model="formData.email"
              id="email"
              name="email"
              type="email"
              autocomplete="email"
              required
              class="appearance-none rounded-none relative block w-full px-3 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
              placeholder="Email address"
            />
          </div>
          <div>
            <label for="username" class="sr-only">Username</label>
            <input
              v-model="formData.username"
              id="username"
              name="username"
              type="text"
              autocomplete="username"
              required
              class="appearance-none rounded-none relative block w-full px-3 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
              placeholder="Username"
            />
          </div>
          <div>
            <label for="password" class="sr-only">Password</label>
            <input
              v-model="formData.password"
              id="password"
              name="password"
              type="password"
              autocomplete="new-password"
              required
              class="appearance-none rounded-none relative block w-full px-3 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
              placeholder="Password"
            />
          </div>
          <div>
            <label for="confirm_password" class="sr-only"
              >Confirm Password</label
            >
            <input
              v-model="formData.confirm_password"
              id="confirm_password"
              name="confirm_password"
              type="password"
              autocomplete="new-password"
              required
              class="appearance-none rounded-none relative block w-full px-3 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
              placeholder="Confirm Password"
            />
          </div>
          <!-- File input -->
          <div class="flex items-center">
            <label for="resume" class="sr-only">Resume</label>
            <div class="relative">
              <input
                ref="fileInput"
                id="resume"
                name="resume"
                type="file"
                accept=".pdf,.doc,.docx"
                class="sr-only"
                @change="handleFileChange"
              />
              <button
                type="button"
                @click="$refs.fileInput.click()"
                class="group relative flex justify-center py-3 px-4 border border-gray-300 text-sm font-medium rounded-md text-white bg-[#63b874] hover:bg-[#3d874c] focus:outline-none"
              >
                Upload Resume
              </button>
            </div>
          </div>
          <!-- About -->
          <div>
            <label for="about" class="sr-only">About</label>
            <textarea
              v-model="formData.about"
              id="about"
              name="about"
              rows="3"
              required
              class="appearance-none rounded-none relative block w-full px-3 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
              placeholder="Tell us about yourself"
            ></textarea>
          </div>
        </div>

        <div class="flex items-center justify-between">
          <div class="text-sm">
            <a href="#" class="font-medium text-green-600 hover:text-blue-500">
              Forgot your password?
            </a>
          </div>
        </div>

        <div>
          <button
            type="submit"
            class="group relative w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-[#63b874] hover:bg-[#3d874c] focus:outline-none"
          >
            <span class="absolute left-0 inset-y-0 flex items-center pl-3">
              <svg
                class="h-5 w-5 text-green-700"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
              >
                <path
                  fill-rule="evenodd"
                  d="M9 2c.86 0 1.57.64 1.67 1.48L11 4v3h-2V4c0-.55.45-1 1-1zM5 6V4c0-1.1.9-2 2-2h6a2 2 0 0 1 2 2v2h2a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h2zm3 10a1 1 0 0 0 1-1V9a1 1 0 1 0-2 0v6a1 1 0 0 0 1 1zm5-2a1 1 0 1 0-2 0 1 1 0 0 0 2 0z"
                  clip-rule="evenodd"
                />
              </svg>
            </span>
            Sign up
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const formData = ref({
  first_name: "",
  last_name: "",
  email: "",
  username: "",
  password: "",
  confirm_password: "",
  resume: null,
  about: "",
});

const submitForm = () => {
  console.log("Form submitted with data:", formData.value);
};

const handleFileChange = (event) => {
  formData.resume = event.target.files[0];
};
</script>

<style scoped>
.logo {
  font-family: "Platypi", serif;
}
</style>
