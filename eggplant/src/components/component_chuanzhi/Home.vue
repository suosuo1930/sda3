<template>
  <div>
    <h2>   我是首页  </h2>
  <Son title=" Koalao  eat  zhuzi " :theme="theme" @handler="handler"> </Son>
  </div>
</template>




<script>
import Son from '@/components/component_chuanzhi/Son'
  export default {
    name: "component_chuanzhi",
    data(){
        return {
          'theme': " 关爱动物",
        }
    },
    components:{
      Son,
    },
    methods:{
      handler(val){
        this.theme = val;
      },
    },
    created(){
      this.$bus.$on("pingxing", (ping)=>{
          alert('pingxing==' +  ping)
      })
    }

  }
</script>

<style scoped>

</style>
