<template>
    <div class="main-div" v-bind:class="{ blur: $store.state.background_blur }">
        <h1 class="live-title">Live Room</h1>
        <ul>
            <room v-for="(room, key) in currentRooms"
                  class="room"
                  v-show="room.active_mode === 'START'"
                  v-bind:room="room"
                  :isLive="true"
                  v-bind:key="key"></room>
        </ul>
        <div class="pagination ">
            <el-pagination
                :current-page.sync="roomPage"
                layout="prev, pager, next"
                :page-size="roomNumPerPage"
                :total="activeRoomNum">
            </el-pagination>
        </div>
        <h1 class="history-title">History</h1>
        <ul>
            <room v-for="(room, key) in currentHistory"
                  class="room"
                  v-bind:room="room"
                  :isLive="false"
                  v-bind:key="key"></room>
        </ul>
        <div class="pagination ">
            <el-pagination
                :current-page.sync="historyPage"
                layout="prev, pager, next"
                :page-size="roomNumPerPage"
                :total="historyNum">
            </el-pagination>
        </div>
    </div>
</template>

<script>
import Room from './Room.vue'

export default {
    components: {
        Room,
    },
    data: function () {
        return {
            roomPage: 1,
            historyPage: 1,
            roomNumPerPage: 8,
        }
    },
    computed: {
        allRooms: function () {
            return this.$store.state.rooms
        },
        activeRooms: function () {
            let allRooms = this.allRooms
            let activeRooms = []
            for (let r of allRooms) {
                if (r.active_mode === 'START') {
                    activeRooms.push(r)
                }
            }
            return activeRooms
        },
        activeRoomNum: function () {
            return this.activeRooms.length
        },
        currentRooms: function () {
            let activeRooms = this.activeRooms
            let totalNum = activeRooms.length
            let startNum = (this.roomPage - 1) * this.roomNumPerPage
            let endNum = startNum + this.roomNumPerPage
            if (endNum > totalNum) {
                endNum = totalNum
            }
            return activeRooms.slice(startNum, endNum)
        },
        currentHistory: function () {
            let allHistory = this.history
            let totalNum = allHistory.length
            let startNum = (this.historyPage - 1) * this.roomNumPerPage
            let endNum = startNum + this.roomNumPerPage
            if (endNum > totalNum) {
                endNum = totalNum
            }
            return allHistory.slice(startNum, endNum)
        },
        history: function () {
            return this.$store.state.history
        },
        historyNum: function () {
            return this.history.length
        }
    }
}
</script>

<style scoped>
.main-div {
}

h1 {
    font-size: 20px;
    text-align: center;
    margin-left: 20px;
    margin-top: 25px;
    color: white;
    padding: 20px;
    width: 140px;
}

.live-title {
    background-color: rgba(255, 211, 124, 0.5);
}

.history-title {
    background-color: rgba(125, 188, 169, 0.4);
}

ul {
    margin: 0 auto;
    width: 1625px;
    padding-left: 0;
}

.pagination {
    display: block;
    margin: 50px auto;
    text-align: center;
}

@media screen and (max-width: 400px) {
    ul {
        width: 320px;
    }
}

@media screen and (min-width: 401px) and (max-width: 700px) {
    ul {
        width: 325px;
    }
}

@media screen and (min-width: 701px) and (max-width: 1000px) {
    ul {
        width: 650px;
    }
}

@media screen and (min-width: 1001px) and (max-width: 1320px) {
    ul {
        width: 975px;
    }
}

@media screen and (min-width: 1321px) and (max-width: 1650px) {
    ul {
        width: 1300px;
    }
}

@media screen and (min-width: 1651px) and (max-width: 1950px) {
    ul {
        width: 1625px;
    }
}
</style>
