<template>
    <div id="app">
        <div class="header">
            <nav-header @goto="changePage" @show="doShowDialog"></nav-header>
        </div>
        <transition name="fade">
            <router-view></router-view>
        </transition>
    </div>
</template>

<script>
    import NavHeader from './components/NavHeader'
    import RoomList from './components/RoomList'
    import Info from './components/Info'
    import LoginPage from './components/LoginPage'
    import Register from './components/Register'
    import Forget from './components/Forget'
    import CreateRoom from './components/CreateRoom'
    import LiveRoom from './components/LiveRoom'

    export default {
        components: {
            NavHeader,
            RoomList,
            Info,
            LoginPage,
            Register,
            Forget,
            CreateRoom,
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
                console.log('切换')
                if (page === 'RoomList') {
                    this.showRooms()
                }
                this.currentView = page
            },
            doShowDialog: function () {
                console.log('准备dispatch')
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
    }

    body {
        display: flex;
        flex-direction: column;
        border: 0;
        margin: 0;
    }

    #app {
        color: #2c3e50;
        font-family: Helvetica Neue, Arial, Hiragino Sans GB, STHeiti, Microsoft YaHei, serif;
        text-align: center;
    }

    #app a {
        color: #42b983;
        text-decoration: none;
    }

    .header {
        width: 100%;
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
</style>
