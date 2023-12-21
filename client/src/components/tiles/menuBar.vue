<!-- HeaderMenu.vue -->

<template>
  <div class="header-menu">
    <ul>
      <li @click="navigateTo('start')">Home</li>
      <li @click="navigateTo('about')">About</li>
      <li @click="navigateTo('contact')">Contact</li>
      <!-- Add more menu items as needed -->
    </ul>
  </div>
</template>

<script>
export default {
  methods: {
    navigateTo(route) {
      // Use Vue Router to navigate to the specified route
      this.$router.push({ name: route });
    }
  }
};

</script>


<style>
</style>