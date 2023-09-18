<template>
  <div>
    <h1> My Companies</h1>
    <div v-for="company in companies" :key="company.id">
      <h2>{{ company.name }}</h2>
      <p>{{ company.description }}</p>
    </div>
  </div>
</template>
<script setup>
import { storeToRefs } from 'pinia'
import { useCompanyStore } from '~~/store/useCompanyStore'
import { useAccountStore } from '~~/store/useAccountStore'

const companyStore = useCompanyStore()
const accountStore = useAccountStore()

const { companies, loading, error } = storeToRefs(companyStore)

const { userCompanies } = companyStore 

onMounted(async () => {
  await userCompanies()
})

</script>