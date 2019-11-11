<template>
  <div id="app">
    <Luff_header></Luff_header>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
  *{
    margin: 0px;
    padding: 0px;
  }
  a{
    text-decoration: none;
  }
  ul{
    list-style: none;
  }

</style>
