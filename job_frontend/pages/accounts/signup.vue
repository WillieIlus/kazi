<template>
  <form @submit.prevent="signUp">
    <input v-model="first_name" type="text" name="first_name" placeholder="Your first name..." class="">
    <input v-model="email" type="email" name="email" placeholder="Your email address..." class="=">

    <input v-model="password" type="password" name="password" placeholder="Your password" class="">
    <input v-model="re_password" type="password" name="re_password" placeholder="Repeat your password" class="">

    <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
      Signup
    </button>
  </form>
</template>
<script setup>
import { useAccountStore } from '~~/store/useAccountStore';
import { useRouter } from 'vue-router'

const router = useRouter()
const accountStore = useAccountStore();

const email = ref('')
const password = ref('')
const first_name = ref('')
const re_password = ref('')
const redirect = false

async function signUp() {
  if (password.value !== re_password.value) {
    alert('Passwords do not match');
  } else if (password.value.length < 8) {
    alert('Password must be more than 8 characters');
  } else {
    try {
      const response = await accountStore.signUp(first_name.value, email.value, password.value);
      if (response) {
        router.push('/accounts/login/')
      }
      if (!response) {
        router.push('/accounts/login/')
      }
    } catch (error) {
      console.log(error);
    }
  }
}

</script>
