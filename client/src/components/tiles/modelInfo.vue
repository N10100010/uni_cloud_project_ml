<template>
  <div v-if="modelInfo">
    <h2>Information pulled form Arxiv</h2>
    <h5>Paper Title: {{ modelInfo.arxiv_info.title }} </h5>
    <p><strong>Author[s]:</strong> {{ modelInfo.arxiv_info.authors }}</p>
    <p><strong>Abstract:</strong> {{ modelInfo.arxiv_info.abstract }}</p>
    <p>
      <strong>arXiv Paper: </strong>
      <a :href="getArxivLink(modelInfo.arxiv_info.arxiv_id)">Link</a>
    </p>
    <hr>
    <h2>Information pulled from HuggingFace</h2>
    <p><strong>Downloads:</strong> {{ modelInfo.huggingface_info.downloads }}</p>
    <p><strong>Likes:</strong> {{ modelInfo.huggingface_info.likes }}</p>
    <p><strong>Library Type:</strong> {{ modelInfo.huggingface_info.library_name }}</p>
    <p><strong>Task Type:</strong> {{ modelInfo.huggingface_info.task }}</p>
    <!--
    <p><strong>Last Modified:</strong> {{ formatLastModified(modelInfo.lastModified) }}</p>
    -->
  </div>
  <p v-else><strong>Loading...</strong></p>
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
    getArxivLink(arxivId) {
        return `https://arxiv.org/abs/${arxivId}`;
    },
    getModelById(relevantId) {
      const path = 'https://bo7apkf9fg.execute-api.eu-central-1.amazonaws.com/TestStage?model_id=nota-ai/bk-sdm-tiny-2m';

      axios
      .get(path)
      .then((response) => {
        console.log(response.data.body.data);
        this.modelInfo = response.data.body.data;
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
