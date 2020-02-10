<template>
  <div class="home">
    <QuestionGet />
  </div>
</template>

<script>
// @ is an alias to /src
import QuestionGet from "@/components/QuestionGet.vue";

export default {
  name: "home",
  components: {
    QuestionGet
  }
};
</script>
