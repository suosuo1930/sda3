<template>
  <el-container>
    <el-header>
      <el-menu
      :default-active="activeIndex2"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <el-menu-item  v-for="item in navLinks" :key="item.id">
        <router-link :to='{name: item.name}'>{{ item.title }} </router-link>
      </el-menu-item>

        <el-submenu index="4">
          <template slot="title" >suosuo</template>
          <el-menu-item index="4-1">选项1</el-menu-item>
          <el-menu-item index="4-2">选项2</el-menu-item>
          <el-menu-item index="4-3">选项3</el-menu-item>
        </el-submenu>
        <el-submenu index="5">
          <template slot="title" >学习中心</template>
          <el-menu-item index="5-1">选项1</el-menu-item>
          <el-menu-item index="5-2">选项2</el-menu-item>
          <el-menu-item index="5-3">选项3</el-menu-item>
      </el-submenu>
    </el-menu>
    </el-header>
    <!--<el-main>Main</el-main>-->
  </el-container>

</template>
<script>
  export default {
    name: "Luff_header",
    data() {
      return {
        activeIndex: '1',
        activeIndex2: '1',
        navLinks: [
          {id: 0, title: "首页", name: 'shouye'},
          {id: 1, title: "免费课", name: "free"},
          {id: 2, title: "实战课", name: "fight"},
          {id: 3, title: "轻课", name: "qing"},
          {id: 4, title: "就业班", name: "offer"},
          {id: 5, title: "题库", name: "question"},
          {id: 6, title: "学员成果", name: "result"},
        ],

      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>


<style scoped>
  .el-menu--horizontal > .el-submenu {
    float: right;
  }

</style>
