<template>
    <div class="card shadow-l" @click="enterRoom">
        <img :src="room.room_img" class="video-image">
        <div class="text">
            <label>{{ room.room_name }}</label>
            <label class="intro">　id：{{ id }}</label>
            <div class="bottom">
                <p class="intro">教师：{{ room.room_creator.nickname }}</p>
                <p class="intro">简介：{{ room.room_introduction }}</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: [
        'room',
        'isLive',
    ],
    data () {
        return {
            currentDate: new Date(),
            id: -1
        }
    },
    mounted: function () {
        if (this.isLive) {
            this.id = this.room.id
        } else {
            this.id = this.room.room_id
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
                if (this.room.history_source !== null) {
                    this.$router.push('/history/' + this.room.room_id)
                }
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
    width: 290px;
    line-height: 50px;
    box-sizing: border-box;
    overflow: hidden;
    display: inline-block;
    border-radius: 7px;
    transition: background 0.5s ease-in-out;
    background-color: white;
    margin: 15px 17.5px;
}

.card:hover {
    cursor: pointer;
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
    color: rgba(255, 255, 255, 0.7);
    line-height: 1.3em;
    margin: auto;
    text-align: left;
}

.bottom {
    margin-top: -10px;
    line-height: 12px;
    height: 70px;
    width: 270px;
    overflow-y: hidden;
}

.bottom:hover {
    overflow-y: auto;
}
</style>
