<template>
    <div class="card shadow-l" @click="enterRoom">
        <img :src="room.room_img" class="video-image">
        <div class="text">
            <label>{{ room.room_name }}</label>
            <label class="intro">　id：{{ room.id }}</label>
            <div class="bottom">
                <p class="intro">教师：{{ room.room_creater.nickname }}</p>
                <p class="intro">简介：{{ room.room_introduction }}</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['room'],
    data () {
        return {
            currentDate: new Date()
        }
    },
    methods: {
        showErrorMes: function (mes) {
            this.$message({
                message: mes,
                type: 'error'
            })
        },
        enterRoom: function () {
            if (this.$store.state.account !== null) {
                this.$router.push('/room/' + this.room.id)
            } else {
                this.showErrorMes('请您先登录')
            }
        }
    }
}
</script>

<style scoped>
.card {
    height: 220px;
    margin: 20px;
    display: inline-block;
    border-radius: 7px;
    transition: background 0.5s ease-in-out;
    background-color: white;
}

.card:hover {
    cursor: pointer;
    background-color: rgb(232, 232, 232);
    background-image: url("http://okonvxmbq.bkt.clouddn.com/never/delete/play.gif");
    background-repeat: no-repeat;
    background-position: center;
    /*z-index: 100;*/
}

.video-image {
    display: block;
    width: 100%;
    height: 100%;
}

.text {
    position: relative;
    height: 100%;
    bottom: 120px;
    background-color: rgba(0, 0, 0, 0.3);
    color: white;
    padding: 10px;
}

.intro {
    font-size: 13px;
    color: rgba(255, 255,255, 0.7);
    line-height: 1.3em;
    margin: auto;
    text-align: left;
}

.bottom {
    margin-top: 13px;
    line-height: 12px;
}
</style>
