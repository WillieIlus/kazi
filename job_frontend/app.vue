<template>
  <div>
    <!-- if accountStore.user.isAuthenticated write hello user if not redirect to login page  -->
    <NuxtLink v-if="accountStore.user.isAuthenticated" to="/accounts/">
      <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
        Dashboard
      </button>
    </NuxtLink>
    <NuxtLink v-if="accountStore.user.isAuthenticated" to="/accounts/logout/">
      <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
        Logout
      </button>
    </NuxtLink>
    <NuxtLink v-if="accountStore.user.isAuthenticated" to="/accounts/profile/">
      <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
        {{ accountStore.user.name }} Profile
      </button>
    </NuxtLink>
    <NuxtLink v-if="accountStore.user.isAuthenticated" to="/companies/">
      <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
        Companies
      </button>
    </NuxtLink>
    <NuxtLink v-if="accountStore.user.isAuthenticated" to="/companies/my/">
    <button  class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
      My Companies
    </button>
    </NuxtLink>

    <NuxtLink v-if="!accountStore.user.isAuthenticated" to="/accounts/login/">
      <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
        Login
      </button>
    </NuxtLink>
    <NuxtLink v-if="!accountStore.user.isAuthenticated" to="/accounts/signup/">
      <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
        Signup
      </button>
    </NuxtLink>

    <NuxtPage>

    </NuxtPage>
  </div>
</template>
<script setup>
import { useAccountStore } from '~~/store/useAccountStore';
import { onMounted } from 'vue';

const accountStore = useAccountStore();

</script>
