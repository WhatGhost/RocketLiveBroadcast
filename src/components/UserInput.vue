<template>
  <div id="user-inputs">
    <input v-model="newRoomText" v-on:keyup.enter="createRoom">
    <button v-on:click="clearRooms">
      Clear
    </button>
  </div>
</template>

<script>
export default {
  data: function () {
    return { newRoomText: '' }
  },
  methods: {
    createRoom () {
      this.$store.dispatch('addRoom' , {text: this.newRoomText})
      this.newRoomText = ''
      console.log(this.newRoomText, 'created!')
    },
    clearRooms () {
      this.$store.dispatch('clearRooms')
      console.log('Rooms cleared!')
    }
  }
}
</script>