<!-- ModelsTable.vue -->

<template>

  <div class="mb-3">
    <label for="searchInput" class="form-label">Search Models:</label>
    <input
      type="text"
      class="form-control"
      id="searchInput"
      v-model="searchQuery"
      placeholder="Enter search term">
  </div>

  <div>
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
          <td>{{ formatModelName(model.id) }}</td>
          <td>{{ model.author }}</td>
          <td>{{ model.pipeline_tag }}</td>
          <td>{{ formatLastModified(model.lastModified) }}</td>
          <td>
            <!-- Add the "Use Model" button here -->
            <button
                class="btn btn-warning btn-sm"
                @click="useModel(model)">Use Model</button>
          </td>
          <!-- Add more columns as needed -->
        </tr>
      </tbody>
    </table>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      models: [],
      searchQuery: '',
    };
  },
  computed: {
    filteredModels() {
      if (!this.models) {
        return [];
      }
      const query = this.searchQuery.toLowerCase();
      return this.models.filter(model =>
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
      const path = 'http://localhost:5001/models_by_creator';
      axios.get(path)
        .then((res) => {
          this.models = res.data.data;
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
      // Navigate to the ModelUse component with the selected model ID
      this.$router.push({ name: 'ModelUse', params: { modelId: model.id } });
    },
  },
};
</script>

<style>
/* Add your styling if needed */
</style>
