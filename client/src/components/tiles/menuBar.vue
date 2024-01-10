<!-- HeaderMenu.vue -->

<template>
  <div class="header-menu">
    <ul>
      <li @click="navigateTo('start')">Home</li>
      <li @click="navigateTo('about')">About</li>
    </ul>
  </div>
</template>

<script>
export default {
  methods: {
    navigateTo(route) {
      this.$router.push({ name: route });
    }
  }
};

</script>


<style>
</style>