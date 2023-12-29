<template>
  <!--<div class="container"><button type="button" class="btn btn-primary">{{ msg }}</button></div>-->
  <div class="container">
  <div class="row">
      <div class="col-sm-10">
        <h1>Hugging Face Demo <img ref="hf_smily" src="/hugging-face.png" alt="Image Description" class="image-icon"></h1>
        <menuBar></menuBar>
      </div>
      <div>
        <hr>
        <h2>About</h2>
     <p>Welcome to the Hugging Demo project! This initiative is part of the Cloud Computing lecture during the WS23/24 semester, led by Professor Tim Reibe.</p>
     <p>This project has been created by <br>
        <ul>
          <li>Manuel Heim [mh357]</li>
          <li>Nicolas Reinhart [nr063]</li>
        </ul>

     </p>
    <h3>Details</h3>
    <ul>
      <li><strong>Semester:</strong> WS23/24</li>
      <li><strong>Professor:</strong> Tim Reibe</li>
      <li><strong>Lecture:</strong> Cloud Computing</li>
      <li><strong>Project Name:</strong> Hugging Demo</li>
    </ul>

    <p>In this project, we explore the fascinating realm of cloud computing, focusing on the innovative use of machine learning. Led by a passion for technology and curiosity, our team has developed the Hugging Demo project to showcase the power and possibilities of cloud-based machine learning applications.</p>

    <h3>Explore the Project</h3>
    <p>Feel free to delve into our project repository on GitHub to discover the codebase, contribute, or simply gain insights into the exciting intersection of cloud computing and machine learning.</p>
    <p><strong>Repository Link:</strong> <a href="https://github.com/N10100010/uni_cloud_project_ml">Hugging Demo Repository</a></p>
  </div>

      </div>
    </div>
</template>

<script>
import axios from 'axios';
import menuBar from './tiles/menuBar.vue'

export default {
  components: {
    menuBar: menuBar,
  },
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5001/ping';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
