<template>
    <div id="app">
        <div class="header">
            <nav-header class="header" @goto="changePage" @show="doShowDialog"></nav-header>
        </div>
        <transition name="fade">
            <router-view></router-view>
        </transition>
        <img class="footer-img" v-bind:class="{ blur: $store.state.background_blur }" src="./assets/footer-img.gif"/>
    </div>
</template>

<script>
import NavHeader from './components/NavHeader'
import RoomList from './components/RoomList'
import LiveRoom from './components/LiveRoom'

export default {
    components: {
        NavHeader,
        RoomList,
        LiveRoom
    },
    data: function () {
        return {
            currentView: 'LiveRoom',
            showDialog: true
        }
    },
    methods: {
        showRooms: function () {
            this.currentView = 'RoomList'
            this.$store.dispatch('getRooms')
        },
        changePage: function (page) {
            if (page === 'RoomList') {
                this.showRooms()
            }
            this.currentView = page
        },
        doShowDialog: function () {
            this.$store.dispatch('openRegisterDialog')
        }
    }
}
</script>

<style>
html {
    border: 0;
    margin: 0;
    height: 100%;
    min-width: 300px;
    min-height: 280px;
}

body {
    display: flex;
    flex-direction: column;
    border: 0;
    margin: 0;
    background-color: #f9fbff;
    height: 85%;
}

#app {
    color: #2c3e50;
    height: 100%;
    font-family: Helvetica Neue, Arial, Hiragino Sans GB, STHeiti, Microsoft YaHei, serif;
}

#app a {
    color: #42b983;
    text-decoration: none;
}

.header {
    width: 100%;
    height: 9%;
}

.fade-enter-active {
    transition: opacity .5s;
}

.fade-leave-active {
    transition: opacity 0s;
}

.fade-enter, .fade-leave-to /* .fade-leave-active in below version 2.1.8 */
{
    opacity: 0;
}

.footer-img {
    width: 100%;
    height: 70px;
    position: fixed;
    bottom: -1px;
    z-index: -1;
}
</style>
