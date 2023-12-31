<template>
  <div v-if="modelInfo">
    <h1>{{ modelInfo.id }}</h1>
    <p><strong>Author:</strong> {{ modelInfo.author }}</p>
    <p><strong>Last Modified:</strong> {{ formatLastModified(modelInfo.lastModified) }}</p>
    <p><strong>Pipeline Tag:</strong> {{ modelInfo.pipeline_tag }}</p>
    <p><strong>Tags:</strong> {{ modelInfo.tags.join(', ') }}</p>
    <p><strong>Downloads:</strong> {{ modelInfo.downloads }}</p>
    <p><strong>Likes:</strong> {{ modelInfo.likes }}</p>

    <!-- Add a link to the arXiv paper using the ID from the tags -->
    <p>
      <strong>arXiv Paper: </strong>
      <a :href="getArxivLink(modelInfo.tags)">Link</a>
    </p>
  </div>
  <p v-else>Loading...</p>
</template>

<script>
import axios from 'axios';

export default {
  props: ['modelId'],
  data() {
    return {
      modelInfo: null,
    };
  },
  methods: {
    formatLastModified(dateString) {
      const date = new Date(dateString);
      return date.toISOString().split('T')[0];
    },
    getArxivLink(tags) {
      console.log(tags)
      const arxivTag = tags.find(tag => tag.startsWith('arxiv:'));
      if (arxivTag) {
        const arxivId = arxivTag.split(':')[1];
        return `https://arxiv.org/abs/${arxivId}`;
      }
      return '#'; // Provide a fallback link or handle as needed
    },
    getModelById(relevantId) {
      const path = 'http://localhost:5001/model_by_id';

      axios
      .put(path, { modelId: encodeURIComponent(relevantId) })
      .then((response) => {
        console.log("REACHED THIS POINT!!!")
        console.log(response.data.data);
        this.modelInfo = response.data.data;
      })
      .catch((error) => {
        console.error('AxiosError:', error);
        console.error('Server response:', error.response);
      });
    },
  },
  created() {
    this.getModelById(this.modelId);
  },
};
</script>
