<template>
    <div id="app">
        <div class="header">
            <nav-header @goto="changePage"></nav-header>
        </div>
        <component @goto="changePage" :is="currentView"></component>
    </div>
</template>

<script>
    import NavHeader from './components/NavHeader'
    import RoomList from './components/RoomList.vue'
    import Info from './components/Info'
    import LoginPage from './components/LoginPage'
    import Register from './components/Register'
    import Forget from './components/Forget'
    import CreateRoom from './components/CreateRoom'

    export default {
        components: {
            NavHeader,
            RoomList,
            Info,
            LoginPage,
            Register,
            Forget,
            CreateRoom,
        },
        data: function () {
            return {
                currentView: 'Register'
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

    .header {
        width: 100%;
    }
</style>
