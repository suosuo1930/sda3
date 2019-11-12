<template>
  <el-row>
    <el-col :span="8" v-for="(o, index) in 2" :key="o" :offset="index > 0 ? 2 : 0">
      <el-card :body-style="{ padding: '0px' }">
        <img :src="course_img" class="image">
        <div style="padding: 14px;">
          <span>好吃的汉堡</span>
          <div class="bottom clearfix">
            <time class="time">{{ currentDate }}</time>
            <el-button type="text" class="button">操作按钮</el-button>
          </div>
        </div>
      </el-card>
    </el-col>
  </el-row>


<!--  <div>-->
<!--    <img :src="course_img" alt="">-->
<!--    <span>{{ why_study }}</span>-->
<!--  </div>-->
</template>

<script>
    export default {
        name: "Detail",
        data(){
            return {
                courseId: 0,
                course_img: '',
                why_study: '',
            }
        },
        created() {
            this.courseId = this.$route.params.courseId
        //    https://www.luffycity.com/api/v1/free/130/detail/
        //     /static/frontend/public_class/Linux2@2x_1566529820.8127303.png
            let url = "https://www.luffycity.com/api/v1/free/" + this.courseId.toString() + "/detail/"
            console.log('url==', url)
            this.$http.get(url)
            .then(res=>{
                let data = res.data.data
                console.log('data=', data)
                this.course_img = "https://hcdn1.luffycity.com" + data.course_img
                this.why_study = data.why_study
                console.log('data.course_img==', data.course_img ,'src==', this.course_img)
            })
            .catch(err=>{
                console.log(err)
            })


        }
    }
</script>

<style scoped>
  .time {
    font-size: 13px;
    color: #999;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }

  .clearfix:after {
    clear: both
  }

</style>
