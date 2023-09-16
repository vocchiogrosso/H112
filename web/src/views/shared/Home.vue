<template>
  <div>
    <h1>Home Page</h1>
    <router-link to="/contractor/navigation">Contractor Navigation</router-link>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
export default defineComponent({
  name: 'Home',
});
</script>