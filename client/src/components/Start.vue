<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Hugging Face Demo <img ref="hf_smily" src="/hugging-face.png" alt="Image Description" class="image-icon"></h1>
        <hr>
        <h2>Start Page</h2>
        <alert :message=message v-if="showMessage"></alert>
      </div>
      <div>
        <models_table>
        </models_table>
      </div>
    </div>
    </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';
import ModelsTable from './tiles/modelsTable.vue';


export default {
  data() {
    return {
      activeAddBookModal: false,
      activeEditBookModal: false,
      addBookForm: {
        title: '',
        author: '',
        read: [],
      },
      books: [],
      editBookForm: {
        id: '',
        title: '',
        author: '',
        read: [],
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
    models_table: ModelsTable,
  },
  methods: {
  },
  created() {
  },
};

</script>
