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
      <h2>Model usage Page</h2>
      <alert :message="message" v-if="showMessage"></alert>
    </div>

    <p>Model ID: {{ modelId }}</p>

    <modelInfoComponent :modelId=modelId></modelInfoComponent>

    <div class="col-sm-10">
      <div class="mb-3">
        <label for="searchInput" class="form-label">What do you want to create today?</label>
        <input
          type="text"
          class="form-control"
          id="promptInput"
          v-model="inputText"
          placeholder="A cat living in a tree house"
          style="background-color: #d3d3d3"
        >
        <button @click="generateImage" class="btn btn-primary">Generate Image</button>
      </div>

      <div class="local_container">
        <img id="modelOutput" src="" alt="" class="centered-image" style="display: none;">
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';
import menuBar from './tiles/menuBar.vue';
import modelInfoComponent from './tiles/modelInfo.vue';

export default {
  props: ['modelId'],
  data() {
    return {
      message: '',
      showMessage: false,
      modelInfo: null,
    };
  },
  components: {
    alert: Alert,
    menuBar: menuBar,
    modelInfoComponent: modelInfoComponent,
  },
  created() {
  },
  methods: {
    generateImage() {
      const model_output = document.getElementById('modelOutput');
      model_output.style.display = 'None';

      try {
        this.inputText.trim();
      } catch (error) {
        alert('Please enter a prompt before generating the image.');
        return;
      }

      axios
        .put(`http://localhost:5001/generate_image/${encodeURIComponent(this.inputText)}`)
        .then((response) => {
          console.log('Image generated:', response.data);
          model_output.src = response.data.data.url;
          model_output.alt = response.data.prompt;
          model_output.style = 'display: block;';
        })
        .catch((error) => {
          console.error('Error generating image:', error);
        });
    },
  },
};
</script>

<style>
  .local_container {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .centered-image {
    max-width: 100%;
    max-height: 100%;
  }
</style>
