import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/component_chuanzhi/Home'
import Luff_header from '@/components/Common/Luff_header'

import Shouye from '@/components/Nav_components/Shouye'
import Free from '@/components/Nav_components/Free'
import Fight from '@/components/Nav_components/Fight'
import Detail from "@/components/Detail/Detail";

Vue.use(Router)
export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/shouye',
    },
    {
      path: '/shouye',
      name: "shouye",
      component: Shouye,
    },
    {
      path: '/free',
      name: "free",
      component: Free,
    },
    {
      path: '/fight',
      name: "fight",
      component: Fight,
    },
    {
      path:"detail/:courseId",
      name: 'course_detail',
      component: Detail,
    }

  ]
})
