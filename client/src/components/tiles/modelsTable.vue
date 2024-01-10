<template>
  <div class="mb-3">
    <label for="searchInput" class="form-label">Search Models:</label>
    <input
      type="text"
      class="form-control"
      id="searchInput"
      v-model="searchQuery"
      placeholder="Enter search term"
      style="background-color: #d3d3d3"
    >
  </div>

  <div v-if="models" id="modelsTable">
    <table class="table table-hover">
      <thead>
        <tr>
          <th>Name</th>
          <th>Author</th>
          <th>Type</th>
          <th>Last Modification</th>
          <th></th>
          <!-- Add more columns as needed -->
        </tr>
      </thead>
      <tbody>
        <tr v-for="model in filteredModels" :key="model._id">
          <td class="hoverTD">{{ formatModelName(model.id) }}</td>
          <td class="hoverTD">{{ model.author }}</td>
          <td class="hoverTD">{{ model.pipeline_tag }}</td>
          <td class="hoverTD">{{ formatLastModified(model.lastModified) }}</td>
          <td class="hoverTD">
            <!-- Add the "Use Model" button here -->
            <button class="btn btn-warning btn-sm" @click="useModel(model)">Use Model</button>
          </td>
          <!-- Add more columns as needed -->
        </tr>
      </tbody>
    </table>
  </div>
  <p v-else><strong>Loading...</strong></p>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      models: null,
      searchQuery: '',
    };
  },
  computed: {
    filteredModels() {
      if (!this.models) {
        return [];
      }
      const query = this.searchQuery.toLowerCase();
      return this.models.filter(
        (model) =>
          model.id.toLowerCase().includes(query) ||
          this.formatLastModified(model.lastModified).includes(query) ||
          model.author.toLowerCase().includes(query)
      );
    },
  },
  mounted() {
    this.fetchModels();
  },
  methods: {
    fetchModels() {
      const path = "https://nizbwiqgrotvvnxos4e67dscsi0gnvwy.lambda-url.eu-central-1.on.aws/";
      axios
        .get(path)
        .then((res) => {
          this.models = res.data.body;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    formatLastModified(dateString) {
      const date = new Date(dateString);
      return date.toISOString().split('T')[0];
    },
    formatModelName(idString) {
      return idString.split('/')[1];
    },
    useModel(model) {
      this.$router.push({ name: 'ModelUse', params: { modelId: model.id } });
    },
  },
};
</script>
