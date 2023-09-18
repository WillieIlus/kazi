<template>
  <div v-if="accountStore.user.isAuthenticated">
    <h1>Hello {{ accountStore.user.first_name }}, {{ accountStore.user.last_name }}</h1>
    <p> your Id is {{ accountStore.user.id }}</p>
  </div>
</template>

<script setup>
import { useAccountStore } from '~~/store/useAccountStore'
const accountStore = useAccountStore()


</script>
