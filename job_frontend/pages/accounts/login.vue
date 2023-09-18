<template>
  <!-- lets do a login page instead of signup -->
  <div class="py-10 px-6">
    <div class="max-w-sm mx-auto py-10 px-6">
      <form v-on:submit.prevent="submitForm">
        <input v-model="email" type="email" name="email" placeholder="Your email address..." class="=">
        <input v-model="password" type="password" name="password" placeholder="Your password" class="">
        <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Login
        </button>
      </form>
    </div>
  </div>
</template>
<script setup>
import { useRouter } from 'vue-router'
import { useAccountStore } from '~~/store/useAccountStore';

const router = useRouter()

const accountStore = useAccountStore();

const email = ref('')
const password = ref('')

async function submitForm(){
  const response = await accountStore.login(email.value, password.value);
  
  if (response) {
    router.push('/accounts/');
  }
}

</script>















