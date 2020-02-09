<template>
  <div class="hello">
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
        <button class="btn btn-danger mb-2 mt-2" v-show="value.author === userName" @click="DeletePost(value.slug, value) ">Delete</button>
      </b-card>
    </li>
    </ul>
    <!-- ここからしゅんえい -->
    <button v-show="next" @click="getNexts()" class="btn btn-success mb-3 mt-1">
      Load More
    </button>
  </div>
</template>

<script>
import axios from "axios";
import { CSRF_TOKEN } from "../common/csrf_token.js"

export default {
  name: "QuestionGet",
  data() {
    return {
      scripts: [],
      next: true,
      nextUrls: [],
      url: "http://localhost:8000/api/keijiban/",
      userUrl: "http://localhost:8000/api/user/",
      count: 0,
      userName: '',
      delete_slug:null,

    }
  },
  // ここからしゅねい
  methods: {
    getPosts:function(url){
      axios.get(url)
    .then(response => {
      this.scripts = this.scripts.concat(response.data.results)
      if (response.data.next != null && this.next === true){
        this.nextUrls.push(response.data.next)
      }
      else if (response.data.next == null){
        this.next = false
      }
      });
    },
    getNexts:function(){
      let nextUrl = this.nextUrls[this.count]
      this.count ++
      this.getPosts(nextUrl)
    },
    getUserName:function(){
      axios.get(this.userUrl)
      .then(response => {
        this.userName = response.data.username
      })
    },
    DeletePost:function(POST, content){
      // axios.delete('/user', {data: {userId: 'xxxx'}}).then(res => {
      // })
      if(POST != null){
        this.delete_slug=POST
        let delete_url='http://localhost:8000/api/keijiban/'+String(POST)+'/'
        if (confirm("Are you sure to delete "+POST+"?")){
          axios({
            method: 'DELETE',
            url: delete_url,
            headers: {
              'X-CSRFTOKEN': CSRF_TOKEN
            }
          })
          // 指定要素の番号取得
          let index = this.scripts.indexOf(content)
          // その番号から削除する要素数をカット
          this.scripts.splice(index, 1)
          this.delete_slug=null
        }
      }
    }
  },
  mounted () {
    this.getPosts(this.url)
    this.getUserName()
    // axios.get("http://localhost:8000/api/keijiban/")
    // .then(response => {this.scripts = response.data.results });

    // axios.get("http://localhost:8000/api/keijiban/")
    //   .then(response => {this.exam = response.data.next });
    // }
  
}
}
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
