<template>
  <button @click="handleLogout">Logout</button>
</template>

<script setup>
import { useAccountStore } from '~~/store/useAccountStore';
import { useRouter } from 'vue-router';

const accountStore = useAccountStore();
const router = useRouter();

const handleLogout = async () => {
  await accountStore.logout();
  await router.push('/accounts/login'); 
}
</script>