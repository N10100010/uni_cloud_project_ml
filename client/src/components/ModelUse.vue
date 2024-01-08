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
        <br>
        <button @click="generateImage" class="btn btn-primary">Generate Image</button>
      </div>

      <div class="local_container" style="display: none;" id="modelOutput">
        <img id="generatedImage" src="" alt="" class="centered-image">
        <button @click="saveImage" class="btn btn-primary">Persist Image</button>
      </div>
      <div class="local_container">
        <p id="perma_link" contenteditable="false" style="display: none;"></p>
      </div>
    </div>
    <br>
    <modelInfoComponent :modelId="modelId"></modelInfoComponent>
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
    saveImage() {
      const perma_tag = document.getElementById('perma_link');
      const img_tag_src = document.getElementById('generatedImage').src;
      const image_data = img_tag_src.split(', ')[1];
      const image_mime = img_tag_src.split(', ')[0].split('/')[1].split(';')[0];

      axios.post('https://69f4t4neu1.execute-api.eu-central-1.amazonaws.com/saveModelOutputStage/', {
        image: image_data,
        mime_type: 'image/' + image_mime
      })
        .then((response) => {
          if (response.status >= 200 && response.status < 300) {
            console.log('Image saved successfully:', response.data.body);
            perma_tag.textContent = response.data.body.data;
            perma_tag.style.display = 'block';
          } else {
            console.error('Error saving image. Status:', response.status);
          }
        })
        .catch((error) => {
          console.error('Error generating image:', error);
        });
    },
    generateImage() {
      const model_output = document.getElementById('modelOutput');
      model_output.style.display = 'None';
      const img_tag = document.getElementById('generatedImage');

      if (!this.inputText || this.inputText.trim() === '') {
        alert('Please enter a prompt before generating the image.');
        return;
      }

      axios
        .post(
          'https://5jjvoee0u1.execute-api.eu-central-1.amazonaws.com/generateModelOutput',
          { prompt: this.inputText } // Send prompt in the request body
        )
        .then((response) => {
          console.log('Image generated:', response.data.body);
          img_tag.src = response.data.body.data;
          img_tag.alt = response.data.body.prompt;
          model_output.style.display = 'block';
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
