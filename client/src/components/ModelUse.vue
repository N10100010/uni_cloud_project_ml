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
        <div class="mb-3">
    <label for="searchInput" class="form-label">What do you want to create today?</label>
    <input
      type="text"
      class="form-control"
      id="promptInput"
      v-model="inputText"
      placeholder="A cat living in a tree house"
      style="background-color: #d3d3d3">
    <button @click="generateImage" class="btn btn-primary">Generate Image</button>

  </div>

  <div class="local_container">
    <img id="modelOutput" src="" alt="" class="centered-image" style="display: none;"/>
  </div>

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
generateImage() {
      // Ensure there is input text before making the request
      try {
        this.inputText.trim()
      } catch(error) {
        alert('Please enter a prompt before generating the image.');
        return;
      }


      // Use Axios for HTTP requests
      axios.put(`http://localhost:5001/generate_image/${encodeURIComponent(this.inputText)}`)
        .then(response => {
          // Handle the response as needed
          console.log('Image generated:', response.data);
          const model_output = document.getElementById('modelOutput')
          //model_output.src = `data:${response.data.data.mimeType};base64,${response.data.data.base64String}`;
          model_output.src = response.data.data.url;
          model_output.alt_t
          model_output.style = 'display: block;';
        })
        .catch(error => {
          // Handle errors
          console.error('Error generating image:', error);
        });
    }
  }
};

</script>

<style>
.local_container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.centered-image {
  max-width: 100%; /* Ensure the image doesn't exceed its container width */
  max-height: 100%; /* Ensure the image doesn't exceed its container height */
}
</style>