<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>
          Hugging Face Demo
          <img ref="hf_smily" src="/hugging-face.png" alt="Image Description" class="image-icon">
        </h1>
        <menuBar></menuBar>
      </div>
    </div>
    <div>
      <hr>
      <h2>Start Page</h2>
      <alert :message="message" v-if="showMessage"></alert>
      <p>Go ahead and select the model you want to use for text-to-image operations.</p>
    </div>
    <div>
      <modelsTable></modelsTable>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';
import modelsTable from './tiles/modelsTable.vue';
import menuBar from './tiles/menuBar.vue';

export default {
  data() {
  },
  components: {
    alert: Alert,
    modelsTable: modelsTable,
    menuBar: menuBar,
  },
  methods: {
  },
  created() {
  },
};
</script>
