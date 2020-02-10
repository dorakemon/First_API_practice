<template>
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
        <br />
        <button
          type="submit"
          class="btn btn-success mb-4 mt-1 col-lg-7">
          Publish
        </button>
      </form>
      <p v-if="error" class="muted mt-2">{{ error }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { CSRF_TOKEN } from "../common/csrf_token.js";

export default {
  name: "QuestionPost",
  data() {
    return {
      script_body: null,
      error: null,
      url: "http://localhost:8000/api/keijiban/"
    };
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
        axios({
          method: "POST",
          url: this.url,
          data: {
            content: this.script_body
          },
          headers: {
            "content-type": "application/json",
            "X-CSRFTOKEN": CSRF_TOKEN
          }
        });
        this.$router.push({ path: "/" });
      }
    }
  }
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
