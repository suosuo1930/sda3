<template>

  <el-carousel :interval="4000" type="card" height="300px">
    <el-carousel-item v-for="item in lunboImgs" :key="item.id">
      <img :src="item.imgSrc" alt="" height="300px">
    </el-carousel-item>
  </el-carousel>

</template>

<script>
    export default {
      name: "Shouye",
        data(){
          return {
              lunboImgs: [
                  {
                      id: 1,
                      imgSrc: "https://hcdn1.luffycity.com/static/frontend/index/banner1(4)_1539945492.0492468.png"
                  },
                  {
                      id: 2,
                      imgSrc: "https://hcdn1.luffycity.com/static/frontend/index/骑士(1)_1539945488.713867.png"
                  },
                  {
                      id: 3,
                      imgSrc: "https://hcdn1.luffycity.com/static/frontend/index/banner11_1538122470.2779157.png"
                  },
                  {
                      id: 4,
                      imgSrc: "https://hcdn1.luffycity.com/static/frontend/index/home-banner4_1535545832.4715614.png"
                  }
              ]
          }
        },

    }
</script>

<style scoped>

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>
