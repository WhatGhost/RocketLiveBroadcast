<template>
    <div class="main-div">
        <label class="currentTime">{{ currentTime }}</label>
        <div class="message-div" v-bind:class="{ highlight: message.highlight }">
            <label>{{ message.nickname }}</label>
            <span class="mes-body shadow-s">{{ message.content }}</span>
        </div>
    </div>
</template>

<script>
export default {
    props: [
        'message'
    ],
    data() {
        return {}
    },
    computed: {
        currentTime: function () {
            return '10:20'
        }
    }
}
</script>

<style scoped>
.main-div {
    padding: 0 2px 5px 5px;
    margin-bottom: 7px;
}

.currentTime {
    font-size: 6px;
    color: #d9d9d9;
    text-align: right;
}

.mes-body {
    background-color: white;
    border-radius: 5px;
    padding: 10px 6px 6px 6px;
}

.highlight span {
    background-color: yellow;
}
</style>
