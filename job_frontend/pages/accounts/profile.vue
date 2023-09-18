<template>
  <div v-if="user">
    <h1>Hello {{ user.first_name }}</h1>
    <p> your Id is {{ user.id }}</p>
    <p> your phone is {{ user.phone }}</p>
    <p> your address is {{ user.address }}</p>
    <p> your email is {{ user.email }}</p>
    <div class="py-10 px-6">
      <form v-on:submit.prevent="submitForm">
        <input v-model="first_name" type="text" name="first_name" placeholder="Your first name..." class="">
        <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Update
        </button>

      </form>
    </div>
  </div>
</template>
<script setup>
import { storeToRefs } from 'pinia';
import { useAccountStore } from '~~/store/useAccountStore';
import { useRouter } from 'vue-router';

const router = useRouter()
const accountStore = useAccountStore();

const { user } = storeToRefs(accountStore)

const first_name = ref('')



async function submitForm() {
  const response = await accountStore.updateProfile(first_name.value);
  if (response) {
    router.push('/accounts/');
  }
}

</script>

