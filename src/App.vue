<template>
    <div id="app">
        <user-input></user-input>
        <room-list></room-list>
        <p>
            Welcome to your Django - Vue.js app!
        </p>
    </div>
</template>

<script>
import RoomList from './components/RoomList.vue'
import UserInput from './components/UserInput.vue'

export default {
    components: {
        RoomList,
        UserInput
    },
}
</script>

<style>
html {
    height: 100%;
}

body {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
}

#app {
    color: #2c3e50;
    margin-top: -100px;
    max-width: 600px;
    font-family: Source Sans Pro, Helvetica, sans-serif;
    text-align: center;
}

#app a {
    color: #42b983;
    text-decoration: none;
}

.logo {
    width: 100px;
    height: 100px
}
</style>
