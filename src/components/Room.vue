<template>
    <div class="one-room">
        <!--图片包含超链接-->
        <!-- <img src="{{room.room_img}}" class="room-img"> -->
        <p>img:{{room.room_img}}</p>
        <div class="txt-introduce">
            <p class="room-name">房间名：{{room.room_name}}</p>
            <p class="room-teacher">教师：{{room.room_creater}}</p>
            <p class="room-id">房间id：{{room.room_id}}</p>
            <p class="room-info">详情：{{room.room_introduction}}</p>
        </div>
    </div>
</template>

<script>
    export default {
        props: ['room']
    }
</script>

<style scoped>
.one-room {
    margin: 20px;
    display: inline-block;
}

p {
    font-size: 12px;
    height: 6px;
    text-align: left;
}
</style>
