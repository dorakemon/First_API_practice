<template>
  <!-- <div class="hello">
    <ul>
    <li v-for="value in scripts" :key="value.id" style="width: 70%;">
        <b-card
          :title= "value.content"
          tag="article"
          
          class="mt-5 lg-sm-10"
        >
        <b-card-text>
          {{value.author}}
        </b-card-text>
        <b-card-text>
          {{value.created_at}}
        </b-card-text>
      </b-card>
    </li>
    </ul>
  </div>-->
  <div class="say">
    <div class="container col-lg-8 pt-3">
      <h1 class="mb-3">Say Something</h1>
      <form @submit.prevent="onSubmit">
        <textarea
          v-model="script_body"
          class="form-control"
          placeholder="What do you want to say?"
          rows="10"
        ></textarea>
        <br>
        <button
          type="submit"
          class="btn btn-success mb-4 mt-1 col-lg-7"
          >Publish
        </button>
      </form>
      <p v-if="error" class="muted mt-2">{{ error }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios"; 
import { CSRF_TOKEN } from "../common/csrf_token.js"

export default {
  name: "QuestionPost",
  data() {
    return {
      script_body: null,
      error: null
    }
  },
  created() {
    document.title = "Editor - BBS";
  },
  methods: {
    onSubmit() {
      // Tell the REST API to create or update a Question Instance
      if (!this.script_body) {
        this.error = "You can't send an empty question!";
      } else if (this.script_body.length > 240) {
        this.error = "Ensure this field has no more than 240 characters!";
      } else {
        //let endpoint = "/api/questions/";
        //let method = "POST"; 
        //if (this.slug !== undefined) {
          //endpoint += `${ this.slug }/`;
          //method = "PUT";
        //const axiosBase = axios.create({
        //  baseURL: "http://localhost:8000",
        //  headers: {
        //    'Content-Type': 'application/json',
            // "Access-Control-Allow-Origin": '*',
        //    'Authorization': 'Token uz9nu2kaaxtz5gyyrzqhtg3isf8it3un',
        //  },
        //  responseType: "json"
        //});
        
        axios({
          method: 'POST',
          url: 'http://localhost:8000/api/keijiban/',
          data: {
            content: this.script_body
          },
          headers: {
            'content-type': 'application/json',
            'X-CSRFTOKEN': CSRF_TOKEN
          }
        })//.then(response => console.log(response.status));
        //.then(response => {
        //  console.log(response.data);
        //}).then(response2 => {
        //  console.log(response2);
        //}).catch(err => {
        //  console.log(err.data)
        //});
        //} 
        this.$router.push({ path: "/" })
      }//else {
        //let endpoint = "/api/questions/";
        //let method = "POST"; 
        //if (this.slug !== undefined) {
          //endpoint += `${ this.slug }/`;
          //method = "PUT";
        //}     
//        apiService(endpoint, method, { content: this.script_body })
//        .then(question_data => {
//          this.$router.push({ 
//            name: 'question', 
//            params: { slug: question_data.slug }
//          })          
//        })  
//      }
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
