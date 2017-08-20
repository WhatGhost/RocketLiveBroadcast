<template>
    <div class="main-div">
        <div class="message-div">
            <button v-for="(user, key) in bannedUsers" :key="key" @click="unban(user)">
                unban: {{ user.nickname }}
            </button>
        </div>
    </div>
</template>

<script>
export default {
    props: [
        'roomInfo',
        'bannedUsers'
    ],
    data() {
        return {}
    },
    methods: {
        unban: function (user) {
            console.log('unban clicked')
            this.$emit('unban', {
                userInfo: user,
                roomId: this.roomInfo.roomId,
            })
        }
    }
}
</script>

<style scoped>
.main-div {
    padding: 0 2px 5px 5px;
    margin-bottom: 7px;
}

.mes-body {
    background-color: white;
    border-radius: 5px;
    padding: 10px 6px 6px 6px;
}
</style>