<!--<template>-->
<!--<li>-->
<!--{{room.text}}-->
<!--</li>-->
<!--</template>-->
<!--<<script>-->
<!--export default {-->
<!--props: ['room']-->
<!--}-->
<!--</script>-->

<template>
    <div class="one-room">
        <!--图片包含超链接-->
        <!--<img src="{{room.room_img}}" class="room-img">-->
        <p>img:{{room.room_id}}</p>
        <div class="txt-introduce">
            <p class="room-name">房间名：{{room.name}}</p>
            <p class="room-teacher">教师：{{room.teacher}}</p>
            <p class="room-id">房间id：{{room.id}}</p>
            <p class="room-info">详情：{{room.info}}</p>
        </div>
    </div>
</template>

<script>
    export default {
        props: ['room']
    }
</script>

<style scoped>

</style>
