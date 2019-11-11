<template>
  <div>
    <h2> 我是 子 组件 </h2>
  <h3> 接受到 父组件 的 title = {{ title }}</h3>
    <h3> 主题为 {{ theme }}</h3>
    <button @click="change"> 改变主题</button>
    <br>
    <hr>
    <button @click="pingxing"> 平行组件传值 </button>
  </div>
</template>

<script>

    export default {
      name: "Son",
      props: ['title', "theme"],
      data(){
          return {

          }
      },
      created(){

      },
      methods:{
        change(){
          this.$emit('handler', '我是 Son ')
        },
        pingxing(){
          this.$bus.$emit('pingxing', 'pingxing')
        }

      }
    }
</script>

<style scoped>

</style>
