<template>
    <div id="app">
        <nav-header></nav-header>
        <button @click="currentView='Info'"></button>
        <component :is='currentView'></component>
    </div>
</template>

<script>
// import RoomList from './components/RoomList.vue'
// import UserInput from './components/UserInput.vue'
import NavHeader from './components/NavHeader'
import Content from './components/Content'
import Info from './components/Info'

export default {
    components: {
        NavHeader,
        Content,
        Info,
    },
    data: function() {
        return {
            currentView: 'Content'
        }
    }
}
</script>

<style>
html {
    height: 100%;
}

body {
    display: flex;
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
