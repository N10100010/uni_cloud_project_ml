<template>
  <div class="container">
  <div class="row">
      <div class="col-sm-10">
        <h1>Hugging Face Demo <img ref="hf_smily" src="/hugging-face.png" alt="Image Description" class="image-icon"></h1>
        <menuBar></menuBar>
      </div>
      <div>
        <hr>
        <h2>Model usage Page</h2>
        <alert :message=message v-if="showMessage"></alert>
      </div>
        <p>Model ID: {{ modelId }}</p>
      <div class="col-sm-10">

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';
import menuBar from './tiles/menuBar.vue';


export default {
  props: ['modelId'],
  data() {
    return {
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
    menuBar: menuBar
  },
  created() {
    this.getModelById(this.modelId)
  },
  methods: {
    getModelById(relevantId) {
        const path = 'http://localhost:5001/model_by_id';
         const data = { modelId: relevantId }; // Include modelId in the request body
         axios.put(path, data)
          .then((response) => {
            console.log(response.data.data);
          })
          .catch((error) => {
            console.error(error);
          });
    },
  },
};

</script>
