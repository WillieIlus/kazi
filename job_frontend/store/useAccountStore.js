import { defineStore } from 'pinia';


import { BASE_URL } from './base';

// import { createPinia } from 'pinia'
// import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

// const pinia = createPinia()
// pinia.use(piniaPluginPersistedstate)


export const useAccountStore = defineStore({
  id: 'user',
  state: () => ({
    user: {
      isAuthenticated: false,
      id: null,
      email: null,
      first_name: null,
      last_name: null,
      phone: null,
      address: null,
      role: null,
      token: null,
      refresh: null,
      avatar: null,
    }
  }),
  actions: {
    
    async initStore() {
      const token = localStorage.getItem('token')
      const refresh = localStorage.getItem('refresh')
      const email = localStorage.getItem('email')
      const first_name = localStorage.getItem('first_name')
      const role = localStorage.getItem('role')
      const avatar = localStorage.getItem('avatar')
      const id = localStorage.getItem('id')
      if (token && refresh) {
        this.user.token = token
        this.user.refresh = refresh
        this.user.email = email
        this.user.first_name = first_name
        this.user.role = role
        this.user.avatar = avatar
        this.user.id = id
        this.user.isAuthenticated = true
      }
    },
    async login(email, password) {
      try {
        const response = await fetch(`${BASE_URL}/accounts/api/auth/jwt/create/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            email: email,
            password: password
          })
        })

        if (!response.ok) {
          throw new Error('Invalid credentials')
        }

        const data = await response.json()

        localStorage.setItem('token', data.access)
        localStorage.setItem('refresh', data.refresh)
        localStorage.setItem('email', email)
        localStorage.setItem('first_name', data.first_name)
        localStorage.setItem('role', data.role)
        localStorage.setItem('avatar', data.avatar)
        localStorage.setItem('id', data.id)
        this.user.token = data.access
        this.user.refresh = data.refresh
        this.user.email = email
        this.user.first_name = data.first_name
        this.user.role = data.role
        this.user.avatar = data.avatar
        this.user.id = data.id
        this.user.isAuthenticated = true


        if (!data.access) {
          throw new Error('Access token not found in response')
        }

        const accessToken = data.access
        localStorage.setItem('token', accessToken)
        this.user.token = accessToken
        this.user.isAuthenticated = true
        return accessToken
      } catch (error) {
        console.error(error)
      }
    },
    async logout() {
      localStorage.removeItem('token')
      localStorage.removeItem('refresh')

      this.user.token = null
      this.user.isAuthenticated = false
      this.user.refresh = null
    },

    async getUser() {
      try {
        const response = await fetch(`${BASE_URL}/accounts/api/users/me/`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${useAccountStore.user.token}`
          }
        })
        if (!response.ok) {
          throw new Error('Invalid credentials')
        }
        const { id, email, first_name, role, avatar } = await response.json()
        this.user.id = id
        this.user.email = email
        this.user.first_name = first_name
        this.user.role = role
        this.user.avatar = avatar
        return { id, email, first_name, role, avatar }
      } catch (error) {
        console.error(error)
      }
    },

    async refreshToken() {
      try {
        const response = await fetch(`${BASE_URL}/accounts/api/auth/jwt/refresh/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            refresh: this.user.refresh
          })
        })
        if (!response.ok) {
          throw new Error('Invalid credentials')
        }
        const { access } = await response.json()
        localStorage.setItem('token', access)
        this.user.token = access
        return access
      } catch (error) {
        console.error(error)
      }
    },
    async signUp(first_name, email, password) {
      try {
        const requestBody = JSON.stringify({
          email: email,
          password: password,
          first_name: first_name,
        });

        const response = await fetch(`${BASE_URL}/accounts/api/users/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: requestBody,
        });

        if (!response.ok) {
          throw new Error('Invalid credentials');
        }
      } catch (error) {
        console.error('Error:', error);
      }
    },
    async updateProfile(first_name){
      try {
          const response = await fetch(`${BASE_URL}/accounts/api/users/me/`, {
            method: 'PATCH',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${this.user.token}`
            },
          body: JSON.stringify({
            first_name: first_name
          })
        });
        const data = await response.json();
        // const index = this.users.findindex(user=>user.id === data.id);
        // this.users[index] = data;
        // if (!response.ok) {
        //   throw new Error('Invalid credentials');
        // }
      } catch (error) {
        console.error('Error:', error);
        this.error. error.message;
      }
    }
  },
  persist: true,
})
