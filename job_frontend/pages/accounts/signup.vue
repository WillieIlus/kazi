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
<template>
  <form @submit.prevent="onHandleSubmit">
    <input v-model="first_name" class="border p-2 w-full" @blur="validateField('first_name')" type="text"
      placeholder="Your Name" />

    <p v-if="errors.first_name" class="text-red-500">
      {{ errors.first_name }}
    </p>
    <input v-model="phone" class="border p-2 w-full" @blur="validateField('phone')" type="text"
      placeholder="phone 07..." />
    <p v-if="errors.phone" class="text-red-500">
      {{ errors.phone }}
    </p>
    <input v-model="email" class="border p-2 w-full" @blur="validateField('email')" type="email" placeholder="Email" />
    <p v-if="errors.email" class="text-red-500">
      {{ errors.email }}
    </p>
    <input v-model="password" class="border p-2 w-full" @blur="validateField('password')" type="password"
      placeholder="Password" />

    <p v-if="errors.password" class="text-red-500">
      {{ errors.password }}
    </p>
    <input v-model="confirmPassword" class="border p-2 w-full" @blur="validateField('confirmPassword')" type="password"
      placeholder="Confirm Password" />
    <p v-if="errors.confirmPassword" class="text-red-500">
      {{ errors.confirmPassword }}
    </p>
    <button :disabled="submitting" :class="{ 'opacity-50': submitting }" type="submit"
      class="bg-blue-500 text-white p-2 w-full disabled:opacity-50">
      <span v-if="submitting">Signing Up...</span>
      <span v-else>Sign Up</span>
    </button>
  </form>

  <div v-if="alerts.emailExists" class="bg-red-100 p-3 my-4">
    <p>Email already exists</p>
    <button @click="alerts.emailExists = false">Ok</button>
  </div>

  <div v-if="alerts.otherError" class="bg-red-100 p-3 my-4">
    <p>An error occurred. Please try again</p>
    <button @click="alerts.otherError = false">Ok</button>
  </div>
</template>

<script setup>
import { useField, useForm } from 'vee-validate';
import * as yup from 'yup';
import { useAccountStore } from '@/store/accounts';

const accountStore = useAccountStore();
const schema = yup.object({
  email: yup.string().email().required(),
  password: yup.string().min(8).required(),
  confirmPassword: yup.string().oneOf([yup.ref('password')], 'Passwords must match')
});
const { handleSubmit, validateField } = useForm({
  validationSchema: schema
});
const { value: email, errorMessage: emailError } = useField('email');
const { value: password, errorMessage: passwordError } = useField('password');
const { value: confirmPassword, errorMessage: confirmError } = useField('confirmPassword');
const errors = {
  email: emailError,
  password: passwordError,
  confirmPassword: confirmError
};
const submitting = ref(false)
const alerts = {
  emailExists: ref(false),
  otherError: ref(false),
};

const onHandleSubmit = handleSubmit(async (values) => {
  submitting.value = true;
  try {
    await accountStore.signup(values.email, values.first_name, values.phone, values.password);
    router.push('/accounts/login');
  } catch (error) {
    if (error.response && error.response.status === 409) {
      alerts.emailExists.value = true; 
    } else if (error.response && error.response.status === 400) {
      errors.value = error.response.data;
    } else {
      alerts.otherError.value = true; 
    }
  } finally {
    submitting.value = false;
  }
});
</script> 
