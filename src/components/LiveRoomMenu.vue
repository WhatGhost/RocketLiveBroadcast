<template>
    <div class="room-menu">
        <!--图片包含超链接-->
        <!--<img src="{{room.room_img}}" class="room-img">-->
        <div class="txt-introduce">
            <p class="room-id">Id: {{ getId }}</p>
            <p class="room-name">直播间名: {{ getRoomname }}</p>
            <p class="room-teacher">教师：{{ getNickname }}</p>
            <p id="room-introduction">简介：{{ getIntroduction }}</p>
        </div>
    </div>
</template>
<script>
export default {

    computed: {
        getIntroduction: function () {
            var url = window.location.href
            var strs = url.split('/')
            for (var i = 0; i < this.$store.state.rooms.length; i++) {
                if (this.$store.state.rooms[i].id === parseInt(strs[5])) {
                    return this.$store.state.rooms[i].room_introduction
                }
            }
        },
        getNickname: function () {
            var url = window.location.href
            var strs = url.split('/')
            for (var i = 0; i < this.$store.state.rooms.length; i++) {
                if (this.$store.state.rooms[i].id === parseInt(strs[5])) {
                    return this.$store.state.rooms[i].room_creater.nickname
                }
            }
        },
        getRoomname: function () {
            var url = window.location.href
            var strs = url.split('/')
            for (var i = 0; i < this.$store.state.rooms.length; i++) {
                if (this.$store.state.rooms[i].id === parseInt(strs[5])) {
                    return this.$store.state.rooms[i].room_name
                }
            }
        },
        getId: function () {
            var url = window.location.href
            var strs = url.split('/')
            return parseInt(strs[5])
        }
    }
}
</script>
<style scoped>
.room-menu {
    display: flex;
    justify-content: center;
    padding-left: 30px
}
</style>
