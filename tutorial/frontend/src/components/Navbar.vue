<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <div class="container">
        <b-navbar-brand to="/" class="">BBS</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-navbar-nav tag="h4">
              <b-nav-item to="/">Home</b-nav-item>
              <b-nav-item to="/say">Say Something</b-nav-item>
              <b-nav-item href="/accounts/logout/">Logout</b-nav-item>
            </b-navbar-nav>
          </b-navbar-nav>
        </b-collapse>
      </div>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: "NavbarComponent"
};
</script>

<style>
.navbar-brand {
  font-weight: bold;
  font-size: 3rem !important;
  -webkit-transition: all 0.3s ease;
  -moz-transition: all 0.3s ease;
  -o-transition: all 0.3s ease;
  transition: all 0.3s ease;
}
.navbar-brand:hover {
  color: #bddc35 !important;
}
</style>
