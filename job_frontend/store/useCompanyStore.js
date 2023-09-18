import { defineStore } from 'pinia';
import { BASE_URL } from './base';

import { useAccountStore } from './useAccountStore';



const accountStore = useAccountStore();

export const useCompanyStore = defineStore('companies', {
  id: 'companies',
  state: () => ({
    companies: [],
    company: null,
    loading: false,
    error: null
  }),
  getters: {
    getCompanies: (state) => state.companies,
    getCompany: (state) => state.company,
    getLoading: (state) => state.loading,
    getError: (state) => state.error,
    companiesCount: state => state.companies.length
  },
  actions: {
    async fetchCompanies() {
      this.loading = true
      try {
        const response = await fetch(`${BASE_URL}/companies/`)
        const data = await response.json()
        this.companies = data
        this.loading = false
      } catch (error) {
        this.error = error.message
        this.loading = false
      }
    },
    async userCompanies(){
      this.loading = true
      try {
        const response = await fetch(`${BASE_URL}/companies/my/`, {
          headers: {
            'Authorization': `Bearer ${accountStore.user.token}`
          }
        })
        const data = await response.json()
        this.companies = data
        this.loading = false
      } catch (error) {
        this.error = error.message
        this.loading = false
      }
    },
    async fetchCompany(slug) {
      this.loading = true
      try {
        const response = await fetch(`${BASE_URL}/companies/${slug}/`)
        const data = await response.json()
        this.company = data
        this.loading = false
      } catch (error) {
        this.error = error.message
        this.loading = false
      }
    },
    async createCompany(company) {
      try {
        console.log(accountStore.user)
        const response = await fetch(`${BASE_URL}/companies/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${accountStore.user.token}`
          },
          
          body: JSON.stringify(company)
        })
        const data = await response.json()
        this.companies.push(data)
      }
      catch (error) {
        this.error = error.message
      }
    },
  }
})