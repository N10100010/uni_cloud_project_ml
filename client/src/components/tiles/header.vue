<template>
  <div>
    <h1 ref="header">Hugging Face Demo <img ref="hs_smily" src="/hugging-face.svg" alt="Image Description" class="image-icon"></h1>
    <hr><br><br>
  </div>
</template>

<script>
export default {
  mounted() {
    this.setSmilySize();
    window.addEventListener('resize', this.setSmilySize);
  },
  methods: {
    setSmilySize() {
      const futureSize = this.$refs.header.clientHeight;
      this.$refs.hs_smily.style.height = `${futureSize}px`;
      this.$refs.hs_smily.style.width = `${futureSize}px`;
    },
  },
};
</script>

<style>
.image-icon {
  width: auto;
  margin-right: 10px; /* Adjust the margin for spacing */
}
</style>
