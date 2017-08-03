<template>
    <div id="app">
        <div class="header">
            <nav-header></nav-header>
        </div>
        <button @click="currentView='Info'">switch to info</button>
        <component :is='currentView'></component>
    </div>
</template>

<script>
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
    border: 0;
    margin: 0;
    height:100%;
}

body {
    display: flex;
    flex-direction: column;
    border: 0;
    margin: 0;
}

#app {
    color: #2c3e50;
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

.header {
    width: 100%;
}
</style>
