<template>
  <div class="say">
    <QuestionPost />
  </div>
</template>

<script>
// @ is an alias to /src
import QuestionPost from "@/components/QuestionPost.vue";

export default {
  name: "say",
  components: {
    QuestionPost
  }
};
</script>
