<template>
    <div class="room-menu">
        <!--图片包含超链接-->
        <!--<img src="{{room.room_img}}" class="room-img">-->
        <div class="txt-introduce">
            <p class="room-id">Id: {{ this.roomId }}</p>
            <p class="room-name">直播间名: {{ this.roomName }}</p>
            <p class="room-teacher">教师： {{ this.roomTeacher }}</p>
            <p id="room-introduction">Id: {{ this.roomIntroduction }}</p>
        </div>
    </div>
</template>
<script>
export default {
    data: function () {
        return {
            roomId: -1,
            roomName: '',
            roomTeacher: '',
            roomIntroduction: ''
        }
    },
    created() {
        for (let i = 0; i < this.$store.state.rooms.length; i++) {
            if (this.$store.state.rooms[i].id === parseInt(this.$route.params['id'])) {
                this.roomIntroduction = this.$store.state.rooms[i].room_introduction
                this.roomTeacher = this.$store.state.rooms[i].room_creater.nickname
                this.roomName = this.$store.state.rooms[i].room_name
            }
        }
        this.roomId = this.$route.params['id']
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
