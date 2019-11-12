// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

Vue.config.productionTip = false
// 1.  导入  element-ui , 且导入 全局 的 css 样式
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI)

// 平行组件传值
let bus = new Vue();
Vue.prototype.$bus = bus;

//  注册 组件为 全局 组件
import Luff_header from '@/components/Common/Luff_header'
Vue.component(Luff_header.name, Luff_header)

// 导入 Axios
import Axiios from 'axios'
// Vue.use(Axiios)
Vue.prototype.$http = Axiios

/* eslint-disable no-new */
let vm = new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})


